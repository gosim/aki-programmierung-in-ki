# Beliebte Klausuraufgaben - Python Programmierung

## Die haeufigsten Programmieraufgaben in Klausuren

**Quelle:** Lehrbuch "Python fuer alle", Kapitel 1-14; GitHub fhswf/pki

---

## Teil 1: Zahlen und Mathematik

---

### Frage B.1: Quersumme berechnen

**Schreiben Sie eine Funktion `quersumme(n)`, die die Summe aller Ziffern einer positiven ganzen Zahl berechnet.**

Beispiel: `quersumme(1234)` soll `10` zurueckgeben (1+2+3+4=10)

<details>
<summary>Loesung anzeigen</summary>

```python
def quersumme(n):
    summe = 0
    while n > 0:
        summe += n % 10   # Letzte Ziffer addieren
        n = n // 10       # Letzte Ziffer entfernen
    return summe

# Test
print(quersumme(1234))   # 10
print(quersumme(9999))   # 36
```

**Erklaerung:**
- `n % 10` gibt die letzte Ziffer (Rest bei Division durch 10)
- `n // 10` entfernt die letzte Ziffer (ganzzahlige Division)

**Alternative mit String:**
```python
def quersumme_string(n):
    return sum(int(ziffer) for ziffer in str(n))
```

</details>

---

### Frage B.2: Zahl umkehren

**Schreiben Sie eine Funktion `zahl_umkehren(n)`, die die Ziffern einer Zahl umkehrt.**

Beispiel: `zahl_umkehren(1234)` soll `4321` zurueckgeben.

<details>
<summary>Loesung anzeigen</summary>

```python
def zahl_umkehren(n):
    umgekehrt = 0
    while n > 0:
        letzte_ziffer = n % 10
        umgekehrt = umgekehrt * 10 + letzte_ziffer
        n = n // 10
    return umgekehrt

# Test
print(zahl_umkehren(1234))   # 4321
print(zahl_umkehren(54321))  # 12345
```

**Erklaerung:**
- `n % 10` holt die letzte Ziffer
- `umgekehrt * 10` schiebt bisherige Ziffern nach links
- `+ letzte_ziffer` fuegt neue Ziffer rechts an

</details>

---

### Frage B.3: Primzahl pruefen

**Schreiben Sie eine Funktion `ist_primzahl(n)`, die `True` zurueckgibt, wenn n eine Primzahl ist, sonst `False`.**

Eine Primzahl ist nur durch 1 und sich selbst teilbar.

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_primzahl(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
print(ist_primzahl(17))   # True
print(ist_primzahl(18))   # False
```

**Erklaerung:**
- Zahlen <= 1 sind keine Primzahlen
- Man muss nur bis sqrt(n) pruefen (Optimierung!)

</details>

---

### Frage B.4: Alle Primzahlen bis N

**Schreiben Sie eine Funktion `primzahlen_bis(n)`, die alle Primzahlen von 2 bis n als Liste zurueckgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_primzahl(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primzahlen_bis(n):
    return [x for x in range(2, n+1) if ist_primzahl(x)]

# Test
print(primzahlen_bis(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
```

</details>

---

### Frage B.5: Fakultaet berechnen

**Schreiben Sie eine Funktion `fakultaet(n)`, die n! berechnet.**

n! = n * (n-1) * (n-2) * ... * 2 * 1

Beispiel: 5! = 120

<details>
<summary>Loesung anzeigen</summary>

**Iterative Loesung:**
```python
def fakultaet(n):
    ergebnis = 1
    for i in range(2, n + 1):
        ergebnis *= i
    return ergebnis

print(fakultaet(5))   # 120
```

**Rekursive Loesung:**
```python
def fakultaet_rekursiv(n):
    if n <= 1:
        return 1
    return n * fakultaet_rekursiv(n - 1)
```

</details>

---

### Frage B.6: Fibonacci-Folge

**Schreiben Sie eine Funktion `fibonacci(n)`, die die ersten n Fibonacci-Zahlen als Liste zurueckgibt.**

Die Folge beginnt mit 0, 1 und jede weitere Zahl ist die Summe der beiden vorherigen.

<details>
<summary>Loesung anzeigen</summary>

```python
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Alternative (nur Ausgabe):**
```python
def fibonacci_print(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
```

</details>

---

### Frage B.7: Armstrong-Zahl pruefen

**Eine Armstrong-Zahl ist gleich der Summe ihrer Ziffern potenziert mit der Anzahl der Ziffern.**

Beispiel: 153 = 1³ + 5³ + 3³ = 153

Schreiben Sie eine Funktion `ist_armstrong(n)`.

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_armstrong(n):
    ziffern = str(n)
    anzahl = len(ziffern)
    summe = sum(int(z) ** anzahl for z in ziffern)
    return summe == n

print(ist_armstrong(153))   # True
print(ist_armstrong(370))   # True
print(ist_armstrong(123))   # False
```

**Bekannte Armstrong-Zahlen:** 0, 1, 153, 370, 371, 407, 1634

</details>

---

### Frage B.8: Vollkommene Zahl pruefen

**Eine vollkommene Zahl ist gleich der Summe ihrer echten Teiler (ohne sich selbst).**

Beispiel: 6 = 1 + 2 + 3

Schreiben Sie eine Funktion `ist_vollkommen(n)`.

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_vollkommen(n):
    if n <= 1:
        return False

    teiler_summe = 0
    for i in range(1, n):
        if n % i == 0:
            teiler_summe += i

    return teiler_summe == n

print(ist_vollkommen(6))    # True (1+2+3=6)
print(ist_vollkommen(28))   # True (1+2+4+7+14=28)
```

**Vollkommene Zahlen:** 6, 28, 496, 8128

</details>

---

## Teil 2: Strings und Texte

---

### Frage B.9: Palindrom pruefen

**Schreiben Sie eine Funktion `ist_palindrom(text)`, die `True` zurueckgibt, wenn der Text vorwaerts und rueckwaerts gleich ist.**

Beispiele: "anna", "otto", "12321"

<details>
<summary>Loesung anzeigen</summary>

```python
def ist_palindrom(text):
    text = text.lower()
    return text == text[::-1]

print(ist_palindrom("Anna"))      # True
print(ist_palindrom("Otto"))      # True
print(ist_palindrom("12321"))     # True
print(ist_palindrom("Hallo"))     # False
```

**Mit Schleife:**
```python
def ist_palindrom_schleife(text):
    text = text.lower()
    links, rechts = 0, len(text) - 1

    while links < rechts:
        if text[links] != text[rechts]:
            return False
        links += 1
        rechts -= 1
    return True
```

</details>

---

### Frage B.10: String umkehren

**Schreiben Sie eine Funktion `umkehren(text)`, die einen String rueckwaerts zurueckgibt.**

<details>
<summary>Loesung anzeigen</summary>

**Mit Slicing (Pythonisch):**
```python
def umkehren(text):
    return text[::-1]

print(umkehren("Hallo"))  # "ollaH"
```

**Mit Schleife:**
```python
def umkehren_schleife(text):
    ergebnis = ""
    for zeichen in text:
        ergebnis = zeichen + ergebnis
    return ergebnis
```

</details>

---

### Frage B.11: Zeichen zaehlen mit Dictionary

**Schreiben Sie eine Funktion `zeichen_zaehlen(text)`, die ein Dictionary mit der Haeufigkeit jedes Zeichens zurueckgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
def zeichen_zaehlen(text):
    zaehler = {}
    for zeichen in text:
        zaehler[zeichen] = zaehler.get(zeichen, 0) + 1
    return zaehler

print(zeichen_zaehlen("hallo"))
# {'h': 1, 'a': 1, 'l': 2, 'o': 1}

print(zeichen_zaehlen("mississippi"))
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

**WICHTIG: Das Muster `dict.get(key, 0) + 1` ist klausurrelevant!**

</details>

---

### Frage B.12: Woerter zaehlen

**Schreiben Sie eine Funktion `woerter_zaehlen(text)`, die die Haeufigkeit jedes Wortes zaehlt.**

<details>
<summary>Loesung anzeigen</summary>

```python
def woerter_zaehlen(text):
    zaehler = {}
    woerter = text.lower().split()

    for wort in woerter:
        zaehler[wort] = zaehler.get(wort, 0) + 1

    return zaehler

text = "Python ist toll und Python ist einfach"
print(woerter_zaehlen(text))
# {'python': 2, 'ist': 2, 'toll': 1, 'und': 1, 'einfach': 1}
```

</details>

---

### Frage B.13: Anagramm pruefen

**Zwei Woerter sind Anagramme, wenn sie die gleichen Buchstaben enthalten.**

Beispiel: "listen" und "silent"

Schreiben Sie eine Funktion `sind_anagramme(wort1, wort2)`.

<details>
<summary>Loesung anzeigen</summary>

```python
def sind_anagramme(wort1, wort2):
    return sorted(wort1.lower()) == sorted(wort2.lower())

print(sind_anagramme("listen", "silent"))  # True
print(sind_anagramme("Erde", "Rede"))      # True
print(sind_anagramme("Hallo", "Welt"))     # False
```

</details>

---

## Teil 3: Listen

---

### Frage B.14: Maximum und Minimum finden (ohne max/min)

**Schreiben Sie Funktionen `finde_max(liste)` und `finde_min(liste)` OHNE die eingebauten Funktionen.**

<details>
<summary>Loesung anzeigen</summary>

```python
def finde_max(liste):
    if not liste:
        return None
    maximum = liste[0]
    for element in liste:
        if element > maximum:
            maximum = element
    return maximum

def finde_min(liste):
    if not liste:
        return None
    minimum = liste[0]
    for element in liste:
        if element < minimum:
            minimum = element
    return minimum

zahlen = [3, 1, 4, 1, 5, 9, 2, 6]
print(finde_max(zahlen))  # 9
print(finde_min(zahlen))  # 1
```

</details>

---

### Frage B.15: Liste umkehren (ohne Slicing)

**Schreiben Sie eine Funktion `liste_umkehren(liste)` OHNE Slicing oder reverse().**

<details>
<summary>Loesung anzeigen</summary>

```python
def liste_umkehren(liste):
    ergebnis = []
    for i in range(len(liste) - 1, -1, -1):
        ergebnis.append(liste[i])
    return ergebnis

print(liste_umkehren([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

**Mit Slicing (einfach):**
```python
def liste_umkehren_slice(liste):
    return liste[::-1]
```

</details>

---

### Frage B.16: Duplikate entfernen

**Schreiben Sie eine Funktion `duplikate_entfernen(liste)`, die eine Liste ohne Duplikate zurueckgibt.**

<details>
<summary>Loesung anzeigen</summary>

**Mit Set:**
```python
def duplikate_entfernen(liste):
    return list(set(liste))

print(duplikate_entfernen([1, 2, 2, 3, 3, 3]))  # [1, 2, 3]
```

**Mit Reihenfolge erhalten:**
```python
def duplikate_entfernen_order(liste):
    gesehen = []
    for element in liste:
        if element not in gesehen:
            gesehen.append(element)
    return gesehen
```

</details>

---

### Frage B.17: Liste flatten (verschachtelt)

**Schreiben Sie eine Funktion `flatten(liste)`, die eine verschachtelte Liste "flach" macht.**

Beispiel: `[[1, 2], [3, [4, 5]]]` wird zu `[1, 2, 3, 4, 5]`

<details>
<summary>Loesung anzeigen</summary>

```python
def flatten(liste):
    ergebnis = []
    for element in liste:
        if isinstance(element, list):
            ergebnis.extend(flatten(element))
        else:
            ergebnis.append(element)
    return ergebnis

print(flatten([1, [2, 3], [4, [5, 6]]]))
# [1, 2, 3, 4, 5, 6]
```

</details>

---

## Teil 4: FizzBuzz und Varianten

---

### Frage B.18: Summe der Vielfachen

**Schreiben Sie eine Funktion `summe_vielfache(n)`, die die Summe aller Zahlen unter n berechnet, die durch 3 ODER 5 teilbar sind.**

Beispiel: Unter 10 sind das: 3, 5, 6, 9 → Summe = 23

<details>
<summary>Loesung anzeigen</summary>

```python
def summe_vielfache(n):
    summe = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            summe += i
    return summe

print(summe_vielfache(10))    # 23
print(summe_vielfache(1000))  # 233168
```

**Mit List Comprehension:**
```python
def summe_vielfache_comp(n):
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)
```

</details>

---

### Frage B.19: Gerade und Ungerade filtern

**Schreiben Sie Funktionen `nur_gerade(liste)` und `nur_ungerade(liste)`.**

<details>
<summary>Loesung anzeigen</summary>

```python
def nur_gerade(liste):
    return [x for x in liste if x % 2 == 0]

def nur_ungerade(liste):
    return [x for x in liste if x % 2 != 0]

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nur_gerade(zahlen))    # [2, 4, 6, 8, 10]
print(nur_ungerade(zahlen))  # [1, 3, 5, 7, 9]
```

</details>

---

## Teil 5: Dateien und Ein-/Ausgabe

---

### Frage B.20: Zeilen in Datei zaehlen

**Schreiben Sie eine Funktion `zeilen_zaehlen(dateiname)`, die die Anzahl der Zeilen zurueckgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
def zeilen_zaehlen(dateiname):
    try:
        with open(dateiname, 'r') as datei:
            return len(datei.readlines())
    except FileNotFoundError:
        print("Datei nicht gefunden!")
        return 0
```

**Speichereffizienter:**
```python
def zeilen_zaehlen_effizient(dateiname):
    anzahl = 0
    with open(dateiname, 'r') as datei:
        for zeile in datei:
            anzahl += 1
    return anzahl
```

</details>

---

### Frage B.21: Woerter aus Datei zaehlen

**Schreiben Sie eine Funktion, die alle Woerter einer Datei zaehlt und ein Dictionary zurueckgibt.**

<details>
<summary>Loesung anzeigen</summary>

```python
def woerter_aus_datei(dateiname):
    zaehler = {}

    with open(dateiname, 'r') as datei:
        for zeile in datei:
            woerter = zeile.lower().split()
            for wort in woerter:
                zaehler[wort] = zaehler.get(wort, 0) + 1

    return zaehler
```

</details>

---

## Teil 6: OOP (Klassen)

---

### Frage B.22: Einfache Klasse Person

**Erstellen Sie eine Klasse `Person` mit Attributen `name` und `alter` sowie einer Methode `vorstellen()`.**

<details>
<summary>Loesung anzeigen</summary>

```python
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def vorstellen(self):
        print(f"Hallo, ich bin {self.name} und {self.alter} Jahre alt.")

person1 = Person("Anna", 25)
person1.vorstellen()  # Hallo, ich bin Anna und 25 Jahre alt.
```

**WICHTIG:**
- `__init__` ist der Konstruktor
- `self` referenziert das aktuelle Objekt

</details>

---

### Frage B.23: Klasse Rechteck mit Methoden

**Erstellen Sie eine Klasse `Rechteck` mit Attributen `breite` und `hoehe` sowie Methoden `flaeche()` und `umfang()`.**

<details>
<summary>Loesung anzeigen</summary>

```python
class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return self.breite * self.hoehe

    def umfang(self):
        return 2 * (self.breite + self.hoehe)

r = Rechteck(5, 3)
print(f"Flaeche: {r.flaeche()}")   # 15
print(f"Umfang: {r.umfang()}")     # 16
```

</details>

---

### Frage B.24: Klasse Bankkonto

**Erstellen Sie eine Klasse `Bankkonto` mit Methoden `einzahlen(betrag)`, `abheben(betrag)` und `kontostand_anzeigen()`.**

<details>
<summary>Loesung anzeigen</summary>

```python
class Bankkonto:
    def __init__(self, inhaber, kontostand=0):
        self.inhaber = inhaber
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag} EUR eingezahlt.")

    def abheben(self, betrag):
        if betrag > self.kontostand:
            print("Nicht genug Guthaben!")
        elif betrag > 0:
            self.kontostand -= betrag
            print(f"{betrag} EUR abgehoben.")

    def kontostand_anzeigen(self):
        print(f"Kontostand: {self.kontostand} EUR")

konto = Bankkonto("Max", 100)
konto.einzahlen(50)           # 50 EUR eingezahlt.
konto.abheben(30)             # 30 EUR abgehoben.
konto.kontostand_anzeigen()   # Kontostand: 120 EUR
```

</details>

---

## Zusammenfassung: Top 10 Klausurmuster

---

**Aussage:** Das Muster `dict.get(key, 0) + 1` ist essentiell zum Zaehlen mit Dictionaries.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Das Muster ersetzt die umstaendliche if/else-Variante:

```python
# Ohne get():
if key in d:
    d[key] += 1
else:
    d[key] = 1

# Mit get() (eleganter):
d[key] = d.get(key, 0) + 1
```

</details>

---

**Aussage:** String-Slicing `[::-1]` kehrt einen String um.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

```python
text = "Hallo"
print(text[::-1])  # "ollaH"
```

Das funktioniert auch mit Listen!

</details>

---

**Aussage:** `n % 10` gibt die letzte Ziffer einer Zahl.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

```python
n = 1234
print(n % 10)   # 4 (letzte Ziffer)
print(n // 10)  # 123 (letzte Ziffer entfernt)
```

</details>

---

**Aussage:** Bei Primzahlpruefung reicht es, bis zur Quadratwurzel zu testen.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Wenn n = a * b und a > sqrt(n), dann muss b < sqrt(n) sein.
Also findet man jeden Teiler bereits beim Pruefen bis sqrt(n).

```python
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        return False
```

</details>

---
