import fonctions.fonctions as fct

def param(parametre:str) -> all:
    """recupere le parametre demande"""
    return fct.json_read("./resources/options_jeu/parametres.json")[parametre]

def touche(action:str) -> str:
    """recupere la touche de l'action demandee"""
    return fct.json_read("./resources/options_jeu/touches.json")[action]

def change_touche(action:str, touche:int) -> None:
    """ change une touche """
    options = fct.json_read("./resources/options_jeu/touches.json")
    options[action] = touche
    fct.json_save(options, "./resources/options_jeu/touches.json")
    return None