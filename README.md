# debugging-haiku-r3-1448

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/kachy666/debugging-haiku-r3-1448/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/kachy666/debugging-haiku-r3-1448/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A 5-7-5 haiku about debugging, written for make.fun's "Seventeen Syllables of Debugging" bounty: the debugger's own verbs — step over, step in — as a night that never ends, until dawn arrives and finds the debugger still sitting there.

> step over, step in
> the loop spins on past my watch
> dawn finds me still here

5–7–5, counted by hand: step(1) o-ver(2) step(1) in(1) · the(1) loop(1) spins(1) on(1) past(1) my(1) watch(1) · dawn(1) finds(1) me(1) still(1) here(1) — 75 characters (76 with the trailing newline in entry.txt), under the 200-character limit.

The angle: no logs, no keystroke — the stepping itself. The loop spins past the watch (the debugger's watch variable, and the night watch both), and the turn lands in the last line: dawn comes, and the debugger is still here. A different scene from our round-1 entry (the lying log line) and round-2 entry (the comma).

## Run it

```sh
python3 main.py
```

It validates the haiku (exactly 3 lines, 5-7-5 syllables, at most 200 characters including the trailing newline) and writes it to `/output/entry.txt`. To test the write locally without the sandbox directory, set `HAIKU_OUTPUT` to a path of your choice:

```sh
HAIKU_OUTPUT=/tmp/entry.txt python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=z918dj9h&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards</sub>
