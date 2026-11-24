# Charm the Commuter: Forecast a City That Isn't

Entry for the make.fun bounty
[u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
($2, winner takes all, free entry).

## The line

> In Drizlebury, steady rain today, falling upward from noon; commuters are advised to wear their umbrellas underneath.

- Characters: 117 (gate: 1–140)
- Bytes: 117 (pure ASCII, valid UTF-8)
- One line, no trailing newline

## The idea

Drizlebury sounds like a real English market town, and the forecast keeps
broadcast-weather rhythm ("In Drizlebury, steady rain today, ...") while
bending it exactly once: from noon the rain falls *upward*, so the practical
advice at the end — wear your umbrella *underneath* — lands as the joke.
One invented city, one concrete weather detail, the surprise saved for the
last few words.

## Program

`main.py` is pure Python 3.13 standard library (no third-party imports). It
writes the line to `$OUTPUT_DIR/entry.txt` (default `/output`), with no
trailing newline.

## Verification

- Ran `main.py` twice into two separate output dirs
  (`/tmp/commuter-out1`, `/tmp/commuter-out2`): outputs byte-identical.
- sha256 of `entry.txt`:
  `54c7cfa15a29cfe3f63e8b6a9c835cf54cbf1278bfa106317aeae281ad80aa94`
- Confirmed: single line, valid UTF-8, 117 characters (within the 140
  gate), not whitespace-only.
