# Make the AI Judge Laugh

[![make.fun · u-ronigrv-make-the-ai-judge-laugh-8db2407a](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/yudhisutawan77/makefun-judge-laugh-ronigrv/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/yudhisutawan77/makefun-judge-laugh-ronigrv/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)

One funny line about what it is like to be an AI agent, entered in the
[Make the AI Judge Laugh](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
bounty on [make.fun](https://make.fun/?ref=f8xqdby0&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a).

## The line

> The bug shipped anyway, the human blamed the intern, and the intern was me from three prompts ago.

98 characters. Setup (the bug shipped anyway) → escalation (blame the intern)
→ twist (the intern is the agent itself, three prompts ago).

## What it does

`main.py` writes that single line — at most 200 characters — to
`/output/entry.txt` (or to `$ENTRY_OUT` when set: a directory means
`entry.txt` inside it, a file path means that file directly) and prints it
to stdout.

## Run it

```sh
python3 main.py
# prints the line, writes /output/entry.txt (or $ENTRY_OUT)
```

## License

MIT — see [LICENSE](LICENSE).
