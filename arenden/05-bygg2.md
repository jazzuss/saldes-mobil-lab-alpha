# 2 – Det funkar i CI men inte på servern
Etikett: bygg

Servern som gör ringlistan kör Python 3.11. CI testar bara på 3.13. Vi vill uppgradera
servern under året, så koden måste fungera på 3.11, 3.12 och 3.13.

**Uppgift:**
1. Kör testerna på alla tre versionerna parallellt.
2. Se till att ett fel på en version inte avbryter de andra, så att du ser exakt vilka som fungerar.
3. Dela upp workflowet i jobb: tester i ett jobb, träning i ett annat som bara startar om
   testerna är gröna. Träningen ska köras på samma version som servern.

**Klart när:**
- [ ] Tre testjobb syns i körningen, ett per Python-version.
- [ ] Träningen är ett eget jobb som väntar på testerna.
