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

## Praktische Uebungen aus den Notebooks (fhswf/pki)

---

**Frage E.23:** Was ist die Ausgabe?

```python
def lohn(stunden, satz):
    if stunden > 40:
        return 40 * satz + (stunden - 40) * satz * 1.5
    return stunden * satz

print(lohn(45, 10))
```

- [ ] a) 450
- [ ] b) 475
- [ ] c) 500
- [ ] d) 525

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- Regulaere Stunden: 40 * 10 = 400
- Ueberstunden: 5 * 10 * 1.5 = 75
- Gesamt: 400 + 75 = 475
</details>

---

**Frage E.24:** Was ist die Ausgabe?

```python
email = "anna@example.com"
domain = email.split("@")[1]
print(domain)
```

- [ ] a) anna
- [ ] b) @example.com
- [ ] c) example.com
- [ ] d) ["anna", "example.com"]

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`split("@")` teilt den String an "@" in eine Liste: ["anna", "example.com"]
`[1]` gibt das zweite Element zurueck: "example.com"
</details>

---

**Frage E.25:** Was ist die Ausgabe?

```python
counts = {}
words = ["a", "b", "a", "c", "a"]
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts["a"])
```

- [ ] a) 1
- [ ] b) 2
- [ ] c) 3
- [ ] d) KeyError

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Das Zaehlmuster zaehlt "a" dreimal (Index 0, 2, 4).
`counts = {"a": 3, "b": 1, "c": 1}`
</details>

---

**Frage E.26:** Was ist die Ausgabe?

```python
line = "From user@mail.de Sat"
if line.startswith("From "):
    words = line.split()
    print(words[1])
```

- [ ] a) From
- [ ] b) user@mail.de
- [ ] c) user
- [ ] d) Sat

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`split()` teilt an Leerzeichen: ["From", "user@mail.de", "Sat"]
`words[1]` ist das zweite Element: "user@mail.de"
</details>

---

**Frage E.27:** Was ist die Ausgabe?

```python
def teiler(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

print(len(teiler(12)))
```

- [ ] a) 4
- [ ] b) 5
- [ ] c) 6
- [ ] d) 12

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Teiler von 12 sind: 1, 2, 3, 4, 6, 12
Das sind 6 Teiler.
</details>

---

**Frage E.28:** Was ist die Ausgabe?

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

print(fib(7))
```

- [ ] a) 8
- [ ] b) 13
- [ ] c) 21
- [ ] d) 5

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Fibonacci: 1, 1, 2, 3, 5, 8, 13
Die 7. Fibonacci-Zahl ist 13.
</details>

---

**Frage E.29:** Was ist die Ausgabe?

```python
text = "X-Value: 0.875"
pos = text.find(":")
wert = float(text[pos+1:].strip())
print(wert > 0.5)
```

- [ ] a) True
- [ ] b) False
- [ ] c) 0.875
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

- `find(":")` gibt Position 7 zurueck
- `text[8:]` ist " 0.875"
- `strip()` entfernt Leerzeichen: "0.875"
- `float("0.875")` = 0.875
- 0.875 > 0.5 ist True
</details>

---

**Frage E.30:** Was ist die Ausgabe?

```python
d = {"a": 5, "b": 3, "c": 8}
max_key = None
max_val = 0
for k, v in d.items():
    if v > max_val:
        max_val = v
        max_key = k
print(max_key)
```

- [ ] a) a
- [ ] b) b
- [ ] c) c
- [ ] d) 8

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Die Schleife findet den Schluessel mit dem hoechsten Wert.
"c" hat den Wert 8 (hoechster Wert).
</details>

---

**Frage E.31:** Was ist die Ausgabe?

```python
brutto = 15000
if brutto <= 10000:
    rate = 0
elif brutto <= 14000:
    rate = 0.14
else:
    rate = 0.22
netto = brutto - brutto * rate
print(netto)
```

- [ ] a) 15000
- [ ] b) 13200
- [ ] c) 12900
- [ ] d) 11700

<details>
<summary>Loesung anzeigen</summary>

**Richtig: d)**

15000 > 14000, also rate = 0.22
netto = 15000 - 15000 * 0.22 = 15000 - 3300 = 11700
</details>

---

**Frage E.32:** Was ist die Ausgabe?

```python
summe = 0
zahlen = [3, 7, 2, 9, 4]
for z in zahlen:
    if z > 5:
        summe += z
print(summe)
```

- [ ] a) 16
- [ ] b) 25
- [ ] c) 9
- [ ] d) 7

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

Nur Zahlen > 5 werden addiert: 7 + 9 = 16
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

### Frage E.22: Woerter umdrehen

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

## Fingeuebungen aus den Praktika (fhswf/pki)

---

### Frage E.33: Rechteck berechnen

**Schreibe Code, der Umfang und Flaeche eines Rechtecks berechnet (Hoehe 5, Breite 8).**

<details>
<summary>Loesung anzeigen</summary>

```python
hoehe = 5
breite = 8

umfang = 2 * (hoehe + breite)
flaeche = hoehe * breite

print(f"Umfang: {umfang} cm")    # 26 cm
print(f"Flaeche: {flaeche} cm²")  # 40 cm²
```

**Formeln:**
- Umfang = 2 * (Hoehe + Breite)
- Flaeche = Hoehe * Breite
</details>

---

### Frage E.34: Kreis berechnen

**Schreibe Code, der Umfang und Flaeche eines Kreises berechnet (Radius 4).**

<details>
<summary>Loesung anzeigen</summary>

```python
import math

radius = 4

umfang = 2 * math.pi * radius
flaeche = math.pi * radius ** 2

print(f"Umfang: {umfang:.2f}")   # 25.13
print(f"Flaeche: {flaeche:.2f}")  # 50.27
```

**Formeln:**
- Umfang = 2 * π * r
- Flaeche = π * r²
</details>

---

### Frage E.35: Potenzberechnung mit Eingabe

**Schreibe Code, der Basis und Exponent vom Benutzer einliest und die Potenz berechnet.**

<details>
<summary>Loesung anzeigen</summary>

```python
basis = float(input("Basis: "))
exponent = float(input("Exponent: "))

ergebnis = basis ** exponent

print(f"{basis} hoch {exponent} = {ergebnis}")
```

**Beispiel:** 2 hoch 10 = 1024
</details>

---

### Frage E.36: Teiler pruefen

**Schreibe Code, der prueft ob eine Zahl ein Teiler einer anderen ist.**

<details>
<summary>Loesung anzeigen</summary>

```python
zahl = int(input("Zahl: "))
teiler = int(input("Moeglicher Teiler: "))

if zahl % teiler == 0:
    print(f"{teiler} ist ein Teiler von {zahl}")
else:
    print(f"{teiler} ist kein Teiler von {zahl}")
```

**Erklaerung:** `a % b == 0` prueft ob a durch b teilbar ist (Rest = 0).
</details>

---

### Frage E.37: Zahlen 1 bis 50 ausgeben

**Schreibe eine While-Schleife, die alle Zahlen von 1 bis 50 ausgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
# Mit while:
i = 1
while i <= 50:
    print(i)
    i += 1

# Alternativ mit for:
for i in range(1, 51):
    print(i)
```
</details>

---

### Frage E.38: Laufende Summe

**Schreibe Code, der Zahlen einliest und die laufende Summe zeigt, bis 0 eingegeben wird.**

<details>
<summary>Loesung anzeigen</summary>

```python
summe = 0

while True:
    zahl = float(input("Zahl eingeben (0 zum Beenden): "))
    summe += zahl
    print(f"Aktuelle Summe: {summe}")
    if zahl == 0:
        break

print(f"Endsumme: {summe}")
```
</details>

---

### Frage E.39: Alle Teiler finden

**Schreibe eine Funktion, die alle Teiler einer Zahl findet und ausgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
def alle_teiler(n):
    teiler = []
    i = 1
    while i <= n:
        if n % i == 0:
            teiler.append(i)
        i += 1
    return teiler

# Test:
print(alle_teiler(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
```
</details>

---

### Frage E.40: Multiplikationstabelle (1x1)

**Schreibe Code, der das kleine Einmaleins (1-10) als Tabelle ausgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()  # Neue Zeile nach jeder Reihe
```

**Ausgabe:**
```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
...
  10  20  30  40  50  60  70  80  90 100
```

**Erklaerung:** `{wert:4d}` formatiert als 4-stellige Zahl (rechtsbuendig).
</details>

---

### Frage E.41: Fibonacci-Folge

**Schreibe eine Funktion, die die ersten n Fibonacci-Zahlen berechnet.**

<details>
<summary>Loesung anzeigen</summary>

```python
def fibonacci(n):
    if n <= 0:
        return []

    folge = [1]
    if n == 1:
        return folge

    folge.append(1)
    while len(folge) < n:
        naechste = folge[-1] + folge[-2]
        folge.append(naechste)

    return folge

# Test:
print(fibonacci(10))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**Erklaerung:** Jede Fibonacci-Zahl ist die Summe der beiden vorherigen.
</details>

---

### Frage E.42: E-Mail-Domain extrahieren

**Schreibe eine Funktion, die die Domain aus einer E-Mail-Adresse extrahiert.**

<details>
<summary>Loesung anzeigen</summary>

```python
def get_domain(email):
    parts = email.split("@")
    if len(parts) == 2:
        return parts[1]
    return None

# Test:
print(get_domain("anna@example.com"))  # "example.com"
print(get_domain("test@uni-dortmund.de"))  # "uni-dortmund.de"
```
</details>

---

## Fragen aus Python for Everybody (Musterloesungen)

---

**Frage E.44:** Was ist die Ausgabe? (Lohnberechnung mit Ueberstunden)

```python
hours = 45
rate = 10
if hours <= 40:
    pay = hours * rate
else:
    overtime = hours - 40
    pay = (rate * 40) + (1.5 * rate * overtime)
print(pay)
```

- [ ] a) 450
- [ ] b) 475.0
- [ ] c) 525.0
- [ ] d) 500

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- hours > 40, also Ueberstundenberechnung
- overtime = 45 - 40 = 5
- pay = (10 * 40) + (1.5 * 10 * 5) = 400 + 75 = 475.0

**Quelle:** exercise3_1.py aus Python for Everybody
</details>

---

**Frage E.45:** Was ist die Ausgabe?

```python
count = 0
total = 0
zahlen = [4, 5, 7]
for z in zahlen:
    count += 1
    total += z
print(total, count, total/count)
```

- [ ] a) 16 3 5.0
- [ ] b) 16 3 5.333333333333333
- [ ] c) 12 3 4.0
- [ ] d) 16 4 4.0

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- total = 4 + 5 + 7 = 16
- count = 3
- average = 16 / 3 = 5.333333333333333

**Quelle:** exercise5_1.py (Akkumulatoren-Muster)
</details>

---

**Frage E.46:** Was ist die Ausgabe?

```python
my_list = []
words = ['a', 'b', 'a', 'c', 'b']
for word in words:
    if word not in my_list:
        my_list.append(word)
print(sorted(my_list))
```

- [ ] a) ['a', 'a', 'b', 'b', 'c']
- [ ] b) ['a', 'b', 'c']
- [ ] c) ['c', 'b', 'a']
- [ ] d) ['a', 'b', 'a', 'c', 'b']

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- Duplikate werden mit `if word not in my_list` gefiltert
- my_list = ['a', 'b', 'c'] (in Reihenfolge des ersten Auftretens)
- sorted() sortiert alphabetisch: ['a', 'b', 'c']

**Quelle:** exercise8_4.py (Woerter aus Datei)
</details>

---

**Frage E.47:** Was ist die Ausgabe?

```python
d = {}
words = ['From', 'To', 'From', 'Subject', 'From']
for w in words:
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1
print(d['From'])
```

- [ ] a) 1
- [ ] b) 2
- [ ] c) 3
- [ ] d) KeyError

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

'From' kommt 3x vor (Index 0, 2, 4).
d = {'From': 3, 'To': 1, 'Subject': 1}

**Quelle:** exercise10_1.py (E-Mail-Zaehlung)
</details>

---

**Frage E.48:** Was ist die Ausgabe?

```python
lst = []
d = {'a': 3, 'b': 1, 'c': 5}
for k, v in d.items():
    lst.append((v, k))
lst.sort(reverse=True)
print(lst[0])
```

- [ ] a) ('a', 3)
- [ ] b) (5, 'c')
- [ ] c) ('c', 5)
- [ ] d) (1, 'b')

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- lst = [(3, 'a'), (1, 'b'), (5, 'c')]
- Nach sort(reverse=True): [(5, 'c'), (3, 'a'), (1, 'b')]
- lst[0] = (5, 'c')

**Tupel werden nach erstem Element sortiert!**

**Quelle:** exercise10_1.py (Maximum finden)
</details>

---

**Frage E.49:** Was ist die Ausgabe?

```python
line = "From user@mail.de Sat Jan 5"
words = line.split()
if len(words) >= 2 and words[0] == 'From':
    print(words[1].split('@')[1])
```

- [ ] a) user
- [ ] b) mail.de
- [ ] c) user@mail.de
- [ ] d) Sat

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

- words = ['From', 'user@mail.de', 'Sat', 'Jan', '5']
- words[1] = 'user@mail.de'
- words[1].split('@') = ['user', 'mail.de']
- [1] = 'mail.de'

**Quelle:** exercise10_1.py (Domain extrahieren)
</details>

---

**Frage E.50:** Was passiert bei diesem Code?

```python
try:
    hours = float(input('Hours: '))  # Eingabe: "abc"
    print(hours)
except ValueError:
    print('Error')
```

- [ ] a) Programm stuerzt ab
- [ ] b) Ausgabe: "abc"
- [ ] c) Ausgabe: "Error"
- [ ] d) Ausgabe: 0.0

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

float("abc") wirft einen ValueError.
Dieser wird von except gefangen, also wird "Error" ausgegeben.

**Quelle:** exercise3_2.py (try/except fuer Eingabe)
</details>

---

**Frage E.51:** Was ist die Ausgabe?

```python
fruit = 'banana'
index = len(fruit) - 1
result = ''
while index >= 0:
    result += fruit[index]
    index -= 1
print(result)
```

- [ ] a) banana
- [ ] b) ananab
- [ ] c) bananab
- [ ] d) a

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

String rueckwaerts durchlaufen:
- index=5: fruit[5]='a', index=4: fruit[4]='n', ...
- result = 'ananab'

**Alternativ:** `fruit[::-1]` macht dasselbe!

**Quelle:** exercise6_1.py (String rueckwaerts)
</details>

---
