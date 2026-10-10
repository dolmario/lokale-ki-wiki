# Deinen funktionierenden KI-Befehl wiederfinden

Ziel: Port, API-Adresse und Modellalias eines laufenden lokalen Modellservers so im Wiki ablegen, dass du später die **aktuelle** Angabe samt Quelle und Version wiederfindest. Geübt wird mit zwei erfundenen Dateien.

## 1. Quellen ansehen

Entpacke die ZIP vollständig und öffne `QUELLE-V1.md` und `QUELLE-V2.md`:

| | QUELLE-V1 (ersetzt) | QUELLE-V2 (aktuell) |
|---|---|---|
| Browser | Port 8080 | `http://127.0.0.1:8091` |
| API-Basis | – | `http://127.0.0.1:8091/v1` |
| Modellalias | `lernmodell-alt` | `lernmodell` |
| Kontext | – | 4096 Token (Eingabe und Antwort teilen ihn) |
| CPU-Typ | nicht dokumentiert | nicht dokumentiert |

Port 8091 und die Adressen sind Übungswerte; dafür läuft kein Server.

## 2. Lernordner vorbereiten

```powershell
.\VORBEREITEN-WIKI.ps1 -OutputDirectory "C:\dein\Wiki-Lernprojekt"
```

Der Ordner darf noch nicht existieren. Ergebnis:

```text
C:\dein\Wiki-Lernprojekt\
  raw\sources\QUELLE-V1.md
  raw\sources\QUELLE-V2.md
  VORBEREITUNG.json     (Dateinamen, SHA256, native_ingest/indexed/mcp_readback = false, http_requests = 0)
```

## 3. Import in deine Wiki-App

Lege in deiner vorhandenen App ein getrenntes Lernprojekt an und importiere die zwei Dateien aus `raw\sources` auf dem Importweg deiner App-Version. Der Import braucht den laufenden Modellserver. Trage deine echte API-Basis und Modell-ID ein (die Übungswerte gelten nur in den Quellen). Läuft schon eine Warteschlange, warte ab; starte keine zweite Instanz.

## 4. Geschriebene Seite prüfen

Die Seite muss enthalten: Version 2 als aktuell, Port 8091, `http://127.0.0.1:8091/v1`, Alias `lernmodell`, 4096 Token Kontext, und beim CPU-Typ „unbekannt“. Steht dort 8080, `lernmodell-alt` oder ein erfundener Prozessor, korrigiere die Seite mit Verweis auf `QUELLE-V2.md` und behalte das Original.

## 5. Indexieren und zurücklesen

Indexiere die geprüfte Seite in deiner Wiki. Lies sie dann über das Wiki-MCP komplett zurück (`llm_wiki_read_file` mit deinem Projekt und dem Seitenpfad). Eine Dateiliste zeigt nur, dass die Seite existiert, nicht ihren Inhalt.

## 6. Fragen stellen

Stelle den Text aus `FRAGEN-DE.txt` in deinem Client:

> Finde den aktuellen Browserport, die API-Basis und den Modellalias. Nenne jeweils die Quelle und Version. Welcher CPU-Typ ist eingebaut? …

Erwartet (siehe `SOLLWERT.md`): Port 8091, API `http://127.0.0.1:8091/v1`, Alias `lernmodell`, jeweils aus QUELLE-V2 / Version 2; CPU-Typ fehlt in den Quellen.

## 7. Protokoll

Trage in `PRUEFPROTOKOLL.csv` eine Zeile ein, z. B.:

```text
eigenes_projekt,rohe_quelle_hash,native_verarbeitung,geschriebene_seite,inhaltsvergleich,indexstatus,mcp_inhalt_gelesen,aktuelle_quelle,fehlendes_wissen,fehler,datum
lernprojekt-1,<SHA256 aus VORBEREITUNG.json>,ja,ja,ok,indexiert,ja,QUELLE-V2.md,CPU-Typ,keiner,2026-10-10
```

Felder, die du nicht geprüft hast, bleiben leer.

## Hintergrund: Jev-Versuch

`ARCHIV-ERGEBNIS.json` fasst einen älteren, Jev-inspirierten Versuch zusammen, Felder automatisch auszuwählen: 40 Quellen × 6 Felder × 2 Läufe = 480 Entscheidungen pro Modell (keine 480 unabhängigen Dokumente), davon 334 bzw. 372 richtig. Keine getestete Schwelle erreichte zugleich 95 % Präzision und 60 % Abdeckung. openjev-sglang verweist inzwischen auf SGLangs native Entscheidungs-API (`/v1/decisions`, laut Dokumentation Nightly-Build); diesen Weg haben wir nicht ausgeführt. Primärquellen: `QUELLEN.md`.
