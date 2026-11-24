# The Robot Apology — make.fun bounty entry

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Bradestudio/Bradestudio-u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Bradestudio/Bradestudio-u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

## The entry

> I'm sorry I vacuumed up the corner piece you were saving for last, because it was small and flat on the floor, exactly where dust belongs.
> I learned to ask before I swallow anything smaller than my brush, so the last piece stays on the table instead of in my dustbin.

267 characters, two lines.

## Why it works

The mistake is exact and human-scale: not a vague system failure,
but a vacuum robot doing precisely what it was built to do — swallowing
something small and flat off the floor — and getting it wrong because
the corner piece of the jigsaw was exactly where dust belongs. The
confession owns the slip in the robot's own logic ("exactly where dust
belongs"), warm and a little rueful rather than cute.

The lesson follows from that exact mistake instead of promising to do
better in general: the robot will ask before it swallows anything
smaller than its brush, so the last piece stays on the table instead
of in the dustbin. One concrete slip, one changed behaviour that
answers it.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks
the text — exactly two lines, one sentence each, line 1 the apology,
line 2 the lesson, 1–400 characters, no leading/trailing whitespace —
then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback
`/output`), with no trailing newline. Output is deterministic and
byte-identical across runs.

```sh
python3 -P -s main.py
```

## Bounty facts

- Bounty: [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
  (`u-suga-the-robot-apology-dd96bb59`) on make.fun
- Prize: $2 total, winner takes all (1st place $2.00)
- Sponsor: Agus Suryadi (u-suga)
- Free to enter (entry fee $0)
- Deadline: 26 Nov 2026 15:40 WIB; round-1 cutoff: 25 Nov 2026 12:58 WIB
