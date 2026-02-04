# Python Lernplan - Klausur 07.02.2026

## Klausurstruktur (60 Punkte, 1 Stunde)

| Aufgabe | Punkte | Thema |
|---------|--------|-------|
| 1 | 30 | Code-Verstaendnis |
| 2 | 15 | FizzBuzz (Modulo) |
| 3 | 15 | Textverarbeitung |

---

## Prioritaet A: MUSS sitzen!

### 1. dict.get() zum Zaehlen
```python
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

### 2. try-except bei Eingabe
```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Fehler!")
```

### 3. for-Schleife mit range()
```python
for i in range(3):  # 0, 1, 2
    print(i)
# ACHTUNG: i hat danach den Wert 2!
```

### 4. Modulo fuer Teilbarkeit
```python
if x % 3 == 0:  # x ist durch 3 teilbar
```

### 5. String-Methoden
```python
text = text.lower()
text = text.replace("ä", "ae")
```

---

## Kapitel-Uebersicht

### Kap 1-2: Grundlagen
- Variablen, Datentypen (int, float, str)
- Operatoren: +, -, *, /, //, %
- input(), print(), type()

### Kap 3: Bedingte Ausfuehrung
- if / elif / else
- try / except (ValueError!)
- and, or, not

### Kap 4: Funktionen
- def, return, Parameter
- Lokale vs. globale Variablen

### Kap 5: Iteration
- for-Schleife, range()
- while-Schleife
- break, continue

### Kap 6: Zeichenketten
- Unveraenderlich (immutable)
- lower(), upper(), replace()
- split(), find(), count()

### Kap 7: Dateien
- open(), read(), write()
- with-Statement
- Modi: "r", "w", "a"

### Kap 8: Listen
- Veraenderbar (mutable)
- append(), pop(), sort()
- Slicing: liste[1:3]

### Kap 9: Dictionaries
- Key-Value-Paare
- get(key, default)
- keys(), values(), items()

### Kap 10: Tupel
- Unveraenderlich
- Runde Klammern: (1, 2, 3)

### Kap 14: OOP
- class, __init__, self
- Instanz vs. Klasse

---

## Lernplan (4 Tage)

### Tag 1: Kernkonzepte
- [ ] Modulo und FizzBuzz ueben
- [ ] dict.get() zum Zaehlen

### Tag 2: Textverarbeitung
- [ ] String-Methoden (lower, replace)
- [ ] try-except bei input

### Tag 3: Code-Verstaendnis
- [ ] for-Schleifen mit range()
- [ ] Quiz durcharbeiten

### Tag 4: Wiederholung
- [ ] Spickzettel vorbereiten
- [ ] Probeklausur unter Zeitdruck

---

## Wichtige Erkenntnisse aus Gedaechtnisprotokollen

1. **Zeit ist knapp** - kaum Zeit fuer Spickzettel
2. **Direkt anfangen** - nicht lange ueberlegen
3. **Textverarbeitung kam viel** - replace() ueben!
4. **FizzBuzz ist Standard** - muss sitzen
5. **dict.get() verstehen** - kommt garantiert
