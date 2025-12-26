from flask import Blueprint, render_template, request
from data import LIEUX, CATEGORIES

lieux_bp = Blueprint('lieux', __name__)

@lieux_bp.route("/lieux")
def guide_lieux():
    # Récupérer le filtre de catégorie s'il existe
    categorie_filter = request.args.get('categorie', None)
    
    # Filtrer les lieux si une catégorie est sélectionnée
    if categorie_filter and categorie_filter != 'tous':
        lieux_filtres = [lieu for lieu in LIEUX if lieu['categorie'] == categorie_filter]
    else:
        lieux_filtres = LIEUX
    
    return render_template("lieux.html", 
                          lieux=lieux_filtres, 
                          categories=CATEGORIES,
                          categorie_active=categorie_filter)

@lieux_bp.route("/lieu/<int:lieu_id>")
def detail_lieu(lieu_id):
    # Trouver le lieu par son ID
    lieu = next((l for l in LIEUX if l['id'] == lieu_id), None)
    
    if lieu:
        return render_template("lieu_detail.html", lieu=lieu)
    else:
        return "Lieu non trouvé", 404