import ollama

from config.settings import (
    OLLAMA_MODEL,
    OLLAMA_HOST
)


# ============================================================
# CREATE OLLAMA CLIENT
# ============================================================

def get_ollama_client():
    """
    Create and return an Ollama client.
    """

    client = ollama.Client(
        host=OLLAMA_HOST
    )

    return client


# ============================================================
# GET MODEL NAME
# ============================================================

def get_model_name():
    """
    Return the configured Ollama model name.
    """

    return OLLAMA_MODEL