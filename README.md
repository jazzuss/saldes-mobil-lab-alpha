
## Kom igång

1. Skapa ditt eget repo från mallen: **Use this template → Create a new repository**.
   Välj ditt eget konto och **Public**.
2. Klona det och skapa ärendena som issues (kräver `gh auth login`):

   ```bash
   git clone https://github.com/<ditt-användarnamn>/<ditt-repo>.git
   cd <ditt-repo>
   bash arenden/skapa.sh
   ```

3. Öppna fliken **Actions** och titta på den första körningen. Börja med ärende F1.

## Så kör man det lokalt

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest                          # testerna
python -m churn.model           # tränar, skriver outputs/modell.joblib och outputs/matvarden.json
python -m churn.evaluate        # kvalitetsgrind: felkod om ROC AUC är under tröskeln
python -m churn.score           # skriver outputs/ringlista.csv
```

## Vad som finns här

| Sökväg | Innehåll |
| --- | --- |
| `data/kundbas.csv` | 2 000 kunder: ålder, region, abonnemang, kostnad, dataförbrukning, supportärenden och om kunden avslutat (`avslutat`) |
| `src/churn/data.py` | Inläsning och features |
| `src/churn/model.py` | Träning. Skriver modell och mätvärden till `outputs/` |
| `src/churn/evaluate.py` | Kvalitetsgrind på mätvärdena |
| `src/churn/score.py` | Ringlistan |
| `tests/` | Tester på tre nivåer: kod, data och modell |
| `models/modell.joblib` | Modellen som kundtjänst använder just nu |
| `arenden/` | Ärendena, och `skapa.sh` som gör dem till issues |
| `.github/workflows/ci.yml` | Vårt CI |
