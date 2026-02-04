# Testfragen Kapitel 3: Bedingte Ausfuehrung

## KLAUSURRELEVANT: try-except bei Benutzereingabe!

---

**Aussage:** Ein `except`-Block wird nur ausgefuehrt, wenn im `try`-Block ein Fehler auftritt.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Der Code im `except`-Block wird nur ausgefuehrt, wenn im `try`-Block eine Ausnahme (Exception) auftritt. Wenn kein Fehler passiert, wird der `except`-Block uebersprungen.
</details>

---

**Aussage:** `elif` ist eine Abkuerzung fuer `else if`.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`elif` kombiniert `else` und `if` in einem Schluesselwort und erlaubt verkettete Bedingungen.
</details>

---

**Aussage:** Nach einem `try`-Block ist `except` optional.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

Ein `try`-Block benoetigt mindestens einen `except`-Block oder einen `finally`-Block. Ohne diese ist der Code syntaktisch falsch.
</details>

---

**Aussage:** `True and False` ergibt `True`.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

`and` ergibt nur `True`, wenn **beide** Seiten `True` sind.
- `True and True` → True
- `True and False` → **False**
- `False and True` → False
- `False and False` → False
</details>

---

**Aussage:** `True or False` ergibt `True`.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`or` ergibt `True`, wenn **mindestens eine** Seite `True` ist.
- `True or True` → True
- `True or False` → **True**
- `False or True` → True
- `False or False` → False
</details>

---

**Frage 3.1:** Welcher Fehler tritt auf bei `int("abc")`?

- [ ] a) TypeError
- [ ] b) ValueError
- [ ] c) SyntaxError
- [ ] d) NameError

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Ein **ValueError** tritt auf, wenn der Wert nicht in den gewuenschten Typ umgewandelt werden kann. "abc" ist keine gueltige Zahl.

Fehlertypen:
- **ValueError**: Wert ist ungueltig (z.B. `int("abc")`)
- **TypeError**: Falscher Datentyp (z.B. `"5" + 3`)
- **SyntaxError**: Fehlerhafte Syntax
- **NameError**: Variable nicht definiert
</details>

---

**Frage 3.2:** Was passiert bei `int(input())` wenn der User "drei" eingibt?

- [ ] a) Es wird 3 zurueckgegeben
- [ ] b) Es wird "drei" als String behalten
- [ ] c) Ein ValueError tritt auf
- [ ] d) Das Programm wartet weiter

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`int("drei")` kann "drei" nicht in eine Zahl umwandeln und wirft einen **ValueError**.
</details>

---

**Frage 3.3:** Was gibt folgender Code aus?

```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
else:
    print("C")
```

- [ ] a) A
- [ ] b) B
- [ ] c) A und B
- [ ] d) C

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

Nur **"A"** wird ausgegeben!

Obwohl `x > 8` auch wahr ist, wird der `elif`-Block nicht mehr geprueft, da bereits die erste Bedingung (`x > 5`) erfuellt war.

Bei `if/elif/else` wird nur der **erste** zutreffende Block ausgefuehrt.
</details>

---

**Frage 3.4:** Was ist die Ausgabe?

```python
x = 15
if x % 3 == 0:
    print("Fizz")
if x % 5 == 0:
    print("Buzz")
```

- [ ] a) Fizz
- [ ] b) Buzz
- [ ] c) Fizz und Buzz (zwei Zeilen)
- [ ] d) FizzBuzz

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Ausgabe:
```
Fizz
Buzz
```

Beide `if`-Bedingungen werden unabhaengig geprueft (kein elif!).
- 15 % 3 == 0 ist True → "Fizz" wird ausgegeben
- 15 % 5 == 0 ist True → "Buzz" wird ausgegeben
</details>

---

### Frage 3.5: try-except (KLAUSURAUFGABE!)

**Schreiben Sie einen try-except-Block, der eine Benutzereingabe in einen Integer umwandelt. Bei ungueltiger Eingabe soll "Ungueltige Zahl" ausgegeben werden.**

<details>
<summary>Loesung anzeigen</summary>

```python
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    print("Ihre Zahl:", zahl)
except ValueError:
    print("Ungueltige Zahl")
```

**Alternative mit Schleife (robuster):**
```python
while True:
    try:
        zahl = int(input("Geben Sie eine Zahl ein: "))
        break  # Schleife verlassen wenn erfolgreich
    except ValueError:
        print("Ungueltige Zahl, bitte erneut versuchen.")

print("Ihre Zahl:", zahl)
```
</details>

---

### Frage 3.6: Warum try-except? (KLAUSURFRAGE!)

**Erklaeren Sie, warum try-except bei Benutzereingaben sinnvoll ist.**

<details>
<summary>Loesung anzeigen</summary>

**Try-except ist bei Benutzereingaben sinnvoll, weil:**

1. **Benutzer koennen unvorhersehbare Eingaben machen**
   - Statt einer Zahl koennte Text eingegeben werden
   - Leerzeichen oder Sonderzeichen sind moeglich

2. **Ohne try-except stuerzt das Programm ab**
   - `int("abc")` wirft einen ValueError
   - Das Programm bricht sofort ab

3. **Mit try-except bleibt das Programm stabil**
   - Fehler werden abgefangen
   - Benutzer erhaelt hilfreiche Fehlermeldung
   - Eingabe kann wiederholt werden

4. **Benutzerfreundlichkeit**
   - Statt kryptischer Fehlermeldung
   - Verstaendliche Hinweise moeglich

**Beispiel ohne try-except:**
```python
zahl = int(input("Zahl: "))  # Absturz bei "abc"!
```

**Beispiel mit try-except:**
```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Bitte eine gueltige Zahl eingeben!")
```
</details>

---

**Frage 3.7:** Was ist die Ausgabe?

```python
try:
    x = int("10")
    print("A")
except ValueError:
    print("B")
print("C")
```

- [ ] a) A
- [ ] b) B C
- [ ] c) A C
- [ ] d) B

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Ausgabe:
```
A
C
```

`int("10")` funktioniert problemlos (kein Fehler), daher:
1. `x = int("10")` ist erfolgreich
2. "A" wird ausgegeben
3. `except`-Block wird uebersprungen
4. "C" wird ausgegeben (nach dem try-except)
</details>

---

**Frage 3.8:** Was ist die Ausgabe?

```python
try:
    x = int("abc")
    print("A")
except ValueError:
    print("B")
print("C")
```

- [ ] a) A C
- [ ] b) B C
- [ ] c) A B C
- [ ] d) Nur ein Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Ausgabe:
```
B
C
```

`int("abc")` wirft einen ValueError, daher:
1. Fehler bei `x = int("abc")`
2. "A" wird NICHT ausgegeben (Code nach Fehler im try wird uebersprungen)
3. `except`-Block wird ausgefuehrt → "B"
4. "C" wird ausgegeben (Programm laeuft normal weiter)
</details>

---

**Frage 3.9:** Welche Bedingung prueft, ob x durch 3 UND durch 5 teilbar ist?

- [ ] a) `x % 3 == 0 or x % 5 == 0`
- [ ] b) `x % 3 == 0 and x % 5 == 0`
- [ ] c) `x % 15 == 0`
- [ ] d) Sowohl b) als auch c)

<details>
<summary>Loesung anzeigen</summary>

**Richtig: d)**

Beide Varianten sind korrekt:
- `x % 3 == 0 and x % 5 == 0` prueft beide Bedingungen
- `x % 15 == 0` nutzt das kgV von 3 und 5

Fuer FizzBuzz: Wenn durch 3 UND 5 teilbar → "FizzBuzz"
</details>

---

**Frage 3.10:** Was ist der Unterschied zwischen `=` und `==`?

<details>
<summary>Loesung anzeigen</summary>

**`=` ist Zuweisung:**
```python
x = 5  # Weist x den Wert 5 zu
```

**`==` ist Vergleich:**
```python
x == 5  # Prueft ob x gleich 5 ist, gibt True oder False zurueck
```

**Haeufiger Fehler:**
```python
if x = 5:  # FALSCH! SyntaxError
if x == 5:  # RICHTIG
```
</details>

---

### Frage 3.11: Komplette FizzBuzz-Bedingung

**Schreiben Sie die if/elif/else-Struktur fuer FizzBuzz:**
- Durch 3 und 5 teilbar → "FizzBuzz"
- Nur durch 3 teilbar → "Fizz"
- Nur durch 5 teilbar → "Buzz"
- Sonst → die Zahl selbst

<details>
<summary>Loesung anzeigen</summary>

```python
def fizzbuzz_check(zahl):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)
```

**Wichtig:** Die Reihenfolge ist entscheidend!
- Zuerst `% 3 and % 5` pruefen (FizzBuzz)
- Dann einzeln % 3 (Fizz)
- Dann einzeln % 5 (Buzz)
- Sonst die Zahl

Wenn man die Reihenfolge aendert, funktioniert es nicht korrekt!
</details>

---
