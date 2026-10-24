from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Fichier JSON pour stocker les configurations en ligne sur Render
CONFIG_FILE = "config_boutique.json"

# Données par défaut si le fichier n'existe pas encore
def charger_donnees():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    
    return {
        "nom_boutique": "TELEMARQUE STORE",
        "taux_change": "2800.0",
        "admin_code": "TELEMARQUE1234",
        "mot_de_passe_email": "1234",
        "email_cible": "florentchayeka@gmail.com",
        "auto_envoi_active": "NON",
        "auto_envoi_heure": "18:00"
    }

def sauvegarder_donnees(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/api/config", methods=["GET", "POST"])
def config_route():
    if request.method == "GET":
        # Renvoie toute la configuration au site web ou à ton application PC
        data = charger_donnees()
        return jsonify(data), 200

    elif request.method == "POST":
        # Reçoit les modifications envoyées depuis le site Netlify et les enregistre
        contenu = request.json
        if not contenu:
            return jsonify({"erreur": "Aucune donnée reçue"}), 400

        data = charger_donnees()

        # Met à jour l'ensemble des clés reçues
        for cle in data.keys():
            if cle in contenu:
                data[cle] = str(contenu[cle])

        sauvegarder_donnees(data)
        return jsonify({"succès": True, "donnees_mises_a_jour": data}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
