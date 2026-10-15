# 7 – Tre pushar i rad ger tre körningar
Etikett: bygg

När man pushar tre gånger på en minut körs tre hela pipelines, fast bara den sista spelar roll.

**Uppgift:** se till att en ny push avbryter körningen som redan pågår på samma gren, men
aldrig körningar på andra grenar.

**Klart när:**
- [ ] Två snabba pushar i rad ger en avbruten och en färdig körning i Actions.
