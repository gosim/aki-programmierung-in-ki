# Klausurfragen-Sammlung

## PKI Klausur - Echte Aufgaben mit Musterloesungen

Diese Sammlung enthaelt die echten Klausuraufgaben basierend auf den Gedaechtnisprotokollen der Studenten.

---

# Aufgabe 1: Code-Verstaendnis (30 Punkte)

## Aufgabe 1a: for-Schleife mit range()

**Was ist die Ausgabe des folgenden Codes?**

```python
i = 27
j = 27

for i in range(3):
    j += 1

print(i, j)
```

**Loesung:**

**Ausgabe:** `2 30`

**Schritt-fuer-Schritt-Erklaerung:**

1. Anfangswerte: `i = 27`, `j = 27`

2. Die for-Schleife mit `range(3)` erzeugt die Werte 0, 1, 2

3. **WICHTIG:** Die Schleifenvariable `i` ueberschreibt den urspruenglichen Wert 27!

4. Durchlaeufe:
   - Durchlauf 1: i = 0, j = 27 + 1 = 28
   - Durchlauf 2: i = 1, j = 28 + 1 = 29
   - Durchlauf 3: i = 2, j = 29 + 1 = 30

5. Nach der Schleife: i = 2 (letzter Wert von range), j = 30

**Wichtige Erkenntnis:**
Die for-Schleife ueberschreibt die Variable `i`. Der urspruengliche Wert 27 geht verloren.

---

## Aufgabe 1b: try-except bei Benutzereingabe

**Schreiben Sie einen try-except-Block fuer die Eingabe eines Integers. Erklaeren Sie, warum das sinnvoll ist.**

**Loesung:**

```python
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    print("Ihre Zahl:", zahl)
except ValueError:
    print("Ungueltige Zahl eingegeben!")
```

**Warum ist try-except sinnvoll?**

1. **Benutzer koennen fehlerhafte Eingaben machen:**
   - Text statt Zahlen eingeben ("abc" statt "123")
   - Leerzeichen oder Sonderzeichen

2. **Ohne try-except stuerzt das Programm ab:**
   - `int("abc")` wirft einen ValueError
   - Das Programm bricht sofort ab

3. **Mit try-except bleibt das Programm stabil:**
   - Fehler werden abgefangen
   - Benutzer erhaelt verstaendliche Fehlermeldung
   - Programm kann weiterlaufen

4. **Benutzerfreundlichkeit:**
   - Statt kryptischer Python-Fehlermeldung
   - Klare, verstaendliche Rueckmeldung

**Erweiterte Version mit Wiederholung:**

```python
while True:
    try:
        zahl = int(input("Geben Sie eine Zahl ein: "))
        break  # Erfolgreiche Eingabe, Schleife verlassen
    except ValueError:
        print("Ungueltige Eingabe! Bitte eine Zahl eingeben.")

print("Sie haben", zahl, "eingegeben.")
```

---

## Aufgabe 1c: Dictionary zum Zaehlen

**Was macht folgender Code? Was ist die Ausgabe?**

```python
count = {}
words = ["a", "b", "c"]
for w in words:
    count[w] = count.get(w, 0) + 1
print(count)
```

**Loesung:**

**Ausgabe:** `{'a': 1, 'b': 1, 'c': 1}`

**Erklaerung:**

Der Code zaehlt die Haeufigkeit jedes Elements in der Liste.

**Schritt-fuer-Schritt:**

1. `count = {}` - Leeres Dictionary erstellen

2. Fuer jedes Wort in der Liste:
   - `count.get(w, 0)` - Holt den aktuellen Zaehler fuer das Wort (oder 0 wenn nicht vorhanden)
   - `+ 1` - Erhoeht den Zaehler um 1
   - `count[w] = ...` - Speichert den neuen Zaehler

3. Durchlaeufe:
   - "a": count.get("a", 0) = 0, dann 0+1=1 → count = {"a": 1}
   - "b": count.get("b", 0) = 0, dann 0+1=1 → count = {"a": 1, "b": 1}
   - "c": count.get("c", 0) = 0, dann 0+1=1 → count = {"a": 1, "b": 1, "c": 1}

**Was macht count.get(w, 0)?**

- Sucht den Schluessel `w` im Dictionary `count`
- Wenn gefunden: gibt den gespeicherten Wert zurueck
- Wenn NICHT gefunden: gibt den Standardwert 0 zurueck

Das ist eleganter als:
```python
if w in count:
    count[w] = count[w] + 1
else:
    count[w] = 1
```

---

# Aufgabe 2: FizzBuzz (15 Punkte)

**Schreiben Sie eine Funktion, die fuer Zahlen von 1 bis n (benutzerdefiniert oder 100) prueft:**
- Wenn durch 3 teilbar: "Fizz" ausgeben
- Wenn durch 5 teilbar: "Buzz" ausgeben
- Wenn durch 3 UND 5 teilbar: "FizzBuzz" ausgeben
- Sonst: die Zahl selbst ausgeben

**Loesung:**

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

# Aufruf mit Standardwert:
fizzbuzz(100)

# Oder mit Benutzereingabe:
try:
    grenze = int(input("Bis zu welcher Zahl? "))
    fizzbuzz(grenze)
except ValueError:
    print("Ungueltige Eingabe, verwende 100")
    fizzbuzz(100)
```

**Wichtige Punkte:**

1. **Reihenfolge ist entscheidend:**
   - ZUERST auf "durch 3 UND 5 teilbar" pruefen (FizzBuzz)
   - DANN einzeln auf 3 oder 5
   - Sonst wuerde z.B. 15 als "Fizz" erkannt werden

2. **Modulo-Operator (%):**
   - `x % y` gibt den Rest der Division zurueck
   - `x % 3 == 0` bedeutet "x ist durch 3 teilbar"

3. **Alternative fuer "durch 3 und 5":**
   - `i % 3 == 0 and i % 5 == 0`
   - ODER: `i % 15 == 0` (kgV von 3 und 5)

**Beispielausgabe fuer fizzbuzz(15):**
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

---

# Aufgabe 3: Textverarbeitung (15 Punkte)

**Eingabe: Ein Text**
**Aufgabe:**
1. Text in Kleinbuchstaben umwandeln
2. Alle deutschen Umlaute ersetzen (`ä`→`ae`, `ö`→`oe`, `ü`→`ue`, `ß`→`ss`)

**Loesung:**

```python
def text_bereinigen(text):
    # Schritt 1: Kleinbuchstaben
    text = text.lower()

    # Schritt 2: Umlaute ersetzen
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")

    return text

# Test:
eingabe = "Größe und Übung"
ergebnis = text_bereinigen(eingabe)
print(ergebnis)  # "groesse und uebung"
```

**Alternative mit Dictionary:**

```python
def text_bereinigen(text):
    text = text.lower()

    ersetzungen = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss"
    }

    for alt, neu in ersetzungen.items():
        text = text.replace(alt, neu)

    return text
```

**Wichtige Punkte:**

1. **Strings sind unveraenderlich:**
   - `text.lower()` gibt einen NEUEN String zurueck
   - Man muss das Ergebnis speichern: `text = text.lower()`

2. **Reihenfolge von lower() und replace():**
   - ZUERST `lower()`, dann die Umlaute ersetzen
   - Sonst muesste man auch "Ä", "Ö", "Ü" separat behandeln

3. **String-Methoden:**
   - `lower()` - Alles in Kleinbuchstaben
   - `upper()` - Alles in Grossbuchstaben
   - `replace(alt, neu)` - Ersetzen

---

# Aufgabe 4: Schaltjahr pruefen (10 Punkte)

**Schreiben Sie ein Programm, das prueft, ob ein eingegebenes Jahr ein Schaltjahr ist.**

Regeln:
- Durch 4 teilbar → Schaltjahr
- ABER durch 100 teilbar → KEIN Schaltjahr
- ABER durch 400 teilbar → doch Schaltjahr

**Loesung:**

```python
jahr = int(input("Jahr: "))

if jahr % 400 == 0:
    print("Schaltjahr")
elif jahr % 100 == 0:
    print("Gemeinjahr")
elif jahr % 4 == 0:
    print("Schaltjahr")
else:
    print("Gemeinjahr")
```

**Alternative (kompakter):**

```python
jahr = int(input("Jahr: "))

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print("Schaltjahr")
else:
    print("Gemeinjahr")
```

**Wichtige Punkte:**

1. **Reihenfolge der Bedingungen:**
   - ZUERST durch 400 pruefen (Sonderfall)
   - DANN durch 100 (Ausnahme)
   - DANN durch 4 (Grundregel)

2. **Testfaelle:**
   - 2000 → Schaltjahr (durch 400 teilbar)
   - 1900 → Gemeinjahr (durch 100, aber nicht durch 400)
   - 2024 → Schaltjahr (durch 4, nicht durch 100)
   - 2023 → Gemeinjahr (nicht durch 4)

---

# Aufgabe 5: Wie viele Zahlen sind gleich? (10 Punkte)

**Schreiben Sie ein Programm, das drei ganze Zahlen vom Benutzer entgegennimmt und angibt, wie viele davon gleich sind.**

- Wenn alle drei gleich → 3
- Wenn genau zwei gleich → 2
- Wenn alle verschieden → 0

**Loesung:**

```python
z1 = int(input("Zahl 1: "))
z2 = int(input("Zahl 2: "))
z3 = int(input("Zahl 3: "))

if z1 == z2 == z3:
    print(3)
elif z1 == z2 or z1 == z3 or z2 == z3:
    print(2)
else:
    print(0)
```

**Wichtige Punkte:**

1. **Verkettete Vergleiche:**
   - Python erlaubt `z1 == z2 == z3` (wie in Mathe!)
   - Entspricht `z1 == z2 and z2 == z3`

2. **Logische Operatoren:**
   - `or` - mindestens eine Bedingung muss wahr sein
   - `and` - alle Bedingungen muessen wahr sein

**Beispiel:**
```
Zahl 1: 3
Zahl 2: -4
Zahl 3: 3
2
```

---

# Aufgabe 6: Pluralendung (10 Punkte)

**Schreiben Sie ein Programm, das den Benutzer nach einer Zahl fragt und grammatikalisch korrekt ausgibt: "N Datei(en) kopiert."**

**Loesung:**

```python
anzahl = int(input("Wie viele Dateien sollen kopiert werden? "))

if anzahl == 1:
    print(f"{anzahl} Datei kopiert.")
else:
    print(f"{anzahl} Dateien kopiert.")
```

**Erweiterte Version mit Validierung:**

```python
try:
    anzahl = int(input("Anzahl: "))
    if anzahl < 0:
        print("Fehler: Negative Zahl!")
    elif anzahl == 1:
        print(f"{anzahl} Datei kopiert.")
    else:
        print(f"{anzahl} Dateien kopiert.")
except ValueError:
    print("Bitte eine ganze Zahl eingeben!")
```

**Wichtige Punkte:**

1. **f-Strings:**
   - `f"{variable}"` - formatierter String
   - Variable wird direkt im Text eingefuegt

2. **Grammatik beachten:**
   - 1 → Singular ("Datei")
   - 0, 2, 3, ... → Plural ("Dateien")

**Beispiel:**
```
Wie viele Dateien sollen kopiert werden? 1
1 Datei kopiert.

Wie viele Dateien sollen kopiert werden? 15
15 Dateien kopiert.
```

---

# Zusammenfassung: Klausurtipps

## Haeufige Fallen:

1. **for-Schleife ueberschreibt Variable:**
   ```python
   i = 100
   for i in range(3):  # i wird 0, 1, 2
       pass
   # i ist jetzt 2, nicht 100!
   ```

2. **range(n) endet bei n-1:**
   ```python
   range(5)  # 0, 1, 2, 3, 4 (nicht 5!)
   range(1, 5)  # 1, 2, 3, 4 (nicht 5!)
   ```

3. **Strings sind unveraenderlich:**
   ```python
   s = "hallo"
   s.upper()  # Gibt "HALLO" zurueck, aber s bleibt "hallo"
   s = s.upper()  # Jetzt ist s = "HALLO"
   ```

4. **dict[key] vs dict.get(key):**
   ```python
   d = {"a": 1}
   d["b"]  # KeyError!
   d.get("b", 0)  # Gibt 0 zurueck (kein Fehler)
   ```

## Wichtigste Konzepte:

1. **Modulo fuer Teilbarkeit:** `x % y == 0`
2. **dict.get() zum Zaehlen:** `d[key] = d.get(key, 0) + 1`
3. **try-except fuer Benutzereingaben**
4. **String-Methoden:** `lower()`, `replace()`
5. **for-Schleifen mit range()**

---
