from abc import ABC, abstractmethod
from functools import total_ordering


@total_ordering
class Form(ABC):
    """
    Abstrakte Basisklasse für alle geschlossenen Formen.

    Diese Klasse definiert das Interface (die Schnittstelle),
    das alle Figuren (wie Dreieck, Viereck, Kreis) implementieren müssen.
    """

    @property
    @abstractmethod
    def flaeche(self) -> float:
        """Gibt den Flächeninhalt der Form zurück."""
        pass

    @property
    @abstractmethod
    def umfang(self) -> float:
        """Gibt den Umfang der Form zurück."""
        pass

    def __eq__(self, other):
        """Vergleich: Haben zwei Formen die gleiche Fläche?"""
        if not isinstance(other, Form):
            return NotImplemented
        # Wir runden auf 5 Stellen, um Probleme mit Kommazahlen zu vermeiden
        return round(self.flaeche, 5) == round(other.flaeche, 5)

    def __lt__(self, other):
        """Vergleich: Ist die Fläche der aktuellen Form kleiner als die von `other`?"""
        if not isinstance(other, Form):
            return NotImplemented
        return self.flaeche < other.flaeche

    def __repr__(self):
        """String-Repräsentation der Form."""
        return f"<{self.__class__.__name__} (A: {self.flaeche:.2f})>"
