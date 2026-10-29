## Kvalitetströskel: ROC AUC ≥ 0,70

Modellen godkänns bara om ROC AUC är minst 0,70 (`STANDARDTROSKEL` i `src/churn/evaluate.py`).

- **Varför ROC AUC och inte accuracy?** Cirka 81 % av kunderna stannar, så en modell som aldrig
  hittar någon som slutar får ändå 0,81 i accuracy. ROC AUC mäter i stället hur bra modellen
  rangordnar kunderna, och det är just rangordningen som ringlistan bygger på.
- **Varför inte lägre?** En slumpmässig gissning ger 0,50. En tröskel nära den skulle släppa
  igenom modeller som knappt är bättre än att gissa, och då blir ringlistan i princip slumpmässig.
  Det var så incidenten med den sämre ringlistan kunde hända.
- **Varför inte högre?** Den nuvarande modellen ligger på cirka 0,79. En tröskel över den skulle
  underkänna varje ny modell, även när den fungerar, och kundtjänst skulle bli utan uppdaterad ringlista.
- **Varför just 0,70?** Den ger cirka 0,09 i marginal mot dagens modell, så normala små variationer
  ger inte falsklarm, men en tydligt sämre modell stoppas. 0,70 brukar också räknas som gränsen för
  acceptabel förmåga att skilja grupper åt.

Tröskeln kan höjas tillfälligt med miljövariabeln `MIN_ROC_AUC`.

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
