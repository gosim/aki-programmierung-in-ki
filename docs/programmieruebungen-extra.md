# Zusaetzliche Programmierfragen - Klausurvorbereitung

## Fokus: Code-Verstaendnis und Ausgabe-Vorhersage

---

**Frage E.1:** Was ist die Ausgabe?

```python
x = 10
y = 3
print(x // y)
print(x % y)
```

- [ ] a) 3.33 und 1
- [ ] b) 3 und 1
- [ ] c) 3 und 0
- [ ] d) 10 und 3

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- `x // y` ist die **Ganzzahldivision**: 10 // 3 = 3 (abgerundet)
- `x % y` ist der **Rest** (Modulo): 10 % 3 = 1

**Merke:** `//` gibt immer eine ganze Zahl, `%` gibt den Rest.
</details>

---

**Frage E.2:** Was ist die Ausgabe?

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

`liste[1:4]` gibt Elemente von Index 1 bis Index 3 (4 ist exklusiv):
- Index 1: 2
- Index 2: 3
- Index 3: 4

Ergebnis: [2, 3, 4]
</details>

---

**Frage E.3:** Was ist die Ausgabe?

```python
text = "Python"
print(text[0] + text[-1])
```

- [ ] a) Pn
- [ ] b) Py
- [ ] c) on
- [ ] d) Python

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

- `text[0]` = erstes Zeichen = "P"
- `text[-1]` = letztes Zeichen = "n"
- "P" + "n" = "Pn"
</details>

---

**Frage E.4:** Was ist die Ausgabe?

```python
zahlen = [3, 1, 4, 1, 5]
zahlen.sort()
print(zahlen[0])
```

- [ ] a) 3
- [ ] b) 1
- [ ] c) 5
- [ ] d) 4

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`sort()` sortiert die Liste **aufsteigend**: [1, 1, 3, 4, 5]
`zahlen[0]` ist das erste Element: 1
</details>

---

**Frage E.5:** Was ist die Ausgabe?

```python
a = 5
b = 2
a, b = b, a
print(a, b)
```

- [ ] a) 5 2
- [ ] b) 2 5
- [ ] c) 5 5
- [ ] d) 2 2

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`a, b = b, a` tauscht die Werte von a und b (Tuple Unpacking).
- Vorher: a=5, b=2
- Nachher: a=2, b=5
</details>

---

**Frage E.6:** Was ist die Ausgabe?

```python
count = {}
text = "aab"
for c in text:
    count[c] = count.get(c, 0) + 1
print(count["a"])
```

- [ ] a) 1
- [ ] b) 2
- [ ] c) 3
- [ ] d) KeyError

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Der Code zaehlt Buchstaben:
- 'a': count.get('a', 0)=0, dann 1
- 'a': count.get('a', 0)=1, dann 2
- 'b': count.get('b', 0)=0, dann 1

count = {'a': 2, 'b': 1}
`count["a"]` = 2
</details>

---

**Frage E.7:** Was ist die Ausgabe?

```python
def verdopple(x):
    return x * 2

ergebnis = verdopple(verdopple(3))
print(ergebnis)
```

- [ ] a) 6
- [ ] b) 9
- [ ] c) 12
- [ ] d) 18

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

- `verdopple(3)` = 3 * 2 = 6
- `verdopple(6)` = 6 * 2 = 12
</details>

---

**Frage E.8:** Was ist die Ausgabe?

```python
x = 15
if x % 3 == 0:
    print("A", end="")
if x % 5 == 0:
    print("B", end="")
```

- [ ] a) A
- [ ] b) B
- [ ] c) AB
- [ ] d) Keine Ausgabe

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

15 ist durch 3 teilbar (15 % 3 == 0) UND durch 5 teilbar (15 % 5 == 0).
Beide if-Bedingungen sind wahr, also wird "A" und dann "B" ausgegeben.

**Hinweis:** Bei FizzBuzz waere es wichtig, elif zu verwenden!
</details>

---

**Frage E.9:** Was ist die Ausgabe?

```python
liste = [1, 2, 3]
liste.append(4)
liste.pop()
print(liste)
```

- [ ] a) [1, 2, 3, 4]
- [ ] b) [1, 2, 3]
- [ ] c) [2, 3, 4]
- [ ] d) [1, 2]

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- `append(4)` fuegt 4 am Ende hinzu: [1, 2, 3, 4]
- `pop()` entfernt das letzte Element: [1, 2, 3]
</details>

---

**Frage E.10:** Was ist die Ausgabe?

```python
s = "hallo"
s = s.replace("l", "x")
print(s)
```

- [ ] a) hallo
- [ ] b) haxlo
- [ ] c) haxxo
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`replace("l", "x")` ersetzt **alle** Vorkommen von "l" durch "x".
"hallo" wird zu "haxxo" (beide l werden ersetzt).
</details>

---

**Frage E.11:** Was ist die Ausgabe?

```python
for i in range(3):
    for j in range(2):
        print(i + j, end=" ")
```

- [ ] a) 0 1 1 2 2 3
- [ ] b) 0 1 2 0 1 2
- [ ] c) 0 0 1 1 2 2
- [ ] d) 0 1 0 1 0 1

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

Verschachtelte Schleifen:
- i=0: j=0 -> 0, j=1 -> 1
- i=1: j=0 -> 1, j=1 -> 2
- i=2: j=0 -> 2, j=1 -> 3

Ausgabe: 0 1 1 2 2 3
</details>

---

**Frage E.12:** Was ist die Ausgabe?

```python
d = {"a": 1, "b": 2}
print(d.get("c", 99))
```

- [ ] a) None
- [ ] b) KeyError
- [ ] c) 99
- [ ] d) "c"

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`d.get("c", 99)` sucht den Schluessel "c":
- "c" ist nicht im Dictionary
- Also wird der Standardwert 99 zurueckgegeben

**Merke:** `d["c"]` wuerde einen KeyError werfen, `d.get("c", 99)` nicht!
</details>

---

**Frage E.13:** Was ist die Ausgabe?

```python
x = 7
while x > 0:
    x -= 2
    if x == 3:
        continue
    print(x, end=" ")
```

- [ ] a) 5 3 1 -1
- [ ] b) 5 1 -1
- [ ] c) 7 5 3 1
- [ ] d) 5 1

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- x=7: x-=2 -> x=5, print 5
- x=5: x-=2 -> x=3, continue (keine Ausgabe)
- x=3: x-=2 -> x=1, print 1
- x=1: x-=2 -> x=-1, print -1
- x=-1: Schleife endet (x > 0 ist False)

Ausgabe: 5 1 -1
</details>

---

**Frage E.14:** Was ist die Ausgabe?

```python
def f(a, b=10):
    return a + b

print(f(5))
print(f(5, 3))
```

- [ ] a) 15 und 8
- [ ] b) 5 und 8
- [ ] c) 15 und 15
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

- `f(5)`: a=5, b=10 (Standardwert) -> 5+10=15
- `f(5, 3)`: a=5, b=3 -> 5+3=8

Der Parameter b hat einen Standardwert von 10, der verwendet wird, wenn kein zweites Argument uebergeben wird.
</details>

---

**Frage E.15:** Was ist die Ausgabe?

```python
s = "  Hallo Welt  "
print(len(s.strip()))
```

- [ ] a) 14
- [ ] b) 10
- [ ] c) 11
- [ ] d) 12

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`strip()` entfernt Leerzeichen am Anfang und Ende:
- Original: "  Hallo Welt  " (14 Zeichen)
- Nach strip(): "Hallo Welt" (10 Zeichen)
</details>

---

**Frage E.16:** Was ist die Ausgabe?

```python
n = 0
for i in range(1, 5):
    n = n + i
print(n)
```

- [ ] a) 4
- [ ] b) 5
- [ ] c) 10
- [ ] d) 15

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`range(1, 5)` erzeugt [1, 2, 3, 4]
n = 0 + 1 + 2 + 3 + 4 = 10
</details>

---

**Frage E.17:** Was ist die Ausgabe?

```python
woerter = ["Apfel", "Birne", "Kirsche"]
print(woerter[-2])
```

- [ ] a) Apfel
- [ ] b) Birne
- [ ] c) Kirsche
- [ ] d) IndexError

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Negative Indizes zaehlen von hinten:
- woerter[-1] = "Kirsche" (letztes)
- woerter[-2] = "Birne" (vorletztes)
- woerter[-3] = "Apfel" (drittletztes)
</details>

---

**Frage E.18:** Was ist die Ausgabe?

```python
x = True
y = False
print(x and y, x or y)
```

- [ ] a) True True
- [ ] b) False True
- [ ] c) True False
- [ ] d) False False

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- `x and y`: True AND False = **False** (beide muessen True sein)
- `x or y`: True OR False = **True** (mindestens einer muss True sein)
</details>

---

**Frage E.19:** Was ist die Ausgabe?

```python
def aendern(liste):
    liste.append(4)

zahlen = [1, 2, 3]
aendern(zahlen)
print(zahlen)
```

- [ ] a) [1, 2, 3]
- [ ] b) [1, 2, 3, 4]
- [ ] c) [4]
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Listen werden per **Referenz** uebergeben. Die Funktion aendert die Original-Liste!
Nach `aendern(zahlen)` ist zahlen = [1, 2, 3, 4]

**Achtung:** Bei unveraenderlichen Typen (int, str) wuerde das nicht funktionieren!
</details>

---

**Frage E.20:** Was ist die Ausgabe?

```python
s = "Python"
print(s[::-1])
```

- [ ] a) Python
- [ ] b) nohtyP
- [ ] c) P
- [ ] d) n

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`s[::-1]` kehrt den String um (Slicing mit Schritt -1).
"Python" wird zu "nohtyP"
</details>

---

## Freitext-Aufgaben zur Uebung

---

### Frage E.21: Schreibe eine Funktion

**Schreibe eine Funktion `ist_gerade(n)`, die True zurueckgibt, wenn n gerade ist, sonst False.**

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_gerade(n):
    return n % 2 == 0

# Test:
print(ist_gerade(4))  # True
print(ist_gerade(7))  # False
```

**Erklaerung:** Eine Zahl ist gerade, wenn der Rest bei Division durch 2 gleich 0 ist.
</details>

---

### Frage E.22: Buchstaben zaehlen

**Schreibe Code, der zaehlt wie oft jeder Buchstabe in "abracadabra" vorkommt.**

<details>
<summary>Loesung anzeigen</summary>

```python
text = "abracadabra"
count = {}
for c in text:
    count[c] = count.get(c, 0) + 1
print(count)
# Ausgabe: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

**Dies ist ein klassisches Klausurbeispiel fuer dict.get()!**
</details>

---

### Frage E.23: Maximum finden

**Schreibe eine Funktion `maximum(liste)`, die den groessten Wert einer Liste zurueckgibt (ohne max() zu verwenden).**

<details>
<summary>Loesung anzeigen</summary>

```python
def maximum(liste):
    if len(liste) == 0:
        return None
    groesster = liste[0]
    for element in liste:
        if element > groesster:
            groesster = element
    return groesster

# Test:
print(maximum([3, 1, 4, 1, 5, 9]))  # 9
```
</details>

---

### Frage E.24: Liste filtern

**Schreibe Code, der aus einer Liste nur die geraden Zahlen in eine neue Liste kopiert.**

<details>
<summary>Loesung anzeigen</summary>

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade = []
for z in zahlen:
    if z % 2 == 0:
        gerade.append(z)
print(gerade)  # [2, 4, 6, 8, 10]
```

**Mit List Comprehension (eleganter):**
```python
gerade = [z for z in zahlen if z % 2 == 0]
```
</details>

---

### Frage E.25: Woerter umdrehen

**Schreibe eine Funktion, die alle Woerter in einem Satz umdreht.**
Beispiel: "Hallo Welt" -> "ollaH tleW"

<details>
<summary>Loesung anzeigen</summary>

```python
def woerter_umdrehen(satz):
    woerter = satz.split()
    umgedreht = []
    for wort in woerter:
        umgedreht.append(wort[::-1])
    return " ".join(umgedreht)

# Test:
print(woerter_umdrehen("Hallo Welt"))  # "ollaH tleW"
```

**Mit List Comprehension:**
```python
def woerter_umdrehen(satz):
    return " ".join([w[::-1] for w in satz.split()])
```
</details>

---
