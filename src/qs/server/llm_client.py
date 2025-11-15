from openai import OpenAI
from qs.server import get_settings
from qs.prompting import SYSTEM_PROMPT

settings = get_settings()
client = OpenAI(api_key=settings.openai.api_key)


def call_llm(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5.1",
        input=[
            {
                "role": "developer",
                "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
            },
            {"role": "user", "content": [{"type": "input_text", "text": prompt}]},
        ],
        text={"format": {"type": "text"}, "verbosity": "medium"},
        reasoning={"effort": "medium", "summary": "auto"},
        tools=[],
        store=False,
        include=["reasoning.encrypted_content", "web_search_call.action.sources"],
    )

    return response.output_text
