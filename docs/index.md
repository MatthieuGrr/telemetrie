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

[Lire la veille du jour](2026/11/2026-11-19.md){ .md-button .md-button--primary } [Archives](archives.md){ .md-button } [Thèmes](tags.md){ .md-button } [Flux RSS](feed.xml){ .md-button }
{ .hero-actions }

</div>

## [Jeudi 19 novembre 2026](2026/11/2026-11-19.md) { .jour }

**3 actus** · 3 min de lecture
{ .veille-meta }

<section class="actu" markdown>

### 🤖 Robotique & infra { #robotique-infra data-fav="2026/11/2026-11-19/#robotique-infra" }

- **Corrélation de pannes pour ROS 2, à la manière de l'automobile** : retour d'expérience sur un démarrage Nav2 Jazzy où un lidar Ethernet ne se connecte jamais. Le log affiche 164 messages, et l'erreur lidar s'y perd au milieu de 120 messages du costmap, sans aucun lien entre eux. Les auteurs reprennent l'idée du Diagnostic Event Manager d'AUTOSAR (dépendances d'événements, « consecutive faults ») dans ros2_medkit : une règle YAML désigne la cause racine, liste les symptômes et une fenêtre temporelle. L'API ne renvoie alors plus qu'une panne, LIDAR_NOT_CONNECTED, avec 6 symptômes masqués mais conservés.
- **ROS 2 sous macOS : le piège de la mémoire partagée Fast DDS** : banc de mesure de tous les RMW sur Apple Silicon. Sur macOS, le transport SHM par défaut de Fast DDS réveille les lecteurs sur un tic de scrutation d'environ 5,7 ms : un capteur à 2 kHz n'arrive qu'à 350-450 Hz, et la livraison s'effondre sous forte charge. Basculer sur Cyclone DDS suffit à retrouver les 2 kHz (~90 µs). Zenoh avec SHM excelle sur les gros messages, Cyclone + iceoryx sur la latence (10 µs p50). Bon rappel : le RMW par défaut n'est pas neutre.
- **Planificateur × contrôleur sur voiture Ackermann, simulation contre réel** : trois contrôleurs géométriques (Regulated Pure Pursuit, Stanley, Vector Pursuit) combinés à deux planificateurs (Hybrid A*, NavFn), testés sur une QCar 1/10 et dans un Gazebo calqué sur le réel (60 essais). Le classement des contrôleurs en précision et en douceur de commande se transfère bien de la simulation au réel. L'étude montre surtout qu'on ne peut pas évaluer planificateur et contrôleur séparément.
- **RoboDx : des agents IA qui réparent du logiciel de navigation** : un générateur de tâches où des fautes connues sont injectées dans le code de navigation d'un robot simulé. Un correctif n'est validé que si le robot roule correctement dans des scénarios cachés, puisqu'un patch peut passer tous les tests unitaires et quand même faire dévier le robot. Le cas le plus intéressant est celui des fautes « silencieuses », qui ne se manifestent qu'en présence d'une autre faute : réparer ce qui casse ne garantit pas d'avoir tout trouvé.
- **Barrière de sécurité alimentée directement par le Doppler d'un radar** : pour éviter un obstacle mobile, il faut sa distance et sa vitesse d'approche. Plutôt que de dériver la vitesse à partir de mesures de distance successives (bruitées et en retard), les auteurs utilisent la vitesse radiale mesurée par un radar FMCW comme dérivée de la barrière. On obtient un filtre fermé sur la vitesse d'avance, avec une marge issue des bornes d'erreur du capteur. Sur 508 rencontres, l'approche ne compte que 2 intrusions dans la zone tampon.

[Open Robotics Discourse](https://discourse.openrobotics.org/t/fault-correlation-for-ros-2-one-cause-many-faults-and-what-automotive-does-about-it/59959){ .src target="_blank" rel="noopener" } [Open Robotics Discourse (2)](https://discourse.openrobotics.org/t/ros-2-on-macos-measured-topic-rates-for-each-rmw-a-fast-dds-shared-memory-pitfall-and-tuned-presets/59951){ .src target="_blank" rel="noopener" } [arXiv](https://arxiv.org/abs/2611.24800){ .src target="_blank" rel="noopener" } [arXiv (2)](https://arxiv.org/abs/2611.23816){ .src target="_blank" rel="noopener" } [arXiv (3)](https://arxiv.org/abs/2611.23654){ .src target="_blank" rel="noopener" } [robotique](themes/robotique.md){ .tag } [matériel](themes/materiel.md){ .tag }
{ .actu-foot }

</section>

<section class="actu" markdown>

### 🔌 Embarqué & tech { #embarque-tech data-fav="2026/11/2026-11-19/#embarque-tech" }

- **Bluetooth 7.0 ratifié, avec le HDT** : la nouvelle couche physique BLE High Data Throughput monte à 7,5 Mb/s (modulation d'ordre supérieur, correction d'erreurs convolutive, débit adaptatif). La spécification apporte aussi la mise à jour des paramètres d'un flux isochrone sans le recréer (IPU), un nouveau schéma de dérivation des clés de session (EKS) et le chiffrement sans appairage (TAK). Les premiers MCU « Bluetooth 7-ready » existent déjà.

[CNX Software](https://www.cnx-software.com/2026/11/18/bluetooth-7-0-specification-ratified-with-hdt-high-data-throughput-support/){ .src target="_blank" rel="noopener" } [embarqué](themes/embarque.md){ .tag } [matériel](themes/materiel.md){ .tag }
{ .actu-foot }

</section>

<section class="actu actu--concept" markdown>

### 💡 Concept du jour : la fonction barrière de contrôle (CBF) { #concept-du-jour-la-fonction-barriere-de-controle-cbf data-fav="2026/11/2026-11-19/#concept-du-jour-la-fonction-barriere-de-controle-cbf" }

Une CBF est une fonction h(x) positive tant que le robot est en sécurité (par exemple distance à l'obstacle moins une marge). Plutôt que de planifier toute une trajectoire sûre, on impose à chaque pas de commande que h ne décroisse pas trop vite : dh/dt ≥ -α·h. Plus on approche de la limite, moins h a le droit de baisser. En pratique, un petit filtre (souvent un problème quadratique) corrige à chaque cycle la commande du planificateur juste ce qu'il faut pour respecter cette condition. C'est pour cela que mesurer directement dh/dt (le Doppler du radar ci-dessus) est intéressant : on ne l'estime plus, on le lit.

[concept](themes/concept.md){ .tag }
{ .actu-foot }

</section>

## Veilles précédentes

<div class="cartes" markdown>

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

</div>

[Les 25 veilles dans les archives →](archives.md){ .lien-suite }

<p class="a-propos" markdown>
Télémétrie est une veille automatisée : les résumés sont rédigés par Rosetta, un assistant IA, à partir des sources citées sous chaque actu. [Voir les sources suivies](sources.md).
</p>
