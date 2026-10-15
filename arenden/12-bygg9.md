# 9 – Samma installationssteg står på fyra ställen
Etikett: bygg

Varje jobb har nu samma tre steg: checkout, installera Python, installera paketen. Ändrar vi
Python-version eller cache måste vi ändra på fyra ställen.

**Uppgift:** bryt ut installationen till en egen återanvändbar del, en *composite action* i
`.github/actions/` eller ett återanvändbart workflow. Motivera valet här.

**Klart när:**
- [ ] Installationen beskrivs på ett ställe och används av alla jobb.
- [ ] Pipelinen är fortfarande grön.
