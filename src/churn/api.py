import json
import os
from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from churn.data import FEATURES, MAL, dela_upp, las_data, skapa_features

MODELLFIL = Path(os.environ.get("MODELLFIL", "outputs/modell.joblib"))
MATVARDEN = MODELLFIL.with_name("matvarden.json")

app = FastAPI(title="Saldes churnmodell")
modell = joblib.load(MODELLFIL) if MODELLFIL.exists() else None
matvarden = json.loads(MATVARDEN.read_text()) if MATVARDEN.exists() else {}


class Kund(BaseModel):
    """Indata: en kund, med samma kolumner som i kundbas.csv."""

    alder: int = Field(ge=18, le=100)
    region: Literal["Väst", "Norr", "Stockholm", "Mitt", "Syd"]
    abonnemang: Literal["Bas", "Standard", "Premium"]
    manader_som_kund: int = Field(ge=0)
    manadskostnad: float = Field(gt=0)
    data_gb_per_manad: float = Field(ge=0)
    supportarenden_12m: int = Field(ge=0)


class Prediktion(BaseModel):
    """Utdata: risken att kunden slutar, mellan 0 och 1."""

    risk: float


def kraver_modell() -> None:
    if modell is None:
        raise HTTPException(status_code=503, detail=f"Ingen modell i {MODELLFIL}")


@app.get("/health")
def health() -> dict:
    kraver_modell()
    return {
        "status": "ok",
        "commit": matvarden.get("commit", "okänd"),
        "roc_auc": matvarden.get("roc_auc"),
    }


@app.post("/predict")
def predict(kund: Kund) -> Prediktion:
    kraver_modell()
    X = skapa_features(pd.DataFrame([kund.model_dump()]))[FEATURES]
    return Prediktion(risk=round(float(modell.predict_proba(X)[0, 1]), 3))


@app.get("/ringlista")
def ringlista(antal: int = 10) -> list[dict]:
    kraver_modell()
    kunder = skapa_features(las_data())
    kvar = kunder[kunder[MAL] == 0]
    X, _ = dela_upp(kvar)
    lista = kvar[["kund_id"]].assign(risk=modell.predict_proba(X)[:, 1].round(3))
    lista = lista.sort_values("risk", ascending=False).head(antal)
    return lista.to_dict(orient="records")
