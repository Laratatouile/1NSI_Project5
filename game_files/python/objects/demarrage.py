import pyxel
import fonctions.touches_param as recup_option


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


def draw(affichage:int, options_globales:dict) -> None:
    """ affiche l'ecran de demarrage """
    if affichage == 0:
        pyxel.text(options_globales["fenetre"]["x"] // 2 - 60, options_globales["fenetre"]["y"] // 2 - 10, "La pomme de terre c'est super", 14)
    if affichage == 1:
        pyxel.text(options_globales["fenetre"]["x"] // 2 - 20, options_globales["fenetre"]["y"] // 2 - 10, "Realise par", 12)
        pyxel.text(options_globales["fenetre"]["x"] // 2 - 30, options_globales["fenetre"]["y"] // 2, "Maxime GEOFFROY", 12)
    if affichage == 2:
        pyxel.text(options_globales["fenetre"]["x"] // 2 - 32, options_globales["fenetre"]["y"] // 2 - 8, "Pour le project 5", 5)
        pyxel.text(options_globales["fenetre"]["x"] // 2 - 27, options_globales["fenetre"]["y"] // 2 + 2, "de NSI de 1ere", 5)
    if affichage == 3:
        pyxel.text(options_globales["fenetre"]["x"] // 2 - 15, options_globales["fenetre"]["y"] // 2 - 5, "Bienvenue", 8)
    return None


