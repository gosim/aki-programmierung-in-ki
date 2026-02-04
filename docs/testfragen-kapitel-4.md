# Testfragen Kapitel 4: Funktionen

---

**Aussage:** Eine Funktion ohne `return` gibt `None` zurueck.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Wenn eine Funktion kein `return` hat oder `return` ohne Wert, gibt sie automatisch `None` zurueck.

```python
def ohne_return():
    x = 5

result = ohne_return()
print(result)  # None
```
</details>

---

**Aussage:** Parameter und Argumente sind dasselbe.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

- **Parameter:** Die Variablen in der Funktionsdefinition
- **Argumente:** Die konkreten Werte beim Funktionsaufruf

```python
def gruss(name):       # name ist ein PARAMETER
    print("Hallo", name)

gruss("Max")           # "Max" ist ein ARGUMENT
```
</details>

---

**Aussage:** `def` ist ein reserviertes Wort in Python.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`def` ist ein Schluesselwort und wird verwendet, um Funktionen zu definieren.
</details>

---

**Aussage:** Eine Funktion kann mehrere return-Anweisungen haben.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Eine Funktion kann mehrere `return`-Anweisungen haben, aber nur eine wird ausgefuehrt (bei der ersten wird die Funktion beendet).

```python
def absolut(x):
    if x < 0:
        return -x
    else:
        return x
```
</details>

---

**Frage 4.1:** Was gibt diese Funktion zurueck?

```python
def test():
    x = 5
```

- [ ] a) 5
- [ ] b) x
- [ ] c) None
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Ohne `return`-Anweisung gibt eine Funktion `None` zurueck.
</details>

---

**Frage 4.2:** Was ist die Ausgabe?

```python
def addiere(a, b):
    return a + b

ergebnis = addiere(3, 4)
print(ergebnis)
```

- [ ] a) None
- [ ] b) 7
- [ ] c) (3, 4)
- [ ] d) "34"

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Die Funktion addiert 3 + 4 und gibt 7 zurueck.
</details>

---

**Frage 4.3:** Was ist die Ausgabe?

```python
def verdopple(x):
    return x * 2

print(verdopple("ab"))
```

- [ ] a) "ab2"
- [ ] b) "abab"
- [ ] c) Fehler
- [ ] d) 4

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Der `*`-Operator bei Strings wiederholt den String.
`"ab" * 2` ergibt `"abab"`.
</details>

---

### Frage 4.4: Funktion schreiben

**Schreiben Sie eine Funktion `ist_teilbar(zahl, teiler)`, die True zurueckgibt, wenn `zahl` durch `teiler` teilbar ist.**

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_teilbar(zahl, teiler):
    return zahl % teiler == 0

# Tests:
print(ist_teilbar(10, 2))   # True
print(ist_teilbar(10, 3))   # False
print(ist_teilbar(15, 5))   # True
print(ist_teilbar(15, 3))   # True
```

**Alternative mit if:**
```python
def ist_teilbar(zahl, teiler):
    if zahl % teiler == 0:
        return True
    else:
        return False
```
</details>

---

**Frage 4.5:** Was ist die Ausgabe?

```python
def f(x):
    x = x + 1
    return x

a = 5
b = f(a)
print(a, b)
```

- [ ] a) 5 5
- [ ] b) 6 6
- [ ] c) 5 6
- [ ] d) 6 5

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

- `a` bleibt 5 (Zahlen werden als Kopie uebergeben)
- `b` ist der Rueckgabewert 6

Die Variable `x` in der Funktion ist lokal und aendert `a` nicht.
</details>

---

**Frage 4.6:** Was ist ein Standardparameter (Default Parameter)?

<details>
<summary>Loesung anzeigen</summary>

Ein Standardparameter hat einen vordefinierten Wert, der verwendet wird, wenn kein Argument uebergeben wird.

```python
def gruss(name, begruessung="Hallo"):
    print(f"{begruessung}, {name}!")

gruss("Max")           # "Hallo, Max!"
gruss("Max", "Hi")     # "Hi, Max!"
```

**Wichtig:** Parameter mit Standardwert muessen nach Parametern ohne Standardwert kommen!
</details>

---

**Frage 4.7:** Was passiert bei diesem Code?

```python
def f(liste):
    liste.append(4)

meine_liste = [1, 2, 3]
f(meine_liste)
print(meine_liste)
```

- [ ] a) [1, 2, 3]
- [ ] b) [1, 2, 3, 4]
- [ ] c) [4]
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Listen werden als **Referenz** uebergeben, nicht als Kopie!
Aenderungen innerhalb der Funktion wirken sich auf die Original-Liste aus.

Das ist ein wichtiger Unterschied zu einfachen Datentypen (int, str).
</details>

---

### Frage 4.8: Warum Funktionen?

**Nennen Sie drei Vorteile von Funktionen.**

<details>
<summary>Loesung anzeigen</summary>

**Vorteile von Funktionen:**

1. **Wiederverwendbarkeit**
   - Code einmal schreiben, mehrfach aufrufen
   - Vermeidet Duplikation

2. **Lesbarkeit**
   - Komplexe Logik in kleine, benannte Einheiten aufteilen
   - Selbstdokumentierend durch Funktionsnamen

3. **Wartbarkeit**
   - Aenderungen nur an einer Stelle noetig
   - Einfacheres Debugging

4. **Abstraktion**
   - Details verstecken
   - Fokus auf das "Was" statt "Wie"

5. **Testbarkeit**
   - Einzelne Funktionen isoliert testen
</details>

---

**Frage 4.9:** Welche eingebauten Funktionen kennen Sie?

<details>
<summary>Loesung anzeigen</summary>

**Wichtige Built-in-Funktionen:**

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `print()` | Ausgabe | `print("Hallo")` |
| `input()` | Eingabe | `name = input()` |
| `len()` | Laenge | `len("abc")` → 3 |
| `type()` | Datentyp | `type(42)` → int |
| `int()` | In Ganzzahl | `int("5")` → 5 |
| `str()` | In String | `str(5)` → "5" |
| `float()` | In Float | `float("3.14")` → 3.14 |
| `range()` | Zahlenbereich | `range(5)` → 0,1,2,3,4 |
| `sum()` | Summe | `sum([1,2,3])` → 6 |
| `min()` | Minimum | `min(1,2,3)` → 1 |
| `max()` | Maximum | `max(1,2,3)` → 3 |
| `abs()` | Absolutwert | `abs(-5)` → 5 |
</details>

---

### Frage 4.10: FizzBuzz als Funktion

**Schreiben Sie eine Funktion `fizzbuzz(n)`, die fuer Zahlen von 1 bis n FizzBuzz ausgibt.**

<details>
<summary>Loesung anzeigen</summary>

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

# Aufruf:
fizzbuzz(15)
```

**Ausgabe:**
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
</details>

---
