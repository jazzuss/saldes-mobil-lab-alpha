# 6 – En README-ändring startar träning
Etikett: bygg

Igår rättade någon ett stavfel i README:n. Det startade hela pipelinen, med träning och allt.

**Uppgift:** begränsa när workflowet startar, så att bara ändringar i kod, data, tester,
beroenden eller workflowet självt startar det.

**Tänk på:** om ett jobb är ett krav för merge (ärende 5) och workflowet inte startar alls,
vad händer då med en pull request som bara ändrar README:n? Skriv vad du ser.

**Klart när:**
- [ ] En commit som bara ändrar README:n startar ingen körning.
- [ ] En commit i `src/` gör det.
