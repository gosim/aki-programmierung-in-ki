# Loesungen-Referenz: Python for Everybody

Dieses Dokument gibt eine Uebersicht aller Loesungen aus dem Ordner `python-for-everybody-solutions-master/`.
Die Loesungen stammen aus dem Kurs "Python for Everybody" von Charles R. Severance.

**Quelle:** https://github.com/csev/py4e

---

## Klausurrelevanz-Legende

| Symbol | Bedeutung |
|--------|-----------|
| ⭐⭐⭐ | Sehr wichtig fuer Klausur |
| ⭐⭐ | Wichtig fuer Klausur |
| ⭐ | Hilfreich, aber weniger klausurrelevant |
| - | Nicht klausurrelevant (Kapitel 11-13) |

---

## Kapitel 3: Bedingte Ausfuehrung (if/elif/else)

### exercise3_1.py ⭐⭐⭐
**Thema:** Lohnberechnung mit Ueberstunden (1.5x ab 40h)

```python
pay = 0.0
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours < 40:
    pay = rate * hours
else:
    overtime = hours - 40
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print('Pay: ', pay)
```

**Wichtige Konzepte:**
- if/else Verzweigung
- Ueberstundenberechnung (haeufige Klausuraufgabe!)
- float() fuer Eingabekonvertierung

---

### exercise3_2.py ⭐⭐⭐
**Thema:** Lohnberechnung mit try/except

```python
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except ValueError:
    print('Error, please enter numeric input')
    quit()
```

**Wichtige Konzepte:**
- try/except fuer Fehlerbehandlung
- ValueError abfangen

---

### exercise3_3.py ⭐⭐
**Thema:** Erweiterte Fehlerbehandlung

---

## Kapitel 4: Funktionen

### exercise4_6.py ⭐⭐⭐
**Thema:** Funktion `computepay()` definieren

```python
def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (rate * 40) + (1.5 * rate * overtime)
    else:
        pay = hours * rate
    return pay

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
print('Pay:', computepay(hours, rate))
```

**Wichtige Konzepte:**
- Funktion mit Parametern definieren
- return-Anweisung
- Wiederverwendbarer Code

---

### exercise4_1.py ⭐
**Thema:** Random-Modul importieren

### exercise4_2.py ⭐
**Thema:** Grundlegende Schleifen

### exercise4_7.py ⭐
**Thema:** Weitere Funktionsuebungen

---

## Kapitel 5: Iteration (Schleifen)

### exercise5_1.py ⭐⭐⭐
**Thema:** While-Schleife mit "done"-Abbruch und try/except

```python
count = 0
total = 0.0

while True:
    eingabe = input('Enter a number: ')
    if eingabe == 'done':
        break
    try:
        zahl = float(eingabe)
    except ValueError:
        print('Invalid input')
        continue

    count += 1
    total = total + zahl

if count > 0:
    average = total / count
    print(total, count, average)
```

**Wichtige Konzepte:**
- while True mit break
- try/except innerhalb der Schleife
- Akkumulatoren: total, count, average
- continue zum Ueberspringen

---

### exercise5_2.py ⭐⭐
**Thema:** Min/Max berechnen

---

## Kapitel 6: Strings (Zeichenketten)

### exercise6_1.py ⭐⭐
**Thema:** String rueckwaerts durchlaufen

```python
fruit = 'banana'
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1
```

**Wichtige Konzepte:**
- String-Indizierung
- len() Funktion
- Rueckwaerts-Iteration

---

### exercise6_3.py ⭐⭐
**Thema:** String-Slicing

### exercise6_5.py ⭐⭐
**Thema:** String-Methoden (find, count)

---

## Kapitel 7: Dateien

### exercise7_1.py ⭐⭐
**Thema:** Datei lesen und in Grossbuchstaben ausgeben

```python
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()      # Zeilenumbruch entfernen
    print(line.upper())       # In Grossbuchstaben
```

**Wichtige Konzepte:**
- open() zum Oeffnen
- for-Schleife ueber Datei
- rstrip() entfernt Whitespace am Ende
- upper() wandelt in Grossbuchstaben

---

### exercise7_2.py ⭐⭐
**Thema:** Dateien mit try/except

### exercise7_3.py ⭐
**Thema:** Zeilen zaehlen

---

## Kapitel 8: Listen

### exercise8_4.py ⭐⭐⭐
**Thema:** Woerter aus Datei lesen, Duplikate filtern, sortieren

```python
my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word not in my_list:
            my_list.append(word)
print(sorted(my_list))
```

**Wichtige Konzepte:**
- split() teilt String in Liste
- Duplikatpruefung mit `in`
- append() fuegt Element hinzu
- sorted() sortiert alphabetisch

---

### exercise8_1.py ⭐⭐
**Thema:** Listen-Funktionen (chop, middle)

### exercise8_2.py ⭐⭐
**Thema:** Listen-Operationen

### exercise8_3.py ⭐
**Thema:** String zu Liste

### exercise8_5.py ⭐
**Thema:** Listen durchlaufen

### exercise8_6.py ⭐
**Thema:** Listen-Slicing

---

## Kapitel 9: Dictionaries ⭐⭐⭐ SEHR WICHTIG!

### exercise9_1.py ⭐⭐⭐
**Thema:** Woerter in Dictionary speichern

```python
dictionary_words = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word not in dictionary_words:
            dictionary_words[word] = 1

# Schnelle Pruefung mit 'in'
if 'Python' in dictionary_words:
    print('True')
```

**Wichtige Konzepte:**
- dict() erstellt Dictionary
- `in` Operator fuer schnelle Lookup

---

### exercise9_3.py ⭐⭐⭐
**Thema:** Zaehlmuster mit Dictionary

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

**DAS WICHTIGSTE MUSTER FUER DIE KLAUSUR!**

---

### exercise9_2.py ⭐⭐
**Thema:** Dictionary-Iteration

### exercise9_4.py ⭐⭐
**Thema:** Dictionary-Methoden

### exercise9_5.py ⭐⭐
**Thema:** Maximum aus Dictionary

---

## Kapitel 10: Tupel und Sortierung

### exercise10_1.py ⭐⭐⭐
**Thema:** E-Mail-Adressen zaehlen und Maximum finden

```python
dictionary_addresses = dict()
lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    if words[1] not in dictionary_addresses:
        dictionary_addresses[words[1]] = 1
    else:
        dictionary_addresses[words[1]] += 1

# Tupel-Liste fuer Sortierung
for key, val in dictionary_addresses.items():
    lst.append((val, key))

lst.sort(reverse=True)

# Maximum ausgeben
for count, email in lst[:1]:
    print(email, count)
```

**Wichtige Konzepte:**
- FileNotFoundError abfangen
- startswith() oder direkter Vergleich
- Tupel (value, key) fuer Sortierung
- sort(reverse=True) fuer absteigend
- Slicing [:1] fuer erstes Element

---

### exercise10_2.py ⭐⭐
**Thema:** Weitere Aggregationen

### exercise10_3.py ⭐⭐
**Thema:** Stunden aus Zeitstempel extrahieren

---

## Kapitel 11-13: Fortgeschrittene Themen (weniger klausurrelevant)

### Kapitel 11: Regular Expressions -
- exercise11_1.py - Grep-aehnliches Programm mit re.findall()
- exercise11_2.py - Weitere Regex-Uebungen

### Kapitel 12: Web-Requests -
- exercise12_3.py - urllib.request fuer HTTP
- exercise12_4.py - URL-Daten verarbeiten
- exercise12_5.py - Weitere Web-Requests

### Kapitel 13: APIs und JSON -
- exercise13_1.py - Geolocation API
- exercise13_2.py - JSON-Parsing

---

## Zusammenfassung: Die 5 wichtigsten Loesungen

| Rang | Datei | Thema | Warum wichtig? |
|------|-------|-------|----------------|
| 1 | exercise9_3.py | Zaehlmuster | `d[k] = d.get(k, 0) + 1` - MUSS sitzen! |
| 2 | exercise3_1.py | Lohnberechnung | Haeufige Klausuraufgabe |
| 3 | exercise5_1.py | While + done | Akkumulatoren verstehen |
| 4 | exercise10_1.py | E-Mail-Zaehlung | Kombiniert alles |
| 5 | exercise8_4.py | Liste + sort | Datei-Parsing |

---

## Dateipfade

Alle Loesungen befinden sich unter:
```
docs/python-for-everybody-solutions-master/
```

Beispiel fuer Zugriff:
```
docs/python-for-everybody-solutions-master/exercise3_1.py
docs/python-for-everybody-solutions-master/exercise5_1.py
docs/python-for-everybody-solutions-master/exercise9_3.py
docs/python-for-everybody-solutions-master/exercise10_1.py
```
