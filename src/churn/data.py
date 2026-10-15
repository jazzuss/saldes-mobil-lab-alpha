"""Inläsning och feature-kod. Rena funktioner, så att de går att enhetstesta.

Ändra inte den här filen i övningarna. Arbetet handlar om pipelinen, inte om modellen.
"""

from pathlib import Path

import pandas as pd

DATAKATALOG = Path(__file__).resolve().parents[2] / "data"

MAL = "avslutat"
NUMERISKA = [
    "alder",
    "manader_som_kund",
    "manadskostnad",
    "data_gb_per_manad",
    "supportarenden_12m",
    "kostnad_per_gb",
]
KATEGORISKA = ["region", "abonnemang"]
FEATURES = NUMERISKA + KATEGORISKA


def las_data(filnamn: str = "kundbas.csv") -> pd.DataFrame:
    return pd.read_csv(DATAKATALOG / filnamn)


def skapa_features(df: pd.DataFrame) -> pd.DataFrame:
    """Lägger till härledda kolumner. Ändrar inte indata."""
    ut = df.copy()
    # +1 så att kunder utan dataförbrukning inte ger division med noll
    ut["kostnad_per_gb"] = ut["manadskostnad"] / (ut["data_gb_per_manad"] + 1)
    ut["region"] = ut["region"].str.strip().str.title()
    return ut


def dela_upp(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    return df[FEATURES], df[MAL]
