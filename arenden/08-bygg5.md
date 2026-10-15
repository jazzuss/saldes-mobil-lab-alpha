# 5 – Bara testad kod till main
Etikett: bygg

Från och med nu ska ingen kunna lägga något på main som inte har passerat testerna och
utvärderingen.

**Uppgift:**
1. Låt workflowet köras på pull requests mot main.
2. Lägg in en regel för main (Settings → Branches eller Rules): pull request krävs, och
   testjobben och utvärderingsjobbet måste vara gröna innan merge.
3. Prova: gör en gren där modellen blir sämre (höj till exempel tröskeln med miljövariabeln
   `MIN_ROC_AUC`, eller ta bort en feature i en kopia). Öppna en pull request.

**Klart när:**
- [ ] Pull requesten med den sämre modellen är röd och går inte att merga.
- [ ] Du har länkat den här.
