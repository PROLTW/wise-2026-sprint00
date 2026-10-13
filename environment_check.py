"""Prueft die Werkzeugkette fuer Sprint 00, ohne Projektlogik."""

import importlib
import platform
import subprocess
import sys


PAKETE = ("pandas", "matplotlib", "simpy", "streamlit")


def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Interpreter: {sys.executable}")
    print(f"System: {platform.system()}")
    print("Kurs-Pakete:")
    for paketname in PAKETE:
        paket = importlib.import_module(paketname)
        print(f"- {paketname}: {paket.__version__}")
    try:
        git_version = subprocess.run(
            ["git", "--version"], check=True, capture_output=True, text=True
        ).stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError) as fehler:
        raise SystemExit(f"Git ist nicht verfuegbar: {fehler}") from fehler
    print(git_version)
    print("SPRINT00_OK")


if __name__ == "__main__":
    main()

