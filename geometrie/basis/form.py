from abc import ABC, abstractmethod


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
