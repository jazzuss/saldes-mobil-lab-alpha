# 8 – Ringlistan görs för hand varje måndag
Etikett: bygg

Varje måndag morgon kör någon `python -m churn.score` på sin dator och mejlar filen till
kundtjänst. Blir hen sjuk blir det ingen ringlista.

**Uppgift:**
1. Lägg till ett jobb **ringlista** som laddar ner den godkända modellen, kör
   `python -m churn.score` och laddar upp `ringlista.csv` som artefakt. Det ska bara köras
   på main, aldrig på en pull request.
2. Låt hela pipelinen köras av sig själv varje måndag 06:00 svensk tid.
3. Lägg till en knapp för att köra pipelinen manuellt.

**Tänk på:** schemat anges med cron i UTC. Vad blir 06:00 svensk tid före och efter
omställningen till vintertid?

**Klart när:**
- [ ] En manuell körning på main ger en artefakt med ringlistan.
- [ ] Körningar på pull requests hoppar över ringlistan (grått jobb).
