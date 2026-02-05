# Python Lernplan - Klausur 07.02.2026

## Klausurstruktur (60 Punkte, 1 Stunde)

| Aufgabe | Punkte | Thema |
|---------|--------|-------|
| 1 | 30 | Code-Verstaendnis (for-Schleife, try-except, dict.get()) |
| 2 | 15 | FizzBuzz (Modulo, Teilbarkeit durch 3/5) |
| 3 | 15 | Textverarbeitung (lower(), Umlaute ersetzen) |

---

# SCHNELLREFERENZ: Alle wichtigen Konzepte

## dict.get() - SEHR WICHTIG!

```python
d = {"a": 1, "b": 2}

# PROBLEM: Direkter Zugriff wirft Fehler bei fehlendem Key
d["c"]              # KeyError! Programm stuerzt ab!

# LOESUNG: get() gibt Standardwert zurueck
d.get("c")          # None (kein Fehler)
d.get("c", 0)       # 0 (Standardwert wenn Key fehlt)
d.get("a", 0)       # 1 (Key existiert, also wird Wert zurueckgegeben)
```

**Warum wichtig?** Ermoeglicht sicheres Zaehlen ohne vorherige Pruefung!

## Das Zaehlmuster mit dict.get()

```python
# OHNE get() - umstaendlich:
count = {}
for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

# MIT get() - elegant:
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

**So funktioniert es Schritt fuer Schritt:**
```python
words = ["a", "b", "a"]
count = {}

# Durchlauf 1: word = "a"
count["a"] = count.get("a", 0) + 1  # get("a", 0) = 0, also count["a"] = 1

# Durchlauf 2: word = "b"
count["b"] = count.get("b", 0) + 1  # get("b", 0) = 0, also count["b"] = 1

# Durchlauf 3: word = "a"
count["a"] = count.get("a", 0) + 1  # get("a", 0) = 1, also count["a"] = 2

# Ergebnis: {"a": 2, "b": 1}
```

## String-Methoden - Uebersicht

| Methode | Beschreibung | Beispiel | Ergebnis |
|---------|--------------|----------|----------|
| `lower()` | Kleinbuchstaben | `"ABC".lower()` | `"abc"` |
| `upper()` | Grossbuchstaben | `"abc".upper()` | `"ABC"` |
| `strip()` | Leerzeichen entfernen | `"  hi  ".strip()` | `"hi"` |
| `split()` | In Liste aufteilen | `"a b c".split()` | `["a","b","c"]` |
| `split(",")` | An Zeichen teilen | `"a,b,c".split(",")` | `["a","b","c"]` |
| `replace(a,b)` | Ersetzen | `"hallo".replace("l","x")` | `"haxxo"` |
| `find(x)` | Position finden | `"hallo".find("l")` | `2` |
| `startswith(x)` | Anfang pruefen | `"hallo".startswith("ha")` | `True` |
| `len(s)` | Laenge | `len("hallo")` | `5` |

**WICHTIG:** Strings sind unveraenderlich! Ergebnis speichern!
```python
text = "HALLO"
text.lower()        # Gibt "hallo" zurueck, text bleibt "HALLO"
text = text.lower() # Jetzt ist text = "hallo"
```

## Slicing - Strings und Listen

```python
s = "Python"    # Index: 0=P, 1=y, 2=t, 3=h, 4=o, 5=n
                # Negativ: -6=P, -5=y, -4=t, -3=h, -2=o, -1=n

s[0]      # "P"     - erstes Zeichen
s[-1]     # "n"     - letztes Zeichen
s[1:4]    # "yth"   - Index 1 bis 3 (4 ist EXKLUSIV!)
s[:3]     # "Pyt"   - von Anfang bis Index 2
s[2:]     # "thon"  - von Index 2 bis Ende
s[::2]    # "Pto"   - jedes zweite Zeichen
s[::-1]   # "nohtyP" - UMKEHREN!
```

## range() - ACHTUNG: Endwert ist exklusiv!

```python
range(5)        # 0, 1, 2, 3, 4      (NICHT 5!)
range(1, 5)     # 1, 2, 3, 4         (NICHT 5!)
range(0, 10, 2) # 0, 2, 4, 6, 8      (Schrittweite 2)
range(5, 0, -1) # 5, 4, 3, 2, 1      (rueckwaerts)
```

## for-Schleife - KLAUSURFALLE!

```python
i = 100
for i in range(3):  # i wird ueberschrieben mit 0, 1, 2
    pass
print(i)  # Ausgabe: 2 (NICHT 100!)
```

**Nach der Schleife hat i den LETZTEN Wert aus range()!**

## Modulo % - Teilbarkeit pruefen

```python
x % 2 == 0   # x ist gerade
x % 2 == 1   # x ist ungerade
x % 3 == 0   # x ist durch 3 teilbar
x % 5 == 0   # x ist durch 5 teilbar
x % 15 == 0  # x ist durch 15 teilbar (3 UND 5)
```

**FizzBuzz-Logik:**
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

## Verkettete Vergleiche (KLAUSURRELEVANT!)

```python
# Statt:
if x >= 0 and x <= 100:
    print("Gueltig")

# Eleganter:
if 0 <= x <= 100:
    print("Gueltig")

# Haeufig bei Notenvergabe:
if 0.0 <= punkte <= 1.0:
    # Punkte sind gueltig
```

## try-except - Fehler abfangen

```python
try:
    zahl = int(input("Zahl: "))  # Kann ValueError werfen
    ergebnis = 10 / zahl         # Kann ZeroDivisionError werfen
except ValueError:
    print("Keine gueltige Zahl!")
except ZeroDivisionError:
    print("Division durch Null!")
except:
    print("Unbekannter Fehler!")
```

**Multiple Exceptions zusammenfassen:**
```python
try:
    zahl = float(input("Zahl: "))
except (ValueError, TypeError):  # Mehrere Exceptions!
    print("Fehler bei Eingabe")
    quit()  # Programm beenden
```

## Listen-Methoden

```python
lst = [1, 2, 3, 2, 4]

# Hinzufuegen/Entfernen
lst.append(5)       # [1, 2, 3, 2, 4, 5] - am Ende hinzufuegen
lst.pop()           # Gibt 5 zurueck, entfernt letztes Element
lst.pop(0)          # Gibt 1 zurueck, entfernt erstes Element
lst.remove(2)       # Entfernt ERSTES Vorkommen von 2
del lst[0]          # Loescht Element an Index 0
del lst[-1]         # Loescht letztes Element

# Suchen - WICHTIG!
lst.index(3)        # 2 - Index von 3 (ValueError wenn nicht gefunden!)
lst.count(2)        # 1 - Anzahl Vorkommen von 2
3 in lst            # True - Prueft ob Element vorhanden
5 in lst            # False

# Sortieren
lst.sort()          # Aufsteigend sortieren (aendert Liste!)
lst.sort(reverse=True)  # Absteigend sortieren
sorted(lst)         # Gibt NEUE sortierte Liste zurueck
lst.reverse()       # Reihenfolge umkehren

# Aggregatfunktionen
len(lst)   # Anzahl Elemente
sum(lst)   # Summe
min(lst)   # Minimum
max(lst)   # Maximum
```

**ACHTUNG: Listen haben KEIN find()!**
```python
# String: find() gibt -1 zurueck wenn nicht gefunden
"hallo".find("x")   # -1

# Liste: index() wirft ValueError wenn nicht gefunden!
[1, 2, 3].index(5)  # ValueError!

# Sicher pruefen:
if 5 in lst:
    pos = lst.index(5)
```

## Dictionary-Methoden

```python
d = {"a": 1, "b": 2}

d["a"]              # 1 (KeyError wenn nicht vorhanden!)
d.get("a")          # 1
d.get("c")          # None
d.get("c", 0)       # 0 (Standardwert)

d.keys()            # dict_keys(["a", "b"])
d.values()          # dict_values([1, 2])
d.items()           # dict_items([("a", 1), ("b", 2)])

"a" in d            # True (prueft NUR Schluessel!)
len(d)              # 2

# items() in Liste konvertieren (fuer Sortierung!)
liste = list(d.items())  # [("a", 1), ("b", 2)]
```

## Tupel-Liste fuer Sortierung (KLAUSURRELEVANT!)

```python
# Maximum aus Dictionary finden - WICHTIGES MUSTER!
d = {"anna": 3, "ben": 5, "clara": 2}

# 1. Tupel-Liste erstellen (Wert, Schluessel)
lst = []
for key, val in d.items():
    lst.append((val, key))  # (Wert, Schluessel)!
# lst = [(3, "anna"), (5, "ben"), (2, "clara")]

# 2. Sortieren (sortiert nach erstem Element = Wert)
lst.sort(reverse=True)
# lst = [(5, "ben"), (3, "anna"), (2, "clara")]

# 3. Maximum ist erstes Element
print(lst[0])       # (5, "ben")
print(lst[0][1])    # "ben" (Name)
print(lst[0][0])    # 5 (Anzahl)
```

## Dateien lesen

```python
# Empfohlen: with-Statement (schliesst automatisch)
with open("datei.txt", "r") as f:
    for line in f:
        line = line.strip()  # Zeilenumbruch entfernen!
        words = line.split() # In Woerter aufteilen
        print(words)
```

## Tupel - unveraenderliche Listen

```python
t = (1, 2, 3)       # Tupel mit Klammern
t = 1, 2, 3         # Auch ohne Klammern
t = (5,)            # Einelementig: Komma wichtig!

# Tuple Unpacking
x, y = (10, 20)     # x=10, y=20
a, b = b, a         # Variablen tauschen!

# In for-Schleifen
for key, value in d.items():
    print(key, value)
```

## Funktionen definieren

```python
def funktionsname(parameter1, parameter2="default"):
    """Docstring: Beschreibung"""
    # Code hier
    return ergebnis

# Aufruf
ergebnis = funktionsname(wert1, wert2)
ergebnis = funktionsname(wert1)  # parameter2 = "default"
```

---

## Prioritaet A: MUSS sitzen!

### 1. dict.get() zum Zaehlen (30 Punkte!)
```python
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

### 2. try-except bei Eingabe
```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Fehler!")
```

### 3. for-Schleife mit range() - KLAUSURFALLE!
```python
i = 27
j = 27
for i in range(3):  # i wird ueberschrieben!
    j += 1
print(i, j)  # Ausgabe: 2 30
# ACHTUNG: i hat danach den Wert 2, nicht 27!
```

### 4. Modulo fuer Teilbarkeit
```python
if x % 3 == 0:  # x ist durch 3 teilbar
if x % 15 == 0:  # x ist durch 3 UND 5 teilbar
```

### 5. String-Methoden
```python
text = text.lower()
text = text.replace("ae", "ae")
```

---

# Kapitel 1-2: Grundlagen und Variablen

## Datentypen

| Typ | Beschreibung | Beispiele |
|-----|--------------|-----------|
| `int` | Ganzzahlen | `42`, `-7`, `0` |
| `float` | Gleitkommazahlen | `3.14`, `-2.5`, `1.0` |
| `str` | Zeichenketten | `"Hallo"`, `'Python'` |
| `bool` | Wahrheitswerte | `True`, `False` |

## Operatoren

### Arithmetische Operatoren

| Operator | Beschreibung | Beispiel | Ergebnis |
|----------|--------------|----------|----------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraktion | `5 - 3` | `2` |
| `*` | Multiplikation | `5 * 3` | `15` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Ganzzahldivision | `7 // 2` | `3` |
| `%` | Modulo (Rest) | `7 % 2` | `1` |
| `**` | Potenz | `2 ** 3` | `8` |

### Der Modulo-Operator (KLAUSURRELEVANT!)

```python
# Teilbarkeit pruefen
x % 2 == 0   # gerade Zahl
x % 3 == 0   # durch 3 teilbar
x % 15 == 0  # durch 3 UND 5 teilbar (FizzBuzz!)
```

### Vergleichsoperatoren

| Operator | Bedeutung |
|----------|-----------|
| `==` | gleich |
| `!=` | ungleich |
| `<` | kleiner |
| `>` | groesser |
| `<=` | kleiner oder gleich |
| `>=` | groesser oder gleich |

## Variablen und Zuweisungen

```python
# Einfache Zuweisung
x = 42
name = "Python"

# Mehrfachzuweisung
a = b = c = 0
x, y = 10, 20

# Zusammengesetzte Operatoren
x += 1   # entspricht x = x + 1
x -= 5   # entspricht x = x - 5
x *= 2   # entspricht x = x * 2
```

## Ein- und Ausgabe

```python
# Ausgabe
print("Hallo Welt")
print("x =", x)

# Eingabe - IMMER String!
name = input("Dein Name: ")
zahl = int(input("Zahl: "))  # Umwandlung noetig!
```

---

# Kapitel 3: Bedingte Ausfuehrung

## if-Anweisung

```python
# Einfache Bedingung
if x > 0:
    print("Positiv")

# Mit else
if x > 0:
    print("Positiv")
else:
    print("Nicht positiv")

# Mit elif (else if)
if x > 0:
    print("Positiv")
elif x < 0:
    print("Negativ")
else:
    print("Null")
```

## Logische Operatoren

| Operator | Beschreibung | Beispiel |
|----------|--------------|----------|
| `and` | UND | `x > 0 and x < 10` |
| `or` | ODER | `x == 0 or x == 1` |
| `not` | Negation | `not x > 0` |

## try-except (KLAUSURRELEVANT!)

```python
# Grundform
try:
    zahl = int(input("Zahl: "))
    print("Eingabe:", zahl)
except ValueError:
    print("Keine gueltige Zahl!")

# Mit Wiederholung
while True:
    try:
        zahl = int(input("Zahl: "))
        break  # Schleife verlassen wenn erfolgreich
    except ValueError:
        print("Bitte eine Zahl eingeben!")
```

**Warum try-except wichtig ist:**
- `int("abc")` wirft ValueError
- Ohne try-except stuerzt das Programm ab
- Mit try-except kann man den Fehler abfangen

## Haeufige Exceptions

| Exception | Ursache |
|-----------|---------|
| `ValueError` | Falscher Wert (z.B. `int("abc")`) |
| `TypeError` | Falscher Typ (z.B. `"a" + 1`) |
| `ZeroDivisionError` | Division durch Null |
| `IndexError` | Index ausserhalb des Bereichs |
| `KeyError` | Schluessel nicht im Dictionary |

---

# Kapitel 4: Funktionen

## Funktionen definieren

```python
# Ohne Parameter
def gruessen():
    print("Hallo!")

# Mit Parametern
def gruessen(name):
    print(f"Hallo, {name}!")

# Mit Rueckgabewert
def quadrat(x):
    return x * x

# Mit Standardwert
def gruessen(name="Welt"):
    print(f"Hallo, {name}!")
```

## Lokale vs. globale Variablen

```python
x = 10  # Globale Variable

def funktion():
    x = 5  # Lokale Variable (ueberdeckt globale!)
    print(x)

funktion()  # Ausgabe: 5
print(x)    # Ausgabe: 10 (globale unveraendert)
```

**Mit global-Keyword:**
```python
x = 10

def aendern():
    global x  # Zugriff auf globale Variable
    x = 5

aendern()
print(x)  # Ausgabe: 5
```

## Mehrere Rueckgabewerte (Tupel)

```python
def min_max(zahlen):
    return min(zahlen), max(zahlen)

minimum, maximum = min_max([3, 1, 4, 1, 5])
print(minimum)  # 1
print(maximum)  # 5
```

---

# Kapitel 5: Iteration (Schleifen)

## for-Schleife

### range()-Funktion

```python
# range(stop) - von 0 bis stop-1
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# range(start, stop) - von start bis stop-1
for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step) - mit Schrittweite
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)
```

### KLAUSURFALLE: for-Schleife ueberschreibt Variable!

```python
i = 27
j = 27

for i in range(3):  # i wird 0, 1, 2 - nicht 27!
    j += 1

print(i, j)  # Ausgabe: 2 30
# i ist NICHT mehr 27, sondern 2 (letzter Wert von range)
```

**WICHTIG:** Nach der Schleife hat `i` den letzten Wert aus range()!

## while-Schleife

```python
x = 0
while x < 5:
    print(x)
    x += 1

# ACHTUNG: Endlosschleife vermeiden!
# while True:  # Ohne break nie beendet!
#     pass
```

## break und continue

```python
# break - Schleife sofort beenden
for i in range(10):
    if i == 5:
        break
    print(i)  # Ausgabe: 0, 1, 2, 3, 4

# continue - Zum naechsten Durchlauf springen
for i in range(5):
    if i == 2:
        continue
    print(i)  # Ausgabe: 0, 1, 3, 4 (2 wird uebersprungen)
```

---

# Kapitel 6: Zeichenketten (Strings)

## Strings sind unveraenderlich (immutable)!

```python
text = "Hallo"
text[0] = "M"  # FEHLER! TypeError

# Stattdessen neuen String erzeugen:
text = "M" + text[1:]  # "Mallo"
```

## Indizierung und Slicing

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5   (positive Indizes)
#   -6 -5 -4 -3 -2 -1   (negative Indizes)

s[0]     # 'P' - erstes Zeichen
s[-1]    # 'n' - letztes Zeichen
s[1:4]   # 'yth' - Index 1 bis 3 (4 exklusiv!)
s[:3]    # 'Pyt' - von Anfang bis Index 2
s[2:]    # 'thon' - von Index 2 bis Ende
s[::-1]  # 'nohtyP' - String umkehren!
```

## String-Methoden (KLAUSURRELEVANT!)

```python
text = "Hallo Welt"

# Gross-/Kleinschreibung
text.lower()   # 'hallo welt'
text.upper()   # 'HALLO WELT'

# Ersetzen
text.replace("Welt", "Python")  # 'Hallo Python'

# WICHTIG: Ergebnis speichern!
text = text.lower()  # text ist jetzt 'hallo welt'

# Aufteilen
"a,b,c".split(",")  # ['a', 'b', 'c']
"Hallo Welt".split()  # ['Hallo', 'Welt']

# Verbinden
" ".join(["Hallo", "Welt"])  # 'Hallo Welt'

# Leerzeichen entfernen
"  Hallo  ".strip()  # 'Hallo'

# Suchen
"Hallo".find("l")   # 2 (Index des ersten 'l')
"Hallo".count("l")  # 2 (Anzahl der 'l')

# Laenge
len("Hallo")  # 5
```

## Umlaute ersetzen (KLAUSURAUFGABE!)

```python
def text_bereinigen(text):
    text = text.lower()
    text = text.replace("ae", "ae")
    text = text.replace("oe", "oe")
    text = text.replace("ue", "ue")
    text = text.replace("ss", "ss")
    return text

# Beispiel
print(text_bereinigen("Groesse"))  # 'groesse'
```

---

# Kapitel 7: Dateien

## Dateien oeffnen und lesen

```python
# Klassische Methode
datei = open("daten.txt", "r")
inhalt = datei.read()
datei.close()

# Mit with-Statement (empfohlen!)
with open("daten.txt", "r") as datei:
    inhalt = datei.read()
# Datei wird automatisch geschlossen
```

## Dateimodi

| Modus | Beschreibung |
|-------|--------------|
| `"r"` | Lesen (read) |
| `"w"` | Schreiben (write) - ueberschreibt! |
| `"a"` | Anhaengen (append) |
| `"r+"` | Lesen und Schreiben |

## Zeilenweise lesen

```python
# Alle Zeilen als Liste
with open("daten.txt", "r") as datei:
    zeilen = datei.readlines()

# Zeilenweise iterieren
with open("daten.txt", "r") as datei:
    for zeile in datei:
        print(zeile.strip())  # strip() entfernt Zeilenumbruch
```

## In Datei schreiben

```python
# Ueberschreiben
with open("ausgabe.txt", "w") as datei:
    datei.write("Zeile 1\n")
    datei.write("Zeile 2\n")

# Anhaengen
with open("log.txt", "a") as datei:
    datei.write("Neuer Eintrag\n")
```

## Fehlerbehandlung

```python
try:
    with open("datei.txt", "r") as f:
        inhalt = f.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
```

---

# Kapitel 8: Listen

## Listen sind veraenderbar (mutable)!

```python
# Erstellen
zahlen = [1, 2, 3, 4, 5]
leer = []
gemischt = [1, "Hallo", 3.14, True]

# Zugriff (wie bei Strings)
zahlen[0]     # 1
zahlen[-1]    # 5
zahlen[1:3]   # [2, 3]

# Aendern (bei Listen moeglich!)
zahlen[0] = 99  # [99, 2, 3, 4, 5]
```

## Listenmethoden

```python
zahlen = [1, 2, 3]

# Hinzufuegen
zahlen.append(4)       # [1, 2, 3, 4]
zahlen.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
zahlen.insert(0, 0)    # [0, 1, 2, 3, 4, 5, 6]

# Entfernen
letztes = zahlen.pop()     # Gibt 6 zurueck, entfernt es
zweites = zahlen.pop(1)    # Gibt Element an Index 1 zurueck
zahlen.remove(3)           # Entfernt erstes Vorkommen von 3

# Sortieren
zahlen.sort()              # Aufsteigend sortieren
zahlen.sort(reverse=True)  # Absteigend sortieren
zahlen.reverse()           # Reihenfolge umkehren
```

## Listen durchlaufen

```python
for element in liste:
    print(element)

# Mit Index
for i, element in enumerate(liste):
    print(f"{i}: {element}")
```

## Aggregatfunktionen

```python
zahlen = [3, 1, 4, 1, 5, 9]

len(zahlen)   # 6 - Anzahl
sum(zahlen)   # 23 - Summe
min(zahlen)   # 1 - Minimum
max(zahlen)   # 9 - Maximum
```

## List Comprehension

```python
# Quadratzahlen von 0 bis 9
quadrate = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Mit Bedingung
gerade = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

---

# Kapitel 9: Dictionaries (KLAUSURRELEVANT!)

## Dictionary erstellen

```python
# Leeres Dictionary
d = {}
d = dict()

# Mit Werten
student = {"name": "Anna", "alter": 22, "matrikel": 12345}
```

## Zugriff auf Elemente

```python
student = {"name": "Anna", "alter": 22}

# Direkter Zugriff
student["name"]  # "Anna"
student["note"]  # KeyError!

# Sicherer Zugriff mit get()
student.get("name")           # "Anna"
student.get("note")           # None
student.get("note", "keine")  # "keine" (Standardwert)
```

## Das Zaehlmuster (AUSWENDIG LERNEN!)

```python
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

**Beispiel:**
```python
text = "die katze und die maus"
words = text.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
# {'die': 2, 'katze': 1, 'und': 1, 'maus': 1}
```

## Dictionary durchlaufen

```python
d = {"a": 1, "b": 2, "c": 3}

# Nur Schluessel
for key in d:
    print(key)

# Nur Werte
for value in d.values():
    print(value)

# Schluessel UND Werte
for key, value in d.items():
    print(f"{key}: {value}")
```

## Wichtige Dictionary-Methoden

```python
d = {"a": 1, "b": 2}

d.keys()    # dict_keys(['a', 'b'])
d.values()  # dict_values([1, 2])
d.items()   # dict_items([('a', 1), ('b', 2)])

"a" in d    # True (prueft Schluessel!)
len(d)      # 2
```

---

# Kapitel 10: Tupel

## Tupel erstellen

```python
# Mit Klammern
t = (1, 2, 3)

# Ohne Klammern (aber mit Komma!)
t = 1, 2, 3

# Einelementiges Tupel - Komma wichtig!
t = (5,)   # Tupel mit einem Element
t = (5)    # Nur die Zahl 5!
```

## Tupel sind unveraenderlich!

```python
t = (1, 2, 3)
t[0] = 99  # TypeError!
```

## Tuple Unpacking

```python
koordinaten = (10, 20)
x, y = koordinaten
print(x)  # 10
print(y)  # 20

# Variablen tauschen
a, b = b, a

# In for-Schleifen
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

## Tupel vs. Listen

| Eigenschaft | Tupel | Liste |
|-------------|-------|-------|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Veraenderbar | Nein | Ja |
| Als Dict-Key | Ja | Nein |

---

# Kapitel 14: Objektorientierte Programmierung (OOP)

## Klasse definieren

```python
class Student:
    def __init__(self, name, matrikel):
        self.name = name
        self.matrikel = matrikel

    def __str__(self):
        return f"Student: {self.name} ({self.matrikel})"

    def vorstellen(self):
        print(f"Ich bin {self.name}")
```

## Objekte erstellen

```python
s1 = Student("Anna", 12345)
s2 = Student("Ben", 67890)

print(s1.name)      # "Anna"
s1.vorstellen()     # "Ich bin Anna"
print(s1)           # "Student: Anna (12345)"
```

## __init__ und self

- `__init__` ist der Konstruktor - wird bei Objekterstellung aufgerufen
- `self` ist die Referenz auf das aktuelle Objekt
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

    def __str__(self):
        return f"{self.name}: {self.noten}"

# Verwendung
s = Student("Anna")
s.note_hinzufuegen(1.3)
s.note_hinzufuegen(2.0)
s.note_hinzufuegen(1.7)
print(s.durchschnitt())  # 1.6666...
```

---

# Zusaetzliche Themen

## NumPy Grundlagen

```python
import numpy as np

# Array erstellen
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # (2, 3)

# Spezielle Arrays
nullen = np.zeros((3, 3))
einsen = np.ones((2, 4))

# Elementweise Operationen
b = a + 1   # Addiert 1 zu jedem Element
c = a * 2   # Multipliziert jedes Element mit 2
```

## Random-Modul

```python
from random import randint, random, choice

# Zufaellige Ganzzahl (inklusive beide Grenzen)
wuerfel = randint(1, 6)

# Zufaellige Fliesskommazahl 0 bis 1
zufall = random()

# Zufaelliges Element aus Liste
farben = ["rot", "gruen", "blau"]
auswahl = choice(farben)
```

---

# Praktische Beispiele aus den Uebungen (fhswf/pki)

## Lohnberechnung mit Ueberstunden

```python
def lohnberechnung(stundenlohn, arbeitsstunden):
    """Berechnet Lohn mit 1.5x Ueberstundenzuschlag ab 40h."""
    if arbeitsstunden > 40:
        regelsatz = 40 * stundenlohn
        ueberstunden = (arbeitsstunden - 40) * stundenlohn * 1.5
        return regelsatz + ueberstunden
    else:
        return arbeitsstunden * stundenlohn

# Beispiel:
print(lohnberechnung(15, 45))  # 40*15 + 5*15*1.5 = 712.50
```

## E-Mail-Adressen aus Datei zaehlen (KLAUSURRELEVANT!)

```python
def count_mail_adresses(filename):
    """Zaehlt E-Mail-Adressen aus From-Zeilen."""
    mail_counts = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                sender = words[1]  # 2. Wort ist die E-Mail
                mail_counts[sender] = mail_counts.get(sender, 0) + 1
    return mail_counts

# Beispiel-Zeile: "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
```

## Domain aus E-Mail extrahieren

```python
def count_mail_domains(filename):
    """Extrahiert und zaehlt Domains aus E-Mail-Adressen."""
    domain_counts = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                sender = words[1]
                domain = sender.split("@")[1]  # Alles nach @
                domain_counts[domain] = domain_counts.get(domain, 0) + 1
    return domain_counts
```

## Maximum aus Dictionary finden

```python
def max_count(counts_dict):
    """Findet den Schluessel mit dem hoechsten Wert."""
    max_key = None
    max_value = 0
    for key, value in counts_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return (max_key, max_value)
```

## Wert aus String mit find() extrahieren

```python
def extract_value(line):
    """Extrahiert Wert nach dem Doppelpunkt."""
    # Beispiel: "X-DSPAM-Confidence: 0.8475" -> 0.8475
    pos = line.find(":")
    if pos != -1:
        wert = line[pos+1:].strip()
        return float(wert)
    return None
```

## Durchschnitt mit While-Schleife und done-Abbruch

```python
def durchschnitt():
    """Berechnet Durchschnitt von Eingaben bis 'done'."""
    anzahl = 0
    summe = 0.0
    while True:
        eingabe = input("Zahl eingeben (oder 'done'): ")
        if eingabe == "done":
            break
        try:
            zahl = float(eingabe)
            summe += zahl
            anzahl += 1
        except ValueError:
            print("Ungueltige Eingabe!")

    if anzahl > 0:
        return summe / anzahl
    return 0
```

## Vokale zaehlen (String durchlaufen)

```python
def count_vocals(text):
    """Zaehlt Vokale in einem Text (case-insensitive)."""
    vokale = "aeiouAEIOU"
    count = 0
    for buchstabe in text:
        if buchstabe in vokale:
            count += 1
    return count

# Beispiel:
print(count_vocals("Hallo Welt"))  # 3 (a, o, e)
```

## Teiler einer Zahl finden (Modulo)

```python
def finde_teiler(n):
    """Findet alle Teiler einer Zahl."""
    teiler = []
    for i in range(1, n + 1):
        if n % i == 0:
            teiler.append(i)
    return teiler

# Beispiel:
print(finde_teiler(12))  # [1, 2, 3, 4, 6, 12]
```

## Fibonacci-Folge

```python
def fibonacci(n):
    """Berechnet die ersten n Fibonacci-Zahlen."""
    if n <= 0:
        return []
    if n == 1:
        return [1]

    folge = [1, 1]
    while len(folge) < n:
        naechste = folge[-1] + folge[-2]
        folge.append(naechste)
    return folge

# Beispiel:
print(fibonacci(10))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

## Steuertabelle mit Progressionsstufen

```python
def nettolohn(brutto):
    """Berechnet Nettolohn basierend auf Steuertabelle."""
    if brutto <= 10000:
        steuersatz = 0
    elif brutto <= 14000:
        steuersatz = 0.14
    elif brutto <= 31000:
        steuersatz = 0.22
    elif brutto <= 56000:
        steuersatz = 0.29
    elif brutto <= 83000:
        steuersatz = 0.32
    else:
        steuersatz = 0.36

    steuer = brutto * steuersatz
    return brutto - steuer

# Beispiel:
print(nettolohn(17000))  # 17000 - 17000*0.22 = 13260.0
```

---

# Musterloesungen aus Python for Everybody

Im Ordner `python-for-everybody-solutions-master/` befinden sich **35 Loesungsdateien** aus dem Kurs "Python for Everybody" von Charles R. Severance.

**Vollstaendige Uebersicht:** Siehe [loesungen-referenz.md](loesungen-referenz.md)

## Die 5 wichtigsten Loesungen fuer die Klausur

| Datei | Thema | Beschreibung |
|-------|-------|--------------|
| `exercise9_3.py` | Zaehlmuster | `d[k] = d.get(k, 0) + 1` |
| `exercise3_1.py` | Lohnberechnung | 1.5x Ueberstunden ab 40h |
| `exercise5_1.py` | While + done | Akkumulatoren (total, count, average) |
| `exercise10_1.py` | E-Mail-Zaehlung | Dictionary + Maximum finden |
| `exercise8_4.py` | Liste + sortieren | Datei parsen, Duplikate filtern |

## Wichtigstes Muster: E-Mail-Zaehlung (exercise10_1.py)

```python
# 1. Dictionary fuer Zaehlung
mail_counts = {}

# 2. Datei zeilenweise lesen
for line in fhand:
    words = line.split()
    if words[0] != 'From':
        continue
    email = words[1]
    # 3. Zaehlen mit dict.get()
    mail_counts[email] = mail_counts.get(email, 0) + 1

# 4. Maximum finden mit Tupel-Liste
lst = []
for key, val in mail_counts.items():
    lst.append((val, key))
lst.sort(reverse=True)

# 5. Ergebnis ausgeben
print(lst[0][1], lst[0][0])  # email, count
```

**Dieses Muster kombiniert:** Datei lesen, split(), dict.get(), Tupel, sort()

---

# Zusammenfassung: Klausurtipps

## Haeufige Fallen

1. **for-Schleife ueberschreibt Variable:**
   ```python
   i = 100
   for i in range(3):
       pass
   # i ist jetzt 2, nicht 100!
   ```

2. **range(n) endet bei n-1:**
   ```python
   range(5)     # 0, 1, 2, 3, 4 (nicht 5!)
   range(1, 5)  # 1, 2, 3, 4 (nicht 5!)
   ```

3. **Strings sind unveraenderlich:**
   ```python
   s = "hallo"
   s.upper()      # Gibt "HALLO" zurueck, s bleibt "hallo"
   s = s.upper()  # Jetzt ist s = "HALLO"
   ```

4. **dict[key] vs dict.get(key):**
   ```python
   d = {"a": 1}
   d["b"]         # KeyError!
   d.get("b", 0)  # Gibt 0 zurueck (kein Fehler)
   ```

## Wichtigste Konzepte

1. **Modulo fuer Teilbarkeit:** `x % y == 0`
2. **dict.get() zum Zaehlen:** `d[key] = d.get(key, 0) + 1`
3. **try-except fuer Benutzereingaben**
4. **String-Methoden:** `lower()`, `replace()`
5. **for-Schleifen mit range()**

---

## Lernplan (4 Tage)

### Tag 1: Kernkonzepte
- [ ] Modulo und FizzBuzz ueben
- [ ] dict.get() zum Zaehlen

### Tag 2: Textverarbeitung
- [ ] String-Methoden (lower, replace)
- [ ] try-except bei input

### Tag 3: Code-Verstaendnis
- [ ] for-Schleifen mit range()
- [ ] Quiz durcharbeiten

### Tag 4: Wiederholung
- [ ] Spickzettel vorbereiten
- [ ] Probeklausur unter Zeitdruck

---

## Wichtige Erkenntnisse aus Gedaechtnisprotokollen

1. **Zeit ist knapp** - kaum Zeit fuer Spickzettel
2. **Direkt anfangen** - nicht lange ueberlegen
3. **Textverarbeitung kam viel** - replace() ueben!
4. **FizzBuzz ist Standard** - muss sitzen
5. **dict.get() verstehen** - kommt garantiert
