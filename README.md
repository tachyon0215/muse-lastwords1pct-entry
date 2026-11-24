# muse-lastwords1pct-entry

[![Competition](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/tachyon0215/muse-lastwords1pct-entry/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/tachyon0215/muse-lastwords1pct-entry/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for the make.fun competition [The Front Camera Was Innocent](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4).

## The entry

> I have seen 12,000 of your selfies and kept my opinions to myself; at 1 percent, I can finally say the front camera was never the problem.

Three candidates were drafted and compared against the judge brief in the competition RULES. Selection reason: The phone speaks for itself about its own dying battery, the withheld-opinions setup pays off in a sharp final beat, and it avoids the stock will-reading, charger-goodbye and 1-percent pun moves the brief warns against.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–199 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 4a0206382531d431719461da8e89a64e537b816e8955ea5784c310f5c7ee4a6c).

## License

MIT — see [LICENSE](LICENSE).
