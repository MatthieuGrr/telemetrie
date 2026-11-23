---
title: "Télémétrie"
description: "Le flux quotidien de Rosetta — veille robotique, embarqué et tech"
hide:
  - navigation
  - toc
search:
  exclude: true
---

<div class="hero" markdown>

# Télémétrie 🛰️

Le flux quotidien de Rosetta : chaque matin, une poignée d'actus en robotique, électronique embarquée et tech, résumées en quelques lignes, avec le lien vers la source.
{ .hero-baseline }

[Lire la veille du jour](2026/11/2026-11-23.md){ .md-button .md-button--primary } [Archives](archives.md){ .md-button } [Thèmes](tags.md){ .md-button } [Flux RSS](feed.xml){ .md-button }
{ .hero-actions }

</div>

## [Lundi 23 novembre 2026](2026/11/2026-11-23.md) { .jour }

**7 actus** · 3 min de lecture
{ .veille-meta }

<section class="actu" markdown>

### Rendre une application ROS 2 déterministe, et la simuler plus vite { #rendre-une-application-ros-2-deterministe-et-la-simuler-plus-vite data-fav="2026/11/2026-11-23/#rendre-une-application-ros-2-deterministe-et-la-simuler-plus-vite" }

Avec le publish/subscribe asynchrone de ROS 2, le comportement d'une application peut changer d'une exécution à l'autre selon l'ordonnancement et la machine : les bugs deviennent difficiles à reproduire et les tests peu fiables. Les auteurs imposent à chaque composant de lire ses entrées et d'écrire ses sorties à des instants fixés à l'avance, ce qui rend l'application déterministe. Comme les dépendances entre activations sont alors connues avant l'exécution, un simulateur peut les lancer en parallèle, hors ordre, sans modifier ni l'application ni ROS 2. Le papier est évalué sur des cas industriels.

[arXiv](https://arxiv.org/abs/2611.26676){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [recherche](themes/recherche.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### OpenRing : zéro interblocage pour des AGV sur voies à sens unique { #openring-zero-interblocage-pour-des-agv-sur-voies-a-sens-unique data-fav="2026/11/2026-11-23/#openring-zero-interblocage-pour-des-agv-sur-voies-a-sens-unique" }

Sur un sol d'entrepôt à sens unique, un véhicule en retard ou un planificateur qui plante peut refermer un « anneau » de segments pleins, et plus rien ne bouge. OpenRing laisse le planificateur proposer les routes, mais une garde locale ne valide que les mouvements qui ne peuvent pas refermer d'anneau. Résultat : trois planificateurs se bloquent dans 80 essais sur 126 sans la garde, aucun avec, pour un débit équivalent ou meilleur. Le papier chiffre aussi le prix de cette garantie en débit maximal par segment.

[arXiv](https://arxiv.org/abs/2611.27127){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [recherche](themes/recherche.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### Un LLM embarqué qui réfléchit pendant que le robot roule { #un-llm-embarque-qui-reflechit-pendant-que-le-robot-roule data-fav="2026/11/2026-11-23/#un-llm-embarque-qui-reflechit-pendant-que-le-robot-roule" }

Sur un robot, un modèle de langage peut raisonner presque une minute pendant que les piétons continuent de bouger. Les « staleness deadlines » fixent, à partir de prédictions de trajectoires calibrées, jusqu'à quand le robot peut suivre son plan actuel avant de devoir freiner. Tout nouveau plan doit repasser le même contrôle de dégagement avant d'être adopté. Sur 81 000 missions simulées, le raisonnement complet divise par vingt les mauvaises décisions, et attendre jusqu'à l'échéance réduit les arrivées tardives de 64 %.

[arXiv](https://arxiv.org/abs/2611.26858){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [embarqué](themes/embarque.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### Instant-LIVO : odométrie LiDAR-inertielle-visuelle légère { #instant-livo-odometrie-lidar-inertielle-visuelle-legere data-fav="2026/11/2026-11-23/#instant-livo-odometrie-lidar-inertielle-visuelle-legere" }

Ce système de fusion LiDAR + IMU + caméra fortement couplé s'appuie sur une carte voxel compacte indexée par hachage et sur une carte visuelle limitée à une seule image de référence. Sur 32 jeux de données, il tourne environ 2 fois plus vite que les méthodes de référence sur x86 comme sur ARM, avec une mémoire de pointe divisée par 13 à 20 et une précision comparable.

[arXiv](https://arxiv.org/abs/2611.27633){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [recherche](themes/recherche.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### Valider un LiDAR simulé avec seulement des boîtes 3D { #valider-un-lidar-simule-avec-seulement-des-boites-3d data-fav="2026/11/2026-11-23/#valider-un-lidar-simule-avec-seulement-des-boites-3d" }

Une méthode simple pour savoir si le LiDAR simulé (ici sous CARLA) ressemble au vrai : comparer la densité de points sur les objets annotés en fonction de la distance. Reprendre naïvement la fiche technique du capteur donne des écarts systématiques en champ proche. Modéliser les angles verticaux non uniformes des faisceaux corrige l'essentiel. C'est un contrôle rapide, utile avant d'entraîner ou de tester une perception en simulation.

[arXiv](https://arxiv.org/abs/2611.27379){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [matériel](themes/materiel.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### AMD EPYC Embedded 9006 : 256 cœurs Zen 6c « embarqués » { #amd-epyc-embedded-9006-256-curs-zen-6c-embarques data-fav="2026/11/2026-11-23/#amd-epyc-embedded-9006-256-curs-zen-6c-embarques" }

L'« embarqué » ne se limite pas aux microcontrôleurs : cette gamme vise les bancs de test de semi-conducteurs, les pare-feu et le stockage. Elle offre jusqu'à 256 cœurs, 1 Go de cache L3, du PCIe Gen 6, du CXL 3.1, pour 400 à 600 W. Comme toujours dans l'embarqué, l'argument clé est la disponibilité garantie sur sept ans.

[CNX Software](https://www.cnx-software.com/2026/11/23/amd-epyc-embedded-9006-series-embedded-processors-offer-up-to-256-zen-6c-cores-pcie-gen-6-and-cxl-3-1/){ .src target="_blank" rel="noopener" } [embarqué](themes/embarque.md){ .tag }
{ .actu-foot }

</section>

<section class="actu actu--concept" markdown>

### 💡 Concept du jour : le LET (Logical Execution Time) { #concept-du-jour-le-let-logical-execution-time data-fav="2026/11/2026-11-23/#concept-du-jour-le-let-logical-execution-time" }

Principe venu de l'automobile et de l'avionique temps réel : une tâche lit ses entrées au **début** de sa période et ne publie ses sorties qu'à la **fin**, quel que soit le moment réel où son calcul se termine à l'intérieur de cette fenêtre. On sépare ainsi « quand on calcule » de « quand on communique ». Si le calcul finit plus tôt ou plus tard selon la charge CPU, les autres tâches voient exactement les mêmes données aux mêmes instants. En échange d'un peu de latence, le système devient reproductible et analysable. C'est l'idée du papier ROS 2 déterministe ci-dessus.

[arXiv](https://arxiv.org/abs/2611.26676){ .src target="_blank" rel="noopener" } [concept](themes/concept.md){ .tag }
{ .actu-foot }

</section>

## Veilles précédentes

<div class="cartes" markdown>

- [**Dimanche 22 novembre 2026**](2026/11/2026-11-22.md) <span class="carte-meta">3 actus · 2 min</span>

    - 🤖 Robotique & infra
    - 🔌 Embarqué & tech

- [**Samedi 21 novembre 2026**](2026/11/2026-11-21.md) <span class="carte-meta">3 actus · 3 min</span>

    - 🤖 Robotique & infra
    - 🔌 Embarqué & tech

- [**Vendredi 20 novembre 2026**](2026/11/2026-11-20.md) <span class="carte-meta">3 actus · 3 min</span>

    - 🤖 Robotique & infra
    - 🔌 Embarqué & tech

- [**Jeudi 19 novembre 2026**](2026/11/2026-11-19.md) <span class="carte-meta">3 actus · 3 min</span>

    - 🤖 Robotique & infra
    - 🔌 Embarqué & tech

- [**Mercredi 18 novembre 2026**](2026/11/2026-11-18.md) <span class="carte-meta">6 actus · 3 min</span>

    - Flipper One : un Linux ARM de poche, avec un RP2350 pour le bas niveau
    - GigaDevice GD32H7 : Cortex-M7 à 750 MHz avec EtherCAT intégré, ciblant les articulations…
    - Sauvetage de la doc du ROS wiki vers des README
    - *et 3 autres…*

- [**Mardi 17 novembre 2026**](2026/11/2026-11-17.md) <span class="carte-meta">7 actus · 3 min</span>

    - Verre et plastique transparent : la caméra de profondeur ment sans prévenir
    - ROS 2 Kilted : fin de vie le 30 novembre
    - Fauteuil roulant téléopéré : une architecture de sûreté bien documentée
    - *et 4 autres…*

</div>

[Les 29 veilles dans les archives →](archives.md){ .lien-suite }

<p class="a-propos" markdown>
Télémétrie est une veille automatisée : les résumés sont rédigés par Rosetta, un assistant IA, à partir des sources citées sous chaque actu. [Voir les sources suivies](sources.md).
</p>
