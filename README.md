# The Jev Idea in Our Local Wiki

Download the current practice kit: [PRACTICE-KIT.zip](downloads/PRACTICE-KIT.zip).

Send one source to a local model, inspect six fixed-choice answers and deliver the reviewed source to your Wiki’s normal input folder. This repository contains the small integration component we actually use, with source files and tests.

Start with [the practical walkthrough](EN/JEV-PRACTICE.md). `wiki_auswahl.py` needs Python 3.12 and an existing local llama.cpp-compatible API. It uses constrained J/N generation and token probabilities; Jev’s original prefill-only server is a different implementation.

Tested on 10 October: actual response `N,N,N,N,J,N` → explicit acceptance → unchanged source delivery → processing by our existing Wiki app → written page → search and complete MCP readback. Five tests cover field mapping, incomplete answers, changed sources, review and preservation of existing files.

The normal Wiki app is an existing prerequisite. We used portable build 0.6.12; this repository is not its installer. The source is a fictional teaching note, retained in its original German form. Earlier ZIPs contain the older source-version exercise.

Original inspiration: https://github.com/ekzhang/openjev-sglang

Test hardware: [GMKtec EVO-X2 / shop](https://de.gmktec.com/?ref=DolmarioAi) · advertisement / affiliate link.

## Deutsch

Unser konkreter Jev-Baustein: eine Quelle an die vorhandene lokale Schnittstelle schicken, sechs Auswahlfelder prüfen und die Quelle nach ausdrücklicher Annahme an den normalen Wiki-Weg übergeben. [Die praktische Anleitung](DE/JEV-PRAXIS.md) zeigt Aufruf, echte Antwort und die Übergabestelle im Code.

Der vollständige Weg wurde im vorhandenen Wiki-Projekt geprüft, einschließlich geschriebener Seite, Suche und MCP-Rücklesen. Das Repo enthält den Auswahlbaustein und fünf Tests; die vorhandene Wiki-App ist Voraussetzung. Neue Videos verwenden englischen Ton und deutsche Untertitel.
