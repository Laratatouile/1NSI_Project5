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
    model["entree"].train()
    model["sortie"].train()

    print(options_globales["monstres"][0]["recompense"])

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
        if i in etat_prec and "recompense" in monstre:
            with torch.no_grad():
                pred_suiv = model_forward(etat_actuel, model)

            # Cible = sorties précédentes légèrement modifiées par la récompense
            cible = model_forward(etat_prec[i], model).clone().detach()

            # Appliquer la récompense sur **toutes les sorties**
            if do_attaque:
                cible[0] += monstre["recompense"]
            if droite:
                cible[1] += monstre["recompense"]
            if gauche:
                cible[2] += monstre["recompense"]
            if haut:
                cible[3] += monstre["recompense"]
            if bas:
                cible[4] += monstre["recompense"]

            # Prédiction actuelle
            pred = model_forward(etat_prec[i], model)

            perte = model["perte"](sortie, cible)

            model["optimiser"].zero_grad()
            perte.backward()
            model["optimiser"].step()

        # Choix de l'action
        with torch.no_grad():
            sortie = model_forward(etat_actuel, model)

        monstre["recompense"] = 0

        # Valeur de epsilon (pourcentage d'exploration)
        EPSILON = 0.3 - (0.0001 * pyxel.frame_count())

        if random.random() < EPSILON:
            # Choix aléatoire (exploration)
            do_attaque = random.choice([True, False])
            droite = random.choice([True, False])
            gauche = random.choice([True, False])
            haut = random.choice([True, False])
            bas = random.choice([True, False])
        else:
            # Choix basé sur la sortie du modèle
            SEUIL = 0.5
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

        dist_player = math.sqrt(abs(monstre["position"]["x"] - joueur_x)**2 + abs(monstre["position"]["y"] - joueur_y)**2)
        
        if do_attaque:
            monstre["attaque"] = True
            if dist_player < 20:
                monstre["recompense"] += 100
                options_globales["player"]["vie"] = max(options_globales["player"]["vie"] - 10, 0)
                if options_globales["player"]["vie"] == 0:
                    options_globales["player"]["mort"] = "zombie"

        if anc_dist_player > dist_player:
            monstre["recompense"] += 1


        cible = torch.zeros_like(sortie)
        cible[0] = 1 if do_attaque else 0
        cible[1] = 1 if droite else 0
        cible[2] = 1 if gauche else 0
        cible[3] = 1 if haut else 0
        cible[4] = 1 if bas else 0

        cible *= monstre["recompense"]



    return options_globales




def draw(options_globales:dict, liste_datas_objets:dict) -> None:
    """ affiche les monstres """
    for monstre in options_globales["monstres"]:
        affichage_pyxel.draw_object(liste_datas_objets["monstre"], monstre["position"]["x"], monstre["position"]["y"])
    return None