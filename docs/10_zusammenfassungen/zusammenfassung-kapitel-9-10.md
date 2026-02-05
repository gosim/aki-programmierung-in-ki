# Zusammenfassung Kapitel 9-10: Dictionaries und Tupel

## Kapitel 9: Dictionaries (KLAUSURRELEVANT!)

### Was ist ein Dictionary?

Ein Dictionary ist eine Datenstruktur, die **Key-Value-Paare** (Schlüssel-Wert-Paare) speichert. Anders als Listen, die über numerische Indizes arbeiten, können Dictionaries beliebige unveränderliche Werte als Schlüssel verwenden.

### Anlegen von Dictionaries

```python
# Leeres Dictionary mit geschweiften Klammern
d = {}

# Leeres Dictionary mit dict()
d = dict()

# Dictionary mit Werten initialisieren
student = {"name": "Anna", "alter": 22, "matrikel": 12345}

# Mit dict() und Keyword-Argumenten
student = dict(name="Anna", alter=22, matrikel=12345)
```

### Zugriff auf Elemente

```python
student = {"name": "Anna", "alter": 22}

# Direkter Zugriff mit eckigen Klammern
print(student["name"])  # Ausgabe: Anna

# ACHTUNG: KeyError wenn Schlüssel nicht existiert!
print(student["note"])  # KeyError: 'note'

# Sicherer Zugriff mit get() - gibt None zurück wenn Key fehlt
print(student.get("note"))  # Ausgabe: None

# get() mit Standardwert
print(student.get("note", "keine Note"))  # Ausgabe: keine Note
```

### Das wichtigste Muster für die Klausur: Zählen mit Dictionaries

```python
# KLAUSURRELEVANTES MUSTER - unbedingt merken!
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

**Erklärung Schritt für Schritt:**
1. `count.get(word, 0)` - Hole den aktuellen Zählwert für `word`, falls nicht vorhanden: 0
2. `+ 1` - Erhöhe den Wert um 1
3. `count[word] = ...` - Speichere den neuen Wert

**Vollständiges Beispiel:**

```python
text = "die katze und die maus und die ente"
words = text.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
# Ausgabe: {'die': 3, 'katze': 1, 'und': 2, 'maus': 1, 'ente': 1}
```

### Wichtige Dictionary-Methoden

```python
student = {"name": "Anna", "alter": 22, "fach": "Informatik"}

# keys() - gibt alle Schlüssel zurück
print(student.keys())    # dict_keys(['name', 'alter', 'fach'])

# values() - gibt alle Werte zurück
print(student.values())  # dict_values(['Anna', 22, 'Informatik'])

# items() - gibt alle Key-Value-Paare als Tupel zurück
print(student.items())   # dict_items([('name', 'Anna'), ('alter', 22), ('fach', 'Informatik')])
```

### Iteration über Dictionaries

```python
student = {"name": "Anna", "alter": 22, "fach": "Informatik"}

# Iteration über Schlüssel (Standard)
for key in student:
    print(key)

# Explizit über Schlüssel
for key in student.keys():
    print(key)

# Über Werte
for value in student.values():
    print(value)

# Über Schlüssel und Werte gleichzeitig (häufig verwendet!)
for key, value in student.items():
    print(f"{key}: {value}")
```

### Der in-Operator für Keys

```python
student = {"name": "Anna", "alter": 22}

# Prüfen ob Schlüssel existiert
if "name" in student:
    print("Name ist vorhanden")

if "note" not in student:
    print("Keine Note eingetragen")

# ACHTUNG: in prüft nur Schlüssel, nicht Werte!
print("Anna" in student)  # False (prüft nur Keys!)
print("Anna" in student.values())  # True (prüft Werte)
```

### KeyError vermeiden

```python
student = {"name": "Anna"}

# SCHLECHT - kann KeyError werfen
# note = student["note"]  # KeyError!

# GUT - mit get() und Standardwert
note = student.get("note", "nicht vorhanden")

# GUT - vorher prüfen
if "note" in student:
    note = student["note"]
else:
    note = "nicht vorhanden"
```

### Weitere nützliche Operationen

```python
d = {"a": 1, "b": 2}

# Element hinzufügen oder ändern
d["c"] = 3  # hinzufügen
d["a"] = 10  # ändern

# Element löschen
del d["b"]

# Länge des Dictionaries
print(len(d))

# Dictionary leeren
d.clear()
```

---

## Kapitel 10: Tupel

### Was ist ein Tupel?

Ein Tupel ist eine **unveränderliche (immutable)** geordnete Sequenz von Elementen. Einmal erstellt, können die Elemente nicht mehr geändert werden.

### Anlegen von Tupeln

```python
# Mit runden Klammern
t = (1, 2, 3)

# Klammern sind optional (aber empfohlen für Lesbarkeit)
t = 1, 2, 3

# Einelementiges Tupel - Komma ist wichtig!
t = (5,)    # Tupel mit einem Element
t = (5)     # KEINE Tupel! Das ist nur die Zahl 5 in Klammern

# Leeres Tupel
t = ()
t = tuple()

# Mit tuple() aus anderen Sequenzen erstellen
t = tuple([1, 2, 3])       # aus Liste
t = tuple("hello")         # aus String: ('h', 'e', 'l', 'l', 'o')
```

### Tuple Unpacking (Entpacken)

```python
# Grundlegendes Unpacking
koordinaten = (10, 20)
x, y = koordinaten
print(x)  # 10
print(y)  # 20

# Mehrere Werte gleichzeitig zuweisen
a, b, c = (1, 2, 3)

# Variablen tauschen ohne Hilfsvariable!
a = 5
b = 10
a, b = b, a  # a ist jetzt 10, b ist jetzt 5

# Unpacking in for-Schleifen (sehr häufig!)
punkte = [(1, 2), (3, 4), (5, 6)]
for x, y in punkte:
    print(f"x={x}, y={y}")

# Mit enumerate()
namen = ["Anna", "Ben", "Clara"]
for index, name in enumerate(namen):
    print(f"{index}: {name}")

# Mit dict.items()
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(f"{key} -> {value}")
```

### Tupel als Dictionary-Keys

Da Tupel **unveränderlich** sind, können sie als Dictionary-Schlüssel verwendet werden. Listen können das **nicht**, weil sie veränderlich sind.

```python
# Tupel als Keys - funktioniert!
positionen = {}
positionen[(0, 0)] = "Start"
positionen[(10, 5)] = "Ziel"

# Koordinaten nachschlagen
print(positionen[(0, 0)])  # Ausgabe: Start

# Listen als Keys - FEHLER!
# d = {}
# d[[1, 2]] = "test"  # TypeError: unhashable type: 'list'
```

**Anwendungsbeispiel:** Schachbrett

```python
schachbrett = {}
schachbrett[(0, 0)] = "Turm"
schachbrett[(0, 1)] = "Springer"
schachbrett[(4, 0)] = "König"

# Position abfragen
position = (4, 0)
if position in schachbrett:
    print(f"Auf {position} steht: {schachbrett[position]}")
```

### Unterschied zwischen Tupel und Liste

| Eigenschaft | Tupel | Liste |
|------------|-------|-------|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Veränderbar | Nein (immutable) | Ja (mutable) |
| Als Dict-Key | Ja | Nein |
| Methoden | Wenige (`count`, `index`) | Viele (`append`, `sort`, etc.) |
| Performance | Schneller | Langsamer |
| Verwendung | Feste Datenstrukturen | Dynamische Sammlungen |

```python
# Liste - veränderbar
liste = [1, 2, 3]
liste[0] = 99  # funktioniert
liste.append(4)  # funktioniert

# Tupel - unveränderbar
tupel = (1, 2, 3)
# tupel[0] = 99  # TypeError: 'tuple' object does not support item assignment
# tupel.append(4)  # AttributeError: 'tuple' object has no attribute 'append'
```

### Die tuple() Funktion

```python
# Liste zu Tupel konvertieren
liste = [1, 2, 3]
t = tuple(liste)  # (1, 2, 3)

# String zu Tupel
t = tuple("abc")  # ('a', 'b', 'c')

# Range zu Tupel
t = tuple(range(5))  # (0, 1, 2, 3, 4)

# Umgekehrt: Tupel zu Liste
t = (1, 2, 3)
liste = list(t)  # [1, 2, 3]
```

### Tupel-Methoden

Tupel haben nur zwei Methoden:

```python
t = (1, 2, 2, 3, 2, 4)

# count() - zählt Vorkommen eines Elements
print(t.count(2))  # Ausgabe: 3

# index() - findet Position des ersten Vorkommens
print(t.index(2))  # Ausgabe: 1
```

### Wann Tupel, wann Listen?

**Verwende Tupel wenn:**
- Die Daten sich nicht ändern sollen (z.B. Koordinaten, RGB-Farben)
- Du die Daten als Dictionary-Key brauchst
- Du Werte von einer Funktion zurückgibst

**Verwende Listen wenn:**
- Du Elemente hinzufügen/entfernen musst
- Du die Reihenfolge ändern musst (sortieren)
- Du eine dynamische Sammlung brauchst

---

## Klausur-Checkliste

### Dictionary - Das musst du können:
- [ ] Dictionary anlegen mit `{}` und `dict()`
- [ ] Elemente mit `d[key]` und `d.get(key, default)` abrufen
- [ ] **Das Zählmuster auswendig kennen!**
- [ ] Mit `keys()`, `values()`, `items()` iterieren
- [ ] Mit `in` prüfen ob Key existiert
- [ ] KeyError mit `get()` vermeiden

### Tupel - Das musst du können:
- [ ] Tupel mit `()` anlegen
- [ ] Einelementiges Tupel: `(5,)` nicht `(5)`
- [ ] Tuple Unpacking: `a, b = (1, 2)`
- [ ] Wissen dass Tupel unveränderlich sind
- [ ] Tupel als Dictionary-Keys verwenden können
- [ ] Unterschied zu Listen erklären können
