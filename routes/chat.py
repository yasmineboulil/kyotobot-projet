from flask import Blueprint, render_template, request, jsonify
from services.ai_service import AIService

chat_bp = Blueprint('chat', __name__)
ai_service = AIService()

@chat_bp.route("/chatpage")
def chat_page():
    return render_template("chat.html")

@chat_bp.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("message", "").strip()
    
    is_inspire = user_input.lower() == "inspire-moi"
    bot_reply = ai_service.get_response(user_input, is_inspire=is_inspire)
    
    return jsonify({"reply": bot_reply})