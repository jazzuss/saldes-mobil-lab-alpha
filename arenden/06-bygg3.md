# 3 – Ingen märkte att modellen blev sämre
Etikett: bygg

Förra incidenten hade inte hänt om pipelinen hade testat modellen. Vi har tester på tre
nivåer i `tests/`, men de täcker för lite.

**Uppgift:** skriv minst ett nytt test per nivå.

| Nivå | Fil | Förslag |
| --- | --- | --- |
| Kod | `tests/test_features.py` | Regionnamn med versaler, som `STOCKHOLM`, blir `Stockholm` |
| Data | `tests/test_data.py` | `kund_id` är unikt, åldern ligger i ett rimligt intervall |
| Modell | `tests/test_model.py` | ROC AUC är minst 0,70, och modellen slår en `DummyClassifier` |

**Tänk på:** accuracy duger inte som mått här. Ungefär 81 % av kunderna är kvar, så en
modell som gissar "ingen slutar" får redan 0,81 i accuracy.

**Klart när:**
- [ ] `pytest` är grönt lokalt och i CI.
- [ ] Du har sett prestandatestet bli rött, till exempel genom att tillfälligt höja tröskeln.
