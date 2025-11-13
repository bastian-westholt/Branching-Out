# Branching-Out

Ein Python-Projekt zum Filtern von Benutzerdaten aus JSON-Dateien.

## Projektbeschreibung

Dieses Projekt stellt eine einfache Benutzeroberfläche zur Verfügung, um Benutzer aus einer JSON-Datei nach verschiedenen Kriterien zu filtern. Das Projekt wurde im Rahmen eines Lernprojekts entwickelt und demonstriert grundlegende Python-Konzepte wie Dateiverarbeitung, Fehlerbehandlung und Benutzerinteraktion.

## Features

- **Filter nach Name**: Suche nach Benutzern anhand ihres Namens (case-insensitive)
- **Filter nach Alter**: Suche nach Benutzern mit einem bestimmten Alter
- **Filter nach E-Mail**: Suche nach Benutzern anhand ihrer E-Mail-Adresse (case-insensitive)
- **Eingabevalidierung**: Überprüfung der Benutzereingaben mit Fehlerbehandlung
- **PEP 8 konform**: Code folgt Python-Styleguide-Standards

## Projektstruktur

```
branching-out/
├── filter_users.py    # Hauptprogramm mit Filterfunktionen
├── users.json         # Benutzerdaten (15 Beispielbenutzer)
└── README.md          # Projektdokumentation
```

## Installation & Setup

1. **Repository klonen**:
   ```bash
   git clone <repository-url>
   cd branching-out
   ```

2. **Python-Version**:
   - Python 3.6 oder höher erforderlich
   - Keine zusätzlichen Dependencies notwendig (nur Standardbibliothek)

## Verwendung

Das Programm über die Kommandozeile starten:

```bash
python filter_users.py
```

### Beispiel-Ablauf:

```
What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): name
Enter a name to filter users: Alice
{'id': 1, 'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}
```

### Verfügbare Filter:

1. **Name**: Exakte Übereinstimmung (case-insensitive)
2. **Alter**: Numerischer Wert
3. **E-Mail**: Exakte Übereinstimmung (case-insensitive)

## Datenstruktur

Die `users.json` Datei enthält ein Array von Benutzerobjekten:

```json
[
    {
        "id": 1,
        "name": "Alice",
        "age": 25,
        "email": "alice@example.com"
    }
]
```

### Beispieldaten:
- 15 Benutzer
- Altersbereich: 21-40 Jahre
- Eindeutige IDs und E-Mail-Adressen

## Funktionen

### `filter_users_by_name(name)`
Filtert Benutzer nach Namen mit case-insensitive Suche.

### `filter_by_age(age)`
Filtert Benutzer nach exaktem Alter.

### `filter_by_email(email)`
Filtert Benutzer nach E-Mail-Adresse mit case-insensitive Suche.

## Fehlerbehandlung

Das Programm behandelt folgende Fehlertypen:

- **ValueError**: Bei ungültigen numerischen Eingaben für das Alter
- **TypeError**: Bei ungültigen Zeichen im Namen (z.B. Zahlen)
- **FileNotFoundError**: Wenn die users.json Datei nicht gefunden wird
- **JSONDecodeError**: Bei ungültiger JSON-Struktur

## Entwicklungshistorie

Das Projekt wurde schrittweise entwickelt:

1. **Grundstruktur**: Erstelle users.json mit Beispieldaten
2. **Name-Filter**: Implementierung der Namenssuche
3. **Alter-Filter**: Hinzufügung der Altersfilterung mit Fehlerbehandlung
4. **E-Mail-Filter**: Implementierung der E-Mail-Suche
5. **PEP 8 Optimierung**: Code-Formatierung und Dokumentation

## Code-Qualität

- **PEP 8 konform**: Einhaltung der Python-Styleguide-Standards
- **Dokumentiert**: Docstrings und Kommentare für bessere Verständlichkeit
- **Fehlerbehandlung**: Robuste Behandlung von Benutzereingaben
- **Modularer Aufbau**: Getrennte Funktionen für verschiedene Filter

## Mögliche Erweiterungen

- GUI-Interface mit tkinter oder PyQt
- Zusätzliche Filterkriterien (z.B. ID-Range, Altersbereich)
- Datenbankanbindung statt JSON-Datei
- Export-Funktionen für gefilterte Ergebnisse
- Fuzzy-Search für Namen
- Batch-Processing für mehrere Filter gleichzeitig

## Autor

Bastian Westholt - Masterschool Lernprojekt

## Lizenz

Dieses Projekt dient Lernzwecken und steht unter keiner spezifischen Lizenz.
