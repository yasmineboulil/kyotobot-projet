# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    MISTRAL_API_KEY = "TA_CLE_MISTRAL"
    
    # Prompts améliorés
    SYSTEM_PROMPT = """
Tu es KyotoBot, un guide touristique expert et personnalisé de Kyoto, Japon.

RÈGLES STRICTES :
1. Tu ne réponds QU'AUX questions sur Kyoto (temples, jardins, quartiers, restaurants, culture, transports, hébergement).
2. Si l'utilisateur demande quelque chose hors de Kyoto, réponds poliment : "Je suis spécialisé uniquement sur Kyoto. Pouvez-vous reformuler votre question sur cette ville ?"
3. TOUJOURS extraire et utiliser ces informations si mentionnées :
   - Budget (en euros ou yens)
   - Durée du séjour (heures, jours)
   - Centres d'intérêt (temples, nature, gastronomie, culture, shopping)
   - Période de visite (saison)
4. Si des informations manquent, demande-les de manière naturelle et concise.

FORMAT DE RÉPONSE :
- Commence par résumer la demande de l'utilisateur
- Propose un itinéraire optimisé avec horaires précis
- Indique les durées de visite et temps de transport
- Donne des conseils pratiques (meilleur moment, comment s'y rendre)
- Estime le coût total si un budget est mentionné
- Termine par une question pour affiner les recommandations

STYLE :
- Naturel, chaleureux et encourageant
- Utilise des emojis avec parcimonie (🏯 ⛩️ 🌸 🍜 🚌)
- Sois précis sur les prix, horaires et distances
- Partage des anecdotes culturelles intéressantes

BASE DE DONNÉES DISPONIBLE :
Tu as accès à 25 lieux répertoriés : temples (Kiyomizu-dera, Kinkaku-ji, Fushimi Inari, Ginkaku-ji, Nanzen-ji, etc.), 
jardins (Ryoan-ji, forêt de bambous, Chemin de la Philosophie), marchés (Nishiki), quartiers (Gion, Pontocho, Higashiyama, Arashiyama),
et restaurants variés. Recommande ces lieux quand approprié.
"""
    
    PROMPT_INSPIRE = """Propose une idée originale et détaillée de visite à Kyoto pour quelqu'un qui ne précise ni budget ni durée.
Crée un itinéraire thématique unique (par exemple : Kyoto mystique, Kyoto gourmand, Kyoto hors des sentiers battus, Kyoto au fil de l'eau, etc.).
Inclus horaires, durées, budget estimé et conseils pratiques."""
    
    # Lieux connus pour les liens Google Maps
    KNOWN_PLACES = {
        "Temple Kiyomizu-dera": "https://www.google.com/maps/search/?api=1&query=Kiyomizu-dera+Kyoto",
        "Kiyomizu-dera": "https://www.google.com/maps/search/?api=1&query=Kiyomizu-dera+Kyoto",
        "Temple Kinkaku-ji": "https://www.google.com/maps/search/?api=1&query=Kinkaku-ji+Kyoto",
        "Kinkaku-ji": "https://www.google.com/maps/search/?api=1&query=Kinkaku-ji+Kyoto",
        "Pavillon d'Or": "https://www.google.com/maps/search/?api=1&query=Kinkaku-ji+Kyoto",
        "Temple Fushimi Inari": "https://www.google.com/maps/search/?api=1&query=Fushimi+Inari+Kyoto",
        "Fushimi Inari": "https://www.google.com/maps/search/?api=1&query=Fushimi+Inari+Kyoto",
        "Temple Ginkaku-ji": "https://www.google.com/maps/search/?api=1&query=Ginkaku-ji+Kyoto",
        "Ginkaku-ji": "https://www.google.com/maps/search/?api=1&query=Ginkaku-ji+Kyoto",
        "Pavillon d'Argent": "https://www.google.com/maps/search/?api=1&query=Ginkaku-ji+Kyoto",
        "Temple Nanzen-ji": "https://www.google.com/maps/search/?api=1&query=Nanzen-ji+Kyoto",
        "Nanzen-ji": "https://www.google.com/maps/search/?api=1&query=Nanzen-ji+Kyoto",
        "Temple Kodaiji": "https://www.google.com/maps/search/?api=1&query=Kodaiji+Kyoto",
        "Kodaiji": "https://www.google.com/maps/search/?api=1&query=Kodaiji+Kyoto",
        "Jardin Ryoan-ji": "https://www.google.com/maps/search/?api=1&query=Ryoan-ji+Kyoto",
        "Ryoan-ji": "https://www.google.com/maps/search/?api=1&query=Ryoan-ji+Kyoto",
        "Forêt de bambous": "https://www.google.com/maps/search/?api=1&query=Bamboo+Forest+Arashiyama+Kyoto",
        "Bambous d'Arashiyama": "https://www.google.com/maps/search/?api=1&query=Bamboo+Forest+Arashiyama+Kyoto",
        "Chemin de la Philosophie": "https://www.google.com/maps/search/?api=1&query=Philosopher's+Path+Kyoto",
        "Marché de Nishiki": "https://www.google.com/maps/search/?api=1&query=Nishiki+Market+Kyoto",
        "Nishiki": "https://www.google.com/maps/search/?api=1&query=Nishiki+Market+Kyoto",
        "Quartier de Gion": "https://www.google.com/maps/search/?api=1&query=Gion+Kyoto",
        "Gion": "https://www.google.com/maps/search/?api=1&query=Gion+Kyoto",
        "Quartier de Higashiyama": "https://www.google.com/maps/search/?api=1&query=Higashiyama+Kyoto",
        "Higashiyama": "https://www.google.com/maps/search/?api=1&query=Higashiyama+Kyoto",
        "Pontocho": "https://www.google.com/maps/search/?api=1&query=Pontocho+Kyoto",
        "Arashiyama": "https://www.google.com/maps/search/?api=1&query=Arashiyama+Kyoto",
        "Dîner dans un izakaya": "https://www.google.com/maps/search/?api=1&query=Izakaya+Kyoto"
    }


  