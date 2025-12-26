from flask import Blueprint, render_template
from data import ITINERAIRES, LIEUX

itineraires_bp = Blueprint('itineraires', __name__)

@itineraires_bp.route("/itineraires")
def liste_itineraires():
    return render_template("itineraires.html", itineraires=ITINERAIRES)

@itineraires_bp.route("/itineraire/<int:itineraire_id>")
def detail_itineraire(itineraire_id):
    # Trouver l'itinéraire par son ID
    itineraire = next((i for i in ITINERAIRES if i['id'] == itineraire_id), None)
    
    if not itineraire:
        return "Itinéraire non trouvé", 404
    
    # Récupérer les détails des lieux pour chaque étape
    etapes_detaillees = []
    for etape in itineraire['etapes']:
        lieu = next((l for l in LIEUX if l['id'] == etape['lieu_id']), None)
        if lieu:
            etapes_detaillees.append({
                'lieu': lieu,
                'heure': etape['heure'],
                'notes': etape['notes']
            })
    
    return render_template("itineraire_detail.html", 
                          itineraire=itineraire, 
                          etapes=etapes_detaillees)