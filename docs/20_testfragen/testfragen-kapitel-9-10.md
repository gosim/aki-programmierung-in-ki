# Testfragen Kapitel 9-10: Dictionaries und Tupel

## KLAUSURRELEVANT: dict.get() zum Zaehlen!

---

## Kapitel 9: Dictionaries

---

**Aussage:** `dict.get(key, 0)` gibt 0 zurueck, wenn key nicht existiert.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

`get(key, default)` gibt den Wert fuer `key` zurueck, oder `default` wenn der Key nicht existiert.
Das ist besonders nuetzlich zum Zaehlen!
</details>

---

**Aussage:** Dictionary-Keys muessen einzigartig sein.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Jeder Key darf nur einmal vorkommen. Wenn man einen Key erneut zuweist, wird der alte Wert ueberschrieben.

```python
d = {"a": 1}
d["a"] = 2  # Key "a" wird ueberschrieben
print(d)  # {"a": 2}
```
</details>

---

**Aussage:** Dictionary-Keys koennen Listen sein.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

Keys muessen "hashable" sein (unveraenderlich). Listen sind veraenderlich und koennen daher nicht als Keys verwendet werden.

Erlaubte Key-Typen: int, float, str, tuple
Nicht erlaubt: list, dict
</details>

---

### Frage 9.1: KLAUSURAUFGABE - Dictionary zum Zaehlen!

**Was ist die Ausgabe?**

```python
count = {}
words = ["a", "b", "c"]
for w in words:
    count[w] = count.get(w, 0) + 1
print(count)
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe:** `{'a': 1, 'b': 1, 'c': 1}`

**Schritt-fuer-Schritt:**

1. `count = {}` - Leeres Dictionary
2. Fuer "a": `count.get("a", 0)` gibt 0 (nicht vorhanden), dann 0+1=1
   - `count = {"a": 1}`
3. Fuer "b": `count.get("b", 0)` gibt 0 (nicht vorhanden), dann 0+1=1
   - `count = {"a": 1, "b": 1}`
4. Fuer "c": `count.get("c", 0)` gibt 0 (nicht vorhanden), dann 0+1=1
   - `count = {"a": 1, "b": 1, "c": 1}`

**Dies war eine echte Klausuraufgabe!**
</details>

---

### Frage 9.3: Erklaerung dict.get() (KLAUSURFRAGE!)

**Erklaeren Sie, was `count.get(w, 0) + 1` macht.**

<details>
<summary>Loesung anzeigen</summary>

**Erklaerung:**

`count.get(w, 0) + 1` besteht aus zwei Teilen:

**1. `count.get(w, 0)`:**
- Sucht den Schluessel `w` im Dictionary `count`
- Wenn `w` existiert: gibt seinen aktuellen Wert zurueck
- Wenn `w` NICHT existiert: gibt den Standardwert 0 zurueck

**2. `+ 1`:**
- Erhoeht den Wert um 1

**3. `count[w] = ...`:**
- Speichert das Ergebnis zurueck im Dictionary

**Warum ist das nuetzlich?**
Ohne `get()` muesste man pruefen, ob der Key existiert:
```python
# Umstaendlich:
if w in count:
    count[w] = count[w] + 1
else:
    count[w] = 1

# Elegant mit get():
count[w] = count.get(w, 0) + 1
```
</details>

---

**Frage 9.4:** Was ist die Ausgabe?

```python
d = {"a": 1, "b": 2}
print(d["c"])
```

- [ ] a) None
- [ ] b) 0
- [ ] c) KeyError
- [ ] d) ""

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Ein **KeyError** tritt auf, wenn man mit `d[key]` auf einen nicht existierenden Key zugreift.

**Loesung:** Benutze `get()`:
```python
print(d.get("c", 0))  # Gibt 0 zurueck (kein Fehler)
```
</details>

---

**Frage 9.5:** Was ist die Ausgabe?

```python
d = {"a": 1, "b": 2}
print(d.get("c", "nicht gefunden"))
```

- [ ] a) None
- [ ] b) KeyError
- [ ] c) "nicht gefunden"
- [ ] d) 0

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

`get(key, default)` gibt den Standardwert zurueck, wenn der Key nicht existiert.
</details>

---

**Frage 9.6:** Wie iteriert man ueber alle Key-Value-Paare eines Dictionarys?

<details>
<summary>Loesung anzeigen</summary>

```python
d = {"a": 1, "b": 2, "c": 3}

# Ueber Keys und Values:
for key, value in d.items():
    print(f"{key}: {value}")

# Nur ueber Keys:
for key in d.keys():
    print(key)

# Nur ueber Values:
for value in d.values():
    print(value)
```

**Ausgabe von items():**
```
a: 1
b: 2
c: 3
```
</details>

---

**Frage 9.7:** Wie erstellt man ein Dictionary aus zwei Listen?

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
```

<details>
<summary>Loesung anzeigen</summary>

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]

# Mit zip() und dict():
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Oder mit Schleife:
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
```
</details>

---

**Frage 9.8:** Was ist die Ausgabe?

```python
d = {}
d["x"] = d.get("x", 0) + 1
d["x"] = d.get("x", 0) + 1
d["x"] = d.get("x", 0) + 1
print(d["x"])
```

- [ ] a) 0
- [ ] b) 1
- [ ] c) 3
- [ ] d) KeyError

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Dreimal wird "x" um 1 erhoeht:
1. `d["x"] = 0 + 1` → d["x"] = 1
2. `d["x"] = 1 + 1` → d["x"] = 2
3. `d["x"] = 2 + 1` → d["x"] = 3
</details>

---

## Kapitel 10: Tupel

---

**Aussage:** Tupel sind unveraenderlich (immutable).

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Nach der Erstellung kann man Tupel nicht mehr aendern. Im Gegensatz zu Listen kann man keine Elemente hinzufuegen, entfernen oder aendern.
</details>

---

**Aussage:** Tupel werden mit eckigen Klammern erstellt.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** NEIN

- Tupel: runde Klammern `()` oder ohne Klammern: `t = 1, 2, 3`
- Listen: eckige Klammern `[]`
</details>

---

**Aussage:** Tupel koennen als Dictionary-Keys verwendet werden.

<details>
<summary>Loesung anzeigen</summary>

**Antwort:** JA

Da Tupel unveraenderlich (immutable) und damit hashable sind, koennen sie als Dictionary-Keys verwendet werden.

```python
d = {}
d[(1, 2)] = "Punkt"  # Tupel als Key - funktioniert!
d[[1, 2]] = "Punkt"  # Liste als Key - TypeError!
```
</details>

---

**Frage 10.1:** Was ist der Unterschied zwischen Liste und Tupel?

- [ ] a) Listen sind schneller
- [ ] b) Tupel koennen mehr Elemente haben
- [ ] c) Listen sind veraenderbar, Tupel nicht
- [ ] d) Tupel koennen nur Zahlen enthalten

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Der Hauptunterschied:
- **Listen sind mutable** (veraenderbar): `append()`, `remove()`, `pop()` etc.
- **Tupel sind immutable** (unveraenderbar): keine Aenderungen nach Erstellung

Wann Tupel verwenden?
- Fuer unveraenderliche Daten (z.B. Koordinaten)
- Als Dictionary-Keys
- Fuer Rueckgabewerte von Funktionen
</details>

---

**Frage 10.2:** Wie erstellt man ein Tupel mit einem Element?

- [ ] a) `t = (1)`
- [ ] b) `t = (1,)`
- [ ] c) `t = [1]`
- [ ] d) `t = 1,`

<details>
<summary>Loesung anzeigen</summary>

**Richtig: b) und d)**

Fuer ein Tupel mit einem Element braucht man ein Komma:
- `(1)` ist nur die Zahl 1 (Klammern fuer Gruppierung)
- `(1,)` ist ein Tupel mit einem Element
- `1,` ist auch ein Tupel mit einem Element

```python
print(type((1)))   # <class 'int'>
print(type((1,)))  # <class 'tuple'>
```
</details>

---

**Frage 10.3:** Was ist die Ausgabe?

```python
t = (1, 2, 3)
print(t[0])
t[0] = 5
```

<details>
<summary>Loesung anzeigen</summary>

**Ausgabe:**
```
1
TypeError: 'tuple' object does not support item assignment
```

Man kann auf Tupel-Elemente zugreifen (`t[0]`), aber sie nicht aendern.
</details>

---

**Frage 10.4:** Tuple Unpacking - Was ist die Ausgabe?

```python
t = (1, 2, 3)
a, b, c = t
print(b)
```

- [ ] a) (1, 2, 3)
- [ ] b) 1
- [ ] c) 2
- [ ] d) Fehler

<details>
<summary>Loesung anzeigen</summary>

**Richtig: c)**

Tuple Unpacking weist jedes Element einer Variablen zu:
- a = 1
- b = 2
- c = 3

Das funktioniert auch mit Listen und in for-Schleifen:
```python
for key, value in d.items():
    print(key, value)
```
</details>

---

**Frage 10.5:** Wie vertauscht man zwei Variablen in Python?

<details>
<summary>Loesung anzeigen</summary>

```python
a = 5
b = 10

# Pythonischer Weg (mit Tuple Unpacking):
a, b = b, a

print(a)  # 10
print(b)  # 5
```

In anderen Sprachen braeuchte man eine temporaere Variable:
```python
temp = a
a = b
b = temp
```

Python macht das elegant mit Tupeln!
</details>

---
