import torch
import torch.nn.functional as F
import torch.optim as optim
import os
import json
import objects.affichage_pyxel as affichage_pyxel
import math


def initialiser() -> dict:
    # creation ou ouverture de l'IA
    # si on a un model pret
    if os.listdir("./resources/torch") != []:
        # detection du nom du model
        nom_model = os.listdir()[0].split(".")[0]
        print(nom_model)
        # recherche des variables
        var_model = json.load(open(f"./resources/torch/{nom_model}.json", "r"))
        model_entree = torch.nn.Linear(var_model["taille_entree"], var_model["taille_cachee"])
        model_sortie = torch.nn.Linear(var_model["taille_cachee"], var_model["taille_sortie"])
        learning_rate = var_model["learning_rate"]

    # si on en a pas
    else:
        # infos => x_perso, y_perso, direction lave, distance_lave, x_joueur, y_joueur
        taille_entree = 6
        # mvts => direction, attaque
        taille_sortie = 5
        # nombre de couches de neurones caches
        taille_cachee = 64
        model_entree = torch.nn.Linear(taille_entree, taille_cachee)
        model_sortie = torch.nn.Linear(taille_cachee, taille_sortie)
        learning_rate = 0.001


    params = list(model_entree.parameters()) + list(model_sortie.parameters())
    optimizer = optim.Adam(params, lr=learning_rate)
    model = {
        "entree" : model_entree,
        "sortie" : model_sortie,
        "perte" : torch.nn.MSELoss(),
        "optimiser" : optimizer
    }
    return model




def model_forward(x, model:dict) -> any:
    """ fonction de prediction """
    x = F.relu(model["entree"](x))
    x = model["sortie"](x)
    return x


etat_prec = {}
action_prec = {}

def update(options_globales: dict, model: dict) -> dict:
    if "monstres" not in options_globales:
        options_globales["monstres"] = []
        options_globales["monstres"].append({
            "etat": [7, 8, 0, 3, 6, 3],
            "position": {"x": 800, "y": 2300},
            "recompense": 0
        })
        return options_globales

    joueur_x = options_globales["player"]["x"]
    joueur_y = options_globales["player"]["y"]

    for i, monstre in enumerate(options_globales["monstres"]):
        etat_actuel = torch.tensor(monstre["etat"], dtype=torch.float32)

        # Apprentissage si possible
        if i in etat_prec and i in action_prec and "recompense" in monstre:
            with torch.no_grad():
                valeur_futur = torch.max(model_forward(etat_actuel, model))
                cible = monstre["recompense"] + 0.99 * valeur_futur

            pred = model_forward(etat_prec[i], model)[action_prec[i]]
            perte = model["perte"](pred, cible)

            model["optimiser"].zero_grad()
            perte.backward()
            model["optimiser"].step()

        # Choix de l'action
        with torch.no_grad():
            sortie = model_forward(etat_actuel, model)

        # Seuil pour activer une sortie (à ajuster si nécessaire)
        SEUIL = 0.5

        # Drapeaux d’action
        do_attaque = sortie[0].item() > SEUIL
        droite     = sortie[1].item() > SEUIL
        gauche     = sortie[2].item() > SEUIL
        haut       = sortie[3].item() > SEUIL
        bas        = sortie[4].item() > SEUIL


        # Si la position n'existe pas encore
        if "position" not in monstre:
            monstre["position"] = {"x": 800, "y": 2300}
        # Appliquer le déplacement
        vitesse = 2

        anc_dist_player = math.sqrt(abs(monstre["position"]["x"] - joueur_x)**2 + abs(monstre["position"]["y"] - joueur_y)**2)

        if droite:
            monstre["position"]["x"] += vitesse
            if monstre["position"]["x"] > 850:
                monstre["position"]["x"] = 850
                monstre["recompense"] -= 10
        if gauche:
            monstre["position"]["x"] -= vitesse
            if monstre["position"]["x"] < 0:
                monstre["position"]["x"] = 0
                monstre["recompense"] -= 10
        if bas:
            monstre["position"]["y"] += vitesse
            if monstre["position"]["y"] > 2450:
                monstre["position"]["y"] = 2450
                monstre["recompense"] -= 10
        if haut:
            monstre["position"]["y"] -= vitesse
            if monstre["position"]["y"] < 0:
                monstre["position"]["y"] = 0
                monstre["recompense"] -= 10

        if do_attaque:
            monstre["attaque"] = True
        
        dist_player = math.sqrt(abs(monstre["position"]["x"] - joueur_x)**2 + abs(monstre["position"]["y"] - joueur_y)**2)

        if anc_dist_player > dist_player:
            monstre["recompense"] += 1
        else:
            monstre["recompense"] -= 1


    return options_globales




def draw(options_globales:dict, liste_datas_objets:dict) -> None:
    """ affiche les monstres """
    for monstre in options_globales["monstres"]:
        affichage_pyxel.draw_object(liste_datas_objets["monstre"], monstre["position"]["x"], monstre["position"]["y"])
    return None