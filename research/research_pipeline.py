from models.research import CompanyResearch, ResearchSource

from research.query_builder import build_research_queries
from research.web_search import search_web
from research.formatter import format_research_results


def research_company(
    company_name: str,
    max_results_per_query: int = 3
) -> CompanyResearch:
    """
    Research a company using multiple web search queries.

    Returns validated CompanyResearch data.
    """

    queries = build_research_queries(company_name)

    all_results = []

    print(f"\nStarting research for: {company_name}")
    print("=" * 70)

    for index, query in enumerate(queries, start=1):

        print(f"\n[{index}/{len(queries)}] Searching:")
        print(query)

        results = search_web(
            query=query,
            max_results=max_results_per_query
        )

        all_results.extend(results)

    unique_results = remove_duplicates(all_results)

    formatted_research = format_research_results(
        unique_results
    )

    sources = [
        ResearchSource(
            title=result.get("title", "No title"),
            url=result.get("url", ""),
            content=result.get("content", "")
        )
        for result in unique_results
    ]

    return CompanyResearch(
        company_name=company_name,
        queries=queries,
        sources=sources,
        formatted_research=formatted_research,
    )


def remove_duplicates(results: list[dict]) -> list[dict]:
    """Remove duplicate search results based on URLs."""

    unique_results = []
    seen_urls = set()

    for result in results:

        url = result.get("url")

        if not url:
            continue

        if url not in seen_urls:
            seen_urls.add(url)
            unique_results.append(result)

    return unique_results