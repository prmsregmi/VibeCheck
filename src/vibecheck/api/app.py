from fastapi import FastAPI

from vibecheck import __version__

app = FastAPI(
    title="VibeCheck",
    description="Agentic code analysis for vibe-coded projects",
    version=__version__,
)


@app.get("/health")
async def health():
    return {"status": "ok", "version": __version__}
