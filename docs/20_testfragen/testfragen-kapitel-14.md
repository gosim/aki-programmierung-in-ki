# Testfragen Kapitel 14: Objektorientierte Programmierung

---

**Aussage:** `self` bezieht sich auf die aktuelle Instanz einer Klasse.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`self` ist eine Referenz auf das aktuelle Objekt. Es wird automatisch uebergeben, wenn eine Methode aufgerufen wird.

```python
class Person:
    def setze_name(self, name):
        self.name = name  # self.name gehoert zur Instanz

p = Person()
p.setze_name("Max")  # self wird automatisch zu p
print(p.name)  # "Max"
```
</details>

---

**Aussage:** `__init__` ist der Konstruktor einer Klasse.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`__init__` wird automatisch aufgerufen, wenn ein neues Objekt erstellt wird. Hier initialisiert man die Attribute.

```python
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

p = Person("Max", 25)  # __init__ wird aufgerufen
```
</details>

---

**Aussage:** Eine Kindklasse erbt alle Methoden der Elternklasse.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Vererbung ermoeglicht es, Code wiederzuverwenden. Die Kindklasse erbt alle Attribute und Methoden.

```python
class Tier:
    def atmen(self):
        print("Atmet")

class Hund(Tier):  # Hund erbt von Tier
    def bellen(self):
        print("Wuff!")

h = Hund()
h.atmen()  # Geerbte Methode
h.bellen()  # Eigene Methode
```
</details>

---

**Aussage:** Attribute ohne `self.` sind Klassenattribute.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** Teilweise korrekt

- `self.attribut` = Instanzattribut (gehoert zum Objekt)
- Ohne `self` im Klassenkoerper = Klassenattribut (gehoert zur Klasse)

```python
class Zaehler:
    anzahl = 0  # Klassenattribut

    def __init__(self):
        self.wert = 0  # Instanzattribut
        Zaehler.anzahl += 1
```
</details>

---

**Frage 14.1:** Was macht `__init__`?

- [ ] a) Loescht ein Objekt
- [ ] b) Initialisiert ein neues Objekt
- [ ] c) Kopiert ein Objekt
- [ ] d) Vergleicht Objekte

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b)**

`__init__` ist der Konstruktor (Initialisierer). Er wird automatisch aufgerufen, wenn man ein neues Objekt mit `Klasse()` erstellt.
</details>

---

**Frage 14.2:** Was ist die Ausgabe?

```python
class Hund:
    def __init__(self, name):
        self.name = name

    def bellen(self):
        print(f"{self.name} sagt Wuff!")

h = Hund("Bello")
h.bellen()
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe:**
```
Bello sagt Wuff!
```

**Erklaerung:**
1. `Hund("Bello")` ruft `__init__` auf mit name="Bello"
2. `self.name = "Bello"` speichert den Namen im Objekt
3. `h.bellen()` ruft die Methode auf, die `self.name` verwendet
</details>

---

### Frage 14.3: Klasse erstellen

**Erstellen Sie eine einfache Klasse `Person` mit Attributen `name` und `alter`.**

<details>
<summary>Loesung anzeigen</summary>

```python
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def vorstellen(self):
        print(f"Ich bin {self.name} und {self.alter} Jahre alt.")

# Verwendung:
p = Person("Max", 25)
p.vorstellen()  # "Ich bin Max und 25 Jahre alt."

# Auf Attribute zugreifen:
print(p.name)   # "Max"
print(p.alter)  # 25
```
</details>

---

**Frage 14.4:** Was ist der Unterschied zwischen Klasse und Objekt?

<details>
<summary>Loesung anzeigen</summary>

**Klasse:**
- Die "Bauanleitung" oder der "Bauplan"
- Definiert Attribute und Methoden
- Es gibt nur eine Definition

**Objekt (Instanz):**
- Ein konkretes Exemplar nach dem Bauplan
- Hat eigene Werte fuer die Attribute
- Es kann viele Objekte geben

**Analogie:**
- Klasse = Backrezept
- Objekt = Ein konkreter Kuchen nach dem Rezept

```python
class Auto:  # Klasse (Bauplan)
    pass

auto1 = Auto()  # Objekt 1
auto2 = Auto()  # Objekt 2 (separate Instanz)
```
</details>

---

**Frage 14.5:** Was ist die Ausgabe?

```python
class Zaehler:
    def __init__(self):
        self.stand = 0

    def erhoehen(self):
        self.stand += 1

z1 = Zaehler()
z2 = Zaehler()
z1.erhoehen()
z1.erhoehen()
z2.erhoehen()
print(z1.stand, z2.stand)
```

- [ ] a) 2 2
- [ ] b) 3 3
- [ ] c) 2 1
- [ ] d) 3 0

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`z1` und `z2` sind separate Objekte mit eigenen Attributen.
- z1.erhoehen() zweimal → z1.stand = 2
- z2.erhoehen() einmal → z2.stand = 1
</details>

---

**Frage 14.6:** Wie funktioniert Vererbung?

<details>
<summary>Loesung anzeigen</summary>

```python
class Tier:  # Elternklasse (Basisklasse)
    def __init__(self, name):
        self.name = name

    def atmen(self):
        print(f"{self.name} atmet")

class Hund(Tier):  # Kindklasse (erbt von Tier)
    def bellen(self):
        print(f"{self.name} bellt: Wuff!")

class Katze(Tier):  # Andere Kindklasse
    def miauen(self):
        print(f"{self.name} miaut: Miau!")

# Verwendung:
h = Hund("Bello")
h.atmen()   # Geerbte Methode
h.bellen()  # Eigene Methode

k = Katze("Minka")
k.atmen()   # Geerbte Methode
k.miauen()  # Eigene Methode
```

**Vorteile:**
- Code-Wiederverwendung
- Hierarchie und Spezialisierung
</details>

---

**Frage 14.7:** Was ist `super()`?

<details>
<summary>Loesung anzeigen</summary>

`super()` ermoeglicht den Zugriff auf Methoden der Elternklasse.

```python
class Tier:
    def __init__(self, name):
        self.name = name

class Hund(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)  # Ruft Tier.__init__ auf
        self.rasse = rasse

h = Hund("Bello", "Labrador")
print(h.name)   # "Bello"
print(h.rasse)  # "Labrador"
```
</details>

---

**Frage 14.8:** Warum muss `self` der erste Parameter sein?

<details>
<summary>Loesung anzeigen</summary>

`self` ist eine Konvention (kein Schluesselwort), aber **muss** der erste Parameter jeder Instanzmethode sein.

Python uebergibt automatisch das Objekt als erstes Argument:

```python
class Beispiel:
    def methode(self, x):
        print(self, x)

obj = Beispiel()
obj.methode(5)  # Wird zu: Beispiel.methode(obj, 5)
```

Ohne `self` wuerde man nicht auf die Attribute des Objekts zugreifen koennen.
</details>

---

### Frage 14.9: Rechteck-Klasse

**Erstellen Sie eine Klasse `Rechteck` mit Breite und Hoehe, die eine Methode `flaeche()` hat.**

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

# Verwendung:
r = Rechteck(5, 3)
print(f"Flaeche: {r.flaeche()}")    # 15
print(f"Umfang: {r.umfang()}")      # 16
```
</details>

---

**Frage 14.10:** Was sind "magische Methoden" (Dunder-Methoden)?

<details>
<summary>Loesung anzeigen</summary>

Methoden mit doppelten Unterstrichen (`__name__`) haben spezielle Bedeutung:

| Methode | Beschreibung | Beispiel-Aufruf |
|---------|--------------|-----------------|
| `__init__` | Konstruktor | `Klasse()` |
| `__str__` | String-Darstellung | `print(obj)` |
| `__len__` | Laenge | `len(obj)` |
| `__add__` | Addition | `obj1 + obj2` |
| `__eq__` | Gleichheit | `obj1 == obj2` |

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

p = Punkt(3, 4)
print(p)  # "Punkt(3, 4)" statt "<Punkt object at 0x...>"
```
</details>

---
