#!/usr/bin/env python3
"""
Lecteur Universel Cesim (.xls Excel BIFF8 et .html Cesim : Rapports, Décisions, Conditions, Événements)
Convertit n'importe quel fichier Cesim (.xls ou .html) en texte structuré lisible par toute IA.

Usage :
    python memoire_agent_cesim/03_outils_et_scripts/lecteur_html_cesim.py 06_conditions_marche_et_evenements/tour_05_evenements.html --filter batteries
    python memoire_agent_cesim/03_outils_et_scripts/lecteur_html_cesim.py 04_rapports_tours/tour_04_resultats_univers1.xls --filter "Score final"
"""
import argparse
import os
import sys
from html.parser import HTMLParser
from calculateur_classement_astien import parse_xls_lines


class CesimReadableParser(HTMLParser):
    """Extrait le texte et les tableaux d'un HTML Cesim en ignorant scripts, CSS et SVG."""

    def __init__(self):
        super().__init__()
        self.skip_depth = 0
        self.lines: list[str] = []
        self.cur: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        if tag in ("script", "style", "svg", "noscript"):
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in ("h1", "h2", "h3", "h4", "caption", "tr", "p", "li", "div", "br", "label"):
            self._flush()

    def handle_endtag(self, tag: str):
        if tag in ("script", "style", "svg", "noscript"):
            if self.skip_depth > 0:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in ("h1", "h2", "h3", "h4", "caption", "tr", "p", "li", "label"):
            self._flush()
        elif tag in ("td", "th"):
            self.cur.append(" | ")

    def handle_data(self, data: str):
        if self.skip_depth:
            return
        cleaned = " ".join(data.split())
        if cleaned:
            self.cur.append(cleaned)

    def _flush(self):
        line = " ".join("".join(self.cur).split()).strip(" |")
        if line:
            self.lines.append(line)
        self.cur = []


def resolve_input_path(arg: str) -> str:
    """Résout le fichier depuis le CWD, la racine du dépôt, le dossier scripts ou le workspace."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    workspace_root = os.path.dirname(repo_root)
    for candidate in (
        arg,
        os.path.join(repo_root, arg),
        os.path.join(script_dir, arg),
        os.path.join(workspace_root, arg),
    ):
        if os.path.isfile(candidate):
            return candidate
    print(f"Fichier introuvable : {arg}", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Convertit un export XLS ou HTML Cesim en texte propre.")
    parser.add_argument("input_path", help="Chemin du fichier XLS ou HTML Cesim à lire.")
    parser.add_argument(
        "--filter",
        dest="keyword",
        default=None,
        help="Filtre insensible à la casse : affiche les lignes correspondantes avec contexte.",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=4,
        help="Nombre de lignes de contexte avant/après chaque match --filter (défaut : 4).",
    )
    args = parser.parse_args()

    target = resolve_input_path(args.input_path)
    if target.lower().endswith(".xls"):
        lines = parse_xls_lines(target)
    else:
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            html_parser = CesimReadableParser()
            html_parser.feed(f.read())
            html_parser._flush()
        lines = html_parser.lines

    if not args.keyword:
        print(f"=== {os.path.basename(target)} ({len(lines)} lignes) ===")
        for line in lines:
            print(line)
        return

    kw = args.keyword.lower()
    matched_indices = [i for i, line in enumerate(lines) if kw in line.lower()]
    if not matched_indices:
        print(f"Aucune occurrence de '{args.keyword}' dans {os.path.basename(target)}.")
        return

    print(f"=== {os.path.basename(target)} — Filtre '{args.keyword}' ({len(matched_indices)} match(s)) ===")
    shown: set[int] = set()
    for idx in matched_indices:
        start = max(0, idx - args.context)
        end = min(len(lines), idx + args.context + 1)
        if shown and start > max(shown) + 1:
            print("---")
        for j in range(start, end):
            if j not in shown:
                print(lines[j])
                shown.add(j)


if __name__ == "__main__":
    main()
