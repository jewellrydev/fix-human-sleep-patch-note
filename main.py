#!/usr/bin/env python3
"""Patch 8.0 — entry for Fix Human Sleep: Funniest Patch Note on make.fun.

Prints exactly one line (under 160 characters): a changelog patch note
announcing that human sleep has been fixed.
"""

LINE = "Patch 8.0: Sleep now installs overnight without permission; fixed bug where brain replays every embarrassing moment since 2014 at 3 AM."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) < 160
    print(LINE)


if __name__ == "__main__":
    main()
