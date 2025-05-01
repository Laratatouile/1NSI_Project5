import pyxel
import objects.affichage_pyxel as affichage_pyxel


def update(options_globales:dict) -> dict:
    options_globales["curseur"]["x"] = pyxel.mouse_x
    options_globales["curseur"]["y"] = pyxel.mouse_y
    return options_globales



def draw(options_globales:dict, liste_datas_objets:dict) -> None:
    if options_globales["whereami"] == "menu_principal" :
        affichage_pyxel.draw_object(
            liste_datas_objets["curseur"],
            options_globales["curseur"]["x"],
            options_globales["curseur"]["y"])
    return None