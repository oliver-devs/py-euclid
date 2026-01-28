import math
from ..basis.form import Form
from ..primitive.elemente import Punkt


class Ellipse(Form):
    """
    Eine geschlossene Kurve, definiert durch zwei Halbachsen a und b.
    """

    def __init__(self, zentrum: Punkt, a: float, b: float):
        self.zentrum = zentrum
        self.a = a  # Halbachse in x-Richtung
        self.b = b  # Halbachse in y-Richtung

    @property
    def flaeche(self) -> float:
        """Formel: pi * a * b"""
        return math.pi * self.a * self.b

    @property
    def umfang(self) -> float:
        """
        Berechnung des Ellipsenumfangs mit der 1. Ramanujan-Näherung.
        Dies ist eine sehr genaue Annäherung, da es keine exakte
        einfache Formel für den Ellipsenumfang gibt.
        """
        a, b = self.a, self.b
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))


class Kreis(Ellipse):
    """
    Ein perfekter Kreis. Ein Spezialfall der Ellipse mit a = b = r.
    """

    def __init__(self, zentrum: Punkt, radius: float):
        super().__init__(zentrum, radius, radius)
        self.radius = radius
