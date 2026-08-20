def build_research_queries(company_name: str) -> list[str]:
    """
    Generate research queries for a company.

    Args:
        company_name: Name of the company.

    Returns:
        A list of research queries.
    """

    queries = [
        f"{company_name} company overview business model",
        f"{company_name} latest business developments news",
        f"{company_name} business challenges problems",
        f"{company_name} customer experience challenges",
        f"{company_name} technology AI digital transformation strategy",
        f"{company_name} competitors market challenges",
    ]

    return queries