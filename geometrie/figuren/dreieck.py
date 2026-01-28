from .polygon import Polygon
from ..primitive.elemente import Punkt


class Dreieck(Polygon):
    """Das allgemeinste aller Dreiecke (definiert durch 3 Punkte)."""

    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt):
        super().__init__([p1, p2, p3])


class RechtwinkligesDreieck(Dreieck):
    """
    Ein Dreieck mit einem 90° Winkel.
    Wir definieren es einfach über die zwei Katheten a und b.
    """

    def __init__(self, a: float, b: float):
        # Wir setzen es in den Ursprung (0,0) für einfache Berechnung
        p1 = Punkt(0, 0)
        p2 = Punkt(a, 0)
        p3 = Punkt(0, b)
        super().__init__(p1, p2, p3)
