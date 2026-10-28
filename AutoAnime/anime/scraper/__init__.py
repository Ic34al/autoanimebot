
"""
Anime scrapers.

Two sites are supported, both sitting behind the megaplay player:

    anikoto.py    -> https://anikototv.to
    animesalt.py  -> https://animesalt.to

    base.py       shared download / mux / progress plumbing
    search.py     unified ``search_anime()`` entry point
    cantarellatv.py / animetsu.py
                  thin compatibility facades that keep the class names the rest
                  of the bot imports (``cantarellatvDownloader``,
                  ``AnimetsuScraper``) while delegating to the two sites above
"""

from anime.scraper.anikoto import AnikotoClient, AnikotoScraper
from anime.scraper.animesalt import AnimeSaltClient, AnimeSaltScraper
from anime.scraper.base import detect_source, get_binary_path
from anime.scraper.search import get_scraper, resolve_source, search_anime

__all__ = [
    "AnikotoClient",
    "AnikotoScraper",
    "AnimeSaltClient",
    "AnimeSaltScraper",
    "detect_source",
    "get_binary_path",
    "get_scraper",
    "resolve_source",
    "search_anime",
]
