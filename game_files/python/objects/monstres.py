import torch
import torch.nn.functional as F
import torch.optim as optim
import os
import json


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
        taille_sortie = 2
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


def update(options_globales:dict, model:dict) -> dict:
    """ Gère tous les monstres du tour (liste d'objets) """
    if "monstres" not in options_globales:
        return options_globales

    for i, monstre in enumerate(options_globales["monstres"]):
        # Récupération de l'état actuel
        etat_actuel = torch.tensor(monstre["etat"], dtype=torch.float32)

        # Apprentissage si récompense disponible
        if i in etat_prec and i in action_prec and "recompense" in monstre:
            with torch.no_grad():
                valeur_futur = torch.max(model_forward(etat_actuel, model))
                cible = monstre["recompense"] + 0.99 * valeur_futur

            pred = model_forward(etat_prec[i], model)[action_prec[i]]
            perte = model["perte"](pred, cible)

            model["optimiser"].zero_grad()
            perte.backward()
            model["optimiser"].step()

        # Choisir une action
        with torch.no_grad():
            q_vals = model_forward(etat_actuel, model)
            action = torch.argmax(q_vals).item()

        # Mémoriser état/action pour la prochaine récompense
        etat_prec[i] = etat_actuel
        action_prec[i] = action

        # Stocker l'action dans le monstre
        monstre["action"] = action
        print(action)

        # S'assurer qu'il y a une position (évite crash si oublié)
        if "position" not in monstre:
            monstre["position"] = {"x": 0, "y": 0}

    return options_globales