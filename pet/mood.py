def mood_from_idle_days(days: int) -> str:
    if days <= 0:
        return "idle"
    if days < 4:
        return "hungry"
    return "ghost"
