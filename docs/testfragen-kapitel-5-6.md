# Testfragen Kapitel 5-6: Iteration und Zeichenketten

## KLAUSURRELEVANT: for-Schleife mit range() und String-Methoden!

---

## Kapitel 5: Iteration (Schleifen)

---

**Aussage:** `range(5)` erzeugt die Zahlen 0, 1, 2, 3, 4.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`range(5)` erzeugt 5 Zahlen, beginnend bei 0: [0, 1, 2, 3, 4]
Die 5 selbst ist NICHT enthalten!
</details>

---

**Aussage:** `break` beendet das gesamte Programm.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

`break` beendet nur die **aktuelle Schleife**, nicht das gesamte Programm. Das Programm laeuft nach der Schleife normal weiter.
</details>

---

**Aussage:** `continue` springt zum naechsten Schleifendurchlauf.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`continue` ueberspringt den Rest des aktuellen Durchlaufs und startet sofort den naechsten Durchlauf der Schleife.
</details>

---

**Frage 5.1:** Was gibt `list(range(1, 6))` aus?

- [ ] a) [0, 1, 2, 3, 4, 5]
- [ ] b) [1, 2, 3, 4, 5]
- [ ] c) [1, 2, 3, 4, 5, 6]
- [ ] d) [1, 6]

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`range(1, 6)` startet bei 1 und endet **vor** 6.
Ergebnis: [1, 2, 3, 4, 5]

**Merke:** Der Endwert ist immer exklusiv (nicht enthalten)!
</details>

---

**Frage 5.2:** Was gibt `list(range(0, 10, 2))` aus?

- [ ] a) [0, 2, 4, 6, 8]
- [ ] b) [0, 2, 4, 6, 8, 10]
- [ ] c) [2, 4, 6, 8, 10]
- [ ] d) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

<details>
<summary>Loesung anzeigen</summary>

**Richtig: a)**

`range(start, stop, step)` - der dritte Parameter ist die Schrittweite.
`range(0, 10, 2)` erzeugt: 0, 2, 4, 6, 8 (in 2er-Schritten, 10 nicht enthalten)
</details>

---

### Frage 5.3: KLAUSURAUFGABE - for-Schleife ueberschreibt Variable!

**Was ist der Wert von i und j nach der Schleife?**

```python
i = 27
j = 27

for i in range(3):
    j += 1

print(i, j)
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe: `2 30`**

**Schritt-fuer-Schritt-Erklaerung:**

1. `i = 27` und `j = 27` (Initialwerte)
2. `for i in range(3):` - Die Schleifenvariable `i` ueberschreibt den alten Wert!
   - Durchlauf 1: i=0, j=28
   - Durchlauf 2: i=1, j=29
   - Durchlauf 3: i=2, j=30
3. Nach der Schleife: i=2 (letzter Wert von range), j=30

**WICHTIG:** Die for-Schleife ueberschreibt die Variable `i`! Der urspruengliche Wert 27 ist verloren.

Dies war eine echte Klausuraufgabe mit 30 Punkten!
</details>

---

**Frage 5.4:** Wie oft wird "Hallo" ausgegeben?

```python
for i in range(5):
    print("Hallo")
```

- [ ] a) 4 mal
- [ ] b) 5 mal
- [ ] c) 6 mal
- [ ] d) Unendlich oft

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`range(5)` erzeugt 5 Werte (0, 1, 2, 3, 4), also wird die Schleife 5 mal durchlaufen.
</details>

---

**Frage 5.5:** Was ist die Ausgabe?

```python
summe = 0
for i in range(1, 4):
    summe += i
print(summe)
```

- [ ] a) 3
- [ ] b) 6
- [ ] c) 10
- [ ] d) 4

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`range(1, 4)` erzeugt [1, 2, 3]
summe = 0 + 1 + 2 + 3 = **6**
</details>

---

**Frage 5.6:** Was ist der Unterschied zwischen `while` und `for`?

<details>
<summary>Loesung anzeigen</summary>

**for-Schleife:**
- Iteriert ueber eine bekannte Anzahl von Elementen
- Benutzt `range()` oder iteriert ueber Listen/Strings
- Gut fuer: "Tue dies n mal" oder "Fuer jedes Element in..."

```python
for i in range(5):
    print(i)
```

**while-Schleife:**
- Laeuft solange eine Bedingung wahr ist
- Anzahl der Durchlaeufe oft unbekannt
- Gut fuer: "Tue dies bis..."

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

**Achtung:** Bei `while` kann eine Endlosschleife entstehen, wenn die Bedingung nie falsch wird!
</details>

---

## Kapitel 6: Zeichenketten (Strings)

---

**Aussage:** Strings in Python sind unveraenderlich (immutable).

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Man kann einzelne Zeichen eines Strings nicht aendern:
```python
s = "Hallo"
s[0] = "M"  # FEHLER! TypeError
```

Stattdessen muss man einen neuen String erstellen:
```python
s = "Hallo"
s = "M" + s[1:]  # "Mallo"
```
</details>

---

**Aussage:** `"Hallo".lower()` gibt "hallo" zurueck.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`lower()` wandelt alle Buchstaben in Kleinbuchstaben um.
</details>

---

**Aussage:** `"abc".replace("a", "x")` veraendert den Original-String.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

Strings sind unveraenderlich! `replace()` gibt einen **neuen** String zurueck, der Originale bleibt unveraendert.

```python
s = "abc"
s.replace("a", "x")  # Gibt "xbc" zurueck, aber s ist immer noch "abc"
s = s.replace("a", "x")  # Jetzt ist s = "xbc"
```
</details>

---

**Frage 6.1:** Was gibt `"Hallo Welt".split()` zurueck?

- [ ] a) "Hallo Welt"
- [ ] b) ["Hallo", "Welt"]
- [ ] c) ("Hallo", "Welt")
- [ ] d) "HalloWelt"

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`split()` ohne Argument trennt am Leerzeichen und gibt eine **Liste** zurueck.
</details>

---

**Frage 6.2:** Wie ersetzt man `"ae"` durch `"ä"` in einem String s?

- [ ] a) `s["ae"] = "ä"`
- [ ] b) `s.replace("ae", "ä")`
- [ ] c) `s.substitute("ae", "ä")`
- [ ] d) `s.change("ae", "ä")`

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`replace(alt, neu)` ersetzt alle Vorkommen von `alt` durch `neu`.

**Wichtig:** Man muss das Ergebnis speichern!
```python
s = s.replace("ae", "ä")
```
</details>

---

**Frage 6.3:** Was ist das Ergebnis?

```python
s = "Python"
print(s[0])
print(s[-1])
print(s[1:4])
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe:**
```
P
n
yth
```

**Erklaerung:**
- `s[0]` = erstes Zeichen = "P"
- `s[-1]` = letztes Zeichen = "n"
- `s[1:4]` = Zeichen 1, 2, 3 (Index 4 exklusiv) = "yth"
</details>

---

**Frage 6.4:** Was gibt `len("Hallo")` zurueck?

- [ ] a) 4
- [ ] b) 5
- [ ] c) 6
- [ ] d) "Hallo"

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`len()` gibt die Anzahl der Zeichen zurueck. "Hallo" hat 5 Zeichen.
</details>

---

### Frage 6.5: KLAUSURAUFGABE - Textverarbeitung!

**Schreiben Sie Code, der einen Text in Kleinbuchstaben umwandelt und alle deutschen Umlaute ersetzt (`ä`->`ae`, `ö`->`oe`, `ü`->`ue`, `ß`->`ss`).**

<details>
<summary>Loesung anzeigen</summary>

```python
text = "Groesse und Uebung"
text = text.lower()
text = text.replace("ä", "ae")
text = text.replace("ö", "oe")
text = text.replace("ü", "ue")
text = text.replace("ß", "ss")
print(text)  # groesse und uebung
```

**Als Funktion:**
```python
def text_bereinigen(text):
    text = text.lower()
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")
    return text

# Test
print(text_bereinigen("Größe und Übung"))
# Ausgabe: groesse und uebung
```

**Mit Dictionary (eleganter):**
```python
def text_bereinigen(text):
    text = text.lower()
    ersetzungen = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}
    for alt, neu in ersetzungen.items():
        text = text.replace(alt, neu)
    return text
```

Dies war eine echte Klausuraufgabe mit 15 Punkten!
</details>

---

**Frage 6.6:** Was ist die Ausgabe?

```python
s = "abc"
s = s.upper()
print(s)
```

- [ ] a) abc
- [ ] b) ABC
- [ ] c) Abc
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`upper()` wandelt alle Buchstaben in Grossbuchstaben um.
Wichtig: Man muss das Ergebnis zuweisen (`s = s.upper()`)!
</details>

---

**Frage 6.7:** Wie zaehlt man, wie oft "a" in einem String vorkommt?

<details>
<summary>Loesung anzeigen</summary>

**Methode 1: Mit count()**
```python
s = "banana"
anzahl = s.count("a")
print(anzahl)  # 3
```

**Methode 2: Mit Schleife**
```python
s = "banana"
anzahl = 0
for zeichen in s:
    if zeichen == "a":
        anzahl += 1
print(anzahl)  # 3
```
</details>

---

**Frage 6.8:** Was gibt `"a,b,c".split(",")` zurueck?

- [ ] a) "abc"
- [ ] b) ["a", "b", "c"]
- [ ] c) ["a,b,c"]
- [ ] d) ("a", "b", "c")

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`split(",")` trennt den String am Komma und gibt eine Liste zurueck.
</details>

---

**Frage 6.9:** Was ist die Ausgabe?

```python
woerter = ["Hallo", "Welt"]
satz = " ".join(woerter)
print(satz)
```

- [ ] a) HalloWelt
- [ ] b) Hallo Welt
- [ ] c) ["Hallo", "Welt"]
- [ ] d) Hallo, Welt

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`join()` verbindet Liste-Elemente mit dem angegebenen Trennzeichen.
`" ".join(["Hallo", "Welt"])` ergibt "Hallo Welt"
</details>

---

**Frage 6.10:** Welche String-Methoden sind fuer die Klausur am wichtigsten?

<details>
<summary>Loesung anzeigen</summary>

**Klausurrelevante String-Methoden:**

| Methode | Funktion | Beispiel |
|---------|----------|----------|
| `lower()` | Kleinbuchstaben | `"ABC".lower()` → "abc" |
| `upper()` | Grossbuchstaben | `"abc".upper()` → "ABC" |
| `replace(alt, neu)` | Ersetzen | `"abc".replace("a", "x")` → "xbc" |
| `split()` | In Liste aufteilen | `"a b".split()` → ["a", "b"] |
| `strip()` | Leerzeichen entfernen | `" ab ".strip()` → "ab" |
| `find(s)` | Position finden | `"abc".find("b")` → 1 |
| `count(s)` | Zaehlen | `"aaa".count("a")` → 3 |
| `len(s)` | Laenge | `len("abc")` → 3 |

**Fuer Klausuraufgabe 3 wichtig:**
- `lower()` - Text in Kleinbuchstaben
- `replace()` - Umlaute ersetzen
</details>

---
