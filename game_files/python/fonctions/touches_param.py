import fonctions.fonctions as fct
import os

def param(parametre:str) -> all:
    "recupere le parametre demande"
    if os.listdir()[-1] == "site_files":
        return fct.json_read("./game_files/resources/options_jeu/parametres.json")[parametre]
    return fct.json_read("../resources/options_jeu/parametres.json")[parametre]

def touche(action:str) -> str:
    "recupere la touche de l'action demandee"
    if os.listdir()[-1] == "site_files":
        return fct.json_read("./game_files/resources/options_jeu/touches.json")[action]
    return fct.json_read("../resources/options_jeu/touches.json")[action]
