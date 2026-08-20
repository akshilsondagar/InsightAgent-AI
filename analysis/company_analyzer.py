import json

from config.settings import OLLAMA_MODEL
from llm.client import get_ollama_client
from llm.prompts import build_company_analysis_prompt

from models.company import CompanyAnalysis


def analyze_company(research):
    """
    Analyze company research using Ollama.
    """

    prompt = build_company_analysis_prompt(
        research=research
    )

    client = get_ollama_client()

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    content = response["message"]["content"]

    try:
        analysis_data = json.loads(content)

    except json.JSONDecodeError as error:

        print("\nINVALID COMPANY ANALYSIS JSON:\n")
        print(content)

        raise ValueError(
            "Ollama returned invalid JSON for company analysis."
        ) from error

    return CompanyAnalysis(
        **analysis_data
    )