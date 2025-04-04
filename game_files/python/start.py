import pyxel
import fonctions.touches_param as recup_option
# import selection_partie
import fonctions.touches_param as recup_param



def update():
    """ calcule ce qu'il y a afficher """
    if pyxel.frame_count == 3 * fps:
        affichage = 1
    elif pyxel.frame_count == 5 * fps:
        affichage = 2
    elif pyxel.frame_count == 7 * fps:
        affichage = 3
    elif pyxel.frame_count == 9 * fps:
        pass
        # selection_partie.App()
    if pyxel.btnp(recup_param.touche("clic_principal")):
        pass
        # selection_partie.App()


def draw():
    """ affiche les graphismes """
    pyxel.cls(0)
    if affichage == 0:
        pyxel.text(taille_fenetre_x // 2 - 30, taille_fenetre_y // 2 - 10, "Zombax the Game", 14)
    if affichage == 1:
        pyxel.text(taille_fenetre_x // 2 - 20, taille_fenetre_y // 2 - 10, "Realise par", 12)
        pyxel.text(taille_fenetre_x // 2 - 30, taille_fenetre_y // 2, "Maxime GEOFFROY", 12)
    if affichage == 2:
        pyxel.text(taille_fenetre_x // 2 - 32, taille_fenetre_y // 2 - 8, "Pour le project 5", 5)
        pyxel.text(taille_fenetre_x // 2 - 27, taille_fenetre_y // 2 + 2, "de NSI de 1ere", 5)
    if affichage == 3:
        pyxel.text(taille_fenetre_x // 2 - 15, taille_fenetre_y // 2 - 5, "Bienvenue", 8)




# variables
affichage = 0
taille_fenetre_x = recup_option.param("taille_fenetre_x")
taille_fenetre_y = recup_option.param("taille_fenetre_y")
fps = recup_option.param("fps")


# parametres de la fenetre
pyxel.init(taille_fenetre_x, taille_fenetre_y, "Zombax the game", fps=fps, quit_key=pyxel.KEY_AC_BOOKMARKS)
pyxel.load("../PYXEL_RESOURCE_FILE.pyxres")
pyxel.fullscreen(recup_option.param("fullscreen"))
pyxel.run(update, draw)