"""Testnivå 3: modell. Kontrakt och reproducerbarhet."""
import os
import numpy as np
import pytest
from churn.evaluate import STANDARDTROSKEL
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from churn.data import FEATURES, dela_upp, las_data, skapa_features
from churn.model import SEED, trana_och_utvardera

ROC_AUC_TROSKEL = float(os.environ.get("MIN_ROC_AUC", STANDARDTROSKEL))

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

def test_roc_auc_over_troskeln(resultat):
    _, matvarden = resultat
    assert matvarden["roc_auc"] >= ROC_AUC_TROSKEL


def test_modellen_slar_dummy(resultat):
    _, matvarden = resultat
    X, y = dela_upp(skapa_features(las_data()))
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=SEED, stratify=y
    )
    dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    dummy_auc = roc_auc_score(y_test, dummy.predict_proba(X_test)[:, 1])
    assert matvarden["roc_auc"] > dummy_auc