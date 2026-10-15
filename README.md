# Churnmodellen – Saldes Mobil AB

> *Saldes Mobil AB är ett påhittat företag och all kunddata är fiktiv. Repot är en övning i
> kursen Kontinuerlig integration och leverans (MLOps25, Nackademin).*

## Välkommen till teamet

Hej och välkommen!

Kul att du börjar hos oss som MLOps-ingenjör. Här är bakgrunden till ditt första uppdrag.

Vi tappar kunder. Analysteamet har byggt en modell som förutsäger vilka kunder som riskerar
att säga upp sitt abonnemang. Varje måndag får kundtjänst en **ringlista** med de kunder som
har högst risk, och ringer dem med ett erbjudande.

I dag sköts det mesta för hand. Modellen tränas på en dator här på kontoret, och modellfilen
ligger incheckad i `models/`. Ringlistan gör någon varje måndag morgon med kommandona nedan.
Vi har ett CI-workflow, men det kör allt i ett enda jobb, installerar om alla paket vid
varje push och testar på en annan Python-version än servern som gör ringlistan (3.11).
Sedan förra veckan är det dessutom rött, och ingen har hunnit ta reda på varför.

För två veckor sedan gick det riktigt fel. Kundtjänst fick en ringlista från en modell som
var sämre än den förra. Ingen märkte det förrän säljarna klagade, och ingen kunde säga vilken
commit eller vilken data modellen kom från.

**Ditt uppdrag:** se till att bara en testad modell med känd härkomst kan bli en ringlista.
Jag har skrivit ärenden åt dig, se *Kom igång* nedan.

Två regler:

- Ändra inte modellen, datan eller feature-koden i `src/churn/data.py`. Den sköter
  analysteamet. Ditt arbete är workflows, tester och inställningar i repot.
- Ingen pushar direkt till main när vi väl har skydd på plats. Allt går via pull requests.

Lycka till, och fråga hellre en gång för mycket.

*Teamleaden*

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
