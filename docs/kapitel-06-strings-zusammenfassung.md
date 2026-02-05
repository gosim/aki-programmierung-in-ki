# Kapitel 6: Zeichenketten (Strings)

## Grundlegendes zu Strings

Strings (Zeichenketten) sind eine der wichtigsten Datentypen in Python. Sie werden verwendet, um Text zu speichern und zu verarbeiten.

### Strings sind unveränderlich (immutable)!

**KLAUSURRELEVANT:** Strings können nach ihrer Erstellung nicht mehr verändert werden. Jede "Änderung" erzeugt einen neuen String!

```python
text = "Hallo"
text[0] = "M"  # FEHLER! TypeError: 'str' object does not support item assignment

# Stattdessen: Neuen String erzeugen
text = "M" + text[1:]  # "Mallo"
```

---

## Indizierung und Slicing

### Indizierung (Einzelne Zeichen)

Strings sind indiziert, wobei der Index bei **0** beginnt. Negative Indizes zählen vom Ende.

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5   (positive Indizes)
#   -6 -5 -4 -3 -2 -1   (negative Indizes)

print(s[0])    # 'P' - erstes Zeichen
print(s[1])    # 'y' - zweites Zeichen
print(s[-1])   # 'n' - letztes Zeichen
print(s[-2])   # 'o' - vorletztes Zeichen
```

### Slicing (Teilstrings)

Mit Slicing kann man Teilstrings extrahieren: `s[start:ende:schritt]`

```python
s = "Python"

print(s[1:4])   # 'yth' - von Index 1 bis 3 (ende ist exklusiv!)
print(s[:3])    # 'Pyt' - von Anfang bis Index 2
print(s[2:])    # 'thon' - von Index 2 bis Ende
print(s[::2])   # 'Pto' - jedes zweite Zeichen
print(s[::-1])  # 'nohtyP' - String umkehren!
```

**Wichtig:** Der End-Index ist immer **exklusiv** (nicht enthalten)!

---

## String-Methoden

### Groß-/Kleinschreibung

```python
text = "Hallo Welt"

print(text.lower())      # 'hallo welt' - alles klein
print(text.upper())      # 'HALLO WELT' - alles groß
print(text.capitalize()) # 'Hallo welt' - Erster Buchstabe groß
print(text.title())      # 'Hallo Welt' - Jedes Wort groß
```

### Ersetzen mit replace()

```python
text = "Hallo Welt"
neu = text.replace("Welt", "Python")
print(neu)  # 'Hallo Python'

# Mehrfaches Ersetzen
text = "aaa"
print(text.replace("a", "b"))     # 'bbb' - alle ersetzen
print(text.replace("a", "b", 2))  # 'bba' - nur 2 ersetzen
```

### Aufteilen mit split()

```python
text = "Hallo Welt Python"
woerter = text.split()      # Trennt bei Leerzeichen
print(woerter)              # ['Hallo', 'Welt', 'Python']

csv = "rot,grün,blau"
farben = csv.split(",")     # Trennt bei Komma
print(farben)               # ['rot', 'grün', 'blau']
```

### Leerzeichen entfernen mit strip()

```python
text = "   Hallo Welt   "
print(text.strip())   # 'Hallo Welt' - beide Seiten
print(text.lstrip())  # 'Hallo Welt   ' - nur links
print(text.rstrip())  # '   Hallo Welt' - nur rechts
```

### Suchen mit find()

```python
text = "Hallo Welt"
print(text.find("Welt"))    # 6 - Index wo 'Welt' beginnt
print(text.find("Python"))  # -1 - nicht gefunden!
print(text.find("l"))       # 2 - erstes Vorkommen
```

### Zählen mit count()

```python
text = "Mississippi"
print(text.count("s"))   # 4
print(text.count("ss"))  # 2
print(text.count("i"))   # 4
```

---

## String-Konkatenation und Wiederholung

### Konkatenation mit +

```python
vorname = "Max"
nachname = "Mustermann"
name = vorname + " " + nachname
print(name)  # 'Max Mustermann'
```

### Wiederholung mit *

```python
linie = "-" * 20
print(linie)  # '--------------------'

echo = "Ha" * 3
print(echo)   # 'HaHaHa'
```

---

## f-Strings für Formatierung

f-Strings (formatted string literals) sind die moderne Art, Variablen in Strings einzufügen.

```python
name = "Anna"
alter = 25

# f-String mit Variablen
print(f"Ich heiße {name} und bin {alter} Jahre alt.")
# Ausgabe: Ich heiße Anna und bin 25 Jahre alt.

# Berechnungen im f-String
print(f"In 10 Jahren bin ich {alter + 10}.")
# Ausgabe: In 10 Jahren bin ich 35.

# Formatierung von Zahlen
preis = 19.99
print(f"Der Preis beträgt {preis:.2f} Euro.")
# Ausgabe: Der Preis beträgt 19.99 Euro.

pi = 3.14159265
print(f"Pi ist ungefähr {pi:.3f}")
# Ausgabe: Pi ist ungefähr 3.142
```

---

## Umlaute ersetzen (KLAUSURAUFGABE!)

**WICHTIG FÜR DIE KLAUSUR:** Häufige Aufgabe ist das Ersetzen von Umlauten!

```python
def umlaute_ersetzen(text):
    """Ersetzt deutsche Umlaute durch ae, oe, ue, ss"""
    text = text.lower()
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")
    return text

# Beispiel
original = "Größe"
ersetzt = umlaute_ersetzen(original)
print(ersetzt)  # 'groesse'
```

**Vollständige Version mit Groß- und Kleinbuchstaben:**

```python
def umlaute_ersetzen(text):
    """Ersetzt alle deutschen Umlaute"""
    ersetzungen = [
        ("ä", "ae"), ("Ä", "Ae"),
        ("ö", "oe"), ("Ö", "Oe"),
        ("ü", "ue"), ("Ü", "Ue"),
        ("ß", "ss")
    ]
    for alt, neu in ersetzungen:
        text = text.replace(alt, neu)
    return text

print(umlaute_ersetzen("Übung macht den Meister"))
# Ausgabe: 'Uebung macht den Meister'
```

---

## Der in-Operator für Teilstrings

Mit `in` prüft man, ob ein Teilstring in einem String enthalten ist.

```python
text = "Hallo Welt"

print("Welt" in text)     # True
print("welt" in text)     # False (Groß-/Kleinschreibung!)
print("Python" in text)   # False

# Oft in if-Bedingungen verwendet
if "Hallo" in text:
    print("Begrüßung gefunden!")

# Negation mit not in
if "Python" not in text:
    print("Python kommt nicht vor")
```

---

## Die len()-Funktion für Länge

```python
text = "Hallo"
print(len(text))  # 5

# Auch Leerzeichen werden gezählt!
text2 = "Hallo Welt"
print(len(text2))  # 10

# Leerer String
print(len(""))  # 0
```

---

## Zusammenfassung der wichtigsten Punkte

| Konzept | Syntax | Beispiel |
|---------|--------|----------|
| Indizierung | `s[i]` | `s[0]`, `s[-1]` |
| Slicing | `s[start:ende:schritt]` | `s[1:4]`, `s[::-1]` |
| Länge | `len(s)` | `len("Hallo")` → 5 |
| Konkatenation | `s1 + s2` | `"Hallo" + " Welt"` |
| Wiederholung | `s * n` | `"-" * 10` |
| Enthält | `x in s` | `"a" in "Hallo"` → True |
| Kleinbuchstaben | `s.lower()` | `"ABC".lower()` → "abc" |
| Großbuchstaben | `s.upper()` | `"abc".upper()` → "ABC" |
| Ersetzen | `s.replace(alt, neu)` | `"Hallo".replace("a", "e")` |
| Aufteilen | `s.split(trenner)` | `"a,b,c".split(",")` |
| Leerzeichen entf. | `s.strip()` | `"  Hi  ".strip()` |
| Suchen | `s.find(x)` | `"Hallo".find("l")` → 2 |
| Zählen | `s.count(x)` | `"Hallo".count("l")` → 2 |
| f-String | `f"...{var}..."` | `f"Wert: {x}"` |

---

## Typische Klausuraufgaben

1. **String umkehren:** `s[::-1]`
2. **Umlaute ersetzen:** `text.replace("ä", "ae")`
3. **Wörter zählen:** `len(text.split())`
4. **Vokale zählen:** Schleife mit `in`-Operator
5. **Teilstring prüfen:** `"suchbegriff" in text`
