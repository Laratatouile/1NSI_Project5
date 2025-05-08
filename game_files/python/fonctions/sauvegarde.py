import fonctions.chiffrement as chiffrement
import pyxel
import torch


def save(options_globales:dict, model:dict) -> None:
    # sauvegarde des options globales
    chiffrement.fichier_sauvegarder("./resources/sauvegardes/save.json", 8, options_globales)
    # sauvegarde des infos pour l'ia
    infos = {
        "taille_entree": model["entree"].in_features,
        "taille_cachee": model["entree"].out_features,
        "taille_sortie": model["sortie"].out_features,
        "learning_rate": model["optimiser"].param_groups[0]["lr"]
    }
    chiffrement.fichier_sauvegarder("./resources/torch/save1.json", 8, infos)
    # sauvegarde des poids du reseau ia
    torch.save({
        "entree": model["entree"].state_dict(),
        "sortie": model["sortie"].state_dict(),
        "optimiseur": model["optimiser"].state_dict()
    }, "./resources/torch/save1.pt")
    # quitter
    pyxel.quit()
