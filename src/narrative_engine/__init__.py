"""Narrative Engine: an RPG/narrative engine exposed as an HTTP API.

The package is split into four layers. Dependencies only point inward:

    api  ->  application  ->  domain
    infrastructure  ->  application (implements its ports)

See docs/architecture.md for the full picture.
"""
