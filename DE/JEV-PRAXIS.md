# Eine Quelle durch unseren lokalen Auswahlweg schicken

Wir haben von Jev das Prinzip übernommen, feste Antworten auszuwählen. Unsere tatsächliche lokale Methode ist die eingeschränkte Ausgabe von sechs J/N-Feldern über llama.cpp mit Token-Wahrscheinlichkeiten. Sie verwendet weder Jevs Modell noch seine Prefill-only-API. Die Methode stammt aus unserem erhaltenen `ingest_konfidenzgatter.py` vom 19. September.

Der praktische Weg:

```text
QUELLE-V2.md
   → wiki_auswahl.py select → vorhandener lokaler Modellserver
   → auswahl.json: sechs Felder, Wahrscheinlichkeiten, vollständiger Aufruf
   → Quelle und Vorschlag prüfen; eigene Annahmeentscheidung treffen
   → wiki_auswahl.py deliver --reviewed --decision accept
   → gewähltes Wiki-Projekt/raw/sources/QUELLE-V2.md
   → Importweg der vorhandenen Wiki-App
   → geschriebene Seite prüfen, indexieren, suchen, Inhalt über MCP rücklesen
```

## Download und Start

Python 3.12 und eine vorhandene lokale OpenAI-kompatible llama.cpp-Schnittstelle reichen für das Auswahlskript. Keine neuen Python-Pakete, keine weitere Serverinstanz und keine SGLang-Installation nötig. Im entpackten Repo zunächst `QUELLE-V2.md` öffnen: aktuelle Adresse, Modellalias und Kontext stehen darin. Der CPU-Typ fehlt.

Im Terminal die tatsächliche lokale Adresse und die ID deines geladenen Modells einsetzen. Unser frischer Probeaufruf nutzte den schon laufenden `qwen3.6-35b` auf `http://127.0.0.1:8090`. Auf einem anderen Rechner zuerst dessen `/v1/models` prüfen.

```powershell
py -3.12 .\wiki_auswahl.py select `
  --source .\QUELLE-V2.md `
  --output .\auswahl.json `
  --endpoint http://127.0.0.1:8090 `
  --model qwen3.6-35b `
  --candidate-a lernserver --candidate-b lernserver
```

Das Skript sendet genau diese eine Quelle an die angegebene Loopback-Adresse. Es startet oder stoppt kein Modell. Die Antwort ist auf sechs Felder begrenzt: `aufnehmen`, `entitaet`, `konzept`, `frage`, `dublette`, `hohe_prioritaet`. Das Ergebnis enthält den Quellhash, die Eingabe und die tatsächliche Rohantwort.

## Die tatsächliche Antwort

Unser neuer Lauf vom 10. Oktober benötigte 244 Eingabe- und 12 Ausgabetoken sowie 11,40 s. Seine Antwort war:

```text
N, N, N, N, J, N
```

Der Aufnahmemodellvorschlag war `N`; die Dublettenfrage bei identischen Kandidatennamen war `J`. Auch bei hohen J/N-Wahrscheinlichkeiten war die Quelle weiterhin selbst zu lesen. Diesen Vorschlag nicht durch ein erfundenes Erfolgsergebnis ersetzen.

## An den Wiki-Eingang übergeben

Nach inhaltlicher Prüfung kann der Aufrufer die Quelle ausdrücklich annehmen, auch wenn der Modellvorschlag `N` war:

```powershell
py -3.12 .\wiki_auswahl.py deliver `
  --source .\QUELLE-V2.md `
  --result .\auswahl.json `
  --project .\MEIN-WIKI-LERNPROJEKT `
  --reviewed --decision accept
```

Das kopiert die Quelle unverändert nach `MEIN-WIKI-LERNPROJEKT\raw\sources`. **Im Projektwurzelordner** hält `QUELLE-V2.md.UEBERGABE.json` fest, ob die eigene Prüfung vom Modellvorschlag abwich. Ein vorhandenes Ergebnis oder Ziel wird nicht überschrieben; bei einer geänderten Quelle ist ein neuer Auswahlaufruf nötig.

`reviewed_by_caller` bezeichnet den Aufrufer. In unserem hier gesicherten Beispiel hat Codex die synthetische Quelle geprüft. Es behauptet keine menschliche Abnahme.

## Was die Wiki-App übernimmt

Die Übertragung in `raw/sources` ist die Schnittstelle zum Importweg der Wiki-App. Einen neuen Lernordner in der vorhandenen App als eigenes Projekt öffnen, deren Import-/Quellwatch-Funktion für diesen Ordner verwenden und mit der echten Modell-ID verarbeiten. Danach die geschriebene Seite mit der Quelle vergleichen, indexieren, suchen und vollständig über `llm_wiki_read_file` rücklesen. Die Kopierfunktion meldet deshalb `native_ingest=false`, `indexed=false`, `mcp_readback=false`.

Am 10. Oktober wurde die Beispielquelle zusätzlich über genau diesen Übergabebefehl in unser vorhandenes Wiki-Projekt `jt` geliefert. Die Quellenüberwachung der App verarbeitete sie und schrieb `wiki/sources/QUELLE-V2.md`. Die anschließende Suche nach `Beispielserver` fand diese Seite; über MCP wurde ihr vollständiger Inhalt rückgelesen. Port 8091, Kontext 4096 und der unbekannte CPU-Typ stimmen mit der synthetischen Quelle überein. Die Seite bezeichnet den Lernfall weiter als erfunden.

Die automatische App-Verarbeitung und ihr Index waren damit erfolgreich. Ein zusätzlich aufgerufener manueller Embedding-Endpunkt antwortete mit 401; dieser separate Aufruf wurde nicht als erfolgreich verbucht. Ein App-Installer gehört weiterhin nicht zum Repo. Unser tatsächlich benutzter portabler Appstand ist 0.6.12; die alten Hinweise auf 0.6.11 beziehen sich auf ein archiviertes Paket. Eine öffentliche Installationsquelle für unseren eigenen Appbuild ist in diesem Repo nicht vorhanden. Dieser Versuch verwendet also eine vorhandene App und ist kein Test ihrer Neuinstallation.

## Warum keine automatische Annahme?

Die erhaltenen Messungen enthalten 40 Quellen × 6 Felder × 2 Läufe, 480 Entscheidungen je Modell. Qwen lag bei 334, HauhauCS bei 372 richtigen Entscheidungen. Keine getestete Schwelle erfüllte gleichzeitig 95 % Richtigkeit und 60 % Abdeckung. Deshalb kann eine Modellwahrscheinlichkeit die Prüfung nicht ersetzen. Die separate Sidecar-Warteschlange, deren drei Ingests und Absturzwiederaufnahme getestet wurden, ist eine andere Komponente. Das neue Auswahlskript ändert diese Warteschlange nicht.

Tests:

```powershell
py -3.12 -m unittest discover -s tests -v
```

Diese prüfen unvollständige Antworten, falsche Feldzuordnung der Wahrscheinlichkeiten, geänderte Quellen, den expliziten Prüfentscheid und Schutz vor Überschreiben. Originales Vorbild: https://github.com/ekzhang/openjev-sglang
