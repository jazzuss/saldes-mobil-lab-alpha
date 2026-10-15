# 4 – Vilken modell fick kundtjänst egentligen?
Etikett: bygg

Modellen i `models/modell.joblib` är incheckad för hand. Vi vet inte från vilken commit eller
vilken data den kom. Modellfiler ska inte ligga i Git.

**Uppgift:**
1. Låt träningsjobbet ladda upp `outputs/` (modell och mätvärden) som en artefakt. Namnet
   ska innehålla commitens SHA.
2. Skapa ett jobb **utvärdera** som laddar ner artefakten och kör
   `python -m churn.evaluate`. Pipelinen ska bli röd om modellen är under tröskeln.
3. Skriv mätvärdena i körningens sammanfattning (Summary), så att en granskare ser dem
   utan att ladda ner något.
4. Ta bort `models/modell.joblib` ur repot och se till att modellfiler inte checkas in igen.

**Tips:** varje jobb startar på en ny, tom runner. Filer flyttas mellan jobb med
`actions/upload-artifact` och `actions/download-artifact`. Kolla `matvarden.json`:
`model.py` skriver redan in commit och en kontrollsumma för datan.

**Klart när:**
- [ ] Artefakten `modell-<sha>` syns längst ner på körningens sida.
- [ ] Mätvärdena syns i Summary.
- [ ] `models/` är borta, och `.gitignore` stoppar modellfiler.
