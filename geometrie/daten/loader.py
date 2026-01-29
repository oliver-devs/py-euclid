import json
from urllib.request import urlopen
from typing import List

# Importiere unsere Klassen
from ..basis.form import Form
from ..primitive.elemente import Punkt
from ..figuren.viereck import Quadrat, Drachen
from ..figuren.ellipse import Kreis


def lade_daten_von_github(url: str = None) -> List[Form]:
    """
    Lädt Geometrie-Daten von einer URL (JSON) und wandelt sie in Objekte um.
    """
    # Falls keine URL angegeben, nutzen wir den Standard (DEINE URL HIER EINFÜGEN!)
    if url is None:
        # TIPP: Ersetze das hier mit deinem echten Raw-Link von Schritt 2!
        url = "https://raw.githubusercontent.com/oliver-devs/py-euclid/refs/heads/main/data.json"

    print(f"📡 Verbinde...\n   Quelle: {url}")

    try:
        # 1. Herunterladen (wie ein Browser)
        with urlopen(url) as response:
            json_text = response.read().decode("utf-8")
            daten = json.loads(json_text)
            print(f"✅ Download erfolgreich: {len(daten)} Einträge gefunden.")

    except Exception as e:
        print(f"❌ Fehler beim Download: {e}")
        return []

    # 2. Objekte bauen (Die "Fabrik")
    objekte = []

    # Standard-Punkt für Kreise (vereinfacht)
    nullpunkt = Punkt(0, 0)

    for eintrag in daten:
        typ = eintrag.get("typ")
        params = eintrag.get("params", {})

        try:
            if typ == "Quadrat":
                # **params entpackt das Dictionary: {"a": 3} wird zu a=3
                form = Quadrat(**params)

            elif typ == "Kreis":
                # Kreis braucht zwingend ein Zentrum, das im JSON fehlt
                form = Kreis(zentrum=nullpunkt, **params)

            elif typ == "Drachen":
                form = Drachen(**params)

            else:
                print(f"⚠️ Unbekannter Typ ignoriert: {typ}")
                continue

            objekte.append(form)

        except TypeError as e:
            print(f"❌ Parameter-Fehler bei {typ}: {e}")

    return objekte
