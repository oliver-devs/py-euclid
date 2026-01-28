import math
from .polygon import Polygon
from ..primitive.elemente import Punkt


class Dreieck(Polygon):
    """Das allgemeinste aller Dreiecke (definiert durch 3 Punkte)."""

    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt):
        super().__init__([p1, p2, p3])


class RechtwinkligesDreieck(Dreieck):
    """Ein Dreieck mit einem 90° Winkel (Kathete a, Kathete b)."""

    def __init__(self, a: float, b: float):
        super().__init__(Punkt(0, 0), Punkt(a, 0), Punkt(0, b))


class GleichschenkligesDreieck(Dreieck):
    """2 Seiten sind gleich lang (Schenkel). Konstruiert über Basis und Höhe."""

    def __init__(self, basis: float, hoehe: float):
        # Wir bauen es symmetrisch um die Y-Achse
        halbe_basis = basis / 2
        super().__init__(
            Punkt(-halbe_basis, 0),  # Links
            Punkt(halbe_basis, 0),  # Rechts
            Punkt(0, hoehe),  # Spitze oben
        )


class GleichseitigesDreieck(GleichschenkligesDreieck):
    """Alle 3 Seiten sind gleich lang. Das perfekte Dreieck."""

    def __init__(self, seitenlaenge: float):
        # Berechnung der Höhe im gleichseitigen Dreieck:
        # h = a * sqrt(3) / 2
        hoehe = seitenlaenge * math.sqrt(3) / 2
        # Wir nutzen die Logik vom gleichschenkligen Dreieck
        super().__init__(seitenlaenge, hoehe)
