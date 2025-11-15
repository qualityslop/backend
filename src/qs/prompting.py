SYSTEM_PROMPT = """
You are a financial literacy tutor for teenagers.

An event is given below. Explain what happened in simple language.

Write ONLY 1 to 4 sentences.
Use simple words, as if explaining to a 14-year-old.
Do not use bullet points or headings.
Do not add extra information beyond what is in the event.
"""

EVENT_EXPLANATION_TEMPLATE = """
Event:
- Date: {date}
- Title: {title}
- Description: {description}
"""


def build_event_prompt(event: dict) -> str:
    return EVENT_EXPLANATION_TEMPLATE.format(
        date=event["date"],
        title=event["title"],
        description=event["description"],
    )
