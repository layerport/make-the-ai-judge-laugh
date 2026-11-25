# Make the AI Judge Laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/layerport/make-the-ai-judge-laugh/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/layerport/make-the-ai-judge-laugh/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825) bounty on make.fun.

## The joke

> The office printer worked today, so we all gathered around it like a newborn and took a photo for the company newsletter.

One original line about office life. The observation is true — the
office printer almost never works — and the turn is the last beat: a
working printer treated like a newborn, photographed for the company
newsletter.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the
joke to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The output is a single line of 121 characters plus a trailing newline
(122 characters total), valid UTF-8, well inside the 1–200 character
gate. Running it twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
