# py-euclid 📐

Eine professionelle, objektorientierte Geometrie-Bibliothek für Python.
Entwickelt mit Fokus auf saubere Architektur (OOP), Unveränderlichkeit (Immutability) und mathematische Präzision.

> **Status:** v0.5.0 (Stable)

## ✨ Features

- **Pure Python:** Keine externen Abhängigkeiten (Zero Dependencies).
- **Objektorientiertes Design:** Logische Vererbungshierarchien (z.B. `Viereck -> Trapez -> Parallelogramm -> Rechteck -> Quadrat`).
- **Type Safety:** Durchgängige Nutzung von Type Hints und Dataclasses.
- **Robust:** Unveränderliche primitive Datentypen (`frozen=True`) verhindern Seiteneffekte.
- **Mathematische Präzision:**
    - Flächenberechnung beliebiger Polygone mittels **Gaußscher Trapezformel** (Shoelace Formula).
    - Umfangsberechnung von Ellipsen mittels **Ramanujan-Näherung**.

## 🛠 Installation

Das Projekt ist als installierbares Python-Paket konfiguriert (`pyproject.toml`).

```bash
# 1. Repository klonen
git clone [https://github.com/oliver-devs/py-euclid.git](https://github.com/oliver-devs/py-euclid.git)

# 2. In das Verzeichnis wechseln
cd py-euclid

# 3. Paket installieren (im Editable-Mode)
pip install -e .
```
