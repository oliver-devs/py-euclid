import math
from dataclasses import dataclass


# --- 0D: Punkt ---
@dataclass(frozen=True)
class Punkt:
    x: float
    y: float

    @staticmethod
    def distanz(p1: "Punkt", p2: "Punkt") -> float:
        return math.dist((p1.x, p1.y), (p2.x, p2.y))


# --- 1D: Gerade ---
@dataclass(frozen=True)
class Gerade:
    m: float  # Steigung
    b: float  # y-Achsenabschnitt

    @classmethod
    def von_punkten(cls, p1: Punkt, p2: Punkt) -> "Gerade":
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        # Prüfen auf vertikale Linie (Division durch Null verhindern)
        if math.isclose(dx, 0, abs_tol=1e-9):
            return cls(float("inf"), p1.x)  # Steigung unendlich

        m = dy / dx
        # Formel: y = mx + b  =>  b = y - mx
        b = p1.y - (m * p1.x)
        return cls(m, b)


# --- 1D: Strahl ---
@dataclass(frozen=True)
class Strahl:
    start: Punkt
    richtung: Punkt


# --- 1D: Strecke ---
@dataclass(frozen=True)
class Strecke:
    start: Punkt
    ende: Punkt

    @property
    def laenge(self) -> float:
        return Punkt.distanz(self.start, self.ende)
