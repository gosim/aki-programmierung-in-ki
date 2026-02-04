# Testfragen Kapitel 1-2: Grundlagen und Variablen

## Kapitel 1: Warum Programmieren lernen?

---

**Aussage:** Python ist eine interpretierte Sprache.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Python ist eine interpretierte Sprache. Der Python-Interpreter uebersetzt den Code Zeile fuer Zeile waehrend der Ausfuehrung. Bei kompilierten Sprachen (wie C++) wird der gesamte Code vorher in Maschinencode uebersetzt.
</details>

---

**Aussage:** In Python muss man Variablentypen explizit deklarieren.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

Python ist dynamisch typisiert. Man schreibt einfach `x = 5` ohne den Typ anzugeben. Python erkennt automatisch, dass x eine Ganzzahl (int) ist.
</details>

---

**Aussage:** Der Python-Interpreter fuehrt Code Zeile fuer Zeile aus.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Der Python-Interpreter liest und fuehrt den Code sequenziell aus, von oben nach unten, Zeile fuer Zeile.
</details>

---

**Frage 1.1:** Was gibt `print("Hallo" + "Welt")` aus?

- [ ] a) Hallo Welt
- [ ] b) HalloWelt
- [ ] c) Hallo + Welt
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Der `+` Operator bei Strings fuegt sie zusammen (Konkatenation) ohne Leerzeichen.
"Hallo" + "Welt" = "HalloWelt"
</details>

---

**Frage 1.2:** Was gibt `print(3 * "ab")` aus?

- [ ] a) 3ab
- [ ] b) ab3
- [ ] c) ababab
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Der `*` Operator bei Strings wiederholt den String.
3 * "ab" = "ababab"
</details>

---

## Kapitel 2: Bezeichner, Ausdruecke und Anweisungen

---

**Aussage:** Der Ausdruck `17 % 5` ergibt 2.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Der Modulo-Operator % gibt den Rest einer Division zurueck.
17 geteilt durch 5 = 3 Rest **2**
Berechnung: 17 = 5 * 3 + 2
</details>

---

**Aussage:** `x = 5` und `x == 5` haben dieselbe Bedeutung.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

- `x = 5` ist eine **Zuweisung** (weist x den Wert 5 zu)
- `x == 5` ist ein **Vergleich** (prueft ob x gleich 5 ist, gibt True oder False zurueck)
</details>

---

**Aussage:** `type(3.14)` gibt `<class 'int'>` zurueck.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

3.14 ist eine Fliesskommazahl (float), daher gibt `type(3.14)` `<class 'float'>` zurueck.
- int: Ganzzahlen (z.B. 42)
- float: Fliesskommazahlen (z.B. 3.14)
- str: Zeichenketten (z.B. "Hallo")
</details>

---

**Aussage:** Variablennamen duerfen mit einer Zahl beginnen.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

Variablennamen muessen mit einem Buchstaben oder Unterstrich beginnen. `2name` ist ungueltig, aber `name2` und `_name` sind erlaubt.
</details>

---

**Frage 2.1:** Was ist das Ergebnis von `10 % 3`?

- [ ] a) 3
- [ ] b) 1
- [ ] c) 3.33
- [ ] d) 0

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

10 geteilt durch 3 = 3 Rest **1**
Berechnung: 10 = 3 * 3 + 1
</details>

---

**Frage 2.2:** Was ergibt `15 % 5`?

- [ ] a) 3
- [ ] b) 5
- [ ] c) 0
- [ ] d) 15

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

15 ist durch 5 teilbar (ohne Rest).
15 geteilt durch 5 = 3 Rest **0**

**Merke:** Wenn `x % y == 0`, dann ist x durch y teilbar!
</details>

---

**Frage 2.3:** Was ergibt `7 // 2`?

- [ ] a) 3.5
- [ ] b) 3
- [ ] c) 4
- [ ] d) 1

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`//` ist die ganzzahlige Division (Floor Division).
7 geteilt durch 2 = 3.5, aber `//` gibt nur den ganzzahligen Teil: **3**

Vergleich:
- `7 / 2` ergibt 3.5 (normale Division)
- `7 // 2` ergibt 3 (ganzzahlige Division)
- `7 % 2` ergibt 1 (Rest/Modulo)
</details>

---

**Frage 2.4:** Was gibt folgender Code aus?

```python
x = 7
y = 3
print(x // y)
print(x % y)
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe:**
```
2
1
```

**Erklaerung:**
- `7 // 3` = 2 (ganzzahlige Division: 7 geteilt durch 3 ist 2 mit Rest)
- `7 % 3` = 1 (Rest der Division: 7 = 2*3 + 1)
</details>

---

**Frage 2.5:** Welcher Operator prueft auf Teilbarkeit?

- [ ] a) //
- [ ] b) %
- [ ] c) /
- [ ] d) **

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Der Modulo-Operator `%` gibt den Rest einer Division zurueck.
Wenn `x % y == 0`, dann ist x durch y teilbar.

Beispiel: `12 % 3 == 0` bedeutet: 12 ist durch 3 teilbar.
</details>

---

**Frage 2.6:** Was ist die korrekte Reihenfolge der Operatorprioritaet (von hoch nach niedrig)?

- [ ] a) +, -, *, /
- [ ] b) **, *, /, +, -
- [ ] c) *, /, +, -, **
- [ ] d) Alle haben gleiche Prioritaet

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

Reihenfolge (Punkt vor Strich, Potenz zuerst):
1. Klammern `()`
2. Potenz `**`
3. Multiplikation `*`, Division `/`, `//`, Modulo `%`
4. Addition `+`, Subtraktion `-`

Beispiel: `2 + 3 * 4` ergibt 14, nicht 20.
</details>

---

### Frage 2.7: Benutzereingabe

**Schreiben Sie Code, der den Benutzer nach seinem Namen fragt und ihn dann begruessst.**

<details>
<summary>Loesung anzeigen</summary>

```python
name = input("Wie heisst du? ")
print("Hallo", name)
```

Oder mit f-String:
```python
name = input("Wie heisst du? ")
print(f"Hallo {name}!")
```

**Wichtig:** `input()` gibt immer einen String zurueck!
</details>

---

### Frage 2.8: Typumwandlung

**Was passiert bei folgendem Code und warum?**

```python
alter = input("Wie alt bist du? ")
naechstes_jahr = alter + 1
```

<details>
<summary>Loesung anzeigen</summary>

**Es gibt einen TypeError!**

`input()` gibt immer einen String zurueck. Man kann einen String nicht mit einer Zahl addieren.

**Loesung:**
```python
alter = int(input("Wie alt bist du? "))
naechstes_jahr = alter + 1
print("Naechstes Jahr bist du", naechstes_jahr)
```

Die Funktion `int()` wandelt den String in eine Ganzzahl um.
</details>

---

**Frage 2.9:** Was ist der Wert von `x` nach folgenden Zeilen?

```python
x = 10
x = x + 5
x = x * 2
```

- [ ] a) 10
- [ ] b) 15
- [ ] c) 30
- [ ] d) 25

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Schritt fuer Schritt:
1. `x = 10` -> x ist 10
2. `x = x + 5` -> x ist 10 + 5 = 15
3. `x = x * 2` -> x ist 15 * 2 = **30**
</details>

---

**Frage 2.10:** Was ist der Datentyp von `"42"`?

- [ ] a) int
- [ ] b) float
- [ ] c) str
- [ ] d) bool

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Alles in Anfuehrungszeichen ist ein String (str), auch wenn es wie eine Zahl aussieht.
- `42` ist ein int
- `"42"` ist ein str
- `42.0` ist ein float
</details>

---

**Frage 2.11:** Was gibt `type(True)` zurueck?

- [ ] a) `<class 'int'>`
- [ ] b) `<class 'str'>`
- [ ] c) `<class 'bool'>`
- [ ] d) `<class 'true'>`

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`True` und `False` sind vom Typ `bool` (Boolean).
Booleans repraesentieren Wahrheitswerte.
</details>

---

**Frage 2.12:** Was ist das Ergebnis von `2 ** 3`?

- [ ] a) 6
- [ ] b) 8
- [ ] c) 5
- [ ] d) 9

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`**` ist der Potenz-Operator.
`2 ** 3` = 2 hoch 3 = 2 * 2 * 2 = **8**
</details>

---
