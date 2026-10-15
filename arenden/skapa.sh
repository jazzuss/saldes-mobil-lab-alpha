#!/usr/bin/env bash
# Skapar etiketterna och ett issue per ärende i ditt repo.
#
# Kör från repots rot, i din egen klon:
#   bash arenden/skapa.sh
#
# Kräver GitHub CLI och inloggning (gh auth login). Går att köra flera gånger:
# ärenden som redan finns hoppas över.
set -euo pipefail

cd "$(dirname "$0")"

if ! gh auth status >/dev/null 2>&1; then
  echo "Du är inte inloggad i gh. Kör: gh auth login" >&2
  exit 1
fi

echo "Skapar etiketter..."
gh label create "felsök"    --color d73a4a --description "Något är rött. Hitta felet."      --force
gh label create "bygg"      --color 0e8a16 --description "Bygg något i pipelinen."          --force
gh label create "analysera" --color 1d76db --description "Undersök och svara med siffror." --force

befintliga=$(gh issue list --state all --limit 200 --json title --jq '.[].title')

for fil in [0-9][0-9]-*.md; do
  titel=$(sed -n '1s/^# //p' "$fil")
  etikett=$(sed -n '2s/^Etikett: //p' "$fil")

  if grep -Fxq -- "$titel" <<<"$befintliga"; then
    echo "Finns redan: $titel"
    continue
  fi

  tail -n +4 "$fil" | gh issue create --title "$titel" --label "$etikett" --body-file -
done

echo "Klart. Öppna fliken Issues i ditt repo."
