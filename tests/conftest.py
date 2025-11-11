import pytest
import asyncio

@pytest.fixture(scope="session")
def event_loop():
    """Créer un event loop pour les tests asynchrones."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
