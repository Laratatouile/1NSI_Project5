import pyxel
import fonctions.touches_param as recup_touche
import objects.affichage_pyxel as affichage_pyxel

# Dictionnaire pour afficher les noms des touches
def recup_touche_press() -> int:
    """ recupere la touche pressee en cours """
    touches = [
        pyxel.KEY_A, pyxel.KEY_B, pyxel.KEY_C, pyxel.KEY_D,
        pyxel.KEY_E, pyxel.KEY_F, pyxel.KEY_G, pyxel.KEY_H,
        pyxel.KEY_I, pyxel.KEY_J, pyxel.KEY_K, pyxel.KEY_L,
        pyxel.KEY_M, pyxel.KEY_N, pyxel.KEY_O, pyxel.KEY_P,
        pyxel.KEY_Q, pyxel.KEY_R, pyxel.KEY_S, pyxel.KEY_T,
        pyxel.KEY_U, pyxel.KEY_V, pyxel.KEY_W, pyxel.KEY_X,
        pyxel.KEY_Y, pyxel.KEY_Z, pyxel.KEY_SPACE,
        pyxel.KEY_RETURN, pyxel.KEY_BACKSPACE,
        pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_LEFT,
        pyxel.KEY_RIGHT
    ]
    for touche in touches:
        if pyxel.btn(touche):
            return touche
    return None



def update(option_globales:dict) -> dict:
    # si je veux modifier une touche
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and option_globales["whereami"] == "parametres":
        if 50 < pyxel.mouse_x < 400:
            if 50 < pyxel.mouse_y < 150:
                option_globales["param"]["btn"] = 0
            elif 150 < pyxel.mouse_y < 250:
                option_globales["param"]["btn"] = 1
            elif 250 < pyxel.mouse_y < 350:
                option_globales["param"]["btn"] = 2
            elif 350 < pyxel.mouse_y < 450:
                option_globales["param"]["btn"] = 3
        elif 750 < pyxel.mouse_x < 850 and 50 < pyxel.mouse_y < 150:
            option_globales["param"] = -1
            option_globales["whereami"] = "menu_principal"
    # si je change une touche
    elif option_globales["param"]["btn"] != -1 and option_globales["whereami"] == "parametres":
        touche = recup_touche_press()
        if touche:
            touche_modif = option_globales["param"]["btn"]
            if touche_modif == 0:
                recup_touche.change_touche("avancer", touche)
            elif touche_modif == 1:
                recup_touche.change_touche("reculer", touche)
            elif touche_modif == 2:
                recup_touche.change_touche("droite", touche)
            elif touche_modif == 3:
                recup_touche.change_touche("gauche", touche)
            option_globales["param"]["btn"] = -1
    return option_globales



def draw(liste_datas_cartes:dict) -> None:
    """ affiche la carte des parametres """
    affichage_pyxel.draw_carte(liste_datas_cartes["parametres"], surcouche="parametres")
    return None
