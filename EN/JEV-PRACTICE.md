# Try the Jev idea in our local Wiki

We adopted Jev’s fixed-choice principle. Our implementation uses a local llama.cpp request constrained to six J/N answers and returns token probabilities. It does not use Jev’s original model or prefill-only API.

## Open the source and select

Requirements: Python 3.12 and an existing local OpenAI-compatible llama.cpp endpoint. No additional Python packages or new model server are needed for this script.

Open `QUELLE-V2.md`, our fictional teaching note. It contains a current port, API address, model alias and context setting; the CPU type is unspecified. This is the original German source used in the recorded experiment.

Use your actual endpoint and loaded model ID, obtained from `/v1/models`:

```powershell
py -3.12 .\wiki_auswahl.py select `
  --source .\QUELLE-V2.md --output .\selection.json `
  --endpoint http://127.0.0.1:8090 --model qwen3.6-35b `
  --candidate-a lernserver --candidate-b lernserver
```

The six fields are admission (`aufnehmen`), entity, concept, question, duplicate and high priority. The script saves the source hash, complete request, raw response and decoded fields. Our actual 10 October run returned `N, N, N, N, J, N`, using 244 input tokens, 12 output tokens and 11.40 seconds.

## Review and deliver

We read the source and explicitly accepted this teaching note, overriding its admission recommendation:

```powershell
py -3.12 .\wiki_auswahl.py deliver `
  --source .\QUELLE-V2.md --result .\selection.json `
  --project C:\MY-WIKI --reviewed --decision accept
```

`--project` is the project root. Delivery writes the unchanged source to `raw/sources`. Its separate record `QUELLE-V2.md.UEBERGABE.json` is written in the project root. Existing files are preserved. A source changed after selection requires a new selection run.

## Follow the normal Wiki workflow

Our existing portable Wiki app detected the delivered source in project `jt` and wrote `wiki/sources/QUELLE-V2.md`. Search found the page and MCP read back its complete content. Port 8091, context 4096 and the unspecified CPU matched the source; the page retained its fictional status.

Use your own app’s source-watch/import function, then compare source and page, search for the result and read it back. The copying command reports only its own operation; it does not claim the later app processing has happened.

Our experiment used an existing portable app build 0.6.12. This repository contains the selection/integration component, not a new Wiki app installer. Automatic app processing and search worked; an extra manual embedding request returned 401 and is separately recorded.

## Tests and earlier measurements

```powershell
py -3.12 -m unittest discover -s tests -v
```

Five tests cover answer completeness, field/probability mapping, changed sources, explicit review and preservation of existing outputs. Earlier measurements comprised 480 decisions per model; no tested threshold met both 95% precision and 60% coverage. This is why we retain the explicit review step.

Original inspiration: https://github.com/ekzhang/openjev-sglang
