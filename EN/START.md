# Find your working local AI command again

This kit contains fictional sources you can compare in a text editor. Actual ingestion requires an existing Wiki app and its running model server. A public download for our archived portable LLM Wiki 0.6.11 build has not been verified here. This kit installs no app and modifies no real Wiki.

1. Extract the complete English ZIP. Open QUELLE-V1.md and QUELLE-V2.md. These small sources are in German; questions are available in English.
2. Version 1 is superseded; version 2 is current. Port 8091, the API address and alias are fictional values. No actual server runs for this exercise.
3. Prepare a new isolated learning folder. Open PowerShell in the companion folder and adapt the example path:

```powershell
.\VORBEREITEN-WIKI.ps1 -OutputDirectory "C:\your\Wiki-Learning-Project"
```

4. Inspect raw\sources and VORBEREITUNG.json there. Both sources were copied unchanged. No ingestion, indexing or MCP call was performed.
5. For actual ingestion, select a separate learning project in your existing app. First check resources and active jobs. Our native ingestion requires a running model server.
6. Verify your actual API base, model ID and project model. The example port does not prescribe your installation.
7. Record the project path and ID. Import only the two fictional sources using your app version's import method. Our helper creates no queue.
8. Read actual job state and errors. Resolve a missing server or busy resources. Do not start a second instance or stop someone else's processes.
9. After actual completion, record the pages genuinely written. Queue status and cached hashes do not prove correct content.
10. Compare page and source: current version, port 8091, complete API address and alias lernmodell. The CPU type is unspecified and must remain unknown.
11. Correct specific errors with source references. Preserve originals and identifiable corrections. A high model score does not replace review.
12. Actually index the reviewed page in your Wiki. Save real index state and errors. Embedding also consumes model resources.
13. Read the full page back through your available Wiki MCP. Use the correct project and real path. Our MCP offers llm_wiki_read_file. A file list is not content readback.
14. Search for a specific source phrase and inspect the result. Ask FRAGEN-EN.txt in your client and preserve the actual response, then open SOLLWERT.md.
15. Complete PRUEFPROTOKOLL.csv. Saved, processed, reviewed, indexed and read back through MCP are separate states. Leave unverified fields blank.
16. ARCHIV-ERGEBNIS.json describes a limited old experiment: 40 sources, six fields and two cold runs yield 480 decisions per model, not 480 independent documents. Correct decisions numbered 334 and 372. No tested threshold achieved both 95 percent precision and 60 percent coverage.

## Jev idea and current sources

Our historical Jev-inspired selection experiment is a separate archive finding. openjev-sglang now points to SGLang's native decisions API. Its /v1/decisions is an SGLang extension; documentation mentions a nightly build until a matching release exists. Values are not calibrated truth probabilities. We neither installed nor executed that external route here. QUELLEN.md lists primary sources.

The new film uses separately approved MOSS narration, our own fictional presenter and DOLMARIO AI llama. Your actual ingestion and complete listening need separate verification.
