import pyxel
import objects.affichage_pyxel as affichage_pyxel
import fonctions.touches_param as recup_option



def update(options_globales:dict) -> dict:
    # recuperation des variables
    vitesse_personnage = recup_option.param("vitesse_personnage") * options_globales["player"]["puissance_boost"]

    # update des touches
    if options_globales["player"]["attaque"] == 0:
        if pyxel.btn(pyxel.KEY_Z):
            options_globales["player"]["y"] = max(options_globales["player"]["y"] - vitesse_personnage, 0)
        if pyxel.btn(pyxel.KEY_S):
            options_globales["player"]["y"] = min(options_globales["player"]["y"] + vitesse_personnage, 2450)
        if pyxel.btn(pyxel.KEY_Q):
            options_globales["player"]["x"] = max(options_globales["player"]["x"] - vitesse_personnage, 0)
        if pyxel.btn(pyxel.KEY_D):
            options_globales["player"]["x"] = min(options_globales["player"]["x"] + vitesse_personnage, 850)

    else:
        options_globales["player"]["attaque"] -= 1


    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        options_globales["player"]["attaque"] = recup_option.param("fps")


    if 250 < options_globales["player"]["y"] < 2250:
        pyxel.camera(0, options_globales["player"]["y"] - 250)

    return options_globales





def draw(options_globales:dict, liste_datas_objets:dict, liste_datas_cartes:dict) -> None:
    affichage_pyxel.draw_carte(liste_datas_cartes["map"])
    affichage_pyxel.draw_object(
        liste_datas_objets["joueur"],
        options_globales["player"]["x"],
        options_globales["player"]["y"]
    )
    return None