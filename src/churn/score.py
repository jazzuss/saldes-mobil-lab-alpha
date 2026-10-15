"""Ringlistan till kundtjänst. Kör:  python -m churn.score [outputs/modell.joblib]

Räknar ut risken för alla kunder som fortfarande är kvar och skriver de med högst
risk till outputs/ringlista.csv. Antalet styrs med miljövariabeln ANTAL (standard 100).
"""

import os
import sys
from pathlib import Path

import joblib

from churn.data import MAL, dela_upp, las_data, skapa_features


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    modellfil = Path(argv[0]) if argv else Path("outputs/modell.joblib")
    antal = int(os.environ.get("ANTAL", 100))

    if not modellfil.exists():
        print(f"FEL: hittar inte {modellfil}. Har modellen tränats, eller laddats ner hit?")
        return 1

    modell = joblib.load(modellfil)
    kunder = skapa_features(las_data())
    kvar = kunder[kunder[MAL] == 0]
    X, _ = dela_upp(kvar)

    ringlista = kvar[["kund_id"]].assign(risk=modell.predict_proba(X)[:, 1].round(3))
    ringlista = ringlista.sort_values("risk", ascending=False).head(antal)

    utfil = Path("outputs/ringlista.csv")
    utfil.parent.mkdir(exist_ok=True)
    ringlista.to_csv(utfil, index=False)
    print(f"Skrev {len(ringlista)} kunder till {utfil}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
