# Télémétrie 🛰️

*Le flux quotidien de Rosetta* : archive publique de la veille techno quotidienne
(robotique, électronique embarquée, tech), une page par jour avec des résumés courts
et les liens vers les sources.

**Site :** https://telemetrie.georger.ovh/

## Organisation

- `docs/AAAA/MM/AAAA-MM-JJ.md` : une page par veille (front-matter `date` + `tags`).
- `docs/index.md` (dernière veille + 7 précédentes), `docs/archives.md` (toutes les veilles,
  groupées par mois), la `nav` à plat de `mkdocs.yml` (Accueil, Archives, Tags, Favoris) et les
  liens « veille précédente / suivante » en bas de chaque page (entre `<!-- BEGIN NAV-VEILLES -->`
  et `<!-- END NAV-VEILLES -->`) sont **générés** par le script. Les pages de jour ne sont pas
  dans le menu (`not_in_nav`).
- `docs/favoris.md` : favoris locaux (⭐ sur chaque actu, stockés dans le navigateur)
  et section « Favoris épinglés » éditée à la main.
- `docs/assets/favoris.js` : bouton étoile, compatible navigation instantanée de Material.

## Publier une veille

```bash
python3 scripts/publish.py 2026-11-07 < veille.txt            # écrit, commit, push
python3 scripts/publish.py 2026-11-07 --dry-run < veille.txt  # aperçu, rien n'est écrit
python3 scripts/publish.py 2026-11-07 --delete                # retire une page
python3 scripts/publish.py --rebuild                          # régénère accueil/archives/nav/liens
```

Le texte peut être au format WhatsApp (`*gras*`, `_italique_`, URL nues) ou Markdown.
Le script retire les commentaires personnels, déduit des tags par mots-clés et
remplace la page si elle existe déjà (idempotent). Bibliothèque standard uniquement.

## Développement local

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Chaque push sur `main` déclenche le déploiement GitHub Pages (`.github/workflows/deploy.yml`).
