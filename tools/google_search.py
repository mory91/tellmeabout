from typing import Iterable

from googlesearch import search  # type: ignore


def get_profile_url(name: str) -> Iterable[str]:
    """Searches for linkedin profile page."""
    res = search(name, advanced=True)
    return [r for r in res]
