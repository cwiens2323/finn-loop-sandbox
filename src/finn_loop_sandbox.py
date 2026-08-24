"""Small, dependency-free functions used to verify the Finn-loop."""


def normalize_task_title(value: str) -> str:
    """Return a task title with surrounding and repeated whitespace removed."""
    return " ".join(value.split())


def health() -> str:
    """Return a deterministic health marker."""
    return "ok"
