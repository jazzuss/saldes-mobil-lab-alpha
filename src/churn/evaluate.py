"""Kvalitetsgrind. Kör:  python -m churn.evaluate [outputs/matvarden.json]

Läser mätvärdena från en tränad modell och avslutar med felkod 1 om ROC AUC är under
tröskeln. Ett steg som avslutar med felkod blir rött i GitHub Actions, och då stoppas
de jobb som väntar på det.

Tröskeln kan ändras med miljövariabeln MIN_ROC_AUC.
"""

import json
import os
import sys
from pathlib import Path

STANDARDTROSKEL = 0.70


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    sokvag = Path(argv[0]) if argv else Path("outputs/matvarden.json")
    troskel = float(os.environ.get("MIN_ROC_AUC", STANDARDTROSKEL))

    if not sokvag.exists():
        print(f"FEL: hittar inte {sokvag}. Har modellen tränats, eller laddats ner hit?")
        return 1

    matvarden = json.loads(sokvag.read_text())
    print(json.dumps(matvarden, indent=2))

    if matvarden["roc_auc"] < troskel:
        print(f"FEL: ROC AUC {matvarden['roc_auc']:.3f} är under tröskeln {troskel:.2f}.")
        return 1
    print(f"OK: ROC AUC {matvarden['roc_auc']:.3f} klarar tröskeln {troskel:.2f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
