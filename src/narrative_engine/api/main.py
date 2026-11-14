"""Application entry point: creates the FastAPI app.

Run it in development with:

    uv run fastapi dev src/narrative_engine/api/main.py
"""

from importlib.metadata import version

from fastapi import FastAPI

app = FastAPI(
    title="Narrative Engine API",
    summary="RPG/narrative engine: character sheets, world state, inventory and narration.",
    # Read the version from pyproject.toml so it is declared in one place only.
    version=version("narrative-engine-api"),
)


@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
    """Liveness probe: the process is up and can answer HTTP requests.

    It does not check PostgreSQL or Redis on purpose. A readiness probe that does
    can be added when the API starts to depend on them.
    """
    return {"status": "ok"}
