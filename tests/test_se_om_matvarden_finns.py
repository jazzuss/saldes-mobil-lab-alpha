import json
from pathlib import Path

def test_senaste_traningen_ar_godkand():
    # Lades till efter förra incidenten: kolla att senaste träningen har ett rimligt ROC AUC.
    matvarden = json.loads(Path("outputs/matvarden.json").read_text())
    assert matvarden["roc_auc"] >= 0.70