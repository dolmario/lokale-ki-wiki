# Deinen funktionierenden KI-Befehl wiederfinden

Ein Lernpaket mit erfundenen Quellen. Du kannst sie im Texteditor vergleichen. Ein echter Import benötigt eine vorhandene Wiki-App und ihren laufenden Modellserver. Eine öffentliche Bezugsquelle für unseren archivierten portablen Build LLM Wiki 0.6.11 ist hier nicht verifiziert. Das Paket installiert keine App und verändert keine echte Wiki.

1. Entpacke die deutsche ZIP vollständig. Öffne QUELLE-V1.md und QUELLE-V2.md.
2. Version 1 ist ersetzt; Version 2 ist aktuell. Port 8091, API-Adresse und Alias sind erfundene Übungswerte. Dafür läuft kein echter Server.
3. Bereite einen neuen Lernordner vor. Öffne PowerShell im Begleitordner und passe den Beispielpfad an:

```powershell
.\VORBEREITEN-WIKI.ps1 -OutputDirectory "C:\dein\Wiki-Lernprojekt"
```

4. Prüfe raw\sources und VORBEREITUNG.json dort. Beide Quellen sind unverändert kopiert. Es wurden weder Import noch Index oder MCP ausgeführt.
5. Für einen tatsächlichen Import wähle ein getrenntes Lernprojekt in deiner vorhandenen App. Prüfe freie Ressourcen und laufende Aufträge. Unser nativer Ingest braucht den laufenden Modellserver.
6. Kontrolliere deine tatsächliche API-Basis, Modell-ID und das Projektmodell. Der Beispielport ist keine Vorgabe für deine Installation.
7. Notiere Projektpfad und Projekt-ID. Importiere nur die zwei erfundenen Quellen über den Importweg deiner App-Version. Unser Werkzeug erstellt keine Warteschlange.
8. Lies tatsächlichen Auftragsstatus und Fehler. Kläre einen fehlenden Server oder belegte Ressourcen. Starte keine zweite Instanz und beende keine fremden Prozesse.
9. Nach dem echten Abschluss notiere die wirklich geschriebenen Seiten. Queue-Status und Cache-Hash allein beweisen ihre Richtigkeit nicht.
10. Vergleiche Seite und Rohquelle: aktuelle Version, Port 8091, vollständige API-Adresse und Alias lernmodell. Der CPU-Typ fehlt und muss unbekannt bleiben.
11. Korrigiere konkrete Fehler mit Quellenbezug. Bewahre Original und nachvollziehbare Korrektur. Ein hoher Modellscore ersetzt diese Prüfung nicht.
12. Indexiere die geprüfte Seite in deiner vorhandenen Wiki. Sichere echten Indexstatus und Fehler. Embedding beansprucht ebenfalls Modellressourcen.
13. Lies die ganze Seite über dein vorhandenes Wiki-MCP zurück. Verwende das richtige Projekt und den wirklichen Pfad. Unser MCP bietet dafür llm_wiki_read_file. Eine Dateiliste ist noch kein Inhaltsrücklesen.
14. Suche nach einer konkreten Formulierung aus der Quelle und prüfe den Treffer. Stelle FRAGEN-DE.txt im eigenen Client und bewahre die Antwort. Öffne erst danach SOLLWERT.md.
15. Fülle PRUEFPROTOKOLL.csv aus. Abgelegt, verarbeitet, geprüft, indexiert und per MCP gelesen sind getrennte Zustände. Ungeprüfte Felder bleiben leer.
16. ARCHIV-ERGEBNIS.json ist ein begrenzter alter Versuch: 40 Quellen, sechs Felder, zwei Kaltläufe, 480 Entscheidungen pro Modell. Es waren keine 480 unabhängigen Dokumente. 334 und 372 Entscheidungen waren richtig. Keine getestete Schwelle erreichte zugleich 95 Prozent Präzision und 60 Prozent Abdeckung.

## Jev-Idee und heutige Quellen

Der alte Jev-inspirierte Auswahlversuch ist ein eigener Archivbefund. openjev-sglang verweist inzwischen auf SGLangs native Entscheidungs-API. Deren /v1/decisions ist eine SGLang-Erweiterung; die Dokumentation nennt einen Nightly-Build, solange keine passende Release vorliegt. Ihre Werte sind keine kalibrierten Wahrheitswahrscheinlichkeiten. Wir haben diesen externen Weg weder installiert noch ausgeführt. QUELLEN.md nennt die Primärquellen.

Der neue Film verwendet die separat bestätigte MOSS-Sprecherin, die eigene fiktive Moderatorin und das DOLMARIO-AI-Lama. Ein eigener erfolgreicher Import und vollständiges Endhören sind gesondert zu belegen.
