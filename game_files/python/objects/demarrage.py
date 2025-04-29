import pyxel
import fonctions.touches_param as recup_option
import objects.affichage_pyxel as affichage_pyxel


def update(options_globales:dict, affichage:int) -> dict:
    """ met a jour l'ecran de demarrage """
    if pyxel.frame_count == 3 * options_globales["fenetre"]["fps"]:
        affichage = 1
    elif pyxel.frame_count == 5 * options_globales["fenetre"]["fps"]:
        affichage = 2
    elif pyxel.frame_count == 7 * options_globales["fenetre"]["fps"]:
        affichage = 3
    elif pyxel.frame_count == 9 * options_globales["fenetre"]["fps"]:
        options_globales["whereami"] = "menu_principal"
    if (recup_option.touche("clic_principal") == "gauche" and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)) or (recup_option.touche("clic_principal") == "droit" and pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT)):
        options_globales["whereami"] = "menu_principal"

    return options_globales, affichage


def draw(affichages:int, liste_datas_cartes:dict) -> None:
    """ affiche l'ecran de demarrage """
    if affichages == 0:
        affichage_pyxel.draw_carte(liste_datas_cartes["demarrage_1"])
    if affichages == 1:
        affichage_pyxel.draw_carte(liste_datas_cartes["demarrage_2"])
    if affichages == 2:
        affichage_pyxel.draw_carte(liste_datas_cartes["demarrage_3"])
    if affichages == 3:
        affichage_pyxel.draw_carte(liste_datas_cartes["demarrage_4"])
    return None