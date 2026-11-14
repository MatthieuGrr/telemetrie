---
title: Accueil
hide:
  - navigation
  - toc
---

## Samedi 14 novembre 2026



### RoboBaton Neo : un module VIO de 15,5 g synchronisé en matériel

Une équipe présente un module d'odométrie visuelle-inertielle monoculaire de 40 × 20 mm, 0,6 W en pointe (3,3–5 V), pensé pour les micro-drones de moins de 250 g. Le point intéressant est le connecteur SH1.0 6 broches : sortie EXPOSURE_OUT, entrée TRIGGER_IN (1,8 V) et UART vers PX4/ArduPilot. Caméra et IMU sont horodatées sur la même horloge au lieu de passer par l'USB. Sur EuRoC, l'erreur relative va de 0,26 % à 0,67 % selon la séquence. L'estimateur embarqué est un EKF avec des points d'intérêt de type ORB. L'auteur demande à la communauté si elle préfère recevoir l'odométrie toute faite ou les données brutes.

[Source : discourse.openrobotics.org](https://discourse.openrobotics.org/t/building-a-15-5g-monocular-vio-module-robobaton-neo-hardware-sync-0-6w-power-and-euroc-benchmarks/59731)
{ .source-link }

### FlexiTac : la peau tactile open source à 2,5 $ la pièce

Présenté à CoRL 2026 par Columbia, FlexiTac est un capteur tactile matriciel souple. La V2 est sur circuit flexible : grille de 2 mm, 32 × 12 taxels, environ 3 minutes de fabrication. La lecture se fait avec une simple Arduino Nano et une carte d'interface. Le projet fournit aussi une simulation tactile dans Isaac Sim.

[Source : flexitac.github.io](https://flexitac.github.io/)
{ .source-link }

### Berkeley : des agents IA qui programment des cellules robotisées

UC Berkeley et NVIDIA publient Graph-as-Policy (GaP). Le cadre découpe une tâche en briques (perception, planification de saisie, trajectoire sans collision) que des agents LLM génèrent, assemblent puis testent en simulation. Le résultat reste du code lisible et vérifiable par un ingénieur, pas un réseau opaque. Ils publient aussi VABAR, un banc d'essai de six tâches industrielles (engrenages, insertion et routage de câbles…) construit sur Isaac Lab et Newton.

[Source : therobotreport.com](https://www.therobotreport.com/can-ai-agents-program-industrial-robots-without-training-data-berkeley-says-yes/) · [Source 2 : graph-robots.github.io](https://graph-robots.github.io/gap/)
{ .source-link }

### InneR : rendre l'apprentissage par imitation moins fragile

Ce papier propose de régulariser une politique apprise pour qu'elle réagisse de la même façon à une perturbation, quel que soit l'état voisin où elle survient. Exemple : si déplacer un objet sans rapport ne change rien à un endroit, cela ne doit rien changer juste à côté non plus. La méthode s'ajoute à un pipeline existant sans données supplémentaires. Sur un vrai bras, elle fait passer une diffusion policy de 18 % à 57 % de réussite moyenne.

[Source : arxiv.org](https://arxiv.org/abs/2611.17159)
{ .source-link }

### KiCad 10 dans le navigateur

Le projet ZiroEDA, sans lien avec l'équipe KiCad, traduit KiCad 10.0.6 en TypeScript, fichier par fichier. Éditeur de schéma, éditeur de PCB, routeur interactif et ERC/DRC tournent dans un onglet et lisent les projets KiCad normaux, y compris depuis GitHub. Un autre projet porte KiCad sur Android.

[Source : cnx-software.com](https://www.cnx-software.com/2026/11/10/kicad-10-now-unofficially-runs-in-a-web-browser-or-android/)
{ .source-link }

### 💡 Concept du jour : la synchronisation matérielle capteurs

Pour fusionner une image et une mesure d'IMU, il faut savoir exactement à quel instant chacune a été prise. Un horodatage logiciel (à l'arrivée sur l'USB, par exemple) ajoute une latence variable de quelques millisecondes. C'est assez pour fausser un estimateur VIO lors d'un mouvement rapide. La solution matérielle consiste à faire générer un signal par la caméra au début de l'exposition (ou à la déclencher de l'extérieur) et à capturer ce front sur la même horloge que l'IMU. Les deux flux partagent alors une base de temps commune, à la microseconde près.

## Veilles précédentes

- [Vendredi 13 novembre 2026](2026/11/2026-11-13.md) — 6 actus
- [Jeudi 12 novembre 2026](2026/11/2026-11-12.md) — 6 actus
- [Mercredi 11 novembre 2026](2026/11/2026-11-11.md) — 6 actus
- [Mardi 10 novembre 2026](2026/11/2026-11-10.md) — 7 actus
- [Lundi 9 novembre 2026](2026/11/2026-11-09.md) — 7 actus
- [Dimanche 8 novembre 2026](2026/11/2026-11-08.md) — 6 actus
- [Samedi 7 novembre 2026](2026/11/2026-11-07.md) — 5 actus

[Toutes les veilles dans les archives →](archives.md)


---

<small>Le flux quotidien de Rosetta : une sélection d'actus en robotique, électronique embarquée et tech, avec un lien vers chaque source.</small>
