# services/ai_service.py
from mistralai import Mistral
from config import Config
from data import LIEUX
import re
import json
from datetime import datetime

class AIService:
    def __init__(self):
        self.client = Mistral(api_key=Config.MISTRAL_API_KEY)
        self.conversation_history = []
        self.user_context = {
            "budget": None,
            "duree": None,
            "interets": [],
            "periode": None
        }
        self.stats = {
            "total_messages": 0,
            "topics": {},
            "budgets": [],
            "durees": []
        }
    
    def extract_user_info(self, message):
        """
        Extrait automatiquement les informations importantes du message utilisateur
        """
        message_lower = message.lower()
        
        # Extraction du budget
        budget_patterns = [
            r'(\d+)\s*€',
            r'(\d+)\s*euros?',
            r'(\d+)\s*¥',
            r'(\d+)\s*yens?',
            r'budget.*?(\d+)',
        ]
        for pattern in budget_patterns:
            match = re.search(pattern, message_lower)
            if match:
                self.user_context["budget"] = int(match.group(1))
                self.stats["budgets"].append(int(match.group(1)))
                break
        
        # Extraction de la durée
        duree_patterns = [
            (r'(\d+)\s*jours?', 'jours'),
            (r'(\d+)\s*heures?', 'heures'),
            (r'(\d+)h', 'heures'),
            (r'(\d+)\s*semaines?', 'semaines'),
            (r'demi[- ]journ[ée]+', 'demi-journée'),
            (r'journ[ée]+', '1 jour')
        ]
        for pattern, unit in duree_patterns:
            match = re.search(pattern, message_lower)
            if match:
                if unit in ['jours', 'heures', 'semaines']:
                    self.user_context["duree"] = f"{match.group(1)} {unit}"
                    self.stats["durees"].append(f"{match.group(1)} {unit}")
                else:
                    self.user_context["duree"] = unit
                    self.stats["durees"].append(unit)
                break
        
        # Extraction des centres d'intérêt
        interets_keywords = {
            "temples": ["temple", "temples", "sanctuaire", "religieux", "spirituel"],
            "nature": ["jardin", "nature", "bambou", "parc", "zen", "promenade"],
            "gastronomie": ["manger", "restaurant", "nourriture", "cuisine", "ramen", "sushi", "kaiseki"],
            "culture": ["culture", "geisha", "traditionnel", "histoire", "musée"],
            "shopping": ["shopping", "boutique", "marché", "achats"]
        }
        
        for interet, keywords in interets_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                if interet not in self.user_context["interets"]:
                    self.user_context["interets"].append(interet)
        
        # Extraction de la période
        periodes = {
            "printemps": ["printemps", "mars", "avril", "mai", "cerisiers", "sakura"],
            "été": ["été", "juin", "juillet", "août"],
            "automne": ["automne", "septembre", "octobre", "novembre", "feuillages", "momiji"],
            "hiver": ["hiver", "décembre", "janvier", "février"]
        }
        
        for periode, keywords in periodes.items():
            if any(keyword in message_lower for keyword in keywords):
                self.user_context["periode"] = periode
                break
    
    def get_relevant_places(self):
        """
        Recommande des lieux basés sur le contexte utilisateur
        """
        if not self.user_context["interets"]:
            return []
        
        relevant = []
        interest_mapping = {
            "temples": "temple",
            "nature": "jardin",
            "gastronomie": "restaurant",
            "shopping": "marche",
            "culture": "quartier"
        }
        
        for interet in self.user_context["interets"]:
            categorie = interest_mapping.get(interet)
            if categorie:
                places = [lieu for lieu in LIEUX if lieu["categorie"] == categorie]
                relevant.extend(places[:3])  # Top 3 par catégorie
        
        return relevant
    
    def enrich_prompt(self, user_message):
        """
        Enrichit le message avec le contexte extrait et les recommandations
        """
        context_info = ""
        
        if self.user_context["budget"]:
            context_info += f"\n[CONTEXTE DÉTECTÉ] Budget: {self.user_context['budget']}€"
        if self.user_context["duree"]:
            context_info += f"\n[CONTEXTE DÉTECTÉ] Durée: {self.user_context['duree']}"
        if self.user_context["interets"]:
            context_info += f"\n[CONTEXTE DÉTECTÉ] Intérêts: {', '.join(self.user_context['interets'])}"
        if self.user_context["periode"]:
            context_info += f"\n[CONTEXTE DÉTECTÉ] Période: {self.user_context['periode']}"
        
        relevant_places = self.get_relevant_places()
        if relevant_places:
            context_info += "\n\n[LIEUX RECOMMANDÉS DE LA BASE DE DONNÉES]:\n"
            for place in relevant_places[:5]:
                context_info += f"- {place['nom']} ({place['categorie']}) - {place['prix']} - {place['duree']}\n"
        
        return user_message + context_info
    
    def update_stats(self, user_message):
        """
        Met à jour les statistiques d'utilisation
        """
        self.stats["total_messages"] += 1
        
        # Analyse des topics
        topics = ["temple", "jardin", "restaurant", "transport", "budget", "itinéraire"]
        for topic in topics:
            if topic in user_message.lower():
                self.stats["topics"][topic] = self.stats["topics"].get(topic, 0) + 1
    
    def get_response(self, user_message, is_inspire=False):
        """
        Obtient une réponse de l'IA avec extraction d'infos et enrichissement
        """
        # Mise à jour des stats
        self.update_stats(user_message)
        
        if is_inspire:
            prompt = Config.PROMPT_INSPIRE
            self.conversation_history.clear()
            self.conversation_history.append({"role": "user", "content": prompt})
        else:
            # Extraction des infos utilisateur
            self.extract_user_info(user_message)
            
            # Enrichissement du prompt avec contexte
            enriched_message = self.enrich_prompt(user_message)
            
            self.conversation_history.append({"role": "user", "content": enriched_message})
        
        messages = [{"role": "system", "content": Config.SYSTEM_PROMPT}] + self.conversation_history
        
        try:
            resp = self.client.chat.complete(
                model="mistral-small-latest",
                messages=messages
            )
            
            bot_reply = resp.choices[0].message.content
            bot_reply = self._add_maps_links(bot_reply)
            self.conversation_history.append({"role": "assistant", "content": bot_reply})
            
            return bot_reply
        except Exception as e:
            return f"❌ Désolé, une erreur s'est produite : {str(e)}. Veuillez réessayer."
    
    def _add_maps_links(self, text):
        """
        Ajoute des liens Google Maps aux lieux connus
        """
        for place, link in Config.KNOWN_PLACES.items():
            # Remplacer uniquement si le lieu n'est pas déjà un lien
            if place in text and f'href="{link}"' not in text:
                text = text.replace(place, f'<a href="{link}" target="_blank">{place}</a>')
        return text
    
    def reset_conversation(self):
        """
        Réinitialise l'historique et le contexte
        """
        self.conversation_history.clear()
        self.user_context = {
            "budget": None,
            "duree": None,
            "interets": [],
            "periode": None
        }
    
    def get_stats(self):
        """
        Retourne les statistiques pour analyse (utile pour le rapport !)
        """
        return {
            "total_messages": self.stats["total_messages"],
            "topics_populaires": dict(sorted(self.stats["topics"].items(), key=lambda x: x[1], reverse=True)),
            "budget_moyen": sum(self.stats["budgets"]) / len(self.stats["budgets"]) if self.stats["budgets"] else 0,
            "durees": self.stats["durees"],
            "contexte_actuel": self.user_context
        }