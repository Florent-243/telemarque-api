import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemple de données partagées
parametres_boutique = {
    "nom_boutique": "TELEMARQUE STORE",
    "taux_change": "2800.0",
}


@app.route("/api/config", methods=["GET"])
def get_config():
  return jsonify(parametres_boutique)


@app.route("/api/config", methods=["POST"])
def update_config():
  data = request.json
  if "taux_change" in data:
    parametres_boutique["taux_change"] = data["taux_change"]
  if "nom_boutique" in data:
    parametres_boutique["nom_boutique"] = data["nom_boutique"]
  return jsonify({"status": "succes", "message": "Paramètres mis à jour en ligne !"})


if __name__ == "__main__":
  # Récupère le port attribué automatiquement par Render (par défaut 5000 en local)
  port = int(os.environ.get("PORT", 5000))
  # Écoute sur 0.0.0.0 pour que Render puisse y accéder
  app.run(host="0.0.0.0", port=port)
