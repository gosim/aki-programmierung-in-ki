# Kapitel 8: Listen

## Grundlagen

Listen sind **geordnete, veränderbare (mutable)** Sammlungen von Elementen in Python. Im Gegensatz zu Strings können Listen nach ihrer Erstellung modifiziert werden.

## Listen anlegen

```python
# Leere Liste erstellen
leere_liste = []
leere_liste = list()

# Liste mit Elementen
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "Hallo", 3.14, True]  # Verschiedene Datentypen möglich

# Liste aus anderem Iterable erstellen
buchstaben = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
```

## Indizierung und Slicing

Listen verwenden die gleiche Indizierung wie Strings:

```python
farben = ["rot", "grün", "blau", "gelb"]

# Einzelne Elemente (Index beginnt bei 0)
farben[0]    # "rot"
farben[-1]   # "gelb" (letztes Element)

# Slicing [start:ende:schritt]
farben[1:3]   # ["grün", "blau"]
farben[:2]    # ["rot", "grün"]
farben[::2]   # ["rot", "blau"] (jedes zweite Element)
farben[::-1]  # ["gelb", "blau", "grün", "rot"] (umgekehrt)

# Elemente ändern (nur bei Listen möglich!)
farben[0] = "orange"  # Liste ist jetzt ["orange", "grün", "blau", "gelb"]
```

## Wichtige Listenmethoden

### Elemente hinzufügen

```python
zahlen = [1, 2, 3]

# Ein Element am Ende anfügen
zahlen.append(4)        # [1, 2, 3, 4]

# Mehrere Elemente anfügen
zahlen.extend([5, 6])   # [1, 2, 3, 4, 5, 6]

# Element an bestimmter Position einfügen
zahlen.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]
```

### Elemente entfernen

```python
zahlen = [1, 2, 3, 4, 5]

# Letztes Element entfernen und zurückgeben
letztes = zahlen.pop()      # letztes = 5, zahlen = [1, 2, 3, 4]

# Element an Index entfernen und zurückgeben
zweites = zahlen.pop(1)     # zweites = 2, zahlen = [1, 3, 4]

# Erstes Vorkommen eines Werts entfernen
zahlen.remove(3)            # zahlen = [1, 4]
# Achtung: ValueError wenn Wert nicht vorhanden!
```

### Sortieren und Umkehren

```python
zahlen = [3, 1, 4, 1, 5, 9, 2, 6]

# Liste sortieren (verändert die Liste!)
zahlen.sort()               # [1, 1, 2, 3, 4, 5, 6, 9]
zahlen.sort(reverse=True)   # [9, 6, 5, 4, 3, 2, 1, 1]

# Liste umkehren
zahlen.reverse()            # [1, 1, 2, 3, 4, 5, 6, 9]
```

## Listen durchlaufen mit for

```python
fruechte = ["Apfel", "Birne", "Kirsche"]

# Einfache Iteration
for frucht in fruechte:
    print(frucht)

# Mit Index (enumerate)
for index, frucht in enumerate(fruechte):
    print(f"{index}: {frucht}")
```

## Der in-Operator

```python
zahlen = [1, 2, 3, 4, 5]

3 in zahlen      # True
10 in zahlen     # False
10 not in zahlen # True
```

## Eingebaute Funktionen für Listen

```python
zahlen = [3, 1, 4, 1, 5, 9, 2, 6]

len(zahlen)   # 8 (Anzahl der Elemente)
sum(zahlen)   # 31 (Summe aller Elemente)
min(zahlen)   # 1 (kleinstes Element)
max(zahlen)   # 9 (größtes Element)
```

## List Comprehensions

List Comprehensions sind eine kompakte Syntax zum Erstellen von Listen:

```python
# Quadratzahlen von 0 bis 9
quadrate = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Mit Bedingung (nur gerade Zahlen)
gerade_quadrate = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Verschachtelt
matrix = [[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## Listen als Funktionsargumente (Referenzsemantik!)

**Wichtig:** Listen werden als Referenz übergeben, nicht als Kopie!

```python
def verdopple_elemente(liste):
    for i in range(len(liste)):
        liste[i] *= 2

zahlen = [1, 2, 3]
verdopple_elemente(zahlen)
print(zahlen)  # [2, 4, 6] - Original wurde verändert!

# Kopie erstellen, um Original zu schützen
def verdopple_sicher(liste):
    kopie = liste[:]  # oder list(liste) oder liste.copy()
    for i in range(len(kopie)):
        kopie[i] *= 2
    return kopie
```

## Unterschied: += vs. extend()

```python
# Fall 1: += erstellt neue Liste und weist neu zu
a = [1, 2, 3]
b = a
a += [4, 5]
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5] - b zeigt auf dieselbe Liste!

# Fall 2: Neuzuweisung mit + erstellt neue Liste
a = [1, 2, 3]
b = a
a = a + [4, 5]
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3] - b zeigt noch auf alte Liste!

# extend() verhält sich wie +=
a = [1, 2, 3]
b = a
a.extend([4, 5])
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5] - beide zeigen auf dieselbe Liste
```

**Merke:** `+=` und `extend()` modifizieren die Liste in-place, während `a = a + [...]` eine neue Liste erstellt.

---

## Klausurbeispiel: IndexError

```python
a = [1, 2, 3]
a[3] = 4  # Was passiert?
```

**Antwort:** Es wird ein `IndexError` ausgelöst!

```
IndexError: list assignment index out of range
```

**Erklärung:** Die Liste `a` hat nur 3 Elemente mit den Indizes 0, 1 und 2. Der Index 3 existiert nicht. Um ein Element hinzuzufügen, muss `append()` verwendet werden:

```python
a = [1, 2, 3]
a.append(4)   # Korrekt: [1, 2, 3, 4]
# oder
a = [1, 2, 3]
a += [4]      # Korrekt: [1, 2, 3, 4]
```

---

## Zusammenfassung der wichtigsten Punkte

| Eigenschaft | Beschreibung |
|-------------|--------------|
| Veränderbar | Listen können nach Erstellung modifiziert werden |
| Indiziert | Zugriff über Index (ab 0), negative Indizes möglich |
| Heterogen | Kann verschiedene Datentypen enthalten |
| Referenz | Wird als Referenz übergeben, nicht kopiert |

| Methode | Beschreibung |
|---------|--------------|
| `append(x)` | Fügt x am Ende hinzu |
| `extend(liste)` | Fügt alle Elemente der Liste hinzu |
| `pop()` / `pop(i)` | Entfernt und gibt letztes/i-tes Element zurück |
| `remove(x)` | Entfernt erstes Vorkommen von x |
| `sort()` | Sortiert die Liste |
| `reverse()` | Kehrt die Reihenfolge um |
