# Sprint 00 - Arbeitsumgebung pruefen

Dieses Repository ist der technische Start fuer Projekt PROLTW. Es enthält
keine Python-Aufgaben und keine Projektlogik. Ziel ist, die eigene
Werkzeugkette einmal vollständig zu prüfen:

```text
Repository klonen -> virtuelle Umgebung anlegen -> Pakete installieren
-> Werkzeugcheck starten -> Git-Status prüfen
```

## Was ist enthalten?

| Datei oder Ordner | Zweck |
| --- | --- |
| `requirements.txt` | Kurs-Pakete fuer die folgenden Sprints |
| `environment_check.py` | prueft Python, Interpreter, Kurs-Pakete und Git |

## Start in VS Code

Alle Befehle werden im geklonten Ordner im VS-Code-Terminal ausgefuehrt.

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe environment_check.py
```

Falls `py` nicht verfuegbar ist, verwenden Sie stattdessen `python`.

### macOS, Linux und Unix

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python environment_check.py
```

Der Umgebungscheck endet erst dann mit `SPRINT00_OK`, wenn Python, Git und alle
Kurs-Pakete erreichbar sind.

## Abschluss von Sprint 00

| Zeit | Aufgabe | Woran man es erkennt |
| --- | --- | --- |
Sprint 00 ist fertig, wenn `environment_check.py` mit `SPRINT00_OK` endet,
`git --version` funktioniert und `git status` den geklonten Repository-Ordner
zeigt. Python-Grundlagen beginnen erst in Sprint 1.
