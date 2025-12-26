# KyotoBot 

Assistant touristique intelligent pour la ville de Kyoto basé sur l'Intelligence Artificielle.

# Description

KyotoBot est une application web qui aide les touristes à planifier leur visite à Kyoto. 
Grâce à un chatbot intelligent alimenté par l'API Mistral AI, l'application génère des itinéraires 
personnalisés en fonction du budget, de la durée de séjour et des centres d'intérêt de l'utilisateur.

# Fonctionnalités

-  **Chatbot IA intelligent** : Conversation naturelle avec extraction automatique d'informations (budget, durée, intérêts)
-  **Guide des lieux** : Base de données de 35 lieux emblématiques de Kyoto avec filtres par catégorie
-  **Itinéraires prédéfinis** : 5 itinéraires complets et détaillés
-  **Navigation intégrée** : Liens vers Google Maps et connexions entre les pages
-  **Design moderne** : Interface élégante avec animations et effets visuels

##  Technologies utilisées

- **Backend** : Python, Flask
- **Frontend** : HTML5, CSS3, JavaScript
- **Intelligence Artificielle** : Mistral AI API (mistral-small-latest)
- **Bibliothèques** : Marked.js (rendu Markdown)

##  Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Clé API Mistral AI

## Étapes d'installation

1. **Cloner le dépôt**
```bash
   git clone https://github.com/VOTRE-PSEUDO/kyotobot-projet.git
   cd kyotobot-projet
```

2. **Installer les dépendances**
```bash
   pip install -r requirements.txt
```

3. **Configurer la clé API**
   - Ouvrir le fichier `config.py`
   - Remplacer `MISTRAL_API_KEY` par votre propre clé API

4. **Lancer l'application**
```bash
   python app.py
```

5. **Ouvrir dans le navigateur**
```
   http://localhost:5000
```


##  Architecture de l'IA

L'application utilise une approche hybride combinant :
- **IA générative** (Mistral AI) pour la génération de réponses conversationnelles
- **Extraction automatique** d'informations (budget, durée, intérêts, période)
- **Base de données structurée** (35 lieux, 5 itinéraires) pour des recommandations précises
- **Prompt engineering** pour des réponses adaptatives (courtes ou détaillées selon la demande)


Ce projet est réalisé dans un cadre pédagogique.
