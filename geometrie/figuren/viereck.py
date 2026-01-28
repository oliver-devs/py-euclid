import math
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


# --- Ebene 1 (Symmetrie): Das Drachen ---
class Drachen(Viereck):
    """
    Ein Viereck, bei dem eine Diagonale Symmetrieachse ist.
    Definiert durch:
    - e: Länge der Symmetrie-Diagonale (vertikal)
    - f: Länge der Quer-Diagonale (horizontal)
    - abstand_oben: Abstand vom Schnittpunkt zur oberen Ecke
    """

    def __init__(self, e: float, f: float, abstand_oben: float):
        # Wir bauen es entlang der Y-Achse auf (Symmetrieachse)
        # Punkt Oben (0, e - abstand_oben)
        # Punkt Unten (0, -abstand_oben)
        # Punkt Rechts (f/2, 0)
        # Punkt Links (-f/2, 0)

        p_oben = Punkt(0, e - abstand_oben)
        p_rechts = Punkt(f / 2, 0)
        p_unten = Punkt(0, -abstand_oben)
        p_links = Punkt(-f / 2, 0)

        # Reihenfolge gegen den Uhrzeigersinn: Unten, Rechts, Oben, Links
        super().__init__(p_unten, p_rechts, p_oben, p_links)
        self.diag_e = e
        self.diag_f = f

    @property
    def flaeche(self) -> float:
        """
        Spezialformel für Drachen: (e * f) / 2
        Viel schneller als die Gauß-Formel.
        """
        return (self.diag_e * self.diag_f) / 2.0


# --- Ebene 1b: Das gleichschenklige Trapez ---
class GleichschenkligesTrapez(Trapez):
    """
    Ein Trapez, das symmetrisch ist.
    Die Schenkel links und rechts sind gleich lang.
    """

    def __init__(self, a: float, c: float, h: float):
        # Automatische Berechnung der Verschiebung für Symmetrie
        verschiebung = (a - c) / 2
        super().__init__(a, c, h, verschiebung)


# --- Ebene 2: Das Parallelogramm ---
class Parallelogramm(Trapez):
    """
    Gegenüberliegende Seiten sind parallel und gleich lang.
    Definiert durch Seite a, Seite b und den Winkel alpha (in Grad).
    """

    def __init__(self, a: float, b: float, alpha_grad: float):
        # Wir müssen die Höhe h und die Verschiebung aus dem Winkel berechnen
        rad = math.radians(alpha_grad)
        h = b * math.sin(rad)
        verschiebung = b * math.cos(rad)

        # Ein Parallelogramm ist ein Trapez, bei dem oben (c) == unten (a) ist.
        super().__init__(a, a, h, verschiebung)


# --- Ebene 3: Die Raute ---
class Raute(Parallelogramm):
    """
    Ein Parallelogramm mit 4 gleich langen Seiten (a = b).
    (Mathematisch ist es AUCH ein Drachen!)
    """

    def __init__(self, a: float, alpha_grad: float):
        super().__init__(a, a, alpha_grad)


# --- Ebene 3: Das Rechteck ---
class Rechteck(Parallelogramm):
    """
    Ein Parallelogramm mit 90° Winkeln.
    Definiert durch Breite b und Höhe h.
    """

    def __init__(self, breite: float, hoehe: float):
        super().__init__(breite, hoehe, 90)

    @property
    def flaeche(self) -> float:
        """Optimierte Flächenformel: Breite * Höhe"""
        # Wir greifen auf die berechneten Eckpunkte zu
        breite = self.eckpunkte[1].x
        hoehe = self.eckpunkte[2].y
        return breite * hoehe


# --- Ebene 4: Das Quadrat ---
class Quadrat(Rechteck):
    """
    Das perfekte Viereck:
    - Ist ein Rechteck (90° Winkel)
    - Ist eine Raute (gleich lange Seiten)
    """

    def __init__(self, a: float):
        super().__init__(a, a)
