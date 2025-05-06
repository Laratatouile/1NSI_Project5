import fonctions.fonctions as fct

def param(parametre:str) -> all:
    """recupere le parametre demande"""
    return fct.json_read("./resources/options_jeu/parametres.json")[parametre]

def touche(action:str) -> str:
    """recupere la touche de l'action demandee"""
    return fct.json_read("./resources/options_jeu/touches.json")[action]
