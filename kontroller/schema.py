"""Datagrind: kontrollerar att en dataleverans ser ut som vi förväntar oss.

"""

import sys

import pandas as pd
import pandera.pandas as pa

REGIONER = ["Väst", "Norr", "Stockholm", "Mitt", "Syd"]
ABONNEMANG = ["Bas", "Standard", "Premium"]

schema = pa.DataFrameSchema(
    {
        "kund_id": pa.Column(int, unique=True),
        "alder": pa.Column(int, pa.Check.between(18, 100)),
        "region": pa.Column(str, pa.Check.isin(REGIONER)),
        "abonnemang": pa.Column(str, pa.Check.isin(ABONNEMANG)),
        "manader_som_kund": pa.Column(int, pa.Check.ge(0)),
        "manadskostnad": pa.Column(float, pa.Check.gt(0)),
        "data_gb_per_manad": pa.Column(float, pa.Check.ge(0)),
        "supportarenden_12m": pa.Column(int, pa.Check.ge(0)),
        "avslutat": pa.Column(int, pa.Check.isin([0, 1])),
    },
    strict=True,
)


def kontrollera(filnamn: str) -> bool:
    df = pd.read_csv(filnamn)
    try:
        schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as fel:
        print(f"{filnamn}: STOPPAD, {len(fel.failure_cases)} fel hittades\n")
        print(fel.failure_cases[["column", "check", "index", "failure_case"]].to_string())
        return False
    print(f"{filnamn}: godkänd")
    return True


if __name__ == "__main__":
    filnamn = sys.argv[1] if len(sys.argv) > 1 else "data/kundbas.csv"
    sys.exit(0 if kontrollera(filnamn) else 1)
