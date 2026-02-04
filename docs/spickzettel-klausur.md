# Python Spickzettel - Klausur PKI

## 1. Modulo-Operator (Teilbarkeit)

```python
x % y     # Rest der Division
x % 3 == 0   # x ist durch 3 teilbar
15 % 5 == 0  # True (15 teilbar durch 5)
```

## 2. FizzBuzz-Logik

```python
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)
```

## 3. try-except (Benutzereingabe)

```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Ungueltige Eingabe!")
```

## 4. Dictionary zum Zaehlen

```python
d = {}
d[key] = d.get(key, 0) + 1

# Buchstaben zaehlen:
for buchstabe in text:
    count[buchstabe] = count.get(buchstabe, 0) + 1
```

## 5. String-Methoden

```python
s.lower()           # kleinbuchstaben
s.upper()           # GROSSBUCHSTABEN
s.replace("a", "b") # ersetzen
s.split()           # in Liste aufteilen
s.strip()           # Leerzeichen entfernen
```

## 6. Umlaute ersetzen

```python
text = text.lower()
text = text.replace("ä", "ae")
text = text.replace("ö", "oe")
text = text.replace("ü", "ue")
text = text.replace("ß", "ss")
```

## 7. Listen

```python
liste.append(x)     # am Ende hinzufuegen
liste.pop()         # letztes entfernen
liste.sort()        # sortieren
liste[1:3]          # slicing (Index 1, 2)
```

## 8. Schleifen

```python
for i in range(5):      # 0, 1, 2, 3, 4
for i in range(1, 6):   # 1, 2, 3, 4, 5
for item in liste:      # ueber Liste
for k, v in d.items():  # ueber Dictionary
```

## 9. Funktionen

```python
def name(param):
    return ergebnis
```

## 10. Wichtige Typen

```python
type(42)     # <class 'int'>
type(3.14)   # <class 'float'>
type("abc")  # <class 'str'>
type([1,2])  # <class 'list'>
type({"a":1})# <class 'dict'>
```

---

## ACHTUNG - Typische Fallen!

1. **range(3)** → 0, 1, 2 (nicht bis 3!)

2. **for-Schleife überschreibt Variable:**
   ```python
   i = 27
   for i in range(3):  # i wird 0,1,2
       pass
   # i ist 2, nicht 27!
   ```

3. **Strings sind unveränderlich:**
   ```python
   s.upper()      # gibt neuen String zurück
   s = s.upper()  # speichern nicht vergessen!
   ```

4. **dict[key] vs dict.get(key):**
   ```python
   d["x"]        # KeyError wenn nicht vorhanden
   d.get("x", 0) # gibt 0 zurück (kein Fehler)
   ```
