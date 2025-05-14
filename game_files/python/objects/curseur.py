import pyxel
import objects.affichage_pyxel as affichage_pyxel
import fonctions.sauvegarde as sauvegarde
from pygame import mixer


def update(options_globales:dict, model) -> dict:
    """ met a jour le curseur """
    options_globales["curseur"]["x"] = pyxel.mouse_x
    options_globales["curseur"]["y"] = pyxel.mouse_y

    if options_globales["whereami"] == "menu_principal":
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 50 < pyxel.mouse_x < 350:
                if 50 < pyxel.mouse_y < 150:
                    options_globales["whereami"] = "jeu"
                    pyxel.camera(0, 2000)
                elif 200 < pyxel.mouse_y < 300:
                    options_globales["param"]["start"] = False
                    options_globales["whereami"] = "parametres"
                elif 350 < pyxel.mouse_y < 450:
                    sauvegarde.save(options_globales, model)
    return options_globales



def draw(options_globales:dict, liste_datas_objets:dict) -> None:
    if options_globales["whereami"] == "menu_principal" or options_globales["whereami"] == "parametres":
        affichage_pyxel.draw_object(
            liste_datas_objets["curseur"],
            options_globales["curseur"]["x"],
            options_globales["curseur"]["y"])
    return None