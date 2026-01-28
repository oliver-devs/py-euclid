from typing import List
from ..basis.form import Form
from ..primitive.elemente import Punkt


class Polygon(Form):
    """
    Allgemeine Klasse für n-Ecke (Dreiecke, Vierecke, Fünfecke...).
    """

    def __init__(self, eckpunkte: List[Punkt]):
        self.eckpunkte = eckpunkte

    @property
    def umfang(self) -> float:
        u = 0.0
        n = len(self.eckpunkte)
        for i in range(n):
            # Abstand vom aktuellen Punkt zum nächsten (Modulo n verbindet den letzten mit dem ersten)
            u += Punkt.distanz(self.eckpunkte[i], self.eckpunkte[(i + 1) % n])
        return u

    @property
    def flaeche(self) -> float:
        """Berechnet die Fläche mit der Gaußschen Trapezformel (Shoelace Formula)."""
        summe = 0.0
        n = len(self.eckpunkte)
        for i in range(n):
            p1 = self.eckpunkte[i]
            p2 = self.eckpunkte[(i + 1) % n]
            # (x1 * y2) - (x2 * y1)
            summe += (p1.x * p2.y) - (p2.x * p1.y)
        return abs(summe) / 2.0
