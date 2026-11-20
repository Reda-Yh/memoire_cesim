#!/usr/bin/env python3
"""
Calculateur Officiel du Barème d'Eric Astien (15 critères = 180 pts ou 21 critères Tour 3+)
Session : ESYBIA2AS (Univers 1) — Bordeaux INP Cesim Global Challenge
Lit nativement les classeurs Excel (.xls BIFF8) ET les exports HTML Cesim sans dépendance externe.

Usage :
    python memoire_agent_cesim/03_outils_et_scripts/calculateur_classement_astien.py
    python memoire_agent_cesim/03_outils_et_scripts/calculateur_classement_astien.py "04_rapports_tours/tour_04_resultats_univers1.xls"
    python memoire_agent_cesim/03_outils_et_scripts/calculateur_classement_astien.py "04_rapports_tours/tour_02_resultats_univers1.xls" --criteria 17
"""
import argparse
import glob
import os
import re
import struct
import sys
from html.parser import HTMLParser


class CesimTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_td = False
        self.in_tr = False
        self.in_h = False
        self.cur_cell = []
        self.cur_row = []
        self.lines = []

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3", "h4", "caption"):
            self.in_h = True
            self.cur_cell = []
        elif tag == "tr":
            self.in_tr = True
            self.cur_row = []
        elif tag in ("td", "th"):
            self.in_td = True
            self.cur_cell = []

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "caption") and self.in_h:
            self.in_h = False
            txt = " ".join("".join(self.cur_cell).split())
            if txt:
                self.lines.append(txt)
        elif tag in ("td", "th") and self.in_td:
            self.in_td = False
            txt = " ".join("".join(self.cur_cell).split())
            self.cur_row.append(txt)
        elif tag == "tr" and self.in_tr:
            self.in_tr = False
            if any(self.cur_row):
                self.lines.append(" | ".join(self.cur_row))

    def handle_data(self, data):
        if self.in_td or self.in_h:
            self.cur_cell.append(data)


def read_ole_stream(data: bytes, target_name: str) -> bytes:
    """Extrait un flux nommé (ex: Workbook) depuis un conteneur binaire OLE2 (.xls)."""
    if data[:8] != b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
        raise ValueError("Le fichier n'est pas un conteneur OLE2 .xls valide.")
    sec_size = 1 << struct.unpack_from("<H", data, 30)[0]
    dir_start = struct.unpack_from("<I", data, 48)[0]
    difat_start = struct.unpack_from("<I", data, 68)[0]
    difat_count = struct.unpack_from("<I", data, 72)[0]

    def get_sec(sid: int) -> bytes:
        off = (sid + 1) * sec_size
        return data[off : off + sec_size]

    difat = [x for x in struct.unpack_from("<109I", data, 76) if x < 0xFFFFFFFC]
    cur = difat_start
    for _ in range(difat_count):
        if cur >= 0xFFFFFFFC:
            break
        vals = struct.unpack_from(f"<{sec_size // 4}I", get_sec(cur), 0)
        difat.extend(x for x in vals[:-1] if x < 0xFFFFFFFC)
        cur = vals[-1]

    fat: list[int] = []
    for fid in difat:
        fat.extend(struct.unpack_from(f"<{sec_size // 4}I", get_sec(fid), 0))

    def read_chain(start: int) -> bytes:
        out = bytearray()
        cur_sec = start
        seen: set[int] = set()
        while cur_sec < 0xFFFFFFFC and cur_sec not in seen:
            seen.add(cur_sec)
            out.extend(get_sec(cur_sec))
            cur_sec = fat[cur_sec]
        return bytes(out)

    dir_bytes = read_chain(dir_start)
    for i in range(0, len(dir_bytes), 128):
        entry = dir_bytes[i : i + 128]
        nlen = struct.unpack_from("<H", entry, 64)[0]
        if nlen < 2:
            continue
        name = entry[: nlen - 2].decode("utf-16le", errors="ignore")
        if name.lower() == target_name.lower():
            s_start = struct.unpack_from("<I", entry, 116)[0]
            s_size = struct.unpack_from("<I", entry, 120)[0]
            return read_chain(s_start)[:s_size]
    raise KeyError(f"Flux OLE introuvable : {target_name}")


def parse_xls_lines(path: str) -> list[str]:
    """Parse un fichier Excel .xls (BIFF8) en lignes 'label | val1 | ...' en pur Python stdlib."""
    with open(path, "rb") as f:
        data = f.read()

    # Certains exports .xls d'anciennes plateformes sont en réalité du HTML renommé en .xls
    head = data[:512].lstrip().lower()
    if head.startswith((b"<html", b"<!doctype", b"<table")):
        p = CesimTableParser()
        p.feed(data.decode("utf-8", errors="ignore"))
        return p.lines

    wb = read_ole_stream(data, "Workbook")
    records: list[tuple[int, bytes]] = []
    pos = 0
    while pos + 4 <= len(wb):
        rid, rlen = struct.unpack_from("<HH", wb, pos)
        records.append((rid, wb[pos + 4 : pos + 4 + rlen]))
        pos += 4 + rlen

    sst: list[str] = []
    sheets: list[tuple[str, int]] = []
    for idx, (rid, pay) in enumerate(records):
        if rid == 0x0085:  # BOUNDSHEET
            bof_off = struct.unpack_from("<I", pay, 0)[0]
            slen, flags = pay[6], pay[7]
            sname = (
                pay[8 : 8 + 2 * slen].decode("utf-16le", errors="ignore")
                if (flags & 1)
                else pay[8 : 8 + slen].decode("latin1", errors="ignore")
            )
            sheets.append((sname, bof_off))
        elif rid == 0x00FC:  # SST + CONTINUE
            chunks = [pay]
            j = idx + 1
            while j < len(records) and records[j][0] == 0x003C:
                chunks.append(records[j][1])
                j += 1
            c_idx, c_pos = 0, 8
            total_unique = struct.unpack_from("<I", chunks[0], 4)[0]

            def read_bytes(n: int) -> bytes:
                nonlocal c_idx, c_pos
                res = bytearray()
                while len(res) < n:
                    take = min(n - len(res), len(chunks[c_idx]) - c_pos)
                    res.extend(chunks[c_idx][c_pos : c_pos + take])
                    c_pos += take
                    if c_pos >= len(chunks[c_idx]) and len(res) < n:
                        c_idx += 1
                        c_pos = 0
                return bytes(res)

            for _ in range(total_unique):
                cch, flags = struct.unpack("<HB", read_bytes(3))
                high = bool(flags & 0x01)
                rt = struct.unpack("<H", read_bytes(2))[0] if (flags & 0x08) else 0
                ext = struct.unpack("<I", read_bytes(4))[0] if (flags & 0x04) else 0
                chars: list[str] = []
                rem = cch
                while rem > 0:
                    if c_pos >= len(chunks[c_idx]):
                        c_idx += 1
                        high = bool(chunks[c_idx][0] & 0x01)
                        c_pos = 1
                    bpc = 2 if high else 1
                    take = min(rem, (len(chunks[c_idx]) - c_pos) // bpc)
                    raw = chunks[c_idx][c_pos : c_pos + take * bpc]
                    c_pos += take * bpc
                    chars.append(raw.decode("utf-16le" if high else "latin1", errors="ignore"))
                    rem -= take
                if rt:
                    read_bytes(rt * 4)
                if ext:
                    read_bytes(ext)
                sst.append("".join(chars))

    def decode_rk(rk: int) -> float:
        if rk & 2:
            val = float(struct.unpack("<i", struct.pack("<I", rk))[0] >> 2)
        else:
            val = struct.unpack("<d", struct.pack("<II", 0, rk & 0xFFFFFFFC))[0]
        return val / 100.0 if (rk & 1) else val

    lines: list[str] = []
    for s_i, (_, bof_off) in enumerate(sheets):
        end_off = sheets[s_i + 1][1] if s_i + 1 < len(sheets) else len(wb)
        p = bof_off
        cells: dict[tuple[int, int], object] = {}
        last_formula_rc: tuple[int, int] | None = None
        while p + 4 <= end_off:
            rid, rlen = struct.unpack_from("<HH", wb, p)
            pay = wb[p + 4 : p + 4 + rlen]
            p += 4 + rlen
            if rid == 0x00FD:  # LABELSST
                r, c, _, si = struct.unpack_from("<HHHI", pay, 0)
                cells[(r, c)] = sst[si] if si < len(sst) else ""
            elif rid == 0x0204:  # LABEL
                r, c, _, slen = struct.unpack_from("<HHHH", pay, 0)
                cells[(r, c)] = (
                    pay[9 : 9 + 2 * slen].decode("utf-16le", errors="ignore")
                    if (pay[8] & 1)
                    else pay[9 : 9 + slen].decode("latin1", errors="ignore")
                )
            elif rid == 0x0203:  # NUMBER
                r, c, _ = struct.unpack_from("<HHH", pay, 0)
                cells[(r, c)] = struct.unpack_from("<d", pay, 6)[0]
            elif rid == 0x027E:  # RK
                r, c, _, rk = struct.unpack_from("<HHHI", pay, 0)
                cells[(r, c)] = decode_rk(rk)
            elif rid == 0x00BD:  # MULRK
                r, c1 = struct.unpack_from("<HH", pay, 0)
                c2 = struct.unpack_from("<H", pay, rlen - 2)[0]
                for k, c in enumerate(range(c1, c2 + 1)):
                    cells[(r, c)] = decode_rk(struct.unpack_from("<I", pay, 4 + k * 6 + 2)[0])
            elif rid == 0x0006:  # FORMULA
                r, c, _ = struct.unpack_from("<HHH", pay, 0)
                rb = pay[6:14]
                if rb[6] == 0xFF and rb[7] == 0xFF:
                    last_formula_rc = (r, c) if rb[0] == 0 else None
                    if rb[0] == 1:
                        cells[(r, c)] = bool(rb[2])
                else:
                    cells[(r, c)] = struct.unpack("<d", rb)[0]
            elif rid == 0x0207 and last_formula_rc:  # STRING (résultat chaîne de formule)
                slen = struct.unpack_from("<H", pay, 0)[0]
                cells[last_formula_rc] = (
                    pay[3 : 3 + 2 * slen].decode("utf-16le", errors="ignore")
                    if (pay[2] & 1)
                    else pay[3 : 3 + slen].decode("latin1", errors="ignore")
                )
                last_formula_rc = None

        if not cells:
            continue
        max_r = max(r for r, _ in cells)
        max_c = max(c for _, c in cells)
        for r in range(max_r + 1):
            row = [cells.get((r, c), "") for c in range(max_c + 1)]
            if not any(x != "" for x in row):
                continue
            if len([x for x in row if x != ""]) == 1 and row[0] != "":
                lines.append(" ".join(str(row[0]).split()))
            else:
                def fmt(x: object) -> str:
                    if isinstance(x, float):
                        return f"{x:.6f}".rstrip("0").rstrip(".")
                    return " ".join(str(x).split())

                lines.append(" | ".join(fmt(x) for x in row))
    return lines


def load_report_lines(path: str) -> list[str]:
    """Charge les lignes d'un rapport Cesim depuis .xls (BIFF8), .html/.htm ou .txt."""
    low = path.lower()
    if low.endswith(".xls"):
        return parse_xls_lines(path)
    if low.endswith((".html", ".htm")):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            p = CesimTableParser()
            p.feed(f.read())
            return p.lines
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().splitlines()


def to_float(s: str) -> float:
    if not s or not s.strip():
        return 0.0
    s = (
        s.replace(" ", "")
        .replace("\xa0", "")
        .replace("\u202f", "")
        .replace(",", ".")
        .replace("%", "")
    )
    try:
        return float(s)
    except ValueError as exc:
        raise ValueError(f"Valeur numérique non interprétable : {s!r}") from exc


def score_higher_better(vals: list[float]) -> list[int]:
    """Formule Excel Eric Astien : 1 + NB.SI(plage; '<' & val)"""
    return [1 + sum(1 for j in range(12) if round(vals[j], 4) < round(vals[i], 4)) for i in range(12)]


def score_lower_better(vals: list[float]) -> list[int]:
    """Formule Excel Eric Astien : 1 + NB.SI(plage; '>' & val)"""
    return [1 + sum(1 for j in range(12) if round(vals[j], 4) > round(vals[i], 4)) for i in range(12)]


def resolve_report_path(arg: str | None) -> str:
    """Résout le rapport XLS/HTML/TXT ou détecte automatiquement le tour le plus récent."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    workspace_root = os.path.dirname(repo_root)
    if arg:
        for candidate in (
            arg,
            os.path.join(repo_root, arg),
            os.path.join(script_dir, arg),
            os.path.join(workspace_root, arg),
        ):
            if os.path.exists(candidate):
                return candidate
        print(f"Fichier introuvable : {arg}")
        sys.exit(1)

    search_dirs = [
        os.path.join(repo_root, "04_rapports_tours"),
        "04_rapports_tours",
        "memoire_agent_cesim/04_rapports_tours",
    ]
    found: list[tuple[int, int, float, str]] = []
    seen_paths: set[str] = set()
    for folder in search_dirs:
        if not os.path.isdir(folder):
            continue
        paths = (
            glob.glob(os.path.join(folder, "*.xls"))
            + glob.glob(os.path.join(folder, "*.html"))
            + glob.glob(os.path.join(folder, "*.htm"))
        )
        for path in paths:
            abs_path = os.path.abspath(path)
            if abs_path in seen_paths:
                continue
            seen_paths.add(abs_path)
            m = re.search(r"tour[_\s,]*0*(\d+)", os.path.basename(path), re.IGNORECASE)
            tour_num = int(m.group(1)) if m else 0
            ext_prio = 1 if path.lower().endswith(".xls") else 0
            found.append((tour_num, ext_prio, os.path.getmtime(path), path))

    if found:
        found.sort(key=lambda item: (item[0], item[1], item[2]), reverse=True)
        return found[0][3]

    print("Aucun rapport XLS/HTML de tour trouvé dans 04_rapports_tours/.")
    sys.exit(1)


def detect_round_number(lines: list[str], target: str) -> int | None:
    """Détecte le numéro de tour (1..10) depuis l'en-tête du rapport ou le nom de fichier."""
    for line in lines[:10]:
        m = re.search(r"\bTour\s+(\d+)\b", line, re.IGNORECASE)
        if m:
            return int(m.group(1))
    m = re.search(r"tour[_ -]?0?(\d+)", os.path.basename(target), re.IGNORECASE)
    return int(m.group(1)) if m else None


def find_previous_round_report(target: str, round_num: int) -> str | None:
    """Trouve le rapport du tour précédent dans le même dossier, sans deviner un autre tour."""
    if round_num <= 1:
        return None
    folder = os.path.dirname(os.path.abspath(target))
    wanted = round_num - 1
    candidates = glob.glob(os.path.join(folder, "*.xls")) + glob.glob(os.path.join(folder, "*.html")) + glob.glob(os.path.join(folder, "*.htm"))
    for candidate in candidates:
        m = re.search(r"tour[_\s,]*0*(\d+)", os.path.basename(candidate), re.IGNORECASE)
        if m and int(m.group(1)) == wanted:
            return candidate
    return None


def extract_labeled_values(lines: list[str], label_prefix: str, occurrence: int = 1) -> list[float]:
    """Extrait une ligne de 12 équipes en exigeant une correspondance non ambiguë."""
    matches = [line for line in lines if "|" in line and line.split("|")[0].strip().startswith(label_prefix)]
    if len(matches) < occurrence:
        raise ValueError(f"Ligne '{label_prefix}' occurrence {occurrence} introuvable (trouvées : {len(matches)}).")
    if len(matches) > 1 and occurrence == 1 and label_prefix != "Dividendes":
        raise ValueError(f"Ligne '{label_prefix}' ambiguë : {len(matches)} occurrences.")
    values = [to_float(value.strip()) for value in matches[occurrence - 1].split("|")[1:13]]
    if len(values) != 12:
        raise ValueError(f"La ligne '{label_prefix}' ne contient pas 12 valeurs.")
    return values


def calculate_shareholder_return(current_lines: list[str], previous_lines: list[str]) -> list[float]:
    """TSR (%) = (cours courant - cours précédent + dividende/action) / cours précédent."""
    current_price = extract_labeled_values(current_lines, "Cours de l'action à la fin du tour")
    previous_price = extract_labeled_values(previous_lines, "Cours de l'action à la fin du tour")
    dividends_row = extract_labeled_values(current_lines, "Dividendes", occurrence=1)
    shares = extract_labeled_values(current_lines, "Actions sur le marché à la fin du tour")
    result = []
    for idx, (now, before, dividend_cash, share_count) in enumerate(zip(current_price, previous_price, dividends_row, shares)):
        if before <= 0 or share_count <= 0:
            raise ValueError(f"Cours précédent ou nombre d'actions invalide pour la colonne {idx + 1}.")
        # La ligne Dividendes est un flux négatif dans le compte de résultat (M USD).
        dividend_per_share = -dividend_cash / share_count
        result.append((now - before + dividend_per_share) / before * 100.0)
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Calculateur du classement Eric Astien (15, 17, 21 ou 22 critères)."
    )
    parser.add_argument("report", nargs="?", default=None, help="Chemin du rapport .xls ou .html")
    parser.add_argument(
        "--criteria",
        type=int,
        choices=(15, 17, 21, 22),
        default=None,
        help="Forcer le nombre de critères (15, 17, 21 ou 22).",
    )
    args = parser.parse_args()
    target = resolve_report_path(args.report)
    lines = load_report_lines(target)
    round_num = detect_round_number(lines, target)

    def parse_str_row(line: str) -> list[str]:
        parts = [p.strip() for p in line.split("|")]
        vals = parts[1:13]
        while len(vals) < 12:
            vals.append("")
        return vals[:12]

    def parse_row(line: str) -> list[float]:
        return [to_float(x) for x in parse_str_row(line)]

    def find_nth_row(prefix: str, n: int = 1) -> list[float]:
        count = 0
        for line in lines:
            if "|" in line:
                label = line.split("|")[0].strip()
                if label == prefix or label.startswith(prefix):
                    count += 1
                    if count == n:
                        return parse_row(line)
        return [0.0] * 12

    def find_all_rows(prefix: str) -> list[list[float]]:
        res = []
        for line in lines:
            if "|" in line:
                label = line.split("|")[0].strip()
                if label == prefix or label.startswith(prefix):
                    res.append(parse_row(line))
        return res

    teams = [
        "Ren'Auto",
        "AURA",
        "IronHorse",
        "YANAUTO",
        "tomobil",
        "GT-Auto VI",
        "Vrooom",
        "POLRAMOS",
        "Ça Roule",
        "BM2P",
        "TABCHOUR",
        "MO'THOR",
    ]

    roe = find_nth_row("Rentabilité des fonds propres (ROE)", 1)
    val_crea = find_nth_row("Création de valeur totale", 1)
    cap_propres = find_nth_row("Total des capitaux propres", 1)
    total_passif = find_nth_row("Total Passif", 1)
    dette_fourn = find_nth_row("Dette fournisseurs", 1)
    indep = [
        cap_propres[i] / (total_passif[i] - dette_fourn[i]) * 100.0
        if (total_passif[i] - dette_fourn[i])
        else 0.0
        for i in range(12)
    ]
    net_income = find_nth_row("Résultat net annuel", 1)
    decouvert = find_nth_row("Dettes à court terme (imprévues)", 1)

    ebit_us = find_nth_row("RÉSULTAT OPÉRATIONNEL (EBIT)", 2)
    ebit_cn = find_nth_row("RÉSULTAT OPÉRATIONNEL (EBIT)", 3)
    ebit_eu = find_nth_row("RÉSULTAT OPÉRATIONNEL (EBIT)", 4)

    ca_us = find_nth_row("Chiffre d'affaires total", 1)
    ca_cn = find_nth_row("Chiffre d'affaires total", 2)
    non_empty_ca = [
        parse_row(l)
        for l in lines
        if "|" in l and l.split("|")[0].strip() == "Chiffre d'affaires" and any(parse_row(l))
    ]
    ca_eu = non_empty_ca[1] if len(non_empty_ca) > 1 else [0.0] * 12

    marge_us = [ebit_us[i] / ca_us[i] * 100.0 if ca_us[i] else 0.0 for i in range(12)]
    marge_cn = [ebit_cn[i] / ca_cn[i] * 100.0 if ca_cn[i] else 0.0 for i in range(12)]
    marge_eu = [ebit_eu[i] / ca_eu[i] * 100.0 if ca_eu[i] else 0.0 for i in range(12)]

    pdm_glob, pdm_us, pdm_cn, pdm_eu = [0.0] * 12, [0.0] * 12, [0.0] * 12, [0.0] * 12
    for idx, line in enumerate(lines):
        if "Parts de marché global, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_glob = parse_row(sub)
                    break
        elif "USA parts de marché, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_us = parse_row(sub)
                    break
        elif "Chine parts de marché, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_cn = parse_row(sub)
                    break
        elif "Europe parts de marché, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_eu = parse_row(sub)
                    break

    dem_insat = [0.0] * 12
    for r in find_all_rows("Demande insatisfaite"):
        for i in range(12):
            dem_insat[i] += r[i]

    stocks_vol = [0.0] * 12
    for idx, line in enumerate(lines):
        if "Stocks, k unités" in line or "Stocks, milliers d'unités" in line:
            for sub in lines[idx + 1 : idx + 15]:
                if "Nombre d'usines" in sub:
                    break
                lbl = sub.split("|")[0].strip()
                if lbl in ("Thermique", "Hybride", "Électrique", "Hydrogène"):
                    r = parse_row(sub)
                    for i in range(12):
                        stocks_vol[i] += r[i]
            break

    moy_pond = find_all_rows("Moyenne pondérée")
    cost_us = moy_pond[0] if len(moy_pond) > 0 else [0.0] * 12
    cost_cn = moy_pond[1] if len(moy_pond) > 1 else [0.0] * 12
    cost_eu = moy_pond[2] if len(moy_pond) > 2 else [0.0] * 12

    prod_eng = find_nth_row("Coefficient de productivité", 1)

    # Nouveaux critères Tour 2+ / Tour 3+ (DDRS + ESG + Certification)
    ddrs_qual = find_nth_row("Qualité", 1)
    ddrs_dd = find_nth_row("Développement durable", 1)
    ddrs_fourn = [ddrs_qual[i] + ddrs_dd[i] for i in range(12)]
    has_esg = any("Score final" in l for l in lines)
    env_score = [0.0] * 12
    soc_score = [0.0] * 12
    gov_score = [0.0] * 12
    cert_pts = [0] * 12
    if has_esg:
        for idx, line in enumerate(lines):
            if "Score final" in line:
                env_score = parse_row(lines[idx + 1])
                soc_score = parse_row(lines[idx + 2])
                gov_score = parse_row(lines[idx + 3])
                break
        for line in lines:
            if "|" in line and ("Certitication" in line or "Certification" in line):
                if line.split("|")[0].strip().startswith("Cert"):
                    certs = parse_str_row(line)
                    for i, c in enumerate(certs):
                        cl = c.lower().strip()
                        if cl in ("or", "gold") or " or" in cl or "gold" in cl:
                            cert_pts[i] = 6
                        elif "argent" in cl or "silver" in cl:
                            cert_pts[i] = 4
                        elif "bronze" in cl:
                            cert_pts[i] = 2
                    break

    if args.criteria is not None:
        criteria_mode = args.criteria
    elif round_num == 1:
        criteria_mode = 15
    elif round_num == 2:
        criteria_mode = 17
    elif round_num is not None and round_num >= 5:
        criteria_mode = 22
    elif round_num is not None and round_num >= 3:
        criteria_mode = 21 if has_esg else (17 if (any(ddrs_fourn) or any(decouvert)) else 15)
    else:
        criteria_mode = 21 if has_esg else (17 if (any(ddrs_fourn) or any(decouvert)) else 15)

    # Vérifier si Part de marché US utilise pdm_us (Tour 2+) ou pdm_glob (Période 1 PDF)
    pdm_us_metric = (
        pdm_glob
        if (criteria_mode == 15 and round_num == 1)
        else (pdm_us if (criteria_mode >= 17 or has_esg or any(ddrs_fourn)) else pdm_glob)
    )

    criteria = [
        ("ROE (%)", roe, score_higher_better(roe), True),
        ("Création de valeur", val_crea, score_higher_better(val_crea), True),
        ("Indépendance financière (%)", indep, score_higher_better(indep), True),
        ("Marge op. US (%)", marge_us, score_higher_better(marge_us), True),
        ("Marge op. Asie (%)", marge_cn, score_higher_better(marge_cn), True),
        ("Marge op. Europe (%)", marge_eu, score_higher_better(marge_eu), True),
        ("Part de marché US (%)", pdm_us_metric, score_higher_better(pdm_us_metric), True),
        ("Part de marché Asie (%)", pdm_cn, score_higher_better(pdm_cn), True),
        ("Part de marché Europe (%)", pdm_eu, score_higher_better(pdm_eu), True),
        ("Demande insatisfaite (k)", dem_insat, score_lower_better(dem_insat), False),
        ("Stocks en volume (k)", stocks_vol, score_lower_better(stocks_vol), False),
        ("Coût moyen unit. US ($)", cost_us, score_lower_better(cost_us), False),
        ("Coût moyen unit. Asie ($)", cost_cn, score_lower_better(cost_cn), False),
        ("Coût moyen unit. Europe ($)", cost_eu, score_lower_better(cost_eu), False),
        ("Productivité Ingénieurs", prod_eng, score_higher_better(prod_eng), True),
    ]

    if criteria_mode >= 17 and (any(ddrs_fourn) or any(decouvert)):
        criteria.append(("Découvert (M$)", decouvert, score_lower_better(decouvert), False))
        criteria.append(("Score DDRS Fournisseurs", ddrs_fourn, score_higher_better(ddrs_fourn), True))
    if criteria_mode >= 21 and has_esg:
        criteria.append(("Impact Environnemental", env_score, score_higher_better(env_score), True))
        criteria.append(("Impact Sociétal", soc_score, score_higher_better(soc_score), True))
        criteria.append(("Impact Gouvernance", gov_score, score_higher_better(gov_score), True))
        criteria.append(("Certification ESG", cert_pts, cert_pts, True))

    if criteria_mode >= 22:
        previous_path = find_previous_round_report(target, round_num or 0)
        if not previous_path:
            raise SystemExit(
                "Impossible de calculer le 22e critère : rapport du tour précédent introuvable. "
                "Fournissez les deux rapports dans le même dossier."
            )
        previous_lines = load_report_lines(previous_path)
        shareholder_return = calculate_shareholder_return(lines, previous_lines)
        criteria.append(("Rentabilité de l'action / TSR (%)", shareholder_return,
                         score_higher_better(shareholder_return), True))

    totals = [sum(criterion[2][i] for criterion in criteria) for i in range(12)]
    print(f"=== CLASSEMENT CALCULÉ ({len(criteria)} CRITÈRES ERIC ASTIEN) — {os.path.basename(target)} ===")
    if criteria_mode >= 22:
        print("Critère TSR calculé depuis les cours des deux tours et les dividendes par action.")
    print("Attention : les ex æquo sont conservés dans le score ; l’ordre affiché entre ex æquo n’est pas un départage officiel.")
    ranking = sorted(range(12), key=lambda i: -totals[i])
    for rank, idx in enumerate(ranking, 1):
        print(
            f"#{rank:2d} | {teams[idx]:12s} | {totals[idx]:3d} pts "
            f"| Net={net_income[idx]:6.0f} M$ | Stocks={stocks_vol[idx]:5.0f} k | Insat={dem_insat[idx]:4.0f} k | Découvert={decouvert[idx]:6.0f} M$"
        )

    ih = 2  # Index d'IronHorse dans le rapport Cesim
    print(f"\n=== DÉTAIL DES {len(criteria)} CRITÈRES POUR IRONHORSE (Valeur | Points | Leader) ===")
    for name, vals, pts, higher_better in criteria:
        best_val = max(vals) if higher_better else min(vals)
        best_idx = vals.index(best_val)
        max_pt = max(pts)
        print(
            f"{name:29s} | IronHorse={vals[ih]:9.2f} ({pts[ih]:2d}/{max_pt:2d} pts) "
            f"| Meilleur={best_val:9.2f} ({teams[best_idx]})"
        )


if __name__ == "__main__":
    main()
