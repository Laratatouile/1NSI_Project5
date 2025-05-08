import torch
import torch.nn.functional as F
import torch.optim as optim
import os
import objects.affichage_pyxel as affichage_pyxel
import math
import fonctions.chiffrement as chiffrement
import random
import pyxel


def initialiser() -> dict:
    # creation ou ouverture de l'IA
    # si on a un model pret
    if os.listdir("./resources/torch") != []:
        # detection du nom du model
        nom_model = os.listdir("./resources/torch")[0].split(".")[0]
        # recherche des variables
        var_model = chiffrement.fichier_ouvrir(f"./resources/torch/{nom_model}.json", 8)
        model_entree = torch.nn.Linear(var_model["taille_entree"], var_model["taille_cachee"])
        model_sortie = torch.nn.Linear(var_model["taille_cachee"], var_model["taille_sortie"])
        learning_rate = var_model["learning_rate"]

    # si on en a pas
    else:
        # infos => x_perso, y_perso, direction lave, distance_lave, x_joueur, y_joueur
        taille_entree = 6
        # mvts => direction
        taille_sortie = 4
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
    model["entree"].train()
    model["sortie"].train()

    if "monstres" not in options_globales:
        options_globales["monstres"] = [{
            "etat": [7, 8, 0, 3, 6, 3, 100],  # état initial avec distance approximative
            "position": {"x": 800, "y": 2300},
            "recompense": 0
        }]
        return options_globales

    joueur_x = options_globales["player"]["x"]
    joueur_y = options_globales["player"]["y"]

    # 🔁 Met à jour la distance IA ↔ joueur dans l'état
    for monstre in options_globales["monstres"]:
        x = monstre["position"]["x"]
        y = monstre["position"]["y"]
        distance = math.hypot(x - joueur_x, y - joueur_y)

        if len(monstre["etat"]) >= 7:
            monstre["etat"][6] = distance
        else:
            monstre["etat"].append(distance)

    EPSILON = max(0.05, 0.3 - 0.00001 * pyxel.frame_count)

    for i, monstre in enumerate(options_globales["monstres"]):
        etat_actuel = torch.tensor(monstre["etat"], dtype=torch.float32)
        sortie = model_forward(etat_actuel, model)

        # Exploration ou exploitation
        if random.random() < EPSILON:
            action = {
                "droite":  random.choice([True, False]),
                "gauche":  random.choice([True, False]),
                "haut":    random.choice([True, False]),
                "bas":     random.choice([True, False])
            }
        else:
            SEUIL = 0.5
            action = {
                "droite":  sortie[0].item() > SEUIL,
                "gauche":  sortie[1].item() > SEUIL,
                "haut":    sortie[2].item() > SEUIL,
                "bas":     sortie[3].item() > SEUIL
            }

        if "position" not in monstre:
            monstre["position"] = {"x": 800, "y": 2300}

        vitesse = 2
        x, y = monstre["position"]["x"], monstre["position"]["y"]
        anc_dist = math.hypot(x - joueur_x, y - joueur_y)

        # Appliquer le mouvement
        if action["droite"]: x += vitesse
        if action["gauche"]: x -= vitesse
        if action["bas"]:    y += vitesse
        if action["haut"]:   y -= vitesse

        recompense = 0

        # Bordures
        if x < 0:
            x = 0
            recompense -= 10
        elif x > 850:
            x = 850
            recompense -= 10

        if y < 0:
            y = 0
            recompense -= 10
        elif y > 2450:
            y = 2450
            recompense -= 10

        monstre["position"]["x"] = x
        monstre["position"]["y"] = y

        dist = math.hypot(x - joueur_x, y - joueur_y)

        # Récompenses de déplacement
        if dist < anc_dist:
            recompense += 0.5
        elif dist > anc_dist:
            recompense -= 0.5

        if recompense >= 0 and any(action.values()):
            recompense += 0.2

        # Attaque uniquement si le monstre ne bouge pas et est proche
        if not any(action.values()) and dist < 20:
            monstre["attaque"] = True
            recompense += 100
            options_globales["player"]["vie"] = max(options_globales["player"]["vie"] - 10, 0)
            if options_globales["player"]["vie"] == 0:
                options_globales["player"]["mort"] = "zombie"

        # === Apprentissage ===
        if i in etat_prec and i in action_prec:
            sortie_prec = model_forward(etat_prec[i], model)
            cible = torch.zeros_like(sortie_prec)

            if action_prec[i]["droite"]: cible[0] = 1
            if action_prec[i]["gauche"]: cible[1] = 1
            if action_prec[i]["haut"]:   cible[2] = 1
            if action_prec[i]["bas"]:    cible[3] = 1

            cible *= recompense

            perte = model["perte"](sortie_prec, cible)
            model["optimiser"].zero_grad()
            perte.backward()
            model["optimiser"].step()

        etat_prec[i] = etat_actuel
        action_prec[i] = action
        monstre["recompense"] = recompense

    return options_globales






def draw(options_globales:dict, liste_datas_objets:dict) -> None:
    """ affiche les monstres """
    for monstre in options_globales["monstres"]:
        affichage_pyxel.draw_object(liste_datas_objets["monstre"], monstre["position"]["x"], monstre["position"]["y"])
    return None