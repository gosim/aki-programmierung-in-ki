#!/usr/bin/env python3
"""
build.py - Parst Markdown-Testfragen und generiert quiz.html

Liest alle Markdown-Quelldateien, parst Frage-Bloecke,
erkennt Fragetypen (yesno, mc, truefalse, freetext),
und generiert eine quiz.html aus dem Template.
"""

import re
import json
import os
import sys
import random

# Seed für reproduzierbare Randomisierung
random.seed(2026)

# --- Umlaut-Konvertierung ---

# Woerter, bei denen ue/ae/oe NICHT konvertiert werden darf
_UE_EXCEPTIONS = {
    # Deutsche Woerter mit echtem ue (lateinisches Suffix -uell, Silbengrenze)
    'aktuell', 'aktuelle', 'aktuellen', 'aktueller', 'aktuelles', 'aktuellste',
    'eventuell', 'manuell', 'manueller',
    'virtuelle', 'virtuellen', 'virtuelles',
    'zuerst',
    # Englische Woerter
    'true', 'trueos', 'value', 'values', 'blue', 'issue', 'issues',
    'continue', 'continues', 'continued', 'rescue',
    # Python Exceptions (englische Begriffe!)
    'valueerror', 'typeerror', 'keyerror', 'indexerror', 'attributeerror',
    'nameerror', 'syntaxerror', 'runtimeerror', 'zerodivisionerror',
    'filenotfounderror', 'importerror', 'modulenotfounderror',
}
_AE_EXCEPTIONS = {'daemon', 'daemons'}
_OE_EXCEPTIONS = {'sudoers', 'videoencoding', 'does', 'goes', 'joe', 'joey'}

_ALL_EXCEPTIONS = _UE_EXCEPTIONS | _AE_EXCEPTIONS | _OE_EXCEPTIONS


def convert_umlauts(text):
    """Konvertiert deutsche Umlaut-Digraphen (ae, oe, ue) in echte Umlaute."""
    if not text:
        return text

    # Code-Bloecke und Inline-Code vor Konvertierung schuetzen
    protected = []

    def protect(m):
        protected.append(m.group(0))
        return f'\x00PROT{len(protected) - 1}\x00'

    text = re.sub(r'```.*?```', protect, text, flags=re.DOTALL)
    text = re.sub(r'<code>.*?</code>', protect, text, flags=re.DOTALL)
    text = re.sub(r'<pre>.*?</pre>', protect, text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', protect, text)

    # Wort fuer Wort ersetzen
    def replace_word(m):
        word = m.group(0)
        lower = word.lower()

        # Ausnahmen pruefen
        if lower in _ALL_EXCEPTIONS:
            return word

        result = word

        # ue -> ue: nur nach Konsonant (nicht nach Vokal oder q)
        # Handles: fuehren->fuehren, but NOT neue (Vokal davor), queue (q davor)
        result = re.sub(r'(?<![qQaeiouAEIOU])ue', '\u00fc', result)
        result = re.sub(r'(?<![qQaeiouAEIOU])Ue', '\u00dc', result)

        # ae -> ae
        result = result.replace('ae', '\u00e4').replace('Ae', '\u00c4')

        # oe -> oe
        result = result.replace('oe', '\u00f6').replace('Oe', '\u00d6')

        return result

    text = re.sub(r'[A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+', replace_word, text)

    # Geschuetzte Abschnitte wiederherstellen
    for i, code in enumerate(protected):
        text = text.replace(f'\x00PROT{i}\x00', code)

    return text


# --- Konfiguration ---

SOURCES = [
    ("../20_testfragen/testfragen-kapitel-1-2.md", "1-2"),
    ("../20_testfragen/testfragen-kapitel-3.md", "3"),
    ("../20_testfragen/testfragen-kapitel-4.md", "4"),
    ("../20_testfragen/testfragen-kapitel-5-6.md", "5-6"),
    ("../20_testfragen/testfragen-kapitel-7-8.md", "7-8"),
    ("../20_testfragen/testfragen-kapitel-9-10.md", "9-10"),
    ("../20_testfragen/testfragen-kapitel-14.md", "14"),
    ("../20_testfragen/programmieruebungen-extra.md", "Extra"),
    ("../30_klausur/beliebte-klausuraufgaben.md", "Beliebte"),
]

# Dateien ohne <details> Bloecke (Klausurfragen)
KLAUSUR_SOURCES = [
    ("../30_klausur/klausurfragen-sammlung.md", "Klausur"),
]

# Referenzen zu Lehrbrief und Vorlesungsmaterialien
CHAPTER_REFERENCES = {
    "1-2": {
        "title": "Kap. 1-2: Grundlagen & Variablen",
        "lehrbrief": "Python für alle, Kapitel 1 (Warum Programmieren?) & Kapitel 2 (Bezeichner, Ausdrücke, Anweisungen)",
        "folien": "vl-02.pdf",
    },
    "3": {
        "title": "Kap. 3: Bedingte Ausführung",
        "lehrbrief": "Python für alle, Kapitel 3 (Bedingte Ausführung: if/elif/else, try/except)",
        "folien": "vl-03.html",
    },
    "4": {
        "title": "Kap. 4: Funktionen",
        "lehrbrief": "Python für alle, Kapitel 4 (Funktionen: def, return, Parameter)",
        "folien": "vl-04.pdf",
    },
    "5-6": {
        "title": "Kap. 5-6: Iteration & Strings",
        "lehrbrief": "Python für alle, Kapitel 5 (Iteration: for, while, range) & Kapitel 6 (Zeichenketten)",
        "folien": "vl-06.html",
    },
    "7-8": {
        "title": "Kap. 7-8: Dateien & Listen",
        "lehrbrief": "Python für alle, Kapitel 7 (Dateien: open, read, write) & Kapitel 8 (Listen)",
        "folien": "vl-07.pdf",
    },
    "9-10": {
        "title": "Kap. 9-10: Dictionaries & Tupel",
        "lehrbrief": "Python für alle, Kapitel 9 (Dictionarys: get, keys, values) & Kapitel 10 (Tupel)",
        "folien": None,
    },
    "14": {
        "title": "Kap. 14: OOP",
        "lehrbrief": "Python für alle, Kapitel 14 (Objektorientierte Programmierung: class, __init__, self)",
        "folien": None,
    },
    "Extra": {
        "title": "Zusätzliche Übungen",
        "lehrbrief": "Gemischte Themen aus Python für alle",
        "folien": None,
    },
    "Klausur": {
        "title": "Echte Klausuraufgaben",
        "lehrbrief": "Basierend auf Gedächtnisprotokollen der Klausur vom 31.01.2026",
        "folien": None,
    },
    "Beliebte": {
        "title": "Beliebte Klausuraufgaben",
        "lehrbrief": "Häufige Programmieraufgaben aus Python für alle, Kap. 1-14",
        "folien": "GitHub: fhswf/pki, fh-swf-hgi/py4e",
    },
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(SCRIPT_DIR, "quiz-template.html")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "quiz.html")


# --- Markdown -> HTML Konvertierung (nur Standardbibliothek) ---

def md_to_html(text):
    """Konvertiert einfaches Markdown in HTML mittels Regex."""
    if not text:
        return ""

    text = text.strip()

    # Code-Bloecke zuerst verarbeiten (vor allem anderen)
    # Mehrzeilige Code-Bloecke ```...```
    def replace_code_block(m):
        lang = m.group(1) or ""
        code = m.group(2)
        # HTML-Entities im Code escapen
        code = code.replace("&", "&amp;")
        code = code.replace("<", "&lt;")
        code = code.replace(">", "&gt;")
        return f'<pre><code class="{lang}">{code}</code></pre>'

    text = re.sub(r'```(\w*)\n(.*?)```', replace_code_block, text, flags=re.DOTALL)

    # Inline-Code schuetzen vor weiterer Verarbeitung
    inline_codes = []

    def protect_inline_code(m):
        inline_codes.append(m.group(1))
        return f"\x00INLINECODE{len(inline_codes) - 1}\x00"

    text = re.sub(r'`([^`]+)`', protect_inline_code, text)

    # Tabellen verarbeiten
    lines = text.split('\n')
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Tabellen erkennen: Zeile mit | am Anfang und Ende
        if re.match(r'^\s*\|.*\|', line):
            table_lines = []
            while i < len(lines) and re.match(r'^\s*\|.*\|', lines[i]):
                table_lines.append(lines[i])
                i += 1
            result_lines.append(convert_table(table_lines))
            continue
        result_lines.append(line)
        i += 1
    text = '\n'.join(result_lines)

    # Blockquotes (> "text")
    def replace_blockquote(m):
        content = m.group(1)
        return f'<blockquote>{content}</blockquote>'

    # Mehrzeilige Blockquotes zusammenfassen
    bq_lines = []
    new_lines = []
    in_blockquote = False
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('> '):
            bq_lines.append(stripped[2:])
            in_blockquote = True
        elif stripped.startswith('>') and len(stripped) == 1:
            bq_lines.append('')
            in_blockquote = True
        else:
            if in_blockquote and bq_lines:
                new_lines.append('<blockquote>' + '<br>'.join(bq_lines) + '</blockquote>')
                bq_lines = []
                in_blockquote = False
            new_lines.append(line)
    if bq_lines:
        new_lines.append('<blockquote>' + '<br>'.join(bq_lines) + '</blockquote>')
    text = '\n'.join(new_lines)

    # Nummerierte Listen ZUERST (1. text) - damit verschachtelte - Items erfasst werden
    text = convert_ordered_lists(text)

    # Ungeordnete Listen (- text)
    text = convert_lists(text)

    # Headings: ### text -> <h3>text</h3>, ## text -> <h2>text</h2>
    text = re.sub(r'^####\s+(.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)

    # Fett: **text** -> <strong>text</strong>
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

    # Kursiv: *text* -> <em>text</em> (nur einfache Sternchen)
    # Sternchen muss direkt am Wort stehen (kein Leerzeichen danach/davor)
    text = re.sub(r'(?<!\*)\*([^*\s][^*]*?[^*\s])\*(?!\*)', r'<em>\1</em>', text)
    # Auch einzelnes Wort: *x* (mind. 1 Nicht-Leerzeichen)
    text = re.sub(r'(?<!\*)\*([^*\s])\*(?!\*)', r'<em>\1</em>', text)

    # Inline-Code wiederherstellen
    for idx, code in enumerate(inline_codes):
        escaped_code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        text = text.replace(f"\x00INLINECODE{idx}\x00", f"<code>{escaped_code}</code>")

    # Absaetze: Doppelte Zeilenumbrueche -> <br><br>
    text = re.sub(r'\n\n+', '<br><br>', text)

    # Einfache Zeilenumbrueche -> <br> (aber nicht in pre/table)
    # Nur ausserhalb von HTML-Tags
    text = re.sub(r'(?<!</pre>)\n(?!<)', '<br>\n', text)

    return text


def convert_table(lines):
    """Konvertiert Markdown-Tabellen-Zeilen in HTML."""
    if len(lines) < 2:
        return '\n'.join(lines)

    html = '<table class="md-table">'

    for idx, line in enumerate(lines):
        # Separator-Zeile ueberspringen (|---|---|)
        if re.match(r'^\s*\|[\s\-:]+\|', line):
            continue

        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        tag = 'th' if idx == 0 else 'td'
        row = '<tr>' + ''.join(f'<{tag}>{cell}</{tag}>' for cell in cells) + '</tr>'
        html += row

    html += '</table>'
    return html


def convert_lists(text):
    """Konvertiert Markdown ungeordnete Listen in HTML."""
    lines = text.split('\n')
    result = []
    in_list = False
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Checkbox-Items: - [ ] oder - [x]
        checkbox_match = re.match(r'^- \[[ x]\] (.+)$', stripped)
        # Einfache Listen-Items: - text (aber nicht ---)
        list_match = re.match(r'^- (.+)$', stripped) if not checkbox_match else None

        if checkbox_match or list_match:
            if not in_list:
                result.append('<ul>')
                in_list = True
            content = checkbox_match.group(1) if checkbox_match else list_match.group(1)
            result.append(f'<li>{content}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
        i += 1

    if in_list:
        result.append('</ul>')

    return '\n'.join(result)


def convert_ordered_lists(text):
    """Konvertiert Markdown nummerierte Listen in HTML (mit Nested Items)."""
    lines = text.split('\n')
    result = []
    in_list = False
    current_item_content = []
    i = 0

    def has_more_numbered_items(start_idx):
        """Prueft ob nach Leerzeilen noch nummerierte Items kommen."""
        for j in range(start_idx, len(lines)):
            stripped = lines[j].strip()
            if stripped == '':
                continue
            if stripped.startswith('- '):
                continue
            if re.match(r'^\d+\.\s+', stripped):
                return True
            return False
        return False

    def flush_item():
        """Fuegt aktuelles Listen-Item mit Sub-Items hinzu."""
        if current_item_content:
            main_text = current_item_content[0]
            sub_items = []
            for sub in current_item_content[1:]:
                sub_stripped = sub.strip()
                if sub_stripped.startswith('- '):
                    sub_items.append(sub_stripped[2:])

            if sub_items:
                result.append(f'<li>{main_text}<ul>')
                for sub in sub_items:
                    result.append(f'<li>{sub}</li>')
                result.append('</ul></li>')
            else:
                result.append(f'<li>{main_text}</li>')
            current_item_content.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        ol_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)

        if ol_match:
            # Neues nummeriertes Item
            if in_list:
                flush_item()
            else:
                result.append('<ol>')
                in_list = True
            current_item_content.append(ol_match.group(2))
        elif in_list and stripped.startswith('- '):
            # Sub-Item innerhalb der Liste
            current_item_content.append(line)
        elif in_list and stripped == '':
            # Leerzeile: pruefen ob Liste weitergeht
            if has_more_numbered_items(i + 1):
                # Liste geht weiter, Leerzeile ignorieren
                pass
            else:
                # Liste endet
                flush_item()
                result.append('</ol>')
                in_list = False
                result.append(line)
        else:
            # Ende der Liste
            if in_list:
                flush_item()
                result.append('</ol>')
                in_list = False
            result.append(line)
        i += 1

    if in_list:
        flush_item()
        result.append('</ol>')

    return '\n'.join(result)


# --- Frage-Extraktion ---

def extract_question_number(block, source_prefix):
    """Extrahiert die Frage-Nummer aus dem Block."""
    # Versuche verschiedene Muster
    patterns = [
        r'###?\s*Frage\s+(\d+\.\d+)',
        r'\*\*Frage\s+(\d+\.\d+):\*\*',
        r'\*\*Frage\s+(\d+\.\d+)\*\*',
        r'\*\*Aussage\s+(\d+\.\d+):\*\*',
        r'\*\*Aussage\s+(\d+\.\d+)\*\*',
        r'###?\s*Frage\s+(\d+\.\d+)',
    ]
    for pat in patterns:
        m = re.search(pat, block)
        if m:
            return m.group(1)
    return None


def detect_question_type(block):
    """Erkennt den Fragetyp basierend auf Block-Inhalt."""
    has_details = '<details>' in block

    if not has_details:
        return None  # Kein Frage-Block

    # MC: Hat Checkboxen UND ("Richtig:" oder "Loesung:" mit Buchstaben) im details
    has_checkboxes = bool(re.search(r'- \[ \] [a-z]\)', block))
    has_richtig = bool(re.search(r'\*\*(Richtig|Loesung):\*{0,2}\s*[a-z]', block, re.IGNORECASE))

    if has_checkboxes and has_richtig:
        return "mc"

    # Ja/Nein: Hat **Aussage:** (ohne Nummer wie X.Y:) UND **Antwort:** JA/NEIN im details
    has_aussage = bool(re.search(r'\*\*Aussage:\*\*', block))
    has_ja_nein_answer = bool(re.search(r'\*\*Antwort:\*\*\s*(JA|NEIN)', block))

    if has_aussage and has_ja_nein_answer:
        return "yesno"

    # Richtig/Falsch: Hat **Aussage X.Y:** (mit Nummer) UND [ ] Richtig
    has_numbered_aussage = bool(re.search(r'\*\*Aussage\s+\d+\.\d+:\*\*', block))
    has_richtig_checkbox = bool(re.search(r'\[\s*\]\s*Richtig', block))

    if has_numbered_aussage and has_richtig_checkbox:
        return "truefalse"

    # Alles andere -> freetext
    return "freetext"


def extract_details_content(block):
    """Extrahiert den Inhalt des <details> Blocks."""
    m = re.search(r'<details>\s*<summary>.*?</summary>\s*(.*?)\s*</details>', block, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def extract_before_details(block):
    """Extrahiert den Inhalt vor dem <details> Block."""
    m = re.search(r'^(.*?)<details>', block, re.DOTALL)
    if m:
        return m.group(1).strip()
    return block.strip()


def parse_yesno(block, question_id, chapter, source):
    """Parst eine Ja/Nein-Frage."""
    before = extract_before_details(block)
    details = extract_details_content(block)

    # Frage-Text nach **Aussage:**
    m = re.search(r'\*\*Aussage:\*\*\s*(.+?)(?:\n\n|\n\*\*Antwort)', before, re.DOTALL)
    question_text = m.group(1).strip() if m else before

    # Korrekte Antwort aus details
    m = re.search(r'\*\*Antwort:\*\*\s*(JA|NEIN)', details)
    correct = [m.group(1)] if m else []

    return {
        "id": question_id,
        "type": "yesno",
        "chapter": chapter,
        "question": question_text,
        "questionHtml": md_to_html(question_text),
        "options": ["JA", "NEIN"],
        "correct": correct,
        "explanation": md_to_html(details),
        "source": source,
    }


def parse_mc(block, question_id, chapter, source):
    """Parst eine Multiple-Choice-Frage."""
    before = extract_before_details(block)
    details = extract_details_content(block)

    # Frage-Text: Alles bis zu den Checkboxen (- [ ])
    # WICHTIG: Code-Bloecke zwischen Fragetext und Optionen muessen mit erfasst werden!
    question_text = None

    # Finde Position der ersten Checkbox
    checkbox_match = re.search(r'\n\s*-\s*\[\s*\]', before)
    if checkbox_match:
        text_before_options = before[:checkbox_match.start()].strip()
    else:
        text_before_options = before.strip()

    # Entferne die Frage-Header (### Frage X.Y: oder **Frage X.Y:**) vom Anfang
    # aber behalte den Rest inkl. Code-Bloecke
    header_match = re.match(r'^(?:###?\s*Frage\s+\d+\.\d+[^*\n]*\n+|\*\*Frage\s+\d+\.\d+:\*\*\s*)', text_before_options)
    if header_match:
        question_text = text_before_options[header_match.end():].strip()
    else:
        question_text = text_before_options

    # Optionen extrahieren
    options = []
    for opt_match in re.finditer(r'- \[ \] ([a-z]\)\s*.+)', before):
        options.append(opt_match.group(1))

    # Korrekte Antworten aus details
    # Format 1: **Richtig: a, c, e** (Komma-separiert, MC-Datei)
    # Format 2: **Richtig: a)** (einzelne Antwort mit Klammer, testfragen-Dateien)
    # Format 3: **Loesung:** a, c, e (Komma-separiert, uebungen-regex.md)
    correct = []
    m = re.search(r'\*\*(?:Richtig|Loesung):\*{0,2}\s*([a-z](?:\s*,\s*[a-z])*)', details, re.IGNORECASE)
    if m:
        correct = [c.strip() for c in m.group(1).split(',')]
    else:
        m2 = re.search(r'\*\*Richtig:\s*([a-z])\)\*\*', details, re.IGNORECASE)
        if m2:
            correct = [m2.group(1)]

    return {
        "id": question_id,
        "type": "mc",
        "chapter": chapter,
        "question": question_text,
        "questionHtml": md_to_html(question_text),
        "options": options,
        "correct": correct,
        "explanation": md_to_html(details),
        "source": source,
    }


def parse_truefalse(block, question_id, chapter, source):
    """Parst eine Richtig/Falsch-Frage."""
    before = extract_before_details(block)
    details = extract_details_content(block)

    # Frage-Text nach **Aussage X.Y:**
    m = re.search(r'\*\*Aussage\s+\d+\.\d+:\*\*\s*(.+?)(?:\n\s*\n|\n\s*\[)', before, re.DOTALL)
    question_text = m.group(1).strip() if m else before

    # Korrekte Antwort aus details
    if re.search(r'\*\*Richtig\*\*', details):
        correct = ["Richtig"]
    elif re.search(r'\*\*Falsch\*\*', details):
        correct = ["Falsch"]
    else:
        correct = []

    return {
        "id": question_id,
        "type": "truefalse",
        "chapter": chapter,
        "question": question_text,
        "questionHtml": md_to_html(question_text),
        "options": ["Richtig", "Falsch"],
        "correct": correct,
        "explanation": md_to_html(details),
        "source": source,
    }


def parse_freetext(block, question_id, chapter, source):
    """Parst eine Freitext-Frage."""
    before = extract_before_details(block)
    details = extract_details_content(block)

    # Gesamter Fragetext
    question_text = before

    # Stufe-Einleitung abschneiden falls vorhanden
    if question_text and re.match(r'^##\s+Stufe\s', question_text):
        m = re.search(r'(###\s+Frage\s+.+)', question_text, re.DOTALL)
        if m:
            question_text = m.group(1).strip()

    return {
        "id": question_id,
        "type": "freetext",
        "chapter": chapter,
        "question": question_text,
        "questionHtml": md_to_html(question_text),
        "options": [],
        "correct": [],
        "explanation": md_to_html(details),
        "source": source,
    }


def get_source_prefix(filename):
    """Generiert das Prefix fuer die Frage-ID basierend auf dem Dateinamen."""
    if filename == "multiple-choice-fragen.md":
        return "mc"
    m = re.search(r'kapitel-(\d+(?:-\d+)?)', filename)
    if m:
        return f"kap{m.group(1)}"
    return "q"


def detect_mc_chapter(block, current_chapter):
    """Erkennt Kapitel-Ueberschriften in der MC-Datei."""
    m = re.search(r'^#\s+Kapitel\s+(\d+):', block, re.MULTILINE)
    if m:
        return m.group(1)
    return current_chapter


def parse_file(filepath, default_chapter):
    """Parst eine komplette Markdown-Datei in Frage-Objekte."""
    filename = os.path.basename(filepath)
    source_prefix = get_source_prefix(filename)
    is_mc_file = filename == "multiple-choice-fragen.md"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # In Bloecke aufteilen (an --- Trennlinien)
    blocks = re.split(r'\n---\s*\n', content)

    questions = []
    question_counter = 0
    current_chapter = default_chapter
    mc_chapter = default_chapter
    used_ids = set()

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Kapitel-Erkennung in MC-Datei
        if is_mc_file:
            ch = detect_mc_chapter(block, None)
            if ch:
                mc_chapter = ch
            current_chapter = mc_chapter

        # Nur Bloecke mit <details> sind Fragen
        if '<details>' not in block:
            continue

        # Fragetyp erkennen
        qtype = detect_question_type(block)
        if qtype is None:
            continue

        # Frage-Nummer extrahieren
        qnum = extract_question_number(block, source_prefix)
        if qnum:
            question_id = f"{source_prefix}_{qnum}"
        else:
            question_counter += 1
            question_id = f"{source_prefix}_{question_counter}"

        # Duplikat-Vermeidung: Suffix anhaengen wenn ID schon vergeben
        base_id = question_id
        suffix = 2
        while question_id in used_ids:
            question_id = f"{base_id}_{suffix}"
            suffix += 1
        used_ids.add(question_id)

        # Je nach Typ parsen
        if qtype == "yesno":
            q = parse_yesno(block, question_id, current_chapter, filename)
        elif qtype == "mc":
            q = parse_mc(block, question_id, current_chapter, filename)
        elif qtype == "truefalse":
            q = parse_truefalse(block, question_id, current_chapter, filename)
        elif qtype == "freetext":
            q = parse_freetext(block, question_id, current_chapter, filename)
        else:
            continue

        questions.append(q)

    return questions


def detect_klausur_chapter(block, current_chapter):
    """Erkennt Kapitel/Aufgaben-Ueberschriften in Klausurfragen (Python/PKI)."""
    # ## Aufgabe 1: Code-Verstaendnis (30 Punkte)
    m = re.search(r'^##?\s+Aufgabe\s+\d+[a-z]?:\s*(.+?)(?:\s*\(|$)', block, re.MULTILINE)
    if m:
        title = m.group(1).strip().lower()
        if 'code' in title or 'verstaendnis' in title or 'for-schleife' in title:
            return "5-6"  # Iteration
        elif 'fizzbuzz' in title or 'modulo' in title:
            return "1-2"  # Grundlagen/Operatoren
        elif 'text' in title or 'string' in title:
            return "5-6"  # Strings
        elif 'dict' in title or 'zaehlen' in title:
            return "9-10"  # Dictionaries
        elif 'try' in title or 'except' in title:
            return "3"  # Bedingte Ausfuehrung
        elif 'funktion' in title:
            return "4"  # Funktionen
        elif 'liste' in title:
            return "7-8"  # Listen
        elif 'datei' in title or 'file' in title:
            return "7-8"  # Dateien
        elif 'class' in title or 'oop' in title:
            return "14"  # OOP
    return current_chapter


def split_multi_loesung_block(block):
    """Split block with multiple **Loesung:** into separate sub-blocks."""
    loesung_matches = list(re.finditer(r'\*\*Loesung:\*\*', block))

    if len(loesung_matches) <= 1:
        return [block]

    # Pattern marking start of a new sub-question (bold numbered/lettered item)
    question_marker = r'\n\n\*\*(?:[\(\[]?[a-z]{1,4}[\)\]]|[0-9]+\.)'

    sub_blocks = []
    prev_answer_end = 0

    for i, match in enumerate(loesung_matches):
        loesung_start = match.start()

        q_start = 0 if i == 0 else prev_answer_end

        # Find end of this answer (start of next sub-question)
        if i + 1 < len(loesung_matches):
            search_region = block[loesung_start:loesung_matches[i + 1].start()]
            q_marker = re.search(question_marker, search_region)
            if q_marker:
                answer_end = loesung_start + q_marker.start()
            else:
                answer_end = loesung_matches[i + 1].start()
        else:
            answer_end = len(block)

        sub_block = block[q_start:answer_end].strip()
        if sub_block:
            sub_blocks.append(sub_block)
        prev_answer_end = answer_end

    return sub_blocks if sub_blocks else [block]


def parse_klausur_file(filepath, default_chapter):
    """Parst klausurfragen-sammlung.md (ohne <details> Bloecke)."""
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'\n---\s*\n', content)

    # Split blocks with multiple **Loesung:** into sub-blocks
    expanded_blocks = []
    for block in blocks:
        expanded_blocks.extend(split_multi_loesung_block(block))
    blocks = expanded_blocks

    questions = []
    question_counter = 0
    current_chapter = default_chapter
    used_ids = set()

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Kapitel erkennen
        ch = detect_klausur_chapter(block, None)
        if ch:
            current_chapter = ch

        # Skip reine Ueberschriften-Bloecke und Zusammenfassungs-Bloecke
        if not re.search(r'\*\*Loesung:\*\*', block, re.IGNORECASE):
            # Auch ### Loesung: Format pruefen
            if not re.search(r'###?\s*Loesung:', block):
                continue

        question_counter += 1
        question_id = f"klausur_{question_counter}"

        # Duplikat-Vermeidung
        base_id = question_id
        suffix = 2
        while question_id in used_ids:
            question_id = f"{base_id}_{suffix}"
            suffix += 1
        used_ids.add(question_id)

        # Frage und Loesung trennen
        # Format 1: **Loesung:** Ja/Nein + **Begruendung:**
        loesung_match = re.search(
            r'\*\*Loesung:\*\*\s*(.*?)$',
            block, re.MULTILINE
        )

        if loesung_match:
            # Alles vor **Loesung:** ist die Frage
            loesung_start = block.index('**Loesung:**')
            question_part = block[:loesung_start].strip()
            answer_part = block[loesung_start:].strip()

            # Pruefe ob Ja/Nein
            ja_nein_match = re.search(
                r'\*\*Loesung:\*\*\s*(Ja|Nein)',
                answer_part, re.IGNORECASE
            )

            if ja_nein_match:
                answer_val = ja_nein_match.group(1).strip()
                correct = ["JA"] if answer_val.lower() == "ja" else ["NEIN"]

                # Frage-Text extrahieren (oft fett markiert)
                q_text = question_part
                # Entferne Ueberschriften und Klausur-Labels
                q_text = re.sub(r'^###?\s+.*\n', '', q_text)
                q_text = re.sub(r'^###?\s+.*\n', '', q_text)
                # Entferne Aufgabentyp-Zeilen
                q_text = re.sub(r'\*\*Aufgabentyp:\*\*.*\n?', '', q_text)
                # Extrahiere den fett markierten Fragetext
                fett_match = re.search(r'\*\*([a-z]\)\s+)?(.+?)\*\*', q_text, re.DOTALL)
                if fett_match:
                    q_text = fett_match.group(2).strip() if fett_match.group(2) else q_text

                q = {
                    "id": question_id,
                    "type": "yesno",
                    "chapter": current_chapter,
                    "question": q_text,
                    "questionHtml": md_to_html(q_text),
                    "options": ["JA", "NEIN"],
                    "correct": correct,
                    "explanation": md_to_html(answer_part),
                    "source": filename,
                }
            else:
                # Freetext-Frage
                q = {
                    "id": question_id,
                    "type": "freetext",
                    "chapter": current_chapter,
                    "question": question_part,
                    "questionHtml": md_to_html(question_part),
                    "options": [],
                    "correct": [],
                    "explanation": md_to_html(answer_part),
                    "source": filename,
                }
        else:
            # ### Loesung: Format (z.B. Rechenaufgaben)
            loesung_heading = re.search(r'(###?\s*Loesung:)', block)
            if loesung_heading:
                split_pos = block.index(loesung_heading.group(1))
                question_part = block[:split_pos].strip()
                answer_part = block[split_pos:].strip()
            else:
                question_part = block
                answer_part = ""

            q = {
                "id": question_id,
                "type": "freetext",
                "chapter": current_chapter,
                "question": question_part,
                "questionHtml": md_to_html(question_part),
                "options": [],
                "correct": [],
                "explanation": md_to_html(answer_part),
                "source": filename,
            }

        questions.append(q)

    return questions


def parse_rechenaufgaben_file(filepath):
    """Parst rechenaufgaben-paging.md (Beispielrechnungen)."""
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'\n---\s*\n', content)

    questions = []
    question_counter = 0
    used_ids = set()

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Nur Bloecke mit **Gegeben:** oder konkreten Aufgaben
        if '**Gegeben:**' not in block and '### Loesung:' not in block:
            continue

        question_counter += 1
        question_id = f"paging_{question_counter}"

        base_id = question_id
        suffix = 2
        while question_id in used_ids:
            question_id = f"{base_id}_{suffix}"
            suffix += 1
        used_ids.add(question_id)

        # Trennung: Alles bis ### Loesung: ist die Aufgabe
        loesung_match = re.search(r'(###?\s*Loesung:)', block)
        if loesung_match:
            split_pos = block.index(loesung_match.group(1))
            question_part = block[:split_pos].strip()
            answer_part = block[split_pos:].strip()
        else:
            question_part = block
            answer_part = ""

        q = {
            "id": question_id,
            "type": "freetext",
            "chapter": "5-6",
            "question": question_part,
            "questionHtml": md_to_html(question_part),
            "options": [],
            "correct": [],
            "explanation": md_to_html(answer_part),
            "source": filename,
        }
        questions.append(q)

    return questions


def main():
    all_questions = []
    stats = {"yesno": 0, "mc": 0, "truefalse": 0, "freetext": 0}

    for filename, chapter in SOURCES:
        filepath = os.path.join(SCRIPT_DIR, filename)
        if not os.path.exists(filepath):
            print(f"WARNUNG: {filename} nicht gefunden, ueberspringe.", file=sys.stderr)
            continue

        questions = parse_file(filepath, chapter)
        all_questions.extend(questions)
        print(f"  {filename}: {len(questions)} Fragen")

    # Klausurfragen und Rechenaufgaben (anderes Format)
    for filename, label in KLAUSUR_SOURCES:
        filepath = os.path.join(SCRIPT_DIR, filename)
        if not os.path.exists(filepath):
            print(f"WARNUNG: {filename} nicht gefunden, ueberspringe.", file=sys.stderr)
            continue

        if filename == "rechenaufgaben-paging.md":
            questions = parse_rechenaufgaben_file(filepath)
        else:
            questions = parse_klausur_file(filepath, label)
        all_questions.extend(questions)
        print(f"  {filename}: {len(questions)} Fragen")

    # Umlaute konvertieren (ae->ä, oe->ö, ue->ü)
    for q in all_questions:
        q['question'] = convert_umlauts(q['question'])
        q['questionHtml'] = convert_umlauts(q['questionHtml'])
        q['explanation'] = convert_umlauts(q['explanation'])
        for i, opt in enumerate(q.get('options', [])):
            q['options'][i] = convert_umlauts(opt)

    # Referenzen zu Lehrbrief/Vorlesungen anhaengen
    for q in all_questions:
        chapter = q.get('chapter', '')
        if chapter in CHAPTER_REFERENCES:
            ref = CHAPTER_REFERENCES[chapter]
            ref_html = '<hr><p class="reference"><strong>📚 Quelle:</strong> '
            ref_html += ref['lehrbrief']
            if ref.get('folien'):
                ref_html += f' | <strong>Folien:</strong> {ref["folien"]}'
            ref_html += '</p>'
            q['explanation'] += ref_html

    # Duplikate entfernen (gleicher question-Text ODER gleicher Code-Block)
    seen_questions = set()
    seen_code = set()
    unique_questions = []
    duplicates_removed = 0

    def extract_code(text):
        """Extrahiert Code aus ```python ... ``` Bloecken."""
        m = re.search(r'```python\n(.*?)\n```', text, re.DOTALL)
        if m:
            # Normalisiere: Whitespace vereinheitlichen
            code = m.group(1).strip()
            code = re.sub(r'\s+', ' ', code)
            return code
        return None

    for q in all_questions:
        q_text = q['question'].strip()
        q_code = extract_code(q['question'])

        # Pruefe auf Text-Duplikat
        if q_text in seen_questions:
            duplicates_removed += 1
            print(f"  DUPLIKAT (Text): [{q['id']}] {q_text[:50]}...")
            continue

        # Pruefe auf Code-Duplikat (wenn Code vorhanden)
        if q_code and q_code in seen_code:
            duplicates_removed += 1
            print(f"  DUPLIKAT (Code): [{q['id']}] {q_code[:50]}...")
            continue

        seen_questions.add(q_text)
        if q_code:
            seen_code.add(q_code)
        unique_questions.append(q)

    all_questions = unique_questions
    if duplicates_removed:
        print(f"\n  {duplicates_removed} Duplikat(e) entfernt.")

    # MC-Optionen randomisieren
    mc_randomized = 0
    for q in all_questions:
        if q['type'] == 'mc' and len(q.get('options', [])) >= 2:
            options = q['options']
            correct = q.get('correct', [])

            # Erstelle Mapping: Buchstabe -> Option-Text
            option_map = {}
            for opt in options:
                m = re.match(r'([a-z])\)\s*(.+)', opt)
                if m:
                    option_map[m.group(1)] = m.group(2)

            if not option_map:
                continue

            # Hole die korrekten Texte
            correct_texts = [option_map.get(c, '') for c in correct if c in option_map]

            # Mische die Optionen
            items = list(option_map.items())
            random.shuffle(items)

            # Weise neue Buchstaben zu und erstelle Mapping alt->neu
            new_letters = ['a', 'b', 'c', 'd'][:len(items)]
            new_options = []
            new_correct = []
            letter_mapping = {}  # alt -> neu

            for i, (old_letter, text) in enumerate(items):
                new_letter = new_letters[i]
                letter_mapping[old_letter] = new_letter
                new_options.append(f"{new_letter}) {text}")
                # Wenn dieser Text korrekt war, merke neuen Buchstaben
                if text in correct_texts:
                    new_correct.append(new_letter)

            q['options'] = new_options
            q['correct'] = sorted(new_correct)

            # Aktualisiere auch die Erklärung
            explanation = q.get('explanation', '')
            for old_l, new_l in letter_mapping.items():
                # Ersetze "Richtig: x)" -> "Richtig: y)"
                explanation = re.sub(
                    rf'(Richtig:\s*){old_l}\)',
                    rf'\g<1>{new_l})',
                    explanation
                )
                # Ersetze "Richtig: x<" -> "Richtig: y<"
                explanation = re.sub(
                    rf'(Richtig:\s*){old_l}<',
                    rf'\g<1>{new_l}<',
                    explanation
                )
            q['explanation'] = explanation

            mc_randomized += 1

    print(f"  {mc_randomized} MC-Fragen randomisiert.")

    # Verteilung der korrekten Antworten ausgeben
    answer_dist = {}
    for q in all_questions:
        if q['type'] == 'mc':
            for c in q.get('correct', []):
                answer_dist[c] = answer_dist.get(c, 0) + 1
    if answer_dist:
        dist_str = ', '.join(f"{k}:{v}" for k, v in sorted(answer_dist.items()))
        print(f"  Verteilung korrekte Antworten: {dist_str}")

    # Statistik zaehlen
    for q in all_questions:
        qtype = q["type"]
        if qtype in stats:
            stats[qtype] += 1

    # JSON erzeugen
    questions_json = json.dumps(all_questions, ensure_ascii=False, indent=2)

    # Template lesen
    if not os.path.exists(TEMPLATE_FILE):
        print(f"FEHLER: Template-Datei {TEMPLATE_FILE} nicht gefunden!", file=sys.stderr)
        sys.exit(1)

    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    # Placeholder ersetzen
    html = template.replace('{{QUESTIONS_JSON}}', questions_json)

    # quiz.html schreiben
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    # Dateigroesse ermitteln
    file_size = os.path.getsize(OUTPUT_FILE)
    if file_size >= 1024 * 1024:
        size_str = f"{file_size / (1024 * 1024):.1f} MB"
    else:
        size_str = f"{file_size / 1024:.1f} KB"

    # Stats ausgeben
    total = len(all_questions)
    print(f"\nParsed {total} questions:")
    print(f"  yesno: {stats['yesno']}")
    print(f"  mc: {stats['mc']}")
    print(f"  truefalse: {stats['truefalse']}")
    print(f"  freetext: {stats['freetext']}")
    print(f"Generated quiz.html ({size_str})")


if __name__ == "__main__":
    main()
