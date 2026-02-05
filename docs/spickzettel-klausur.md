# Python Spickzettel - Klausur PKI (A4)

## 1. dict.get() Zaehlmuster (30 Punkte!)
```python
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
# get(key, 0) gibt 0 zurueck wenn key nicht existiert
```

## 2. try-except bei input
```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Ungueltige Eingabe!")
```

## 3. for-Schleife mit range() - KLAUSURFALLE!
```python
i = 27
j = 27
for i in range(3):  # i wird 0, 1, 2 - UEBERSCHRIEBEN!
    j += 1
print(i, j)  # Ausgabe: 2 30  (i ist 2, NICHT 27!)
```

## 4. FizzBuzz (Modulo)
```python
for x in range(1, 101):
    if x % 15 == 0:      # oder: x % 3 == 0 and x % 5 == 0
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
```

## 5. String-Methoden
```python
s = s.lower()              # kleinbuchstaben - SPEICHERN!
s = s.replace("alt", "neu") # ersetzen
s.split()                  # "a b" -> ['a', 'b']
s.strip()                  # Leerzeichen entfernen
" ".join(liste)            # ['a','b'] -> "a b"
```

## 6. Umlaute ersetzen (15 Punkte!)
```python
text = text.lower()
text = text.replace("ä", "ae").replace("ö", "oe")
text = text.replace("ü", "ue").replace("ß", "ss")
```

## 7. OOP: class, __init__, self, __str__
```python
class Student:
    def __init__(self, name, note):  # Konstruktor
        self.name = name             # self = aktuelles Objekt
        self.note = note

    def __str__(self):               # fuer print()
        return f"{self.name}: {self.note}"

s = Student("Anna", 1.3)
print(s.name)  # Anna
print(s)       # Anna: 1.3
```

## 8. Listen: append, pop, sort
```python
liste = [3, 1, 2]
liste.append(4)      # [3, 1, 2, 4] - am Ende
liste.pop()          # gibt 4 zurueck, entfernt es
liste.sort()         # [1, 2, 3] - sortiert
liste[1:3]           # [1, 2] - slicing (Index 1, 2)
```

## 9. Dateien: with open()
```python
# Lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()      # alles lesen
    # oder: for zeile in f:  # zeilenweise

# Schreiben
with open("datei.txt", "w") as f:   # w=ueberschreiben, a=anhaengen
    f.write("Text\n")
```

## 10. Wichtige Typen und range()
```python
range(5)      # 0, 1, 2, 3, 4 (NICHT 5!)
range(1, 6)   # 1, 2, 3, 4, 5
for k, v in d.items():  # ueber Dictionary
```

---

## FALLEN - AUSWENDIG LERNEN!

| Falle | Falsch | Richtig |
|-------|--------|---------|
| range(3) | 0,1,2,3 | 0,1,2 |
| for i ueberschreibt | i bleibt | i = letzter Wert |
| s.upper() | aendert s | s = s.upper() |
| d["x"] wenn fehlt | gibt None | KeyError! |
| d.get("x", 0) | KeyError | gibt 0 |
