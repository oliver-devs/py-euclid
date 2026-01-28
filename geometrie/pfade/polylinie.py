from dataclasses import dataclass
from typing import List
from ..primitive.elemente import Punkt


@dataclass(frozen=True)
class Polylinie:
    """
    Ein Pfad aus mehreren verbundenen Punkten.
    """

    punkte: List[Punkt]

    def __post_init__(self):
        """Validierung nach der Erstellung."""
        if len(self.punkte) < 2:
            raise ValueError("Eine Polylinie braucht mindestens 2 Punkte.")

    @property
    def laenge(self) -> float:
        """Berechnet die Gesamtlänge des Pfades."""
        gesamt = 0.0
        # Wir laufen durch die Liste bis zum vorletzten Punkt
        for i in range(len(self.punkte) - 1):
            p_aktuell = self.punkte[i]
            p_naechster = self.punkte[i + 1]
            gesamt += Punkt.distanz(p_aktuell, p_naechster)
        return gesamt
