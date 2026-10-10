# Lokale KI-Wiki: einen funktionierenden Befehl wiederfinden

**Zweck:** Du hast einen Befehl zum Laufen gebracht (Port, API-Adresse, Modellalias) und willst ihn in drei Monaten samt Quelle und Version wiederfinden. Dieses Paket zeigt den Weg dafür an einem kleinen, erfundenen Beispiel.

## Datenfluss

```text
QUELLE-V1.md / QUELLE-V2.md        (Rohquellen, Version 2 ist aktuell)
        │  VORBEREITEN-WIKI.ps1 kopiert sie bytegleich
        ▼
<Lernordner>\raw\sources\*.md  +  VORBEREITUNG.json   (Dateiname + SHA256)
        │  Import in deine vorhandene Wiki-App
        ▼
Wiki-Seite (von der App geschrieben)
        │  Vergleich mit der Rohquelle
        ▼
geprüfte Seite → Index → Rücklesen per MCP (llm_wiki_read_file)
        ▼
Antwort auf FRAGEN-DE.txt, Vergleich mit SOLLWERT.md, Eintrag in PRUEFPROTOKOLL.csv
```

## Downloads

| Sprache | Komplettes Lernpaket | Anleitung |
| --- | --- | --- |
| Deutsch | [WIKI-LERNPAKET-DE.zip](https://raw.githubusercontent.com/dolmario/lokale-ki-wiki/main/WIKI-LERNPAKET-DE.zip) | [DE/START.md](DE/START.md) |
| English | [WIKI-LERNPAKET-EN.zip](https://raw.githubusercontent.com/dolmario/lokale-ki-wiki/main/WIKI-LERNPAKET-EN.zip) | [EN/START.md](EN/START.md) |

## Was herauskommt

Der Aufruf

```powershell
.\VORBEREITEN-WIKI.ps1 -OutputDirectory "C:\dein\Wiki-Lernprojekt"
```

legt einen neuen Ordner an (ein vorhandener Ordner wird abgelehnt) mit:

- `raw\sources\QUELLE-V1.md` und `QUELLE-V2.md`, unverändert kopiert,
- `VORBEREITUNG.json` mit beiden Dateinamen, ihren SHA256-Werten und den Feldern `native_ingest`, `indexed`, `mcp_readback` (alle `false`) und `http_requests: 0`.

Das Skript startet kein Modell, ruft keine API auf und verändert keine echte Wiki.

## Die erwartete Antwort

Die Quellen sind erfundene Server-Notizen. Nach dem Import muss deine Wiki-Seite sagen:

| Frage | Richtige Antwort | Quelle |
|---|---|---|
| Browserport | 8091 | QUELLE-V2 (Version 1 nannte 8080 und ist ersetzt) |
| API-Basis | `http://127.0.0.1:8091/v1` | QUELLE-V2 |
| Modellalias | `lernmodell` (alt: `lernmodell-alt`) | QUELLE-V2 |
| Kontext | 4096 Token, Eingabe und Antwort teilen ihn | QUELLE-V2 |
| CPU-Typ | steht in keiner Quelle: „unbekannt“ | – |

Ein Wiki, das einen CPU-Typ erfindet oder Port 8080 als aktuell ausgibt, hat die Seite falsch geschrieben; dann korrigierst du sie mit Verweis auf die Rohquelle.

## Voraussetzungen und Grenzen

Ein tatsächlicher Import braucht eine bereits vorhandene Wiki-App mit laufendem Modellserver. Das Paket enthält keinen App-Installer; für unseren archivierten portablen LLM-Wiki-Build 0.6.11 ist keine öffentliche Neuinstallationsquelle verifiziert. Quellen und Versionsstand: [QUELLEN.md](QUELLEN.md).

`ARCHIV-ERGEBNIS.json` enthält aggregierte Zahlen eines älteren Auswahlversuchs (40 Quellen × 6 Felder × 2 Läufe = 480 Entscheidungen pro Modell; 334 bzw. 372 richtig; kein Schwellwert erreichte zugleich 95 % Präzision und 60 % Abdeckung). Private Quelltexte sind nicht enthalten.

## English

Purpose: keep a working command (port, API address, model alias) findable together with its source and version. Data flow: raw sources → `VORBEREITEN-WIKI.ps1` copies them byte-identically to `raw\sources` and writes `VORBEREITUNG.json` (names + SHA256) → import into your existing Wiki app → compare page with raw source → index → read back via MCP → answer `FRAGEN-EN.txt` and compare with `SOLLWERT.md`. Expected answer: port 8091, API `http://127.0.0.1:8091/v1`, alias `lernmodell`, CPU type unknown. The helper calls no API and touches no real Wiki; a real import needs your own app and running model server. See [EN/START.md](EN/START.md).
