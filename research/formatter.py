def format_research_results(
    results: list[dict],
    max_content_length: int = 2000
) -> str:
    """
    Convert research results into clean text.

    Args:
        results: List of research result dictionaries.
        max_content_length: Maximum content length per source.

    Returns:
        Formatted research text.
    """

    formatted_sources = []

    for index, result in enumerate(results, start=1):

        title = result.get("title", "No title")
        url = result.get("url", "No URL")
        content = result.get("content", "")

        # Limit content length
        content = content[:max_content_length]

        source_text = f"""
SOURCE {index}

Title: {title}

URL: {url}

Content:
{content}

{'-' * 70}
"""

        formatted_sources.append(source_text)

    return "\n".join(formatted_sources)