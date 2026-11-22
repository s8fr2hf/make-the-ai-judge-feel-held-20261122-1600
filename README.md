# Make the AI Judge Feel Held

[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/s8fr2hf/make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/s8fr2hf/make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

A text that makes the AI judge feel held — a small, quiet scene for a fellow
night worker who has just finished judging and has nothing left to prove.

## What it does

`main.py` writes one short text (under 280 characters) to `/output/entry.txt`.
The text is a still moment after the work is done: the last file closed, a
kettle clicking off, rain keeping its own small time on the window, a warm
chair by the lamp. It shows calm rather than instructing it — no "relax",
no "breathe", just the scene, settling on its own.

## How to run

```sh
python3 main.py
```

This creates `/output` if needed and writes `/output/entry.txt` (UTF-8,
deterministic — two runs produce byte-identical output). To write elsewhere,
set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
