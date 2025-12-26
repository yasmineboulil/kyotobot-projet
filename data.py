# data.py

LIEUX = [
    # ===== TEMPLES =====
    {
        "id": 1,
        "nom": "Temple Kiyomizu-dera",
        "categorie": "temple",
        "description": "Temple bouddhiste emblématique perché sur une colline avec une vue spectaculaire sur Kyoto. Célèbre pour sa terrasse en bois construite sans clous.",
        "duree": "1h30",
        "prix": "400¥",
        "conseil": "Visitez tôt le matin pour éviter la foule. Magnifique lors de la floraison des cerisiers.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Kiyomizu-dera+Kyoto",
        "image": "kiyomizu.jpg"
    },
    {
        "id": 2,
        "nom": "Temple Kinkaku-ji (Pavillon d'Or)",
        "categorie": "temple",
        "description": "Temple zen recouvert de feuilles d'or, entouré d'un magnifique jardin japonais avec un étang.",
        "duree": "1h",
        "prix": "500¥",
        "conseil": "Idéal en fin de matinée quand le soleil illumine le pavillon doré.",
        "quartier": "Kita",
        "maps": "https://www.google.com/maps/search/?api=1&query=Kinkaku-ji+Kyoto",
        "image": "kinkakuji.jpg"
    },
    {
        "id": 3,
        "nom": "Temple Fushimi Inari",
        "categorie": "temple",
        "description": "Célèbre pour ses milliers de torii vermillon formant des tunnels sur la montagne. Dédié à la déesse du riz.",
        "duree": "2h-3h",
        "prix": "Gratuit",
        "conseil": "Randonnée de 2h pour atteindre le sommet. Moins de monde tôt le matin ou en soirée.",
        "quartier": "Fushimi",
        "maps": "https://www.google.com/maps/search/?api=1&query=Fushimi+Inari+Kyoto",
        "image": "fushimi.jpg"
    },
    {
        "id": 4,
        "nom": "Temple Ginkaku-ji (Pavillon d'Argent)",
        "categorie": "temple",
        "description": "Temple zen avec jardins secs et mousses. Malgré son nom, il n'est pas recouvert d'argent mais offre une élégance sobre.",
        "duree": "1h",
        "prix": "500¥",
        "conseil": "Montez jusqu'au point de vue pour admirer Kyoto. Parfait en automne avec les feuillages.",
        "quartier": "Sakyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Ginkaku-ji+Kyoto",
        "image": "ginkakuji.jpg"
    },
    {
        "id": 5,
        "nom": "Temple Nanzen-ji",
        "categorie": "temple",
        "description": "Grand complexe zen avec un aqueduc en briques rouges photogénique et de magnifiques jardins.",
        "duree": "1h30",
        "prix": "600¥",
        "conseil": "Ne manquez pas l'aqueduc et le jardin Tenjuan. Gratuit d'explorer les enceintes extérieures.",
        "quartier": "Sakyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Nanzen-ji+Kyoto",
        "image": "nanzenji.jpg"
    },
    {
        "id": 6,
        "nom": "Temple Byodo-in",
        "categorie": "temple",
        "description": "Temple inscrit au patrimoine mondial, représenté sur les pièces de 10 yen. Architecture du Paradis de la Terre Pure.",
        "duree": "1h",
        "prix": "600¥",
        "conseil": "Situé à Uji (30 min de Kyoto). Combinez avec une visite des plantations de thé.",
        "quartier": "Uji",
        "maps": "https://www.google.com/maps/search/?api=1&query=Byodo-in+Uji",
        "image": "byodoin.jpg"
    },
    {
        "id": 7,
        "nom": "Temple Sanjusangendo",
        "categorie": "temple",
        "description": "Hall long de 120m abritant 1001 statues de Kannon dorées. Impressionnant et unique.",
        "duree": "45min",
        "prix": "600¥",
        "conseil": "Photos interdites à l'intérieur. Venez tôt pour admirer les statues dans le calme.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Sanjusangendo+Kyoto",
        "image": "sanjusangendo.jpg"
    },
    
    # ===== JARDINS & NATURE =====
    {
        "id": 8,
        "nom": "Jardin Ryoan-ji",
        "categorie": "jardin",
        "description": "Jardin zen minimaliste mondialement connu pour son jardin de pierres. Méditation et contemplation.",
        "duree": "45min",
        "prix": "500¥",
        "conseil": "Visitez en semaine pour profiter du calme. Parfait pour la méditation.",
        "quartier": "Ukyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Ryoan-ji+Kyoto",
        "image": "ryoanji.jpg"
    },
    {
        "id": 9,
        "nom": "Forêt de bambous d'Arashiyama",
        "categorie": "jardin",
        "description": "Majestueuse allée de bambous géants créant une atmosphère mystique et apaisante.",
        "duree": "30min-1h",
        "prix": "Gratuit",
        "conseil": "Allez-y très tôt le matin (7h) pour éviter les touristes et profiter de la sérénité.",
        "quartier": "Arashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Bamboo+Forest+Arashiyama+Kyoto",
        "image": "bamboo.jpg"
    },
    {
        "id": 10,
        "nom": "Chemin de la Philosophie",
        "categorie": "jardin",
        "description": "Promenade de 2km le long d'un canal bordé de cerisiers. Idéal pour une balade contemplative.",
        "duree": "1h-1h30",
        "prix": "Gratuit",
        "conseil": "Incontournable au printemps (sakura) et en automne (momiji). Connecte Ginkaku-ji à Nanzen-ji.",
        "quartier": "Sakyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Philosopher's+Path+Kyoto",
        "image": "philosopher.jpg"
    },
    {
        "id": 11,
        "nom": "Parc Maruyama",
        "categorie": "jardin",
        "description": "Grand parc public avec un célèbre cerisier pleureur illuminé la nuit au printemps.",
        "duree": "1h",
        "prix": "Gratuit",
        "conseil": "Parfait pour un hanami (pique-nique sous les cerisiers) en avril.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Maruyama+Park+Kyoto",
        "image": "maruyama.jpg"
    },
    {
        "id": 12,
        "nom": "Jardin Okochi Sanso",
        "categorie": "jardin",
        "description": "Villa et jardin d'un acteur de cinéma avec vue panoramique sur Kyoto et Arashiyama.",
        "duree": "45min",
        "prix": "1000¥ (inclut thé matcha)",
        "conseil": "Moins touristique qu'Arashiyama. Vue magnifique depuis les hauteurs.",
        "quartier": "Arashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Okochi+Sanso+Kyoto",
        "image": "okochi.jpg"
    },
    
    # ===== MARCHÉS =====
    {
        "id": 13,
        "nom": "Marché de Nishiki",
        "categorie": "marche",
        "description": "Marché couvert de 400m appelé 'la cuisine de Kyoto'. Plus de 100 boutiques de produits frais et spécialités locales.",
        "duree": "1h-1h30",
        "prix": "Gratuit (achats en plus)",
        "conseil": "Goûtez les spécialités : tsukemono, mochi, tamagoyaki. Fermé mercredi pour certaines boutiques.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Nishiki+Market+Kyoto",
        "image": "nishiki.jpg"
    },
    {
        "id": 14,
        "nom": "Marché Kobo-san (Temple To-ji)",
        "categorie": "marche",
        "description": "Marché aux puces mensuel (21 de chaque mois) avec antiquités, artisanat et nourriture.",
        "duree": "1h-2h",
        "prix": "Gratuit",
        "conseil": "Plus de 1000 stands. Venez tôt pour les meilleures trouvailles. Atmosphère authentique.",
        "quartier": "Minami",
        "maps": "https://www.google.com/maps/search/?api=1&query=Toji+Temple+Market+Kyoto",
        "image": "kobo.jpg"
    },
    
    # ===== QUARTIERS =====
    {
        "id": 15,
        "nom": "Quartier de Gion",
        "categorie": "quartier",
        "description": "Quartier historique des geishas avec ses maisons en bois traditionnelles et ruelles pavées.",
        "duree": "2h",
        "prix": "Gratuit",
        "conseil": "Promenez-vous le soir pour apercevoir des geikos et maikos. Respectez leur espace, ne les suivez pas.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Gion+Kyoto",
        "image": "gion.jpg"
    },
    {
        "id": 16,
        "nom": "Pontocho",
        "categorie": "quartier",
        "description": "Ruelle étroite bordée de restaurants traditionnels et modernes. Ambiance magique le soir avec les lanternes.",
        "duree": "1h-2h",
        "prix": "Variable (restaurants)",
        "conseil": "Idéal pour dîner dans un restaurant traditionnel kaiseki ou izakaya en bord de rivière.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Pontocho+Kyoto",
        "image": "pontocho.jpg"
    },
    {
        "id": 17,
        "nom": "Quartier d'Arashiyama",
        "categorie": "quartier",
        "description": "Zone pittoresque à l'ouest de Kyoto avec le pont Togetsukyo, temples et nature.",
        "duree": "Demi-journée",
        "prix": "Gratuit (attractions payantes)",
        "conseil": "Combinez forêt de bambous, temples et balade en rickshaw. Louez un vélo pour explorer.",
        "quartier": "Arashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Arashiyama+Kyoto",
        "image": "arashiyama.jpg"
    },
    {
        "id": 18,
        "nom": "Quartier de Higashiyama",
        "categorie": "quartier",
        "description": "Quartier préservé avec ruelles traditionnelles, boutiques d'artisanat et temples historiques.",
        "duree": "2h-3h",
        "prix": "Gratuit",
        "conseil": "Montez les rues Ninenzaka et Sannenzaka. Louez un kimono pour une expérience immersive.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Higashiyama+District+Kyoto",
        "image": "higashiyama.jpg"
    },
    
    # ===== RESTAURANTS =====
    {
        "id": 19,
        "nom": "Kikunoi",
        "categorie": "restaurant",
        "description": "Restaurant kaiseki 3 étoiles Michelin offrant une expérience culinaire traditionnelle raffinée.",
        "duree": "2h-3h",
        "prix": "15000-30000¥",
        "conseil": "Réservation obligatoire plusieurs semaines à l'avance. Expérience gastronomique inoubliable.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Kikunoi+Kyoto",
        "image": "kikunoi.jpg"
    },
    {
        "id": 20,
        "nom": "Ippudo Ramen",
        "categorie": "restaurant",
        "description": "Chaîne de ramen populaire offrant d'excellents ramens tonkotsu à prix abordable.",
        "duree": "45min-1h",
        "prix": "1000-1500¥",
        "conseil": "File d'attente possible aux heures de pointe. Le ramen shiromaru est un classique.",
        "quartier": "Plusieurs",
        "maps": "https://www.google.com/maps/search/?api=1&query=Ippudo+Ramen+Kyoto",
        "image": "ippudo.jpg"
    },
    {
        "id": 21,
        "nom": "Nishiki Warai",
        "categorie": "restaurant",
        "description": "Restaurant d'okonomiyaki (crêpe japonaise garnie) populaire dans le marché de Nishiki.",
        "duree": "1h",
        "prix": "1200-2000¥",
        "conseil": "Essayez l'okonomiyaki au fruits de mer. Ambiance conviviale, cuisine devant vous.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Nishiki+Warai+Kyoto",
        "image": "warai.jpg"
    },
    {
        "id": 22,
        "nom": "Yoshikawa Tempura",
        "categorie": "restaurant",
        "description": "Restaurant traditionnel spécialisé dans les tempuras avec jardin zen.",
        "duree": "1h30",
        "prix": "5000-10000¥",
        "conseil": "Asseyez-vous au comptoir pour voir le chef préparer les tempuras. Réservation recommandée.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Yoshikawa+Tempura+Kyoto",
        "image": "yoshikawa.jpg"
    },
    {
        "id": 23,
        "nom": "Gion Tanto",
        "categorie": "restaurant",
        "description": "Restaurant de gyoza (raviolis japonais) artisanaux dans le quartier de Gion.",
        "duree": "45min",
        "prix": "800-1500¥",
        "conseil": "Spécialité : gyoza au porc avec sauce maison. Petit restaurant familial, arrivez tôt.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Gion+Tanto+Kyoto",
        "image": "tanto.jpg"
    },
    {
        "id": 24,
        "nom": "Honke Owariya",
        "categorie": "restaurant",
        "description": "Restaurant de soba (nouilles de sarrasin) historique établi en 1465. Le plus ancien de Kyoto.",
        "duree": "1h",
        "prix": "1500-3000¥",
        "conseil": "Goûtez le hourai soba servi dans cinq petites boîtes laquées. Atmosphère traditionnelle.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Honke+Owariya+Kyoto",
        "image": "owariya.jpg"
    },
    {
        "id": 25,
        "nom": "Izuju",
        "categorie": "restaurant",
        "description": "Restaurant de sushi traditionnel de Kyoto (sabazushi - sushi de maquereau mariné).",
        "duree": "45min",
        "prix": "1500-2500¥",
        "conseil": "Spécialité locale unique à Kyoto. Commandez le sabazushi classique à emporter ou sur place.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Izuju+Kyoto",
        "image": "izuju.jpg"
    },
    # ===== HÉBERGEMENTS =====
    {
        "id": 26,
        "nom": "Ryokan Yoshikawa",
        "categorie": "hebergement",
        "description": "Ryokan traditionnel de luxe avec chambres tatami, futons et onsen privé. Expérience authentique avec dîner kaiseki inclus.",
        "duree": "Nuit",
        "prix": "30000-50000¥/nuit",
        "conseil": "Réservez longtemps à l'avance. Dîner kaiseki exceptionnel inclus. Expérience traditionnelle japonaise complète.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Ryokan+Yoshikawa+Kyoto",
        "image": "yoshikawa.jpg"
    },
    {
        "id": 27,
        "nom": "Hotel Gracery Kyoto Sanjo",
        "categorie": "hebergement",
        "description": "Hôtel moderne et confortable près de la gare de Sanjo. Excellent rapport qualité-prix avec chambres occidentales.",
        "duree": "Nuit",
        "prix": "8000-15000¥/nuit",
        "conseil": "Idéalement situé pour explorer le centre. Station de métro à 3 min à pied. Chambres petites mais bien équipées.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Hotel+Gracery+Kyoto+Sanjo",
        "image": "gracery.jpg"
    },
    {
        "id": 28,
        "nom": "K's House Kyoto",
        "categorie": "hebergement",
        "description": "Auberge de jeunesse moderne et sociale avec dortoirs et chambres privées. Atmosphère conviviale et internationale.",
        "duree": "Nuit",
        "prix": "2500-6000¥/nuit",
        "conseil": "Parfait pour les petits budgets et rencontrer d'autres voyageurs. Cuisine commune disponible. Très propre.",
        "quartier": "Shimogyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=K's+House+Kyoto",
        "image": "kshouse.jpg"
    },
    {
        "id": 29,
        "nom": "The Millennials Kyoto",
        "categorie": "hebergement",
        "description": "Hôtel capsule futuriste avec lits pods personnalisables. Design moderne et technologique.",
        "duree": "Nuit",
        "prix": "3000-5000¥/nuit",
        "conseil": "Expérience unique de capsule hotel moderne. Parfait pour voyageurs solo. Wifi excellent.",
        "quartier": "Shimogyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=The+Millennials+Kyoto",
        "image": "millennials.jpg"
    },
    {
        "id": 30,
        "nom": "Guesthouse Kyoto Oumi",
        "categorie": "hebergement",
        "description": "Maison d'hôtes chaleureuse dans une machiya (maison traditionnelle). Ambiance familiale et authentique.",
        "duree": "Nuit",
        "prix": "4000-8000¥/nuit",
        "conseil": "Propriétaires adorables et serviables. Petite mais très cosy. Cuisine commune. Parfait pour expérience locale.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Guesthouse+Kyoto+Oumi",
        "image": "oumi.jpg"
    },
    {
        "id": 31,
        "nom": "Rihga Royal Hotel Kyoto",
        "categorie": "hebergement",
        "description": "Grand hôtel 5 étoiles près de la gare de Kyoto. Confort occidental premium avec restaurants et spa.",
        "duree": "Nuit",
        "prix": "15000-30000¥/nuit",
        "conseil": "Idéal pour voyageurs exigeant confort occidental. Proche de la gare JR. Petit-déjeuner buffet excellent.",
        "quartier": "Shimogyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Rihga+Royal+Hotel+Kyoto",
        "image": "rihga.jpg"
    },
    {
        "id": 32,
        "nom": "Piece Hostel Sanjo",
        "categorie": "hebergement",
        "description": "Auberge design avec café intégré. Mélange parfait entre confort et budget. Ambiance artistique.",
        "duree": "Nuit",
        "prix": "3500-7000¥/nuit",
        "conseil": "Excellent café au rez-de-chaussée. Design soigné. Bon compromis qualité-prix pour jeunes voyageurs.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Piece+Hostel+Sanjo+Kyoto",
        "image": "piece.jpg"
    },
    {
        "id": 33,
        "nom": "Kyoto Gion Ryokan Q-beh",
        "categorie": "hebergement",
        "description": "Petit ryokan abordable dans le quartier de Gion. Chambres traditionnelles simples mais authentiques.",
        "duree": "Nuit",
        "prix": "8000-15000¥/nuit",
        "conseil": "Emplacement exceptionnel à Gion. Expérience ryokan à prix raisonnable. Réservez tôt.",
        "quartier": "Higashiyama",
        "maps": "https://www.google.com/maps/search/?api=1&query=Kyoto+Gion+Ryokan+Q-beh",
        "image": "qbeh.jpg"
    },
    {
        "id": 34,
        "nom": "Sakura Terrace The Gallery",
        "categorie": "hebergement",
        "description": "Hôtel boutique élégant avec galerie d'art. Design contemporain inspiré de l'art japonais traditionnel.",
        "duree": "Nuit",
        "prix": "12000-20000¥/nuit",
        "conseil": "Proche de la gare de Kyoto (7 min à pied). Onsen sur le toit. Design magnifique. Excellent petit-déjeuner.",
        "quartier": "Minami",
        "maps": "https://www.google.com/maps/search/?api=1&query=Sakura+Terrace+The+Gallery+Kyoto",
        "image": "sakura.jpg"
    },
    {
        "id": 35,
        "nom": "Len Kyoto Kawaramachi",
        "categorie": "hebergement",
        "description": "Hôtel capsule premium pour femmes uniquement. Très sécurisé, propre et confortable.",
        "duree": "Nuit",
        "prix": "4000-6000¥/nuit",
        "conseil": "Réservé aux femmes. Excellente sécurité. Design féminin et soigné. Centre-ville accessible.",
        "quartier": "Nakagyo",
        "maps": "https://www.google.com/maps/search/?api=1&query=Len+Kyoto+Kawaramachi",
        "image": "len.jpg"
    }
]

CATEGORIES = [
    {"id": "temple", "nom": "Temples", "emoji": "🏯"},
    {"id": "jardin", "nom": "Jardins & Nature", "emoji": "🌳"},
    {"id": "marche", "nom": "Marchés", "emoji": "🛍️"},
    {"id": "quartier", "nom": "Quartiers", "emoji": "🏘️"},
    {"id": "restaurant", "nom": "Restaurants", "emoji": "🍜"},
    {"id": "hebergement", "nom": "Hébergements", "emoji": "🏨"} 
]



ITINERAIRES = [
    {
        "id": 1,
        "nom": "Kyoto en 1 jour",
        "emoji": "🌸",
        "duree": "1 journée",
        "budget": "5000-8000¥",
        "description": "L'essentiel de Kyoto en une journée bien remplie : temples iconiques, quartiers traditionnels et gastronomie locale.",
        "etapes": [
            {"lieu_id": 3, "heure": "8h00", "notes": "Arrivez tôt pour éviter la foule aux torii"},
            {"lieu_id": 1, "heure": "10h30", "notes": "Vue panoramique sur Kyoto"},
            {"lieu_id": 18, "heure": "12h00", "notes": "Déjeuner et shopping dans les ruelles"},
            {"lieu_id": 15, "heure": "14h30", "notes": "Balade dans le quartier des geishas"},
            {"lieu_id": 13, "heure": "16h30", "notes": "Goûtez les spécialités locales"},
            {"lieu_id": 16, "heure": "19h00", "notes": "Dîner dans un restaurant traditionnel"}
        ],
        "conseils": "Achetez un pass bus journalier (700¥). Portez des chaussures confortables. Prévoyez de l'eau."
    },
    {
        "id": 2,
        "nom": "Circuit temples classiques",
        "emoji": "⛩️",
        "duree": "1 journée",
        "budget": "3000-4000¥",
        "description": "Plongez dans l'histoire et la spiritualité de Kyoto en visitant ses temples les plus emblématiques.",
        "etapes": [
            {"lieu_id": 2, "heure": "9h00", "notes": "Pavillon doré illuminé par le soleil du matin"},
            {"lieu_id": 8, "heure": "11h00", "notes": "Jardin zen et méditation"},
            {"lieu_id": 5, "heure": "13h30", "notes": "Aqueduc photogénique et jardins"},
            {"lieu_id": 4, "heure": "15h30", "notes": "Pavillon d'argent et point de vue"},
            {"lieu_id": 7, "heure": "17h00", "notes": "1001 statues dorées de Kannon"}
        ],
        "conseils": "Commencez tôt pour profiter du calme. Photos interdites dans certains temples. Respectez le silence."
    },
    {
        "id": 3,
        "nom": "Kyoto gourmand",
        "emoji": "🍜",
        "duree": "Demi-journée",
        "budget": "4000-6000¥",
        "description": "Un voyage culinaire à travers les saveurs authentiques de Kyoto, du marché aux restaurants traditionnels.",
        "etapes": [
            {"lieu_id": 13, "heure": "10h00", "notes": "Dégustations au marché : tsukemono, mochi, tamagoyaki"},
            {"lieu_id": 21, "heure": "12h00", "notes": "Déjeuner d'okonomiyaki"},
            {"lieu_id": 24, "heure": "14h30", "notes": "Goûter de soba traditionnel"},
            {"lieu_id": 25, "heure": "16h00", "notes": "Sushi de maquereau (spécialité Kyoto)"},
            {"lieu_id": 16, "heure": "19h00", "notes": "Dîner dans un izakaya en bord de rivière"}
        ],
        "conseils": "Venez avec l'estomac vide ! Évitez si allergies alimentaires. Apportez du cash (certains n'acceptent pas les cartes)."
    },
    {
        "id": 4,
        "nom": "Nature & Zen",
        "emoji": "🌳",
        "duree": "1 journée",
        "budget": "2000-3000¥",
        "description": "Échappez à l'agitation urbaine et reconnectez-vous avec la nature dans les jardins et forêts de Kyoto.",
        "etapes": [
            {"lieu_id": 9, "heure": "7h30", "notes": "Forêt de bambous au lever du soleil (presque seul)"},
            {"lieu_id": 12, "heure": "9h00", "notes": "Villa avec vue panoramique et thé matcha inclus"},
            {"lieu_id": 10, "heure": "11h00", "notes": "Promenade contemplative le long du canal"},
            {"lieu_id": 11, "heure": "14h00", "notes": "Pique-nique sous les cerisiers"},
            {"lieu_id": 8, "heure": "16h00", "notes": "Méditation dans le jardin de pierres"}
        ],
        "conseils": "Parfait au printemps (sakura) et en automne (koyo). Apportez un bento pour le pique-nique."
    },
    {
        "id": 5,
        "nom": "Kyoto Instagram",
        "emoji": "📸",
        "duree": "1 journée",
        "budget": "4000-6000¥",
        "description": "Les spots les plus photogéniques de Kyoto pour des photos mémorables. Option : louez un kimono !",
        "etapes": [
            {"lieu_id": 3, "heure": "8h00", "notes": "Torii vermillon au lever du soleil"},
            {"lieu_id": 9, "heure": "10h00", "notes": "Allée de bambous géants"},
            {"lieu_id": 18, "heure": "12h00", "notes": "Ruelles Ninenzaka et Sannenzaka en kimono"},
            {"lieu_id": 15, "heure": "15h00", "notes": "Maisons en bois traditionnelles"},
            {"lieu_id": 2, "heure": "17h00", "notes": "Pavillon doré au coucher du soleil"}
        ],
        "conseils": "Louez un kimono à Higashiyama (3000-5000¥). Arrivez tôt aux spots populaires. Batterie externe pour smartphone !"
    }
     
]