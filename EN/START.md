# Find your working local AI command again

Goal: store the port, API address and model alias of a running local model server in a Wiki so that you can later find the **current** value with its source and version. You practise with two fictional files.

## 1. Look at the sources

Extract the ZIP completely and open `QUELLE-V1.md` and `QUELLE-V2.md` (the sources are in German, the questions exist in English):

| | QUELLE-V1 (superseded) | QUELLE-V2 (current) |
|---|---|---|
| Browser | port 8080 | `http://127.0.0.1:8091` |
| API base | – | `http://127.0.0.1:8091/v1` |
| Model alias | `lernmodell-alt` | `lernmodell` |
| Context | – | 4096 tokens (input and answer share it) |
| CPU type | not documented | not documented |

Port 8091 and the addresses are practice values; no server runs for them.

## 2. Prepare the learning folder

```powershell
.\VORBEREITEN-WIKI.ps1 -OutputDirectory "C:\your\Wiki-Learning-Project"
```

The folder must not exist yet. Result:

```text
C:\your\Wiki-Learning-Project\
  raw\sources\QUELLE-V1.md
  raw\sources\QUELLE-V2.md
  VORBEREITUNG.json     (file names, SHA256, native_ingest/indexed/mcp_readback = false, http_requests = 0)
```

## 3. Import into your Wiki app

Create a separate learning project in your existing app and import the two files from `raw\sources` using your app version's import route. Import needs the running model server. Enter your real API base and model ID (the practice values only apply inside the sources). If a queue is already running, wait; do not start a second instance.

## 4. Check the written page

The page must contain: version 2 as current, port 8091, `http://127.0.0.1:8091/v1`, alias `lernmodell`, 4096 tokens context, and "unknown" for the CPU type. If it says 8080, `lernmodell-alt` or an invented processor, correct the page with a reference to `QUELLE-V2.md` and keep the original.

## 5. Index and read back

Index the reviewed page in your Wiki. Then read it back completely through the Wiki MCP (`llm_wiki_read_file` with your project and the page path). A file list only shows that the page exists, not its content.

## 6. Ask the questions

Put the text from `FRAGEN-EN.txt` into your client. Expected (see `SOLLWERT.md`): port 8091, API `http://127.0.0.1:8091/v1`, alias `lernmodell`, each from QUELLE-V2 / version 2; the CPU type is missing from the sources.

## 7. Record

Add a row to `PRUEFPROTOKOLL.csv`, for example:

```text
eigenes_projekt,rohe_quelle_hash,native_verarbeitung,geschriebene_seite,inhaltsvergleich,indexstatus,mcp_inhalt_gelesen,aktuelle_quelle,fehlendes_wissen,fehler,datum
lernprojekt-1,<SHA256 from VORBEREITUNG.json>,yes,yes,ok,indexed,yes,QUELLE-V2.md,CPU type,none,2026-10-10
```

Leave fields you did not check empty.

## Background: the Jev experiment

`ARCHIV-ERGEBNIS.json` summarises an older, Jev-inspired attempt to select fields automatically: 40 sources × 6 fields × 2 runs = 480 decisions per model (not 480 independent documents), of which 334 and 372 were correct. No tested threshold reached 95 % precision and 60 % coverage at once. openjev-sglang now points to SGLang's native decisions API (`/v1/decisions`, a nightly build according to its documentation); we did not run that route. Primary sources: `QUELLEN.md`.
