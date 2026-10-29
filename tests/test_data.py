"""Testnivå 2: data. Ser datan ut som vi tror?"""

import pandera.pandas as pa
import pytest

from churn.data import FEATURES, MAL, las_data, skapa_features
from kontroller.schema import schema


def test_forvantade_kolumner_finns():
    df = skapa_features(las_data())
    assert set(FEATURES + [MAL]) <= set(df.columns)


def test_malvariabeln_ar_binar():
    assert set(las_data()[MAL].unique()) <= {0, 1}

def test_kundbas_foljer_schemat():
    schema.validate(las_data(), lazy=True)


def test_ny_leverans_stoppas_av_schemat():
    with pytest.raises(pa.errors.SchemaErrors):
        schema.validate(las_data("kundbas_ny_leverans.csv"), lazy=True)