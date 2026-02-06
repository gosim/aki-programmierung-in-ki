# Klausurfragen-Sammlung

## PKI Klausur - Echte Aufgaben mit Musterloesungen

Diese Sammlung enthaelt die echten Klausuraufgaben basierend auf den Gedaechtnisprotokollen der Studenten.

---

# Aufgabe 1: Code-Verstaendnis (30 Punkte)

## Aufgabe 1a: for-Schleife mit range()

**Was ist die Ausgabe des folgenden Codes?**

```python
i = 27
j = 27

for i in range(3):
    j += 1

print(i, j)
```

**Loesung:**

**Ausgabe:** `2 30`

**Schritt-fuer-Schritt-Erklaerung:**

1. Anfangswerte: `i = 27`, `j = 27`

2. Die for-Schleife mit `range(3)` erzeugt die Werte 0, 1, 2

3. **WICHTIG:** Die Schleifenvariable `i` ueberschreibt den urspruenglichen Wert 27!

4. Durchlaeufe:
   - Durchlauf 1: i = 0, j = 27 + 1 = 28
   - Durchlauf 2: i = 1, j = 28 + 1 = 29
   - Durchlauf 3: i = 2, j = 29 + 1 = 30

5. Nach der Schleife: i = 2 (letzter Wert von range), j = 30

**Wichtige Erkenntnis:**
Die for-Schleife ueberschreibt die Variable `i`. Der urspruengliche Wert 27 geht verloren.

---

## Aufgabe 1b: try-except bei Benutzereingabe

**Schreiben Sie einen try-except-Block fuer die Eingabe eines Integers. Erklaeren Sie, warum das sinnvoll ist.**

**Loesung:**

```python
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    print("Ihre Zahl:", zahl)
except ValueError:
    print("Ungueltige Zahl eingegeben!")
```

**Warum ist try-except sinnvoll?**

1. **Benutzer koennen fehlerhafte Eingaben machen:**
   - Text statt Zahlen eingeben ("abc" statt "123")
   - Leerzeichen oder Sonderzeichen

2. **Ohne try-except stuerzt das Programm ab:**
   - `int("abc")` wirft einen ValueError
   - Das Programm bricht sofort ab

3. **Mit try-except bleibt das Programm stabil:**
   - Fehler werden abgefangen
   - Benutzer erhaelt verstaendliche Fehlermeldung
   - Programm kann weiterlaufen

4. **Benutzerfreundlichkeit:**
   - Statt kryptischer Python-Fehlermeldung
   - Klare, verstaendliche Rueckmeldung

**Erweiterte Version mit Wiederholung:**

```python
while True:
    try:
        zahl = int(input("Geben Sie eine Zahl ein: "))
        break  # Erfolgreiche Eingabe, Schleife verlassen
    except ValueError:
        print("Ungueltige Eingabe! Bitte eine Zahl eingeben.")

print("Sie haben", zahl, "eingegeben.")
```

---

## Aufgabe 1c: Dictionary zum Zaehlen

**Was macht folgender Code? Was ist die Ausgabe?**

```python
count = {}
words = ["a", "b", "c"]
for w in words:
    count[w] = count.get(w, 0) + 1
print(count)
```

**Loesung:**

**Ausgabe:** `{'a': 1, 'b': 1, 'c': 1}`

**Erklaerung:**

Der Code zaehlt die Haeufigkeit jedes Elements in der Liste.

**Schritt-fuer-Schritt:**

1. `count = {}` - Leeres Dictionary erstellen

2. Fuer jedes Wort in der Liste:
   - `count.get(w, 0)` - Holt den aktuellen Zaehler fuer das Wort (oder 0 wenn nicht vorhanden)
   - `+ 1` - Erhoeht den Zaehler um 1
   - `count[w] = ...` - Speichert den neuen Zaehler

3. Durchlaeufe:
   - "a": count.get("a", 0) = 0, dann 0+1=1 → count = {"a": 1}
   - "b": count.get("b", 0) = 0, dann 0+1=1 → count = {"a": 1, "b": 1}
   - "c": count.get("c", 0) = 0, dann 0+1=1 → count = {"a": 1, "b": 1, "c": 1}

**Was macht count.get(w, 0)?**

- Sucht den Schluessel `w` im Dictionary `count`
- Wenn gefunden: gibt den gespeicherten Wert zurueck
- Wenn NICHT gefunden: gibt den Standardwert 0 zurueck

Das ist eleganter als:
```python
if w in count:
    count[w] = count[w] + 1
else:
    count[w] = 1
```

---

# Aufgabe 2: FizzBuzz (15 Punkte)

**Schreiben Sie eine Funktion, die fuer Zahlen von 1 bis n (benutzerdefiniert oder 100) prueft:**
- Wenn durch 3 teilbar: "Fizz" ausgeben
- Wenn durch 5 teilbar: "Buzz" ausgeben
- Wenn durch 3 UND 5 teilbar: "FizzBuzz" ausgeben
- Sonst: die Zahl selbst ausgeben

**Loesung:**

```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Aufruf mit Standardwert:
fizzbuzz(100)

# Oder mit Benutzereingabe:
try:
    grenze = int(input("Bis zu welcher Zahl? "))
    fizzbuzz(grenze)
except ValueError:
    print("Ungueltige Eingabe, verwende 100")
    fizzbuzz(100)
```

**Wichtige Punkte:**

1. **Reihenfolge ist entscheidend:**
   - ZUERST auf "durch 3 UND 5 teilbar" pruefen (FizzBuzz)
   - DANN einzeln auf 3 oder 5
   - Sonst wuerde z.B. 15 als "Fizz" erkannt werden

2. **Modulo-Operator (%):**
   - `x % y` gibt den Rest der Division zurueck
   - `x % 3 == 0` bedeutet "x ist durch 3 teilbar"

3. **Alternative fuer "durch 3 und 5":**
   - `i % 3 == 0 and i % 5 == 0`
   - ODER: `i % 15 == 0` (kgV von 3 und 5)

**Beispielausgabe fuer fizzbuzz(15):**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

---

# Aufgabe 3: Textverarbeitung (15 Punkte)

**Eingabe: Ein Text**
**Aufgabe:**
1. Text in Kleinbuchstaben umwandeln
2. Alle deutschen Umlaute ersetzen (`ä`→`ae`, `ö`→`oe`, `ü`→`ue`, `ß`→`ss`)

**Loesung:**

```python
def text_bereinigen(text):
    # Schritt 1: Kleinbuchstaben
    text = text.lower()

    # Schritt 2: Umlaute ersetzen
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")

    return text

# Test:
eingabe = "Größe und Übung"
ergebnis = text_bereinigen(eingabe)
print(ergebnis)  # "groesse und uebung"
```

**Alternative mit Dictionary:**

```python
def text_bereinigen(text):
    text = text.lower()

    ersetzungen = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss"
    }

    for alt, neu in ersetzungen.items():
        text = text.replace(alt, neu)

    return text
```

**Wichtige Punkte:**

1. **Strings sind unveraenderlich:**
   - `text.lower()` gibt einen NEUEN String zurueck
   - Man muss das Ergebnis speichern: `text = text.lower()`

2. **Reihenfolge von lower() und replace():**
   - ZUERST `lower()`, dann die Umlaute ersetzen
   - Sonst muesste man auch "Ä", "Ö", "Ü" separat behandeln

3. **String-Methoden:**
   - `lower()` - Alles in Kleinbuchstaben
   - `upper()` - Alles in Grossbuchstaben
   - `replace(alt, neu)` - Ersetzen

---

# Aufgabe 4: Schaltjahr pruefen (10 Punkte)

**Schreiben Sie ein Programm, das prueft, ob ein eingegebenes Jahr ein Schaltjahr ist.**

Regeln:
- Durch 4 teilbar → Schaltjahr
- ABER durch 100 teilbar → KEIN Schaltjahr
- ABER durch 400 teilbar → doch Schaltjahr

**Loesung:**

```python
jahr = int(input("Jahr: "))

if jahr % 400 == 0:
    print("Schaltjahr")
elif jahr % 100 == 0:
    print("Gemeinjahr")
elif jahr % 4 == 0:
    print("Schaltjahr")
else:
    print("Gemeinjahr")
```

**Alternative (kompakter):**

```python
jahr = int(input("Jahr: "))

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print("Schaltjahr")
else:
    print("Gemeinjahr")
```

**Wichtige Punkte:**

1. **Reihenfolge der Bedingungen:**
   - ZUERST durch 400 pruefen (Sonderfall)
   - DANN durch 100 (Ausnahme)
   - DANN durch 4 (Grundregel)

2. **Testfaelle:**
   - 2000 → Schaltjahr (durch 400 teilbar)
   - 1900 → Gemeinjahr (durch 100, aber nicht durch 400)
   - 2024 → Schaltjahr (durch 4, nicht durch 100)
   - 2023 → Gemeinjahr (nicht durch 4)

---

# Aufgabe 5: Wie viele Zahlen sind gleich? (10 Punkte)

**Schreiben Sie ein Programm, das drei ganze Zahlen vom Benutzer entgegennimmt und angibt, wie viele davon gleich sind.**

- Wenn alle drei gleich → 3
- Wenn genau zwei gleich → 2
- Wenn alle verschieden → 0

**Loesung:**

```python
z1 = int(input("Zahl 1: "))
z2 = int(input("Zahl 2: "))
z3 = int(input("Zahl 3: "))

if z1 == z2 == z3:
    print(3)
elif z1 == z2 or z1 == z3 or z2 == z3:
    print(2)
else:
    print(0)
```

**Wichtige Punkte:**

1. **Verkettete Vergleiche:**
   - Python erlaubt `z1 == z2 == z3` (wie in Mathe!)
   - Entspricht `z1 == z2 and z2 == z3`

2. **Logische Operatoren:**
   - `or` - mindestens eine Bedingung muss wahr sein
   - `and` - alle Bedingungen muessen wahr sein

**Beispiel:**
```
Zahl 1: 3
Zahl 2: -4
Zahl 3: 3
2
```

---

# Aufgabe 6: Pluralendung (10 Punkte)

**Schreiben Sie ein Programm, das den Benutzer nach einer Zahl fragt und grammatikalisch korrekt ausgibt: "N Datei(en) kopiert."**

**Loesung:**

```python
anzahl = int(input("Wie viele Dateien sollen kopiert werden? "))

if anzahl == 1:
    print(f"{anzahl} Datei kopiert.")
else:
    print(f"{anzahl} Dateien kopiert.")
```

**Erweiterte Version mit Validierung:**

```python
try:
    anzahl = int(input("Anzahl: "))
    if anzahl < 0:
        print("Fehler: Negative Zahl!")
    elif anzahl == 1:
        print(f"{anzahl} Datei kopiert.")
    else:
        print(f"{anzahl} Dateien kopiert.")
except ValueError:
    print("Bitte eine ganze Zahl eingeben!")
```

**Wichtige Punkte:**

1. **f-Strings:**
   - `f"{variable}"` - formatierter String
   - Variable wird direkt im Text eingefuegt

2. **Grammatik beachten:**
   - 1 → Singular ("Datei")
   - 0, 2, 3, ... → Plural ("Dateien")

**Beispiel:**
```
Wie viele Dateien sollen kopiert werden? 1
1 Datei kopiert.

Wie viele Dateien sollen kopiert werden? 15
15 Dateien kopiert.
```

---

# Aufgabe 7: Module importieren (PROBEKLAUSUR!)

## Aufgabe 7a: Spezifische Funktion importieren

**Wie koennen Sie nur die Funktion `sqrt` aus dem Modul `math` importieren?**

**Loesung:**

```python
from math import sqrt

# Jetzt kann sqrt direkt verwendet werden:
print(sqrt(16))  # 4.0
```

**Erklaerung:**
- `from modul import funktion` importiert nur die angegebene Funktion
- Die Funktion kann dann OHNE Modulprefix verwendet werden
- Alternative: `from math import sqrt, pi, sin` fuer mehrere Funktionen

---

## Aufgabe 7b: Modul mit Alias importieren

**Wie koennen Sie das Modul `math` unter dem Namen `m` importieren?**

**Loesung:**

```python
import math as m

# Jetzt wird m statt math verwendet:
print(m.sqrt(16))  # 4.0
print(m.pi)        # 3.141592653589793
```

**Erklaerung:**
- `import modul as alias` gibt dem Modul einen Kurznamen
- Nuetzlich fuer lange Modulnamen: `import numpy as np`
- Spart Tipparbeit und ist Konvention (np, pd, plt)

---

## Alle Import-Varianten im Ueberblick

```python
# 1. Ganzes Modul importieren
import math
print(math.sqrt(16))  # 4.0

# 2. Modul mit Alias
import math as m
print(m.sqrt(16))     # 4.0

# 3. Spezifische Funktion importieren
from math import sqrt
print(sqrt(16))       # 4.0

# 4. Mehrere Funktionen importieren
from math import sqrt, pi, sin
print(pi)             # 3.141592653589793

# 5. Alles importieren (NICHT EMPFOHLEN!)
from math import *    # Kann Namenskonflikte verursachen
```

---

# Aufgabe 8: NumPy Grundlagen (PROBEKLAUSUR!)

**Was tut folgender NumPy-Code? Geben Sie die Werte der Matrix c an.**

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.ones((3, 3))
c = a + b
```

**Loesung:**

**Wert von c:**
```python
c = [[2, 3, 4],
     [5, 6, 7],
     [8, 9, 10]]
```

**Erklaerung:**

1. `np.array([[1,2,3], [4,5,6], [7,8,9]])` erstellt eine 3x3-Matrix:
   ```
   a = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
   ```

2. `np.ones((3, 3))` erstellt eine 3x3-Matrix nur mit Einsen:
   ```
   b = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
   ```

3. `c = a + b` addiert die Matrizen **elementweise**:
   ```
   c[0,0] = 1 + 1 = 2
   c[0,1] = 2 + 1 = 3
   c[0,2] = 3 + 1 = 4
   ... usw.
   ```

**Wichtige NumPy-Funktionen:**

```python
import numpy as np

np.array([1, 2, 3])      # 1D-Array
np.array([[1,2], [3,4]]) # 2D-Array (Matrix)
np.zeros((2, 3))         # 2x3-Matrix mit Nullen
np.ones((3, 3))          # 3x3-Matrix mit Einsen
np.eye(3)                # 3x3-Einheitsmatrix
np.arange(0, 10, 2)      # [0, 2, 4, 6, 8]

# Elementweise Operationen
a + b   # Addition
a - b   # Subtraktion
a * b   # Multiplikation (elementweise!)
a @ b   # Matrixmultiplikation
```

---

# Aufgabe 9: random Modul (PROBEKLAUSUR!)

**Schreiben Sie eine Funktion `wuerfel5()`, die eine Liste mit fuenf Zufallszahlen von 1 bis 6 zurueckgibt.**

**Loesung:**

```python
from random import randint

def wuerfel5():
    ergebnis = []
    for _ in range(5):
        ergebnis.append(randint(1, 6))
    return ergebnis

# Test:
print(wuerfel5())  # z.B. [3, 1, 5, 2, 6]
```

**Alternative mit List Comprehension:**

```python
from random import randint

def wuerfel5():
    return [randint(1, 6) for _ in range(5)]
```

**Wichtige random-Funktionen:**

```python
from random import randint, random, choice, shuffle

randint(1, 6)        # Zufallszahl 1 bis 6 (inklusive!)
random()             # Zufallszahl 0.0 bis 1.0
choice([1,2,3])      # Zufaelliges Element aus Liste
shuffle(liste)       # Liste mischen (in-place!)
```

---

# Aufgabe 10: Dreierpasch (PROBEKLAUSUR!)

**Schreiben Sie eine Funktion `dreierpasch(wurf)`, die True zurueckgibt, wenn die Liste mindestens drei gleiche Augenzahlen enthaelt.**

**Loesung:**

```python
def dreierpasch(wurf):
    # Zaehle jede Augenzahl
    zaehler = {}
    for zahl in wurf:
        zaehler[zahl] = zaehler.get(zahl, 0) + 1

    # Pruefe ob mindestens eine Zahl 3x oder oefter vorkommt
    for anzahl in zaehler.values():
        if anzahl >= 3:
            return True
    return False

# Test:
print(dreierpasch([3, 1, 2, 3, 3]))  # True (dreimal 3)
print(dreierpasch([1, 2, 3, 4, 5]))  # False
print(dreierpasch([6, 6, 6, 6, 1]))  # True (viermal 6)
```

**Alternative mit max():**

```python
def dreierpasch(wurf):
    zaehler = {}
    for zahl in wurf:
        zaehler[zahl] = zaehler.get(zahl, 0) + 1
    return max(zaehler.values()) >= 3
```

---

# Aufgabe 11: Dictionary vs Menge (PROBEKLAUSUR!)

**Was ist der Unterschied zwischen einem Dictionary und einer Menge (Set) in Python?**

**Loesung:**

| Eigenschaft | Dictionary | Menge (Set) |
|-------------|------------|-------------|
| Syntax | `{"a": 1, "b": 2}` | `{1, 2, 3}` |
| Speichert | Key-Value-Paare | Nur Werte |
| Zugriff | `d["key"]` | `x in s` |
| Duplikate | Keys eindeutig | Keine Duplikate |
| Reihenfolge | Erhalten (ab 3.7) | Nicht garantiert |

**Beispiele:**

```python
# Dictionary: Key-Value-Paare
person = {"name": "Anna", "alter": 25}
print(person["name"])  # "Anna"

# Menge (Set): Nur einzigartige Werte
zahlen = {1, 2, 2, 3, 3, 3}
print(zahlen)  # {1, 2, 3} - Duplikate entfernt!

# Set aus Liste erstellen (Duplikate entfernen)
liste = [1, 2, 2, 3, 3, 3]
eindeutig = set(liste)  # {1, 2, 3}
```

**Wann was verwenden?**
- **Dictionary:** Wenn Werte zu Schluesseln gehoeren (z.B. Name → Alter)
- **Set:** Wenn nur eindeutige Werte wichtig sind (z.B. alle verschiedenen Woerter)

---

# Aufgabe 12: Listen-Operationen (PROBEKLAUSUR!)

## Aufgabe 12a: Liste erweitern mit +=

**Was ist der Wert von `a` nach folgender Code-Zeile?**

```python
a = [1, 2, 3]
a += [4, 5]
```

**Loesung:**

`a = [1, 2, 3, 4, 5]`

**Erklaerung:**
- `a += [4, 5]` ist aequivalent zu `a.extend([4, 5])`
- Die Elemente 4 und 5 werden einzeln angehaengt
- Die Liste wird **in-place** erweitert

---

## Aufgabe 12b: Liste erweitern mit extend()

**Was ist der Wert von `a` nach folgender Code-Zeile?**

```python
a = [1, 2, 3]
a.extend([4, 5])
```

**Loesung:**

`a = [1, 2, 3, 4, 5]`

**Erklaerung:**
- `extend()` fuegt alle Elemente der uebergebenen Liste einzeln hinzu
- Gleich wie `a += [4, 5]`

---

## Aufgabe 12c: IndexError (WICHTIG!)

**Was ist an folgendem Code falsch?**

```python
a = [1, 2, 3]
a[3] = 4
```

**Loesung:**

**IndexError: list assignment index out of range**

**Erklaerung:**
- Liste `a` hat 3 Elemente mit Indizes 0, 1, 2
- Index 3 existiert NICHT
- Man kann nicht auf einen nicht existierenden Index zuweisen

**Richtig waere:**
```python
a = [1, 2, 3]
a.append(4)  # [1, 2, 3, 4]
# ODER
a = [1, 2, 3]
a += [4]     # [1, 2, 3, 4]
```

---

# Aufgabe 13: List Comprehension (PROBEKLAUSUR!)

## Aufgabe 13a: Quadratzahlen

**Erzeugen Sie eine Liste mit den Quadraten der Zahlen von 1 bis k.**

**Loesung:**

```python
k = 5
quadrate = [i**2 for i in range(1, k+1)]
print(quadrate)  # [1, 4, 9, 16, 25]
```

**Erklaerung:**
- `range(1, k+1)` erzeugt Zahlen 1 bis k
- `i**2` berechnet das Quadrat
- List Comprehension: `[ausdruck for variable in iterable]`

---

## Aufgabe 13b: List Comprehension verstehen

**Schreiben Sie den Wert von `a` nach: `a = [i**2 for i in range(5)]`**

**Loesung:**

`a = [0, 1, 4, 9, 16]`

**Erklaerung:**
- `range(5)` erzeugt 0, 1, 2, 3, 4
- Quadrate: 0², 1², 2², 3², 4² = 0, 1, 4, 9, 16

---

# Aufgabe 14: input() Falle (PROBEKLAUSUR!)

**Was ist an folgendem Code falsch?**

```python
number = input("Bitte eine Zahl eingeben: ")
print(number * 2)
```

**Loesung:**

**Das Problem:** `input()` gibt IMMER einen **String** zurueck!

Wenn der Benutzer "5" eingibt:
- `number` ist der String `"5"` (nicht die Zahl 5)
- `"5" * 2` ergibt `"55"` (String-Verdopplung!)
- NICHT 10 wie erwartet

**Korrektur:**

```python
number = int(input("Bitte eine Zahl eingeben: "))
print(number * 2)  # Jetzt: 10
```

**Mit Fehlerbehandlung:**

```python
try:
    number = int(input("Bitte eine Zahl eingeben: "))
    print(number * 2)
except ValueError:
    print("Ungueltige Zahl!")
```

---

# Aufgabe 15: Klasse Student (PROBEKLAUSUR!)

**Erstellen Sie eine Klasse `Student` mit:**
1. Konstruktor mit Name und optionaler Notenliste
2. Methode `add_grade(grade)` zum Hinzufuegen einer Note
3. Methode `average_grade()` fuer den Notendurchschnitt
4. Methode `__str__()` fuer die String-Darstellung

**Loesung:**

```python
class Student:
    def __init__(self, name, noten=None):
        self.name = name
        if noten is None:
            self.noten = []
        else:
            self.noten = noten

    def add_grade(self, grade):
        self.noten.append(grade)

    def average_grade(self):
        if len(self.noten) == 0:
            return 0
        return sum(self.noten) / len(self.noten)

    def __str__(self):
        avg = self.average_grade()
        return f"{self.name}: Noten={self.noten}, Durchschnitt={avg:.2f}"

# Beispielcode
student = Student("Max Mustermann")
student.add_grade(85)
student.add_grade(92)
print(student)  # Max Mustermann: Noten=[85, 92], Durchschnitt=88.50
```

**Wichtige Punkte:**

1. **Mutable Default Argument Falle:**
   - FALSCH: `def __init__(self, name, noten=[])`
   - Die leere Liste wird GETEILT zwischen allen Instanzen!
   - RICHTIG: `noten=None` und dann im Body pruefen

2. **`self` Parameter:**
   - Jede Methode braucht `self` als ersten Parameter
   - `self.attribut` greift auf Instanzattribute zu

3. **`__str__` Methode:**
   - Wird von `print()` aufgerufen
   - Muss einen String zurueckgeben

---

# Zusammenfassung: Klausurtipps

## Haeufige Fallen:

1. **for-Schleife ueberschreibt Variable:**
   ```python
   i = 100
   for i in range(3):  # i wird 0, 1, 2
       pass
   # i ist jetzt 2, nicht 100!
   ```

2. **range(n) endet bei n-1:**
   ```python
   range(5)  # 0, 1, 2, 3, 4 (nicht 5!)
   range(1, 5)  # 1, 2, 3, 4 (nicht 5!)
   ```

3. **Strings sind unveraenderlich:**
   ```python
   s = "hallo"
   s.upper()  # Gibt "HALLO" zurueck, aber s bleibt "hallo"
   s = s.upper()  # Jetzt ist s = "HALLO"
   ```

4. **dict[key] vs dict.get(key):**
   ```python
   d = {"a": 1}
   d["b"]  # KeyError!
   d.get("b", 0)  # Gibt 0 zurueck (kein Fehler)
   ```

## Wichtigste Konzepte:

1. **Modulo fuer Teilbarkeit:** `x % y == 0`
2. **dict.get() zum Zaehlen:** `d[key] = d.get(key, 0) + 1`
3. **try-except fuer Benutzereingaben**
4. **String-Methoden:** `lower()`, `replace()`
5. **for-Schleifen mit range()**

---
