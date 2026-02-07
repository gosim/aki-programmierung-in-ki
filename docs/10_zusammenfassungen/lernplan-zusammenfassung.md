# Python Lernplan - Klausur 07.02.2026

## Inhaltsverzeichnis

1. [Grundlagen (Kapitel 1-2)](#1-grundlagen-kapitel-1-2) - Datentypen, Built-ins, Operatoren
2. [Bedingte Ausfuehrung (Kapitel 3)](#2-bedingte-ausfuehrung-kapitel-3) - if/elif/else, try-except
3. [Funktionen (Kapitel 4)](#3-funktionen-kapitel-4) - def, return, *args, **kwargs
4. [Schleifen (Kapitel 5)](#4-schleifen-kapitel-5) - for, while, break, continue
5. [Strings (Kapitel 6)](#5-strings-kapitel-6) - Slicing, Methoden, Umlaute
6. [Dateien (Kapitel 7)](#6-dateien-kapitel-7) - open, read, write
7. [Listen (Kapitel 8)](#7-listen-kapitel-8) - Methoden, List Comprehension
8. [Dictionaries (Kapitel 9)](#8-dictionaries-kapitel-9---klausurrelevant) - dict.get(), Zaehlmuster ⭐
9. [Tupel (Kapitel 10)](#9-tupel-kapitel-10) - Unpacking, Vergleich zu Listen
10. [OOP (Kapitel 14)](#10-oop---objektorientierte-programmierung-kapitel-14) - Klassen, Objekte
11. [Zusaetzliche Module](#11-zusaetzliche-module) - import, Set, random
12. [NumPy (Kapitel 3)](#12-numpy-kapitel-3) - Arrays, Slicing, Operationen ⭐
13. [Matplotlib (Kapitel 4)](#13-matplotlib-kapitel-4) - Plots, Subplots, Speichern
14. [Regulaere Ausdruecke (Kapitel 11)](#14-regulaere-ausdruecke-kapitel-11) - re.search, re.findall, Muster
15. [Praktische Beispiele](#15-praktische-beispiele) - Lohn, Fibonacci, etc.
16. [Klausurtipps](#16-klausurtipps) - Fallen, Lernplan ⭐

---

## Klausurstruktur (60 Punkte, 1 Stunde)

| Aufgabe | Punkte | Thema |
|---------|--------|-------|
| 1 | 30 | Code-Verstaendnis (for-Schleife, try-except, dict.get()) |
| 2 | 15 | FizzBuzz (Modulo, Teilbarkeit durch 3/5) |
| 3 | 15 | Textverarbeitung (lower(), Umlaute ersetzen) |

---

# 1. Grundlagen (Kapitel 1-2)

## Datentypen und Typumwandlung

| Typ | Beschreibung | Beispiele |
|-----|--------------|-----------|
| `int` | Ganzzahlen | `42`, `-7`, `0` |
| `float` | Gleitkommazahlen | `3.14`, `-2.5`, `1.0` |
| `str` | Zeichenketten | `"Hallo"`, `'Python'` |
| `bool` | Wahrheitswerte | `True`, `False` |

```python
# Typumwandlung
int("42")      # 42
str(42)        # "42"
float("3.14")  # 3.14
list("abc")    # ['a', 'b', 'c']
bool(0)        # False
bool("")       # False
bool([])       # False
bool(1)        # True
```

## Built-in-Funktionen

| Funktion | Beschreibung | Beispiel | Ergebnis |
|----------|--------------|----------|----------|
| `print()` | Ausgabe auf Konsole | `print("Hallo")` | Hallo |
| `input()` | Eingabe vom Benutzer | `name = input("Name: ")` | (wartet) |
| `len()` | Laenge (String, Liste) | `len("abc")` | `3` |
| `type()` | Datentyp abfragen | `type(42)` | `<class 'int'>` |
| `int()` | In Ganzzahl umwandeln | `int("5")` | `5` |
| `str()` | In String umwandeln | `str(5)` | `"5"` |
| `float()` | In Dezimalzahl | `float("3.14")` | `3.14` |
| `bool()` | In Boolean | `bool(0)` | `False` |
| `range()` | Zahlenbereich erzeugen | `range(5)` | `0, 1, 2, 3, 4` |
| `sum()` | Summe einer Liste | `sum([1, 2, 3])` | `6` |
| `min()` | Minimum | `min(1, 2, 3)` | `1` |
| `max()` | Maximum | `max(1, 2, 3)` | `3` |
| `abs()` | Absolutwert | `abs(-5)` | `5` |
| `round()` | Runden | `round(3.7)` | `4` |
| `sorted()` | Sortierte Kopie | `sorted([3,1,2])` | `[1, 2, 3]` |
| `list()` | In Liste umwandeln | `list("abc")` | `["a","b","c"]` |
| `enumerate()` | Index + Wert | `enumerate(["a","b"])` | `(0,"a"), (1,"b")` |

**KLAUSURFALLE: input() gibt IMMER einen String zurueck!**
```python
alter = input("Alter: ")    # alter ist "25" (String!)
alter = int(input("Alter: "))  # alter ist 25 (Integer)
```

## Operatoren (Arithmetisch, Vergleich, Modulo)

| Operator | Beschreibung | Beispiel | Ergebnis |
|----------|--------------|----------|----------|
| `+` `-` `*` `/` | Grundrechenarten | `7 / 2` | `3.5` |
| `//` | Ganzzahldivision | `7 // 2` | `3` |
| `%` | Modulo (Rest) | `7 % 2` | `1` |
| `**` | Potenz | `2 ** 3` | `8` |
| `==` `!=` | gleich, ungleich | `5 == 5` | `True` |
| `<` `>` `<=` `>=` | Vergleiche | `3 < 5` | `True` |

**Modulo fuer Teilbarkeit (KLAUSURRELEVANT!):**
```python
x % 2 == 0   # x ist gerade
x % 3 == 0   # x ist durch 3 teilbar
x % 15 == 0  # x ist durch 15 teilbar (3 UND 5)
```

**FizzBuzz-Logik (KLAUSURAUFGABE!):**
```python
for x in range(1, 101):
    if x % 15 == 0:      # ZUERST 15 pruefen!
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
```

**Verkettete Vergleiche:**
```python
if 0 <= x <= 100:    # Statt: if x >= 0 and x <= 100
    print("Gueltig")
```

## Variablen und Zuweisungen

```python
x = 42                # Einfache Zuweisung
a, b = 10, 20         # Mehrfachzuweisung
x += 1                # x = x + 1
x -= 5                # x = x - 5
x *= 2                # x = x * 2
```

---

# 2. Bedingte Ausfuehrung (Kapitel 3)

## if-Anweisung und logische Operatoren

```python
# if / elif / else
if x > 0:
    print("Positiv")
elif x < 0:
    print("Negativ")
else:
    print("Null")

# Einzeiler (ternary)
ergebnis = "ja" if x > 0 else "nein"

# Logische Operatoren
x > 0 and x < 10      # UND
x == 0 or x == 1      # ODER
not x > 0             # Negation
```

## try-except und Exceptions

```python
# Grundform
try:
    zahl = int(input("Zahl: "))  # Kann ValueError werfen
    ergebnis = 10 / zahl         # Kann ZeroDivisionError werfen
except ValueError:
    print("Keine gueltige Zahl!")
except ZeroDivisionError:
    print("Division durch Null!")
except:
    print("Unbekannter Fehler!")

# Mit Wiederholung
while True:
    try:
        zahl = int(input("Zahl: "))
        break  # Schleife verlassen wenn erfolgreich
    except ValueError:
        print("Bitte eine Zahl eingeben!")

# Mit quit() bei Fehler
try:
    f = open("datei.txt")
except FileNotFoundError:
    print("Datei nicht gefunden!")
    quit()

# Multiple Exceptions
try:
    zahl = float(input("Zahl: "))
except (ValueError, TypeError):
    print("Fehler bei Eingabe")
    quit()
```

**Haeufige Exceptions:**

| Exception | Ursache |
|-----------|---------|
| `ValueError` | Falscher Wert (z.B. `int("abc")`) |
| `TypeError` | Falscher Typ (z.B. `"a" + 1`) |
| `ZeroDivisionError` | Division durch Null |
| `IndexError` | Index ausserhalb des Bereichs |
| `KeyError` | Schluessel nicht im Dictionary |
| `FileNotFoundError` | Datei nicht gefunden |

---

# 3. Funktionen (Kapitel 4)

## Funktionen definieren und aufrufen

```python
# Mit Parametern und Standardwert
def gruessen(name="Welt"):
    print(f"Hallo, {name}!")

# Mit Rueckgabewert
def quadrat(x):
    return x * x

# Aufruf
ergebnis = quadrat(5)        # 25
gruessen()                    # Hallo, Welt!
gruessen("Anna")              # Hallo, Anna!

# Mehrere Rueckgabewerte (Tupel)
def min_max(zahlen):
    return min(zahlen), max(zahlen)

minimum, maximum = min_max([3, 1, 4, 1, 5])
```

## Lokale vs. globale Variablen

```python
x = 10  # Globale Variable

def funktion():
    x = 5  # Lokale Variable (ueberdeckt globale!)
    print(x)

funktion()  # Ausgabe: 5
print(x)    # Ausgabe: 10 (globale unveraendert)

# Mit global-Keyword:
def aendern():
    global x
    x = 5

aendern()
print(x)  # Ausgabe: 5
```

## *args und **kwargs

```python
# *args - sammelt Positions-Argumente als Tupel
def summe(*zahlen):
    print(type(zahlen))  # <class 'tuple'>
    return sum(zahlen)

print(summe(1, 2, 3, 4, 5))  # 15

# **kwargs - sammelt Keyword-Argumente als Dictionary
def person_info(**daten):
    print(type(daten))  # <class 'dict'>
    for key, value in daten.items():
        print(f"{key}: {value}")

person_info(name="Anna", alter=25)

# Reihenfolge: normale Parameter, Standardwert, *args, **kwargs
def beispiel(a, b, c=10, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

beispiel(1, 2, 3, 4, 5, name="Test", wert=42)
# a=1, b=2, c=3
# args=(4, 5)
# kwargs={'name': 'Test', 'wert': 42}

# Entpacken
zahlen = [1, 2, 3]
print(*zahlen)        # 1 2 3

daten = {"name": "Max", "alter": 30}
person_info(**daten)  # Wie: person_info(name="Max", alter=30)
```

---

# 4. Schleifen (Kapitel 5)

## for-Schleife

```python
# range(stop) - von 0 bis stop-1
for i in range(5):      # 0, 1, 2, 3, 4 (NICHT 5!)
    print(i)

# range(start, stop, step)
for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
for i in range(10, 0, -1): # 10, 9, 8, ..., 1
    print(i)

# Ueber String/Liste iterieren
for zeichen in "abc":
    print(zeichen)  # a, b, c

for element in [1, 2, 3]:
    print(element)

# Mit Index (enumerate)
for i, element in enumerate(["a", "b", "c"]):
    print(i, element)  # 0 a, 1 b, 2 c
```

**KLAUSURFALLE: for-Schleife ueberschreibt Variable!**
```python
i = 27
for i in range(3):  # i wird 0, 1, 2 - nicht 27!
    pass
print(i)  # Ausgabe: 2 (NICHT 27!)
```

## while-Schleife, break und continue

```python
x = 0
while x < 5:
    print(x)
    x += 1

# break - Schleife sofort beenden
for i in range(10):
    if i == 5:
        break
    print(i)  # Ausgabe: 0, 1, 2, 3, 4

# continue - Zum naechsten Durchlauf springen
for i in range(5):
    if i == 2:
        continue
    print(i)  # Ausgabe: 0, 1, 3, 4 (2 uebersprungen)
```

---

# 5. Strings (Kapitel 6)

## String-Grundlagen, Slicing und Methoden

**Strings sind unveraenderlich (immutable)!**
```python
text = "Hallo"
text[0] = "M"       # FEHLER! TypeError
text = "M" + text[1:]  # "Mallo" - neuen String erzeugen

# WICHTIG: Ergebnis von Methoden SPEICHERN!
text = "HALLO"
text.lower()        # Gibt "hallo" zurueck, text bleibt "HALLO"
text = text.lower() # Jetzt ist text = "hallo"
```

**Indizierung und Slicing:**
```python
s = "Python"
#    0  1  2  3  4  5   (positive Indizes)
#   -6 -5 -4 -3 -2 -1   (negative Indizes)

s[0]      # "P"     - erstes Zeichen
s[-1]     # "n"     - letztes Zeichen
s[1:4]    # "yth"   - Index 1 bis 3 (4 ist EXKLUSIV!)
s[:3]     # "Pyt"   - von Anfang bis Index 2
s[2:]     # "thon"  - von Index 2 bis Ende
s[::-1]   # "nohtyP" - UMKEHREN!
```

**String-Methoden:**

| Methode | Beschreibung | Beispiel | Ergebnis |
|---------|--------------|----------|----------|
| `lower()` | Kleinbuchstaben | `"ABC".lower()` | `"abc"` |
| `upper()` | Grossbuchstaben | `"abc".upper()` | `"ABC"` |
| `strip()` | Leerzeichen entfernen | `"  hi  ".strip()` | `"hi"` |
| `split()` | In Liste aufteilen | `"a b c".split()` | `["a","b","c"]` |
| `replace(a,b)` | Ersetzen | `"hallo".replace("l","x")` | `"haxxo"` |
| `find(x)` | Position (-1 wenn fehlt) | `"hallo".find("x")` | `-1` |
| `startswith(x)` | Anfang pruefen | `"hallo".startswith("ha")` | `True` |
| `count(x)` | Anzahl zaehlen | `"hallo".count("l")` | `2` |
| `join()` | Liste verbinden | `" ".join(["a","b"])` | `"a b"` |

```python
"Hallo" + " Welt"   # "Hallo Welt" - Verkettung
"ab" * 3            # "ababab" - Wiederholung
"x" in "text"       # True - Enthalten?
```

## Umlaute ersetzen (KLAUSURAUFGABE!)

```python
# Loesung 1: Mit mehreren replace()
def text_bereinigen(text):
    text = text.lower()
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")
    return text

# Loesung 2: Mit Dictionary (eleganter!)
def text_bereinigen(text):
    text = text.lower()
    ersetzungen = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}
    for alt, neu in ersetzungen.items():
        text = text.replace(alt, neu)
    return text

print(text_bereinigen("Größe"))  # 'groesse'
```

---

# 6. Dateien (Kapitel 7)

## Dateien lesen und schreiben

```python
# Lesen mit with-Statement (empfohlen!)
with open("daten.txt", "r") as datei:
    inhalt = datei.read()
# Datei wird automatisch geschlossen

# Zeilenweise iterieren
with open("daten.txt", "r") as datei:
    for zeile in datei:
        zeile = zeile.strip()  # Zeilenumbruch entfernen!
        words = zeile.split()
        print(words)

# Schreiben (ueberschreibt!)
with open("ausgabe.txt", "w") as datei:
    datei.write("Zeile 1\n")

# Anhaengen
with open("log.txt", "a") as datei:
    datei.write("Neuer Eintrag\n")

# Fehlerbehandlung
try:
    with open("datei.txt", "r") as f:
        inhalt = f.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
    quit()
```

**Dateimodi:** `"r"` Lesen, `"w"` Schreiben (ueberschreibt), `"a"` Anhaengen

---

# 7. Listen (Kapitel 8)

## Listen-Grundlagen und Methoden

**Listen sind veraenderbar (mutable)!**
```python
zahlen = [1, 2, 3, 4, 5]
zahlen[0] = 99  # [99, 2, 3, 4, 5] - Aendern moeglich!

# Zugriff (wie Strings)
liste[0]      # 1
liste[-1]     # 5
liste[1:3]    # [2, 3]
liste[::-1]   # [5, 4, 3, 2, 1]

# Hinzufuegen
lst.append(5)       # am Ende
lst.insert(0, 0)    # an Index
lst.extend([7, 8])  # mehrere

# Entfernen
lst.pop()           # letztes entfernen + zurueckgeben
lst.pop(0)          # an Index entfernen
lst.remove(2)       # ERSTES Vorkommen von 2 entfernen
del lst[0]          # an Index loeschen

# Suchen
3 in lst            # True - enthalten?
lst.index(3)        # Index (ValueError wenn nicht gefunden!)
lst.count(2)        # Anzahl

# Sortieren
lst.sort()              # aufsteigend (aendert Liste!)
lst.sort(reverse=True)  # absteigend
sorted(lst)             # NEUE sortierte Liste
lst.reverse()           # Reihenfolge umkehren

# Aggregatfunktionen
len(lst), sum(lst), min(lst), max(lst)

# Durchlaufen
for element in liste:
    print(element)
for i, element in enumerate(liste):
    print(f"{i}: {element}")
```

**WICHTIG: Unterschied index() vs. find()**
```python
"hallo".find("x")   # -1 (String: gibt -1 wenn nicht gefunden)
[1, 2, 3].index(5)  # ValueError! (Liste: wirft Fehler!)

# Sicher pruefen:
if 5 in lst:
    pos = lst.index(5)
```

## List Comprehension

```python
quadrate = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, ...]
gerade = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

# 8. Dictionaries (Kapitel 9) - KLAUSURRELEVANT!

## Dictionary-Grundlagen und Methoden

```python
# Erstellen
d = {}
student = {"name": "Anna", "alter": 22}

# Zugriff
student["name"]           # "Anna" - KeyError wenn Key fehlt!
student.get("name")       # "Anna" - None wenn Key fehlt
student.get("note", 0)    # 0 (Standardwert wenn Key fehlt)

# Aendern/Hinzufuegen/Entfernen
student["name"] = "Max"   # Aendern
student["note"] = 1.3     # Hinzufuegen
del student["name"]       # Loeschen
student.pop("name")       # Loeschen + zurueckgeben

# Pruefen
"name" in student         # True - Key vorhanden?
len(student)              # Anzahl Eintraege

# Methoden
d.keys()                  # alle Schluessel
d.values()                # alle Werte
d.items()                 # alle (Key, Value) Paare
list(d.items())           # in Liste konvertieren

# Durchlaufen
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(f"{key}: {value}")
```

## dict.get() und Zaehlmuster - AUSWENDIG LERNEN!

```python
d = {"a": 1, "b": 2}
d["c"]              # KeyError! Programm stuerzt ab!
d.get("c")          # None (kein Fehler)
d.get("c", 0)       # 0 (Standardwert)

# Das Zaehlmuster:
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

# Schritt fuer Schritt:
words = ["a", "b", "a"]
count = {}
# word="a": count.get("a",0)=0 → count["a"]=1
# word="b": count.get("b",0)=0 → count["b"]=1
# word="a": count.get("a",0)=1 → count["a"]=2
# Ergebnis: {"a": 2, "b": 1}
```

## Maximum aus Dictionary finden

```python
d = {"anna": 3, "ben": 5, "clara": 2}

# Tupel-Liste erstellen (Wert, Schluessel)
lst = []
for key, val in d.items():
    lst.append((val, key))
# lst = [(3, "anna"), (5, "ben"), (2, "clara")]

# Sortieren und Maximum
lst.sort(reverse=True)
print(lst[0][1], lst[0][0])  # "ben" 5
```

## Praktisches Beispiel: E-Mail-Adressen zaehlen

```python
def count_mail_adresses(filename):
    mail_counts = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                sender = words[1]
                mail_counts[sender] = mail_counts.get(sender, 0) + 1
    return mail_counts

# Maximum finden
counts = count_mail_adresses("mbox.txt")
lst = [(val, key) for key, val in counts.items()]
lst.sort(reverse=True)
print(lst[0][1], lst[0][0])
```

---

# 9. Tupel (Kapitel 10)

## Tupel-Grundlagen und Unpacking

```python
# Erstellen
t = (1, 2, 3)
t = 1, 2, 3           # Klammern optional
t = (5,)              # Einelementig: Komma wichtig!
t = (5)               # NUR die Zahl 5, kein Tupel!

# Tupel sind unveraenderlich!
t[0] = 99  # TypeError!

# Zugriff (wie Listen)
t[0], t[-1], t[1:3]

# Tuple Unpacking
x, y = (10, 20)
a, b = b, a           # Variablen tauschen!

# In for-Schleifen
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

**Tupel vs. Listen:**

| Eigenschaft | Tupel | Liste |
|-------------|-------|-------|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Veraenderbar | Nein | Ja |
| Als Dict-Key | Ja | Nein |

---

# 10. OOP - Objektorientierte Programmierung (Kapitel 14)

## Klassen und Objekte

**Unterschied Klasse vs. Objekt (PROBEKLAUSUR!):**
- **Klasse:** Bauplan/Vorlage - definiert WAS ein Objekt hat/kann
- **Objekt:** Konkrete Instanz - HAT eigene Werte
- **Merkregel:** Klasse = Keksausstecher, Objekte = Kekse

```python
class Student:
    def __init__(self, name, matrikel):  # Konstruktor
        self.name = name                  # Instanzattribut
        self.matrikel = matrikel

    def __str__(self):                    # fuer print()
        return f"Student: {self.name} ({self.matrikel})"

    def vorstellen(self):                 # Methode
        print(f"Ich bin {self.name}")

# Objekte erstellen und verwenden
s1 = Student("Anna", 12345)
print(s1.name)      # "Anna"
s1.vorstellen()     # "Ich bin Anna"
print(s1)           # "Student: Anna (12345)"
```

**__init__ und self:**
- `__init__` = Konstruktor (bei Objekterstellung aufgerufen)
- `self` = Referenz auf aktuelles Objekt
- Alle Methoden brauchen `self` als ersten Parameter

## Beispiel: Student mit Noten

```python
class Student:
    def __init__(self, name, noten=None):
        self.name = name
        self.noten = noten if noten else []

    def note_hinzufuegen(self, note):
        self.noten.append(note)

    def durchschnitt(self):
        if len(self.noten) == 0:
            return 0
        return sum(self.noten) / len(self.noten)

s = Student("Anna")
s.note_hinzufuegen(1.3)
s.note_hinzufuegen(2.0)
print(s.durchschnitt())  # 1.65
```

---

# 11. Zusaetzliche Module

## Module importieren (PROBEKLAUSUR!)

```python
import math               # Ganzes Modul
print(math.sqrt(16))      # 4.0

import math as m          # Mit Alias
print(m.sqrt(16))

from math import sqrt     # Nur bestimmte Funktion
print(sqrt(16))           # Ohne Prefix!

from math import sqrt, pi, sin  # Mehrere

# Konventionen:
import numpy as np
import pandas as pd
```

## Set (Menge) - PROBEKLAUSUR!

```python
# Dictionary vs Set:
# Dict: {"a": 1, "b": 2} - Key-Value-Paare
# Set:  {1, 2, 3}        - nur Werte, KEINE Duplikate

s = {1, 2, 2, 3, 3}       # {1, 2, 3} - Duplikate entfernt!
eindeutig = set([1,2,2,3])  # Liste zu Set
print(eindeutig)            # {1, 2, 3}
3 in s                    # True

# set() funktioniert mit JEDEM Iterable, nicht nur Listen!
set((1, 2, 2, 3))        # {1, 2, 3} - Tupel
set("hallo")             # {'h', 'a', 'l', 'o'} - String
set(range(5))            # {0, 1, 2, 3, 4} - Range

# KLAUSURFALLE: Leeres Set vs. leeres Dictionary!
leer = set()             # leeres Set
leer = {}                # ACHTUNG: leeres Dictionary, KEIN Set!

# Set-Operationen
a, b = {1, 2, 3}, {2, 3, 4}
a | b    # {1, 2, 3, 4} - Vereinigung
a & b    # {2, 3} - Schnittmenge
a - b    # {1} - Differenz ("Was hat a, was b nicht hat?")
b - a    # {4} - Differenz ("Was hat b, was a nicht hat?")
```

## Random-Modul

```python
from random import randint, choice, shuffle

wuerfel = randint(1, 6)       # 1-6 (inklusive!)
auswahl = choice(["a","b"])   # Zufaelliges Element
shuffle(liste)                # Liste mischen (in-place!)
```

---

# 12. NumPy (Kapitel 3)

## Arrays erstellen (PROBEKLAUSUR!)

```python
import numpy as np

# Aus Listen
a = np.array([1, 2, 3])              # 1D-Array
m = np.array([[1, 2, 3], [4, 5, 6]]) # 2D-Array (Matrix)

# Spezielle Arrays
np.zeros((2, 3))     # 2x3 mit Nullen (float!)
np.ones((3, 3))      # 3x3 mit Einsen
np.eye(3)            # 3x3 Einheitsmatrix
np.diag([1, 2, 3])   # Diagonalmatrix

# Zahlenfolgen
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8] - wie range()
np.linspace(0, 1, 5)      # [0, 0.25, 0.5, 0.75, 1.0] - gleichmaessig verteilt
```

## Array-Attribute

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape    # (2, 3) - Dimensionen (Zeilen, Spalten)
a.ndim     # 2 - Anzahl Dimensionen
a.size     # 6 - Gesamtanzahl Elemente
a.dtype    # int64 - Datentyp
```

## Reshape und Transponieren

```python
a = np.arange(12)          # [0, 1, 2, ..., 11]
b = a.reshape(3, 4)        # 3x4 Matrix
# [[0,  1,  2,  3],
#  [4,  5,  6,  7],
#  [8,  9, 10, 11]]

b.T                         # Transponiert (4x3)
# [[ 0,  4,  8],
#  [ 1,  5,  9],
#  [ 2,  6, 10],
#  [ 3,  7, 11]]
```

**KLAUSURFALLE: reshape erzeugt eine ANSICHT (View), keine Kopie!**
```python
m1 = np.arange(4)
m2 = m1.reshape(2, 2)
m1[0] = 99          # Aendert AUCH m2!
# m2 = [[99, 1], [2, 3]]
```

## Array-Slicing (2D)

```python
a = np.arange(36).reshape(6, 6)
# [[ 0,  1,  2,  3,  4,  5],
#  [ 6,  7,  8,  9, 10, 11],
#  [12, 13, 14, 15, 16, 17],
#  [18, 19, 20, 21, 22, 23],
#  [24, 25, 26, 27, 28, 29],
#  [30, 31, 32, 33, 34, 35]]

a[2, 3]          # 15 - Element in Zeile 2, Spalte 3
a[2:4, 2:4]      # [[14, 15], [20, 21]] - Teilmatrix
a[:, 0]          # [0, 6, 12, 18, 24, 30] - ganze Spalte 0
a[0, :]          # [0, 1, 2, 3, 4, 5] - ganze Zeile 0
a[::2, ::2]      # Jede zweite Zeile/Spalte
```

**WICHTIG: Spalten direkt ansprechen - Vorteil gegenueber verschachtelten Listen!**

## Elementweise Operationen (PROBEKLAUSUR!)

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.ones((3, 3))

# Elementweise (jedes Element einzeln!)
c = a + b    # Addition
c = a * b    # Multiplikation
c = a ** 2   # Quadrieren
c = a * 3    # Skalar * Array (Broadcasting)

#  a:          b:          c = a + b:
# [1, 2, 3]   [1, 1, 1]   [2,  3,  4]
# [4, 5, 6] + [1, 1, 1] = [5,  6,  7]
# [7, 8, 9]   [1, 1, 1]   [8,  9, 10]

# Matrizenmultiplikation (NICHT elementweise!)
c = a @ b    # oder: np.dot(a, b)
```

**KLAUSURFALLE: `*` ist elementweise, `@` ist Matrizenmultiplikation!**

## Aggregatfunktionen mit axis

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

a.sum()          # 21 - Summe aller Elemente
a.sum(axis=0)    # [5, 7, 9] - Summe pro Spalte (ueber Zeilen)
a.sum(axis=1)    # [6, 15] - Summe pro Zeile (ueber Spalten)

a.min(), a.max()          # Minimum/Maximum
a.mean()                  # Durchschnitt
np.sqrt(a)                # Wurzel (elementweise)
```

**Merkregel axis:** `axis=0` → entlang Zeilen (↓), `axis=1` → entlang Spalten (→)

## Boolean Indexing

```python
a = np.array([1, 5, 3, 8, 2, 7])
mask = a > 4            # [False, True, False, True, False, True]
a[mask]                 # [5, 8, 7] - nur Elemente > 4
a[a > 4] = 0            # Alle Werte > 4 auf 0 setzen
```

## Zufallszahlen mit NumPy

```python
np.random.rand(2, 3)        # 2x3 Zufallswerte zwischen 0 und 1
np.random.randint(1, 7, 10) # 10 Wuerfelwuerfe (1-6)
np.random.seed(42)          # Reproduzierbare Ergebnisse
```

---

# 13. Matplotlib (Kapitel 4)

## Import und einfacher Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

## Achsenbeschriftung, Titel und Legende

```python
x = np.linspace(0, 10, 30)
y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x, y1, label="Kosinus")
plt.plot(x, y2, label="Sinus")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("Trigonometrische Funktionen")
plt.legend()
plt.grid()
plt.show()
```

## Linien-Stile, Farben und Marker

```python
# Format-String: 'FarbeMarkerLinie'
plt.plot(x, y1, 'ro-')    # rot, Kreise, durchgezogen
plt.plot(x, y2, 'b--')    # blau, gestrichelt
plt.plot(x, y1, 'g^:')    # gruen, Dreiecke, gepunktet

# Oder mit Keywords
plt.plot(x, y1, color='red', linestyle='--', linewidth=2, marker='o')
```

| Farbe | Code | Linie | Code | Marker | Code |
|-------|------|-------|------|--------|------|
| Blau | `b` | Durchgezogen | `-` | Punkt | `.` |
| Rot | `r` | Gestrichelt | `--` | Kreis | `o` |
| Gruen | `g` | Strich-Punkt | `-.` | Dreieck | `^` |
| Schwarz | `k` | Gepunktet | `:` | Quadrat | `s` |

## Scatter Plot und Histogramm

```python
# Scatter Plot
plt.scatter(x, y, c='red', s=20)   # c=Farbe, s=Groesse

# Histogramm
daten = np.random.randn(1000)
plt.hist(daten, bins=30)
plt.show()
```

## Subplots (mehrere Plots)

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5))

ax1.plot(x, y1)
ax1.set_ylabel("cos(t)")

ax2.plot(x, y2)
ax2.set_xlabel("t")
ax2.set_ylabel("sin(t)")

plt.show()
```

## Speichern

```python
plt.savefig("plot.png")   # als PNG (Bitmap)
plt.savefig("plot.pdf")   # als PDF (Vektor)
```

## Contour-Plot (2D-Funktionen)

```python
x, y = np.mgrid[-3:3:100j, -3:3:100j]
z = np.sin(x) * np.cos(y)

plt.contourf(x, y, z, levels=10, cmap='viridis')
plt.colorbar()
plt.show()
```

## 3D-Plot

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
```

---

# 14. Regulaere Ausdruecke (Kapitel 11)

## Import und Grundlagen

```python
import re

# re.search() - Pruefen ob Muster vorkommt
if re.search('From:', line):
    print(line)

# ^ fuer Zeilenanfang
if re.search('^From:', line):
    print(line)
```

## Sonderzeichen und Muster

| Zeichen | Bedeutung | Beispiel |
|---------|-----------|----------|
| `.` | Ein beliebiges Zeichen | `F..m` passt auf `From`, `Fxxm` |
| `^` | Zeilenanfang | `^From` - Zeile beginnt mit "From" |
| `$` | Zeilenende | `end$` - Zeile endet mit "end" |
| `\d` | Eine Ziffer `[0-9]` | `\d{5}` - fuenf Ziffern (PLZ) |
| `\D` | Keine Ziffer `[^0-9]` | |
| `\w` | Wortzeichen `[a-zA-Z0-9_]` | `\w+` - ein Wort |
| `\W` | Kein Wortzeichen | |
| `\s` | Leerzeichen/Whitespace | `\s+` - ein oder mehr Leerzeichen |
| `\S` | Kein Leerzeichen | `\S+@\S+` - E-Mail-Muster |
| `\b` | Wortgrenze | `\bHallo\b` - ganzes Wort |

## Quantoren (Wiederholungen)

| Quantor | Bedeutung | Beispiel |
|---------|-----------|----------|
| `+` | 1 oder mehr | `\d+` - mindestens eine Ziffer |
| `*` | 0 oder mehr | `\d*` - Ziffern optional |
| `?` | 0 oder 1 | `\d?` - hoechstens eine Ziffer |
| `{n}` | Genau n mal | `\d{5}` - genau 5 Ziffern |
| `+?` | Non-greedy (so wenig wie moeglich) | |

## Zeichenklassen

```python
[a-z]        # Kleinbuchstaben a-z
[A-Z]        # Grossbuchstaben A-Z
[0-9]        # Ziffern (wie \d)
[a-zA-Z0-9]  # Buchstaben und Ziffern
[^0-9]       # NICHT Ziffern (invertiert mit ^)
[aeiou]      # Nur Vokale
```

## re.findall() - Alle Treffer extrahieren

```python
import re

# Alle E-Mail-Adressen finden
s = 'Von csev@umich.edu an cwen@iupui.edu'
lst = re.findall('\S+@\S+', s)
print(lst)  # ['csev@umich.edu', 'cwen@iupui.edu']

# Alle Zahlen finden
s = 'Preis: 12.50 Euro, Rabatt: 3.00'
lst = re.findall('[0-9.]+', s)
print(lst)  # ['12.50', '3.00']

# Postleitzahlen finden (genau 5 Ziffern)
text = "58590 Iserlohn und 58095 Hagen"
lst = re.findall(r'\d{5}', text)
print(lst)  # ['58590', '58095']
```

## Klammern () fuer selektives Extrahieren

```python
# OHNE Klammern: ganzer Match
re.findall('\S+@\S+', text)        # ['csev@umich.edu']

# MIT Klammern: nur der Teil IN den Klammern
re.findall('^From (\S+)', line)    # ['csev@umich.edu']

# Mehrere Gruppen → Tupel
re.findall(r'([\w.-]+)@([\w.-]+)', text)
# [('csev', 'umich.edu')]

# Stunde aus Zeitstempel extrahieren
# "From user@host Sat Jan 5 09:14:16 2008"
re.findall('^From .* ([0-9][0-9]):', line)  # ['09']
```

## match.group() - Gruppen aus re.search()

```python
import re

m = re.search(r'(\w+)@(\w+)', 'Mail: anna@fh.de')

# Pruefen ob Match gefunden wurde!
if m:
    m.group()    # 'anna@fh.de'  - ganzer Match
    m.group(0)   # 'anna@fh.de'  - dasselbe wie group()
    m.group(1)   # 'anna'        - erste Klammer
    m.group(2)   # 'fh'          - zweite Klammer

# KLAUSURFALLE: Immer pruefen ob Match existiert!
m = re.search(r'\d+', 'kein Treffer')
# m ist None → m.group() wuerde AttributeError werfen!
if m:
    print(m.group())
```

**Unterschied findall() vs. search().group():**
- `re.findall()` → gibt **Liste** aller Treffer zurueck
- `re.search().group()` → gibt nur den **ersten** Treffer zurueck

## re.sub() - Suchen und Ersetzen

```python
import re

# Alle Ziffern entfernen
text = "Haus Nr. 42 in 58095 Hagen"
neu = re.sub(r'\d+', '', text)
print(neu)  # "Haus Nr.  in  Hagen"

# Artikel am Zeilenanfang entfernen
text = "Der Rektor ist seit 2024 da"
neu = re.sub(r'^(Der|Die|Das) ', '', text)
print(neu)  # "Rektor ist seit 2024 da"
```

## Escapezeichen

```python
# Sonderzeichen mit \ escapen
re.findall(r'\$[0-9.]+', 'Preis: $10.00')  # ['$10.00']
# \$ = echtes Dollarzeichen, \. = echter Punkt
```

**WICHTIG: Immer Raw-Strings `r'...'` fuer Regex-Muster verwenden!**

## Praktische Beispiele

```python
# E-Mail-Adressen aus Datei zaehlen
import re

counts = {}
with open('mbox.txt') as f:
    for line in f:
        if re.search('^From ', line):
            emails = re.findall('\S+@\S+', line)
            for email in emails:
                counts[email] = counts.get(email, 0) + 1

# Durchschnitt von extrahierten Zahlen
zahlen = []
with open('mbox.txt') as f:
    for line in f:
        found = re.findall('^New Revision: ([0-9.]+)', line)
        for z in found:
            zahlen.append(float(z))
print(sum(zahlen) / len(zahlen))
```

**Regex testen:** [regex101.com](https://regex101.com)

---

# 15. Praktische Beispiele

```python
# Lohnberechnung mit Ueberstunden
def lohnberechnung(stundenlohn, arbeitsstunden):
    if arbeitsstunden > 40:
        return 40 * stundenlohn + (arbeitsstunden - 40) * stundenlohn * 1.5
    return arbeitsstunden * stundenlohn

# Durchschnitt mit done-Abbruch
def durchschnitt():
    anzahl, summe = 0, 0.0
    while True:
        eingabe = input("Zahl (oder 'done'): ")
        if eingabe == "done":
            break
        try:
            summe += float(eingabe)
            anzahl += 1
        except ValueError:
            print("Ungueltig!")
    return summe / anzahl if anzahl > 0 else 0

# Vokale zaehlen
def count_vocals(text):
    return sum(1 for c in text if c in "aeiouAEIOU")

# Teiler finden
def finde_teiler(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Fibonacci
def fibonacci(n):
    if n <= 0: return []
    if n == 1: return [1]
    folge = [1, 1]
    while len(folge) < n:
        folge.append(folge[-1] + folge[-2])
    return folge
```

---

# 16. Klausurtipps

## Haeufige Fallen - AUSWENDIG LERNEN!

| Falle | Falsch | Richtig |
|-------|--------|---------|
| `range(3)` | 0,1,2,3 | 0,1,2 |
| `for i` ueberschreibt | i bleibt | i = letzter Wert |
| `s.upper()` | aendert s | s = s.upper() |
| `d["x"]` wenn fehlt | None | KeyError! |
| `d.get("x", 0)` | KeyError | gibt 0 |
| `input()` Typ | int | immer String! |
| `liste.index(x)` wenn fehlt | -1 | ValueError! |
| `"abc".find(x)` wenn fehlt | ValueError | -1 |

## Wichtigste Konzepte und Lernplan

1. **Modulo:** `x % y == 0` fuer Teilbarkeit
2. **dict.get():** `d[key] = d.get(key, 0) + 1`
3. **try-except** fuer Benutzereingaben
4. **String-Methoden:** `lower()`, `replace()`
5. **for-Schleifen** mit `range()`

**Lernplan (4 Tage):**
- Tag 1: Modulo, FizzBuzz, dict.get()
- Tag 2: String-Methoden, try-except
- Tag 3: for-Schleifen, Quiz durcharbeiten
- Tag 4: Spickzettel, Probeklausur unter Zeitdruck

**Erkenntnisse aus Gedaechtnisprotokollen:**
- Zeit ist knapp - direkt anfangen
- Textverarbeitung kam viel - replace() ueben!
- FizzBuzz und dict.get() - muss sitzen

---

**Weitere Loesungen:** Siehe [loesungen-referenz.md](loesungen-referenz.md)
