from .polygon import Polygon
from ..primitive.elemente import Punkt


# --- Ebene 0: Das allgemeine Viereck ---
class Viereck(Polygon):
    """
    Ein beliebiges Viereck, definiert durch 4 Punkte.
    """

    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt, p4: Punkt):
        super().__init__([p1, p2, p3, p4])


# --- Ebene 1: Das Trapez ---
class Trapez(Viereck):
    """
    Ein Viereck mit mindestens zwei parallelen Seiten (a und c).
    Definiert durch:
    - a: Länge der Basis unten
    - c: Länge der Basis oben
    - h: Höhe
    - verschiebung: Wie weit die obere Seite nach rechts verschoben ist (für Schräge)
    """

    def __init__(self, a: float, c: float, h: float, verschiebung: float = 0):
        # Wir konstruieren die 4 Punkte:
        # Unten links (0,0) bis unten rechts (a,0)
        # Oben fängt es bei (verschiebung, h) an und geht bis (c + verschiebung, h)

        p1 = Punkt(0, 0)
        p2 = Punkt(a, 0)
        p3 = Punkt(c + verschiebung, h)
        p4 = Punkt(verschiebung, h)

        super().__init__(p1, p2, p3, p4)

        # Speichern für direkten Zugriff (optional)
        self.basis_a = a
        self.basis_c = c
        self.hoehe = h

    @property
    def flaeche(self) -> float:
        """
        Optimierung: Statt der komplexen Gauß-Formel nehmen wir
        hier die einfache Trapez-Formel: (a + c) / 2 * h
        """
        return (self.basis_a + self.basis_c) / 2 * self.hoehe
