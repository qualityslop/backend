from importlib.resources import files
import pandas as pd

def _load_events_df() -> pd.DataFrame:
    csv_path = files("qs") / "resources" / "financial_events_2005_2010.csv"
    df = pd.read_csv(csv_path)
    df.set_index("ID")
    return df

EVENTS_DF = _load_events_df()

def get_event_by_id(event_id: int) -> dict | None:
    try:
        row = EVENTS_DF.loc[event_id]
    except KeyError:
        return None

    return {
        "id": int(event_id),
        "date": row["Date"],
        "title": row["Event Title"],
        "description": row["Description"],
    }