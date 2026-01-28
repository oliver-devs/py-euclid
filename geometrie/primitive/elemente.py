import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Punkt:
    """
    Repräsentiert einen Punkt im 2D-Koordinatensystem.
    Unveränderlich (Immutable).
    """

    x: float
    y: float

    @staticmethod
    def distanz(p1: "Punkt", p2: "Punkt") -> float:
        """
        Berechnet die euklidische Distanz zwischen zwei Punkten.
        """
        return math.dist((p1.x, p1.y), (p2.x, p2.y))
