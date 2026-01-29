import sys
import os

# Trick, damit Python den Ordner 'geometrie' sicher findet
sys.path.append(os.getcwd())

from geometrie.daten.loader import lade_daten_von_github


def main():
    print("--- 🚀 System-Start v0.6: Data-Link Aktiviert ---")

    # 1. Daten laden (passiert über das Internet!)
    # Wenn du den Link im loader.py fest eingetragen hast, brauchst du hier keine Argumente.
    mission_payload = lade_daten_von_github()

    if not mission_payload:
        print("❌ Mission abgebrochen: Keine Daten erhalten.")
        return

    print(f"\n📦 Empfangene Fracht ({len(mission_payload)} Einheiten):")
    for form in mission_payload:
        print(f"   - {form}")

    # 2. Sortieren (Beweis, dass Issue #1 und Issue #2 zusammenarbeiten)
    print("\n⚙️  Optimiere Laderaum (Sortierung nach Größe)...")
    mission_payload.sort()

    print("✅ Optimierte Fracht:")
    for form in mission_payload:
        print(f"   - {form}")


if __name__ == "__main__":
    main()
