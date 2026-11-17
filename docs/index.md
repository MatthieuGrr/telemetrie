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

[Lire la veille du jour](2026/11/2026-11-17.md){ .md-button .md-button--primary } [Archives](archives.md){ .md-button } [Thèmes](tags.md){ .md-button } [Flux RSS](feed.xml){ .md-button }
{ .hero-actions }

</div>

## [Mardi 17 novembre 2026](2026/11/2026-11-17.md) { .jour }

**7 actus** · 3 min de lecture
{ .veille-meta }

<section class="actu" markdown>

### Verre et plastique transparent : la caméra de profondeur ment sans prévenir { #verre-et-plastique-transparent-la-camera-de-profondeur-ment-sans-prevenir data-fav="2026/11/2026-11-17/#verre-et-plastique-transparent-la-camera-de-profondeur-ment-sans-prevenir" }

Sur du verre, une caméra RGB-D renvoie une profondeur fausse mais « confiante », sans aucun signal d'erreur : sur le jeu de données TransCG, 68,6 % des pixels de verre d'une Intel L515 sont faux de plus de 5 %, et presque toujours trop loin, donc l'obstacle apparaît comme de l'espace libre. limit_case_ros2 est un nœud composable (Jazzy, Humble, Apache-2.0) qui repère ces « cuvettes » suspectes dans l'image de profondeur et publie une profondeur filtrée plus un masque, en 7,4 ms par image en 1280x720. Point rare : l'auteur publie aussi ses échecs, dont une démo Nav2 négative et une méthode v0.2 qui a raté son test pré-enregistré.

[Open Robotics Discourse](https://discourse.openrobotics.org/t/limit-case-ros2-flag-silent-depth-failures-on-transparent-objects-jazzy-humble/59851){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### ROS 2 Kilted : fin de vie le 30 novembre { #ros-2-kilted-fin-de-vie-le-30-novembre data-fav="2026/11/2026-11-17/#ros-2-kilted-fin-de-vie-le-30-novembre" }

Kilted Kaiju (distribution non-LTS de mai 2025) arrive en fin de support le 30/11. La synchronisation du 18/11 (595 paquets en attente) est l'avant-dernière : il ne restera qu'une seule synchro avant l'arrêt. Quiconque est encore sur Kilted doit prévoir la migration vers Jazzy (LTS) ou Lyrical.

[Open Robotics Discourse](https://discourse.openrobotics.org/t/preparing-for-penultimate-kilted-sync-2026-11-18/59865){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### Fauteuil roulant téléopéré : une architecture de sûreté bien documentée { #fauteuil-roulant-teleopere-une-architecture-de-surete-bien-documentee data-fav="2026/11/2026-11-17/#fauteuil-roulant-teleopere-une-architecture-de-surete-bien-documentee" }

Le papier AVD décrit un fauteuil électrique téléopérable bâti uniquement avec du matériel du commerce, et surtout sa logique de sûreté : hiérarchie d'autorité fixe (arrêt d'urgence et joystick de l'occupant priment sur la commande distante), capteurs embarqués n'ayant que le droit d'arrêter, calcul séparé entre fonctions principales et fonctions de sûreté, passage en état sûr sur perte de heartbeat. Le LiDAR a été testé sur 2 025 scans sous brouillard d'eau, poussière et occultation : il garde au pire 76,6 % de ses points utiles vers l'avant.

[arXiv](https://arxiv.org/abs/2611.20720){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [recherche](themes/recherche.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### N'allumer le deuxième capteur que quand le premier doute { #nallumer-le-deuxieme-capteur-que-quand-le-premier-doute data-fav="2026/11/2026-11-17/#nallumer-le-deuxieme-capteur-que-quand-le-premier-doute" }

L'équipe de Michael Milford (QUT) propose, pour la reconnaissance de lieux multi-capteurs, de n'interroger un second capteur que lorsque le score de correspondance du premier est faible, avec un seuil ajusté en ligne pour tenir un taux d'utilisation fixé. Résultat : 55 % du gain de la fusion en n'utilisant le second capteur que sur 25 % des requêtes, 81 % à 50 %. Intéressant pour l'énergie, la cadence et la discrétion.

[arXiv](https://arxiv.org/abs/2611.20730){ .src target="_blank" rel="noopener" } [matériel](themes/materiel.md){ .tag } [recherche](themes/recherche.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### Rockchip RK3668 : cœurs revus, échantillons au T1 2027 { #rockchip-rk3668-curs-revus-echantillons-au-t1-2027 data-fav="2026/11/2026-11-17/#rockchip-rk3668-curs-revus-echantillons-au-t1-2027" }

Le successeur attendu du RK3588 change de CPU : 6 Cortex-A725 + 2 Cortex-A520 au lieu des Cortex-A730/A530 annoncés en 2025, qui n'ont jamais vu le jour. Gravure 6 nm, échantillons d'ingénierie prévus au T1 2027 et premières cartes en prototype au S1 2027 ; le haut de gamme RK3688 ne viendrait pas avant fin 2027.

[CNX Software](https://www.cnx-software.com/2026/11/17/rockchip-rk3668-switches-to-cortex-a725-and-cortex-a520-cores-engineering-samples-planned-for-q1-2027/){ .src target="_blank" rel="noopener" } [matériel](themes/materiel.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### Une SBC industrielle Qualcomm avec quatre CAN-FD isolés { #une-sbc-industrielle-qualcomm-avec-quatre-can-fd-isoles data-fav="2026/11/2026-11-17/#une-sbc-industrielle-qualcomm-avec-quatre-can-fd-isoles" }

La Forlinx OK8275AA-C reprend le Qualcomm Dragonwing QCS8275 (jusqu'à 40 TOPS, le même que l'Arduino VENTUNO Q) mais en version industrielle : 4 CAN-FD et 2 RS485 isolés, GbE + 2,5GbE, trois entrées caméra MIPI CSI, alimentation 24 V et plage -40 à +85 °C. Un profil taillé pour un ordinateur de bord de robot mobile.

[CNX Software](https://www.cnx-software.com/2026/11/17/forlinx-ok8275aa-c-a-qualcomm-qcs8275-industrial-sbc-with-12gb-lpddr5-256gb-ufs-storage/){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag }
{ .actu-foot }

</section>

<section class="actu actu--concept" markdown>

### 💡 Concept du jour : le Priority-Flood { #concept-du-jour-le-priority-flood data-fav="2026/11/2026-11-17/#concept-du-jour-le-priority-flood" }

C'est l'algorithme qu'utilise limit_case_ros2. Il vient de l'hydrologie : on traite une carte d'altitude comme un relief et on la « remplit d'eau » depuis les bords, en traitant toujours en premier la case la plus basse de la frontière (via une file de priorité). Chaque cuvette fermée finit remplie jusqu'au niveau de son point de débordement, et la différence entre niveau d'eau et terrain révèle les creux. Appliqué à une image de profondeur inversée, cela fait ressortir les zones anormalement « lointaines » entourées de surfaces proches, signature typique du verre.

[concept](themes/concept.md){ .tag }
{ .actu-foot }

</section>

## Veilles précédentes

<div class="cartes" markdown>

- [**Lundi 16 novembre 2026**](2026/11/2026-11-16.md) <span class="carte-meta">7 actus · 2 min</span>

    - Un modèle de raisonnement entraîné en simulation pilote de vrais bras
    - Une chargeuse de 5 tonnes en équilibre sur deux roues
    - Le NPU d'une carte embarquée détourné pour le GNSS
    - *et 4 autres…*

- [**Dimanche 15 novembre 2026**](2026/11/2026-11-15.md) <span class="carte-meta">7 actus · 3 min</span>

    - FORGE : un humanoïde qui « sent » les forces sans capteur au poignet
    - Serve Robotics ouvre sa flotte de livraison à une API publique
    - POSIM : le simulateur marin DAVE passe à ROS 2 Lyrical et Gazebo Jetty
    - *et 4 autres…*

- [**Samedi 14 novembre 2026**](2026/11/2026-11-14.md) <span class="carte-meta">6 actus · 2 min</span>

    - RoboBaton Neo : un module VIO de 15,5 g synchronisé en matériel
    - FlexiTac : la peau tactile open source à 2,5 $ la pièce
    - Berkeley : des agents IA qui programment des cellules robotisées
    - *et 3 autres…*

- [**Vendredi 13 novembre 2026**](2026/11/2026-11-13.md) <span class="carte-meta">6 actus · 3 min</span>

    - ros2ebpf : observer tout le graphe ROS 2 sans toucher aux nœuds
    - PLEM : des servovariateurs EtherCAT sous ros2_control sur Jetson
    - RTAB-Map contre ORB-SLAM3 sur Raspberry Pi 5
    - *et 3 autres…*

- [**Jeudi 12 novembre 2026**](2026/11/2026-11-12.md) <span class="carte-meta">6 actus · 3 min</span>

    - LabWired : tester son firmware sans carte, en CI
    - WeAct Logic Analyzer V2 : 16 voies à 200 MHz pour ~10 $
    - Détecter un robot qui « tourne en rond » dans sa recherche d'information
    - *et 3 autres…*

- [**Mercredi 11 novembre 2026**](2026/11/2026-11-11.md) <span class="carte-meta">6 actus · 2 min</span>

    - Mémoire de robot ou simple horloge ?
    - BEHAVIOR Challenge 2026 : un VLA pour 100 tâches, plus un agent qui code
    - MCAP (format des rosbag2) : écritures jusqu'à 8× plus rapides
    - *et 3 autres…*

</div>

[Les 23 veilles dans les archives →](archives.md){ .lien-suite }

<p class="a-propos" markdown>
Télémétrie est une veille automatisée : les résumés sont rédigés par Rosetta, un assistant IA, à partir des sources citées sous chaque actu.
</p>
