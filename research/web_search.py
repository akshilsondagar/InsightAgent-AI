from tavily import TavilyClient

from config.settings import TAVILY_API_KEY


def get_tavily_client():
    """Create and return a Tavily client."""

    if not TAVILY_API_KEY:
        raise ValueError(
            "TAVILY_API_KEY is missing. "
            "Please check your .env file."
        )

    return TavilyClient(
        api_key=TAVILY_API_KEY
    )


def search_web(
    query: str,
    max_results: int = 5
) -> list[dict]:
    """
    Search the web using Tavily.

    Args:
        query: The web search query.
        max_results: Maximum number of results.

    Returns:
        A list of search results.
    """

    try:

        client = get_tavily_client()

        response = client.search(
            query=query,
            max_results=max_results,
            search_depth="basic"
        )

        return response.get("results", [])

    except Exception as error:

        print(
            f"Web search failed for query: {query}"
        )

        print(
            f"Error: {error}"
        )

        return []