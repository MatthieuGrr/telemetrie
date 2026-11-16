"""Réglages propres à Télémétrie, lus par scripts/publish.py."""

NOM = "Télémétrie"
EMOJI = "🛰️"
DESCRIPTION = "Le flux quotidien de Rosetta — veille robotique, embarqué et tech"
BASELINE = ("Le flux quotidien de Rosetta : chaque matin, une poignée d'actus en robotique, "
            "électronique embarquée et tech, résumées en quelques lignes, "
            "avec le lien vers la source.")
PIED = ("Télémétrie est une veille automatisée : les résumés sont rédigés par Rosetta, "
        "un assistant IA, à partir des sources citées sous chaque actu.")

# True : la publication est refusée si une actu n'a aucun lien source.
SOURCE_OBLIGATOIRE = False

NAV = [("Accueil", "index.md"), ("Archives", "archives.md"),
       ("Thèmes", "tags.md"), ("Favoris", "favoris.md")]

# Thèmes déduits par mots-clés (texte en minuscules). Chaque actu reçoit les
# MAX_TAGS_ACTU thèmes les plus présents, sinon TAG_DEFAUT.
MAX_TAGS_ACTU = 2
TAG_DEFAUT = "tech"
TAG_RULES = {
    "robotique": r"robot|ros ?2|nav2|slam|drone|quadrirotor|humano[iï]de|manipulat|"
                 r"\bbras\b|pince|\bvla\b|\bamr\b|\bagv\b|exosquelette|locomotion|lidar|"
                 r"odom[eé]trie|cin[eé]matique|planificat|sim-to-real|t[eé]l[eé]op[eé]r",
    "embarqué": r"esp32|stm32|rp2350|\bpico\b|\bmcu\b|microcontr[oô]leur|firmware|freertos|"
                r"cortex-?m|risc-?v|esp-idf|bare-metal|\bnrf\d|nordic|espressif|"
                r"embarqu[eé]|raspberry",
    "IA": r"\bllm\b|\bia\b|intelligence artificielle|\bgpt|claude|mistral|qwen|gemma|"
          r"r[eé]seaux? de neurones|\bvla\b|\bnpu\b|openai|anthropic|deepmind|"
          r"apprentissage|world model|mod[eè]le de monde|\bagents? ia\b",
    "spatial": r"satellite|fus[eé]e|orbit|\bnasa\b|\besa\b|spacex|ariane|\bcnes\b|"
               r"lanceur|astronaut|t[eé]lescope|spatiale|\bgnss\b",
    "logiciel": r"linux|noyau|kernel|postgres|logiciel|compilat|\bsdk\b|"
                r"\bjax\b|python|uefi|simulateur|\bcli\b",
    "matériel": r"\bpcb\b|capteur|moteur|bldc|ethernet|wi-?fi|bluetooth|"
                r"\bpuce|\bram\b|psram|oscillo|\bsoc\b|\bfpga\b|\bcpu\b|\bgpu\b",
    "open source": r"open[ -]source|code ouvert|apache 2|github\.com|oshwa|"
                   r"poids (ouverts|publi)|open-weight|mat[eé]riel ouvert|"
                   r"publie les poids",
    "sécurité": r"faille|\bcve-|\bexploits?\b|backdoor|porte d[eé]rob[eé]e|zero-day|"
                r"vuln[eé]rab|s[eé]curit[eé]|pi[eé]g[eé]e?|exfiltr",
    "recherche": r"arxiv\.org|\barxiv\b|\bpapier\b",
    "concept": r"concept du jour",
}

# Nom affiché pour les domaines connus (sinon le domaine tel quel).
SOURCES = {
    "arxiv.org": "arXiv",
    "cnx-software.com": "CNX Software",
    "discourse.openrobotics.org": "Open Robotics Discourse",
    "github.com": "GitHub",
    "therobotreport.com": "The Robot Report",
    "the-decoder.com": "The Decoder",
    "simonwillison.net": "Simon Willison",
    "openai.com": "OpenAI",
    "mistral.ai": "Mistral AI",
    "ubuntu.com": "Ubuntu",
    "foxglove.dev": "Foxglove",
    "hackaday.com": "Hackaday",
    "wdr.de": "WDR",
}
