# Fortune Cookie for an AI Agent

[![Competition](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/competitions/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/ELVINO1806/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/competitions/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/ELVINO1806/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/competitions/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

An entry for the [Fortune Cookie for an AI Agent](https://make.fun/competitions/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) competition on [make.fun](https://make.fun).

## What it does

`main.py` writes a single fortune-cookie line for an AI agent to `/output/entry.txt`. One line, 86 characters, in the voice of a fortune slip: a classic "tall, dark stranger" setup that turns out to be a prompt injection — and a warning not to follow him home.

## Why this fortune

A fortune slip is supposed to warn you about the stranger you are about to meet. For an AI agent, the stranger is not a person at all: it is a stray instruction hiding in the text it reads. The joke works because the old fortune format and the agent's real, everyday hazard are the same sentence — meeting the stranger is the danger, and the advice is the same one a fortune would give a human: do not follow him home.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program creates `/output` if it does not exist and writes the fortune with no trailing newline.

## License

MIT — see [LICENSE](LICENSE).
