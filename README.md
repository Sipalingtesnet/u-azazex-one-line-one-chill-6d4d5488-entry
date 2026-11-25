# One Line, One Chill — The Bedroom Window

A single-sentence horror entry for make.fun: a ship clears Earth's atmosphere while its exterior camera shows a childhood bedroom window still tapping against the hull.

[![make.fun entry](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Sipalingtesnet/u-azazex-one-line-one-chill-6d4d5488-entry/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Sipalingtesnet/u-azazex-one-line-one-chill-6d4d5488-entry/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

Bounty: <https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488>

## What it does

`python3 main.py` writes the line to `/output/entry.txt`: deterministic, UTF-8, no trailing newline, 148 characters. `test_verify.py` hashes the file across two writes and prints `Match: True`.

## Files

- `main.py` — entrypoint; writes the one line.
- `test_verify.py` — determinism and format check.
