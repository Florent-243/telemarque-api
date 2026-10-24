from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemple de données partagées (en attendant une vraie base de données en ligne)
parametres_boutique = {
    "nom_boutique": "TELEMARQUE STORE",
    "taux_change": "2800.0",
}


# Route pour que ton site Netlify ou ton application lise les données
@app.route("/api/config", methods=["GET"])
def get_config():
  return jsonify(parametres_boutique)


# Route pour modifier les paramètres depuis le web (Netlify)
@app.route("/api/config", methods=["POST"])
def update_config():
  data = request.json
  if "taux_change" in data:
    parametres_boutique["taux_change"] = data["taux_change"]
  if "nom_boutique" in data:
    parametres_boutique["nom_boutique"] = data["nom_boutique"]
  return jsonify({"status": "succes", "message": "Paramètres mis à jour en ligne !"})


if __name__ == "__main__":
  app.run(debug=True)
