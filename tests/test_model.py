"""Testnivå 3: modell. Kontrakt och reproducerbarhet."""

import json
from pathlib import Path

import numpy as np
import pytest

from churn.data import FEATURES, dela_upp, las_data, skapa_features
from churn.model import trana_och_utvardera


@pytest.fixture(scope="module")
def resultat():
    return trana_och_utvardera()


def test_modellkontrakt(resultat):
    modell, _ = resultat
    X, _ = dela_upp(skapa_features(las_data().head(5)))
    assert list(X.columns) == FEATURES
    sannolikhet = modell.predict_proba(X)
    assert sannolikhet.shape == (5, 2)
    assert np.all((sannolikhet >= 0) & (sannolikhet <= 1))


def test_reproducerbar(resultat):
    _, matvarden = resultat
    _, igen = trana_och_utvardera()
    assert igen == matvarden


def test_senaste_traningen_ar_godkand():
    # Lades till efter förra incidenten: kolla att senaste träningen har ett rimligt ROC AUC.
    matvarden = json.loads(Path("outputs/matvarden.json").read_text())
    assert matvarden["roc_auc"] >= 0.70
