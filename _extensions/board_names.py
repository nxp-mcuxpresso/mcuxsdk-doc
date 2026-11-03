"""Board-name matching shared by documentation extensions.

Copyright 2026 NXP
SPDX-License-Identifier: Apache-2.0
"""

from __future__ import annotations

import re


def normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def aliases(name: str) -> set[str]:
    out = {name}
    for prefix in ("evkb", "evkc", "evk9", "evk"):
        if name.startswith(prefix):
            out.add(name[len(prefix):] + prefix)
        if name.endswith(prefix):
            out.add(prefix + name[:-len(prefix)])
    return out
