import fonctions.fonctions as fct

def param(parametre:str) -> all:
    data = fct.json_read("../resources/options_jeu/parametres.json")
    print(data)
    if data == None:
        data = fct.json_read("./resources/options_jeu/parametres.json")
    return data[parametre]

def touche(action:str) -> str:
    data = fct.json_read("../resources/options_jeu/touches.json")
    if data == None:
        data = fct.json_read("./resources/options_jeu/touches.json")
    return data[action]
