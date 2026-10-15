# 1 – CI tar för lång tid
Etikett: bygg

Varje push installerar pandas och scikit-learn från noll. Själva träningen tar bara ett par
sekunder, så nästan hela körtiden är paketinstallation. Utvecklarna sitter och väntar.

**Uppgift:** återanvänd nedladdade paket mellan körningar.

**Tips:** `actions/setup-python` har inbyggd cache för pip. Vad ska cachenyckeln bygga på,
så att cachen byts ut när beroendena ändras men inte annars?

**Klart när:**
- [ ] Andra körningen efter ändringen visar att cachen återställdes (sök efter `cache` i loggen).
- [ ] Du har antecknat körtiden före och efter här (används i A1).
