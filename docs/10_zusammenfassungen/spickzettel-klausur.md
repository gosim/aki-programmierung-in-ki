# Python Spickzettel - Klausur PKI

## 1. Built-in Funktionen
```python
print("Hallo")           # Ausgabe
input("Name: ")          # Eingabe (gibt String zurueck!)
len("abc")               # 3 - Laenge
type(42)                 # <class 'int'>
int("5")                 # 5 - String zu Integer
str(5)                   # "5" - zu String
float("3.14")            # 3.14 - zu Dezimalzahl
bool(0)                  # False (0, "", [], {} sind False)
abs(-5)                  # 5 - Absolutwert
round(3.7)               # 4 - Runden
sum([1,2,3])             # 6 - Summe
min(1, 2, 3)             # 1
max(1, 2, 3)             # 3
sorted([3,1,2])          # [1,2,3] - neue sortierte Liste
list("abc")              # ['a','b','c']
range(5)                 # 0,1,2,3,4 (NICHT 5!)
range(1, 6)              # 1,2,3,4,5
range(0, 10, 2)          # 0,2,4,6,8
```

## 2. Operatoren
```python
# Arithmetisch
+  -  *  /               # Grundrechenarten
//                       # Ganzzahldivision: 7 // 2 = 3
%                        # Modulo (Rest): 7 % 2 = 1
**                       # Potenz: 2 ** 3 = 8

# Vergleich
==  !=                   # gleich, ungleich
<  >  <=  >=             # kleiner, groesser
0 <= x <= 100            # Verketteter Vergleich!

# Logisch
and  or  not             # und, oder, nicht
x % 2 == 0 and x > 0     # gerade UND positiv
```

## 3. Verzweigungen (if/elif/else)
```python
if x > 0:
    print("positiv")
elif x < 0:
    print("negativ")
else:
    print("null")

# Einzeiler (ternary)
ergebnis = "ja" if x > 0 else "nein"
```

## 4. Schleifen
```python
# for-Schleife
for i in range(5):       # 0,1,2,3,4
    print(i)

for zeichen in "abc":    # a, b, c
    print(zeichen)

for i, wert in enumerate(liste):  # Index + Wert
    print(i, wert)

# while-Schleife
while bedingung:
    # Code
    if abbruch:
        break            # Schleife verlassen
    if ueberspringen:
        continue         # zum naechsten Durchlauf

# KLAUSURFALLE: for ueberschreibt Variable!
i = 27
for i in range(3):       # i wird 0, 1, 2
    pass
print(i)                 # 2 (NICHT 27!)
```

## 5. Funktionen
```python
def funktion(param1, param2=10):  # param2 hat Standardwert
    """Docstring - Beschreibung"""
    ergebnis = param1 + param2
    return ergebnis              # Wert zurueckgeben

# Aufruf
x = funktion(5)          # x = 15
x = funktion(5, 3)       # x = 8

# *args - beliebig vielePositions-Argumente (als Tupel)
def summe(*zahlen):
    return sum(zahlen)
summe(1, 2, 3)           # 6
summe(1, 2, 3, 4, 5)     # 15

# **kwargs - beliebig viele Keyword-Argumente (als Dict)
def info(**daten):
    for key, val in daten.items():
        print(f"{key}: {val}")
info(name="Anna", alter=25)  # name: Anna, alter: 25

# Kombination
def alles(a, b, *args, **kwargs):
    print(a, b)          # Pflicht-Parameter
    print(args)          # Tupel mit Rest-Positionen
    print(kwargs)        # Dict mit Keyword-Args
```

## 6. Strings
```python
s = "Hallo Welt"

# Zugriff (Index ab 0!)
s[0]                     # "H" - erstes Zeichen
s[-1]                    # "t" - letztes Zeichen
s[1:4]                   # "all" - Index 1,2,3 (4 exklusiv!)
s[:5]                    # "Hallo" - von Anfang
s[6:]                    # "Welt" - bis Ende
s[::-1]                  # "tleW ollaH" - umgekehrt!

# Methoden (IMMER SPEICHERN!)
s.lower()                # "hallo welt"
s.upper()                # "HALLO WELT"
s.strip()                # Leerzeichen entfernen
s.split()                # ["Hallo", "Welt"]
s.split(",")             # an Komma trennen
s.replace("a", "x")      # "Hxllo Welt"
s.find("lo")             # 3 - Index (-1 wenn nicht gefunden)
s.startswith("Ha")       # True
s.endswith("lt")         # True
s.count("l")             # 3 - Anzahl
len(s)                   # 10 - Laenge
"x" in s                 # False - enthalten?

# WICHTIG: Strings unveraenderlich!
s.upper()                # gibt "HALLO WELT" zurueck
s = s.upper()            # SPEICHERN notwendig!

# Zusammenfuegen
" ".join(["a","b","c"])  # "a b c"
"Hallo" + " " + "Welt"   # "Hallo Welt"
"ab" * 3                 # "ababab"
```

## 7. Listen
```python
liste = [1, 2, 3, 4, 5]

# Zugriff (wie Strings)
liste[0]                 # 1
liste[-1]                # 5
liste[1:3]               # [2, 3]
liste[::-1]              # [5, 4, 3, 2, 1]

# Aendern (Listen sind mutable!)
liste[0] = 10            # [10, 2, 3, 4, 5]

# Hinzufuegen
liste.append(6)          # am Ende: [1,2,3,4,5,6]
liste.insert(0, 0)       # an Index: [0,1,2,3,4,5]
liste.extend([7, 8])     # mehrere: [1,2,3,4,5,7,8]

# Entfernen
liste.pop()              # letztes entfernen + zurueckgeben
liste.pop(0)             # an Index entfernen + zurueckgeben
liste.remove(3)          # erstes 3 entfernen
del liste[0]             # an Index loeschen

# Suchen
3 in liste               # True - enthalten?
liste.index(3)           # 2 - Index (ValueError wenn nicht da!)
liste.count(3)           # 1 - Anzahl

# Sortieren
liste.sort()             # aufsteigend (aendert Liste!)
liste.sort(reverse=True) # absteigend
sorted(liste)            # NEUE sortierte Liste
liste.reverse()          # Reihenfolge umkehren

# Laenge und Aggregation
len(liste)               # Anzahl Elemente
sum(liste)               # Summe
min(liste)               # Minimum
max(liste)               # Maximum

# ACHTUNG: Listen haben KEIN find()!
# Nutze: index() oder "in"
```

## 8. Dictionaries
```python
d = {"name": "Anna", "alter": 25}

# Zugriff
d["name"]                # "Anna" - KeyError wenn nicht da!
d.get("name")            # "Anna" - None wenn nicht da
d.get("xyz", 0)          # 0 - Standardwert wenn nicht da

# Aendern/Hinzufuegen
d["name"] = "Max"        # aendern
d["neu"] = "Wert"        # hinzufuegen

# Entfernen
del d["name"]            # loeschen
d.pop("name")            # loeschen + zurueckgeben

# Pruefen
"name" in d              # True - Key vorhanden?
"Anna" in d.values()     # True - Wert vorhanden?

# Iteration
for key in d:            # nur Keys
for key in d.keys():     # nur Keys
for val in d.values():   # nur Werte
for k, v in d.items():   # Key + Wert

# ZAEHLMUSTER - SEHR WICHTIG!
count = {}
for wort in text.split():
    count[wort] = count.get(wort, 0) + 1
```

## 9. Tupel
```python
t = (1, 2, 3)            # unveraenderlich!
t = 1, 2, 3              # Klammern optional

# Zugriff wie Listen
t[0]                     # 1
t[1:3]                   # (2, 3)

# Unpacking
a, b, c = (1, 2, 3)      # a=1, b=2, c=3
x, y = y, x              # Tauschen!

# Tupel-Liste fuer Sortierung nach Wert
lst = []
for k, v in d.items():
    lst.append((v, k))   # (Wert, Key)!
lst.sort(reverse=True)   # nach Wert sortiert
```

## 10. Dateien
```python
# Lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()           # alles
    # oder:
    for zeile in f:             # zeilenweise
        zeile = zeile.strip()   # Zeilenumbruch entfernen

# Schreiben
with open("datei.txt", "w") as f:  # w = ueberschreiben
    f.write("Text\n")

with open("datei.txt", "a") as f:  # a = anhaengen
    f.write("Mehr Text\n")
```

## 11. try-except
```python
try:
    zahl = int(input("Zahl: "))
    ergebnis = 10 / zahl
except ValueError:
    print("Keine gueltige Zahl!")
except ZeroDivisionError:
    print("Division durch 0!")
except:
    print("Unbekannter Fehler!")

# Mit quit() bei Fehler
try:
    f = open("datei.txt")
except FileNotFoundError:
    print("Datei nicht gefunden!")
    quit()
```

## 12. OOP (Klassen)
```python
class Student:
    def __init__(self, name, note):  # Konstruktor
        self.name = name             # Instanzattribut
        self.note = note

    def ist_bestanden(self):         # Methode
        return self.note <= 4.0

    def __str__(self):               # fuer print()
        return f"{self.name}: {self.note}"

# Verwendung
s = Student("Anna", 1.3)
print(s.name)            # Anna
print(s.ist_bestanden()) # True
print(s)                 # Anna: 1.3
```

## 13. FizzBuzz & Umlaute (Klausuraufgaben!)
```python
# FizzBuzz
for x in range(1, 101):
    if x % 15 == 0:          # ZUERST 15 pruefen!
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

# Umlaute ersetzen - Variante 1
text = text.lower()
text = text.replace("ä", "ae")
text = text.replace("ö", "oe")
text = text.replace("ü", "ue")
text = text.replace("ß", "ss")

# Umlaute ersetzen - Variante 2 (mit Dict)
ersetzungen = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}
for alt, neu in ersetzungen.items():
    text = text.replace(alt, neu)
```

---

## KLAUSURFALLEN - AUSWENDIG LERNEN!

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

## 14. Typumwandlung
```python
int("42")      # 42
str(42)        # "42"
float("3.14")  # 3.14
list("abc")    # ['a', 'b', 'c']
bool(0)        # False
bool("")       # False
bool([])       # False
bool(1)        # True
```

## 15. Module importieren (KLAUSURRELEVANT!)
```python
# Ganzes Modul
import math
print(math.sqrt(16))     # 4.0

# Modul mit Alias
import math as m
print(m.sqrt(16))        # 4.0

# Spezifische Funktion importieren
from math import sqrt
print(sqrt(16))          # 4.0

# Mehrere Funktionen
from math import sqrt, pi, sin
```

## 16. NumPy Grundlagen (KLAUSURRELEVANT!)
```python
import numpy as np

# Arrays erstellen
np.array([1, 2, 3])           # 1D-Array
np.array([[1,2], [3,4]])      # 2D-Matrix
np.zeros((2, 3))              # 2x3 mit Nullen
np.ones((3, 3))               # 3x3 mit Einsen

# Elementweise Operationen!
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.ones((3, 3))
c = a + b    # [[2,3,4], [5,6,7], [8,9,10]]
```

## 17. random Modul
```python
from random import randint, choice, shuffle

randint(1, 6)         # Zufallszahl 1-6 (inklusive!)
choice([1,2,3])       # Zufaelliges Element
shuffle(liste)        # Liste mischen (in-place!)
```

## 18. Set (Menge)
```python
s = {1, 2, 3}              # Set erstellen
s = {1, 2, 2, 3, 3}        # {1, 2, 3} - keine Duplikate!
s = set([1, 2, 2, 3])      # Liste zu Set
3 in s                     # True - Element pruefen

# Unterschied zu Dictionary:
# Dict: {"a": 1} - Key-Value-Paare
# Set:  {1, 2, 3} - nur Werte, keine Duplikate
```
