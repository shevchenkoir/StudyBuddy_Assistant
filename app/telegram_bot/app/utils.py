def clamp_len(s: str, n: int = 4000) -> str:
    return s if len(s) <= n else s[: n-3] + "..."
