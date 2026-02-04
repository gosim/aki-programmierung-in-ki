# Testfragen Kapitel 7-8: Dateien und Listen

---

## Kapitel 7: Dateien

---

**Aussage:** `open("datei.txt", "r")` oeffnet eine Datei zum Lesen.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Modi fuer `open()`:
- `"r"` - Read (Lesen, Standard)
- `"w"` - Write (Schreiben, ueberschreibt!)
- `"a"` - Append (Anhaengen)
- `"x"` - Exclusive (Fehler wenn existiert)
</details>

---

**Aussage:** Nach `open()` muss man die Datei mit `close()` schliessen.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Man sollte Dateien immer schliessen. Besser: `with`-Statement verwenden!

```python
# Manuell (nicht empfohlen):
f = open("datei.txt", "r")
inhalt = f.read()
f.close()

# Mit with (empfohlen):
with open("datei.txt", "r") as f:
    inhalt = f.read()
# Datei wird automatisch geschlossen
```
</details>

---

**Aussage:** Der Modus "w" ueberschreibt eine existierende Datei.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`"w"` loescht den Inhalt und schreibt neu. Um anzuhaengen, benutze `"a"`.
</details>

---

**Frage 7.1:** Welcher Modus haengt Text an eine Datei an?

- [ ] a) "r"
- [ ] b) "w"
- [ ] c) "a"
- [ ] d) "x"

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`"a"` steht fuer "append" (anhaengen).
</details>

---

**Frage 7.2:** Wie liest man eine ganze Datei in einen String?

<details>
<summary>Loesung anzeigen</summary>

```python
with open("datei.txt", "r") as f:
    inhalt = f.read()  # Ganze Datei als String
```

**Alternativen:**
```python
# Zeile fuer Zeile lesen (als Liste):
with open("datei.txt", "r") as f:
    zeilen = f.readlines()  # Liste von Strings

# Zeile fuer Zeile iterieren:
with open("datei.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())  # strip() entfernt Zeilenumbruch
```
</details>

---

**Frage 7.3:** Was passiert bei diesem Code, wenn "test.txt" nicht existiert?

```python
f = open("test.txt", "r")
```

- [ ] a) Eine leere Datei wird erstellt
- [ ] b) FileNotFoundError
- [ ] c) None wird zurueckgegeben
- [ ] d) Das Programm wartet

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Ein **FileNotFoundError** tritt auf. Man sollte das mit try-except behandeln:

```python
try:
    with open("test.txt", "r") as f:
        inhalt = f.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
```
</details>

---

**Frage 7.4:** Wie schreibt man in eine Datei?

<details>
<summary>Loesung anzeigen</summary>

```python
# Neue Datei erstellen / ueberschreiben:
with open("output.txt", "w") as f:
    f.write("Hallo Welt\n")
    f.write("Zweite Zeile\n")

# An existierende Datei anhaengen:
with open("output.txt", "a") as f:
    f.write("Angehaengte Zeile\n")
```
</details>

---

## Kapitel 8: Listen

---

**Aussage:** Listen in Python sind veraenderbar (mutable).

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Listen koennen nach der Erstellung geaendert werden:
- Elemente hinzufuegen (`append`, `insert`)
- Elemente entfernen (`remove`, `pop`)
- Elemente aendern (`liste[i] = x`)
</details>

---

**Aussage:** `liste.append(x)` fuegt x am Anfang der Liste ein.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

`append()` fuegt am **Ende** ein. Fuer den Anfang: `insert(0, x)`.

```python
liste = [1, 2, 3]
liste.append(4)      # [1, 2, 3, 4]
liste.insert(0, 0)   # [0, 1, 2, 3, 4]
```
</details>

---

**Aussage:** `liste[1:3]` enthaelt die Elemente an Index 1 und 2.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Beim Slicing ist der Endindex **exklusiv** (nicht enthalten).
`liste[1:3]` gibt Index 1 und 2 zurueck.
</details>

---

**Frage 8.1:** Was macht `liste.pop()`?

- [ ] a) Entfernt erstes Element
- [ ] b) Entfernt und gibt letztes Element zurueck
- [ ] c) Leert die Liste
- [ ] d) Sortiert die Liste

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`pop()` entfernt das letzte Element und gibt es zurueck.
`pop(i)` entfernt das Element an Index i.

```python
liste = [1, 2, 3]
x = liste.pop()    # x = 3, liste = [1, 2]
y = liste.pop(0)   # y = 1, liste = [2]
```
</details>

---

**Frage 8.2:** Was ist das Ergebnis?

```python
liste = [3, 1, 4, 1, 5]
liste.sort()
print(liste[0])
```

- [ ] a) 3
- [ ] b) 1
- [ ] c) 5
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`sort()` sortiert die Liste aufsteigend: [1, 1, 3, 4, 5]
Das erste Element (Index 0) ist 1.
</details>

---

**Frage 8.3:** Was ist die Ausgabe?

```python
liste = [1, 2, 3, 4, 5]
print(liste[1:4])
```

- [ ] a) [1, 2, 3, 4]
- [ ] b) [2, 3, 4]
- [ ] c) [2, 3, 4, 5]
- [ ] d) [1, 2, 3]

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`liste[1:4]` gibt Index 1, 2, 3 zurueck (4 ist exklusiv).
Das sind die Werte [2, 3, 4].
</details>

---

**Frage 8.4:** Was ist die Ausgabe?

```python
liste = [1, 2, 3]
liste.append([4, 5])
print(len(liste))
```

- [ ] a) 3
- [ ] b) 4
- [ ] c) 5
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`append()` fuegt das Element als Ganzes ein, nicht die einzelnen Elemente.
liste = [1, 2, 3, [4, 5]] - Das ist eine Liste mit 4 Elementen!

Fuer einzelne Elemente: `extend()` oder `+=`
```python
liste = [1, 2, 3]
liste.extend([4, 5])  # [1, 2, 3, 4, 5]
```
</details>

---

**Frage 8.5:** Wie erstellt man eine Liste mit den Zahlen 1 bis 10?

<details>
<summary>Loesung anzeigen</summary>

```python
# Mit range():
liste = list(range(1, 11))
print(liste)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mit List Comprehension:
liste = [i for i in range(1, 11)]

# Manuell (nicht empfohlen):
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
</details>

---

**Frage 8.6:** Wie entfernt man alle Vorkommen eines Wertes aus einer Liste?

<details>
<summary>Loesung anzeigen</summary>

```python
liste = [1, 2, 2, 3, 2, 4]

# Methode 1: Schleife (rueckwaerts)
while 2 in liste:
    liste.remove(2)
print(liste)  # [1, 3, 4]

# Methode 2: List Comprehension
liste = [1, 2, 2, 3, 2, 4]
liste = [x for x in liste if x != 2]
print(liste)  # [1, 3, 4]
```

**Achtung:** `remove(x)` entfernt nur das ERSTE Vorkommen!
</details>

---

**Frage 8.7:** Was ist die Ausgabe?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

- [ ] a) [1, 2, 3]
- [ ] b) [1, 2, 3, 4]
- [ ] c) [4]
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`b = a` erstellt KEINE Kopie! Beide Variablen zeigen auf dieselbe Liste.
Aenderungen an `b` aendern auch `a`.

Fuer eine echte Kopie:
```python
b = a.copy()  # oder: b = a[:]
```
</details>

---

**Frage 8.8:** Wichtige Listen-Methoden

<details>
<summary>Loesung anzeigen</summary>

| Methode | Beschreibung | Beispiel |
|---------|--------------|----------|
| `append(x)` | Element am Ende | `[1,2].append(3)` → [1,2,3] |
| `insert(i, x)` | Element an Position | `[1,3].insert(1, 2)` → [1,2,3] |
| `remove(x)` | Erstes x entfernen | `[1,2,2].remove(2)` → [1,2] |
| `pop()` | Letztes entfernen | `[1,2,3].pop()` → 3 |
| `pop(i)` | An Index entfernen | `[1,2,3].pop(0)` → 1 |
| `sort()` | Sortieren | `[3,1,2].sort()` → [1,2,3] |
| `reverse()` | Umkehren | `[1,2,3].reverse()` → [3,2,1] |
| `index(x)` | Index finden | `[1,2,3].index(2)` → 1 |
| `count(x)` | Zaehlen | `[1,2,2].count(2)` → 2 |
| `copy()` | Kopie erstellen | `a.copy()` |
| `extend(l)` | Liste erweitern | `[1].extend([2,3])` → [1,2,3] |
</details>

---

**Frage 8.9:** Was ist die Ausgabe?

```python
liste = [1, 2, 3, 4, 5]
print(liste[-1])
print(liste[-2])
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe:**
```
5
4
```

Negative Indizes zaehlen vom Ende:
- `[-1]` = letztes Element
- `[-2]` = vorletztes Element
- usw.
</details>

---

**Frage 8.10:** Wie prueft man, ob ein Element in einer Liste ist?

<details>
<summary>Loesung anzeigen</summary>

```python
liste = [1, 2, 3, 4, 5]

# Mit in-Operator:
if 3 in liste:
    print("3 ist enthalten")

if 6 not in liste:
    print("6 ist nicht enthalten")
```
</details>

---
