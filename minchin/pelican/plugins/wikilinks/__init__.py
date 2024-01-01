import logging

from pelican import signals

from .constants import __version__  # NOQA
from .wikilinks import replace_wikilinks


def register():
    """Register the plugin pieces with Pelican."""

    signals.all_generators_finalized.connect(replace_wikilinks)
