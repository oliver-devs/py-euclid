import sys
import os

# Trick, damit Python den Ordner 'geometrie' sicher findet
sys.path.append(os.getcwd())

from geometrie.primitive.elemente import Punkt
from geometrie.figuren.dreieck import GleichseitigesDreieck
from geometrie.figuren.viereck import Quadrat, Drachen, GleichschenkligesTrapez
from geometrie.figuren.ellipse import Kreis


def print_header(titel):
    print(f"\n{'-'*40}")
    print(f" {titel}")
    print(f"{'-'*40}")


def main():
    print_header("NASA GEOMETRIE DEMO v1.0")

    # 1. Ein Punkt
    p1 = Punkt(0, 0)
    p2 = Punkt(3, 4)
    dist = Punkt.distanz(p1, p2)
    print(f"📍 Abstand zwischen {p1} und {p2}: {dist} (Erwartet: 5.0)")

    # 2. Ein perfektes Dreieck
    dreieck = GleichseitigesDreieck(seitenlaenge=10)
    print_header("📐 Gleichseitiges Dreieck")
    print(f"Seitenlänge: 10")
    print(f"Umfang:      {dreieck.umfang:.2f}")
    print(f"Fläche:      {dreieck.flaeche:.2f}")

    # 3. Das Haus der Vierecke (Quadrat)
    quadrat = Quadrat(a=5)
    print_header("🟦 Quadrat")
    print(f"Seitenlänge: 5")
    print(f"Umfang:      {quadrat.umfang:.2f}")
    print(f"Fläche:      {quadrat.flaeche:.2f}")

    # 4. Der Exot (Drachen)
    drachen = Drachen(e=10, f=6, abstand_oben=3)
    print_header("🪁 Drachen")
    print(f"Diagonale e: 10, Diagonale f: 6")
    print(f"Fläche:      {drachen.flaeche:.2f} (Sollte 30.0 sein)")

    # 5. Runde Sachen (Kreis)
    kreis = Kreis(zentrum=p1, radius=10)
    print_header("🔴 Kreis")
    print(f"Radius:      10")
    print(f"Umfang:      {kreis.umfang:.2f}")
    print(f"Fläche:      {kreis.flaeche:.2f}")

    print("\n✅ Simulation erfolgreich beendet.")

    # BONUS: Symmetrisches Trapez
    sym_trapez = GleichschenkligesTrapez(a=10, c=6, h=4)
    print_header("⚖️ Gleichschenkliges Trapez")
    print(f"Unten: 10, Oben: 6, Höhe: 4")
    print(f"Fläche:      {sym_trapez.flaeche:.2f} (Sollte 32.0 sein)")


if __name__ == "__main__":
    main()
