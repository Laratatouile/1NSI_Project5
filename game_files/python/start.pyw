import pyxel
import fonctions.touches_param as recup_option
import fonctions.chiffrement as chiffrement


# importation des objects
import objects.demarrage as demarrage
import objects.menu_principal as menu_principal



def update():
    """ calcule ce qu'il y a afficher """
    # importation des variables
    global affichage, options_globales

    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        options_globales, affichage = demarrage.update(options_globales, affichage)

    elif options_globales["whereami"] == "menu_principal":
        options_globales = menu_principal.update(options_globales)

    return None



   


def draw() -> None:
    """ affiche les graphismes """
    # importation des variables
    global affichage, options_globales

    # clear
    pyxel.cls(0)

    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        demarrage.draw(affichage, options_globales)

    return None




# variables
global options_globales, affichage, options_jeu

affichage = 0

options_globales = {
    "whereami" : "start",
    "fenetre" : {
        "x" : recup_option.param("taille_fenetre_x"),
        "y" : recup_option.param("taille_fenetre_y"),
        "fps" : recup_option.param("fps")
    },
}



# parametres de la fenetre
pyxel.init(
    options_globales["fenetre"]["x"],
    options_globales["fenetre"]["y"],
    "La pomme de terre c'est super",
    fps=options_globales["fenetre"]["fps"],
    quit_key=pyxel.KEY_AC_BOOKMARKS
    )

pyxel.fullscreen(recup_option.param("fullscreen"))
pyxel.run(update, draw)