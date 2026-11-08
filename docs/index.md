---
title: Accueil
hide:
  - navigation
  - toc
---

## Dimanche 8 novembre 2026



### Latent RL Prior : recycler la simulation pour apprendre avec peu de démos

Idée en deux temps. D'abord, on entraîne en simulation, par apprentissage par renforcement avec accès à l'état exact, un « décodeur d'actions » qui sait déjà bien manipuler. Ensuite, on le gèle et on n'apprend plus que la petite interface qui relie les images de la caméra à ce décodeur. Sur trois tâches simulées, la méthode bat le fine-tuning complet de π0.5 et de GR00T quand les données sont rares, avec jusqu'à 10× moins de démonstrations.

[Source : arxiv.org](https://arxiv.org/abs/2611.08458)
{ .source-link }

### Coldframe : un honeypot qui se fait passer pour un contrôleur de frigo de supermarché

En 2026, des attaquants ont pris la main sur des superviseurs de réfrigération exposés sur Internet (mots de passe par défaut, firmware jamais mis à jour) pour forcer des cycles de dégivrage. Coldframe imite un Danfoss AK-SM 800A ou un Dixell XWEB jusqu'aux en-têtes HTTP, à la version de TLS et au certificat, de façon à tromper les scanners. Il enregistre ensuite les identifiants testés et les CVE exploitées. Le tout tient dans un seul fichier Python, sans dépendance : une bonne leçon concrète de sécurité OT.

[Source : github.com](https://github.com/hedgerow-dev/coldframe)
{ .source-link }

### Un « homelab » à 10 $ sur une clé 4G OpenStick

Une clé modem 4G (4× Cortex-A53, 512 Mo de RAM, 4 Go d'eMMC, Wi-Fi, GPS) reflashée sous Debian devient un mini-serveur silencieux. L'auteur y fait tourner AdGuard Home, des conteneurs Podman et un agent IA, et indique la RAM consommée par chaque service. Utile pour voir ce qui tient vraiment dans 450 Mo.

[Source : blog.bosscher.ch](https://blog.bosscher.ch/posts/openstick/)
{ .source-link }

### T3R : alléger un modèle VLA sans le réentraîner

Les modèles VLA (vision-langage-action) traitent des centaines de « tokens » visuels à chaque décision, ce qui coûte cher. T3R retire d'abord les zones d'image inutiles grâce à une segmentation, puis oriente l'attention vers les régions utiles à l'action. Sur LIBERO, 85 % des tokens de la caméra de scène sont supprimés sans perte de réussite, et le gain atteint +7 points quand les objets sont déplacés. La méthode ne demande aucun réentraînement.

[Source : arxiv.org](https://arxiv.org/abs/2611.08413)
{ .source-link }

### Social Humanoid : un humanoïde qui réagit aux mouvements d'un partenaire

Ce travail (CoRL 2026, Berkeley) commande un Unitree G1 (29 degrés de liberté) en deux niveaux. En haut, un modèle génère le mouvement du robot en fonction de celui de l'humain, et l'anticipe même quand l'humain est masqué. En bas, un contrôleur corps entier exécute ce mouvement. Le papier apporte aussi un benchmark de 260 h d'interactions humain-humanoïde.

[Source : von31.github.io](https://von31.github.io/social-humanoid/)
{ .source-link }

### 💡 Concept du jour : la quantification

Quantifier un réseau de neurones, c'est stocker ses poids (et parfois ses calculs) sur moins de bits : 8 ou 4 bits entiers au lieu de 16 ou 32 bits flottants. Le modèle devient 2 à 8 fois plus léger et beaucoup plus rapide sur un NPU ou un microcontrôleur, au prix d'une petite perte de précision, que l'on limite en calibrant les plages de valeurs sur quelques exemples. C'est l'une des techniques qui permettent de faire tourner un modèle de robot sur une carte embarquée plutôt que sur un serveur.

## Veilles précédentes

- [Samedi 7 novembre 2026](2026/11/2026-11-07.md) — 5 actus
- [Vendredi 6 novembre 2026](2026/11/2026-11-06.md) — 7 actus
- [Jeudi 5 novembre 2026](2026/11/2026-11-05.md) — 7 actus
- [Mercredi 4 novembre 2026](2026/11/2026-11-04.md) — 6 actus
- [Mardi 3 novembre 2026](2026/11/2026-11-03.md) — 7 actus
- [Lundi 2 novembre 2026](2026/11/2026-11-02.md) — 6 actus
- [Dimanche 1er novembre 2026](2026/11/2026-11-01.md) — 5 actus

[Toutes les veilles dans les archives →](archives.md)


---

<small>Le flux quotidien de Rosetta : une sélection d'actus en robotique, électronique embarquée et tech, avec un lien vers chaque source.</small>
