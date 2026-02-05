# Zusätzliche Themen - Programmierung für KI

## 1. NumPy Grundlagen

NumPy ist die fundamentale Bibliothek für numerische Berechnungen in Python.

### Arrays erstellen

```python
import numpy as np

# Array aus Liste erstellen
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Spezielle Arrays
nullen = np.zeros((3, 3))    # 3x3 Matrix mit Nullen
einsen = np.ones((2, 4))     # 2x4 Matrix mit Einsen
```

### Shape und Dimensionen

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)    # (2, 3) - 2 Zeilen, 3 Spalten
print(a.ndim)     # 2 - Anzahl Dimensionen
```

### Element-weise Operationen

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.ones((3, 3))

c = a + b    # Addition jedes Elements mit 1
d = a * 2    # Multiplikation jedes Elements mit 2
e = a ** 2   # Quadrieren jedes Elements
```

---

## 2. Module importieren

### Verschiedene Import-Varianten

```python
# Gesamtes Modul importieren
import math
ergebnis = math.sqrt(16)    # 4.0

# Einzelne Funktion importieren
from math import sqrt
ergebnis = sqrt(16)         # 4.0

# Modul mit Alias importieren
import numpy as np
arr = np.array([1, 2, 3])

# Mehrere Funktionen importieren
from math import sqrt, pi, sin
```

---

## 3. Random Modul

Für Zufallszahlen und zufällige Auswahlen.

```python
from random import randint, random, choice

# Zufällige Ganzzahl zwischen a und b (inklusive)
zahl = randint(1, 6)        # Würfelwurf: 1, 2, 3, 4, 5 oder 6

# Zufällige Fließkommazahl zwischen 0 und 1
wert = random()             # z.B. 0.7234...

# Zufälliges Element aus Liste wählen
farben = ["rot", "grün", "blau"]
auswahl = choice(farben)    # z.B. "grün"
```

---

## 4. Wichtige eingebaute Funktionen

### Sequenz-Funktionen

```python
# range() - Zahlenfolge erzeugen
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8, 2):    # 2, 4, 6 (Start, Stop, Schritt)
    print(i)

# Aggregatfunktionen
zahlen = [3, 1, 4, 1, 5, 9]
print(len(zahlen))          # 6 - Anzahl Elemente
print(sum(zahlen))          # 23 - Summe
print(min(zahlen))          # 1 - Minimum
print(max(zahlen))          # 9 - Maximum
```

### Typumwandlung

```python
# Typ abfragen
print(type(42))             # <class 'int'>
print(type("Hallo"))        # <class 'str'>

# Umwandlungen
int("42")                   # 42 (String zu Integer)
float("3.14")               # 3.14 (String zu Float)
str(100)                    # "100" (Integer zu String)
```

### Datenstruktur-Konstruktoren

```python
# Leere Strukturen erstellen
liste = list()              # []
tupel = tuple()             # ()
woerterbuch = dict()        # {}
menge = set()               # set()

# Aus anderen Typen konvertieren
list("abc")                 # ['a', 'b', 'c']
tuple([1, 2, 3])            # (1, 2, 3)
set([1, 2, 2, 3])           # {1, 2, 3} - Duplikate entfernt
```

---

## Zusammenfassung

| Thema | Wichtige Elemente |
|-------|-------------------|
| **NumPy** | `np.array()`, `np.ones()`, `np.zeros()`, `.shape` |
| **Import** | `import`, `from ... import`, Alias mit `as` |
| **Random** | `randint(a, b)`, `random()`, `choice()` |
| **Eingebaut** | `range()`, `len()`, `sum()`, `min()`, `max()`, Typumwandlung |
