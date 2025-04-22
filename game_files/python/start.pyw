import pyxel
import fonctions.touches_param as recup_option
import fonctions.chiffrement as chiffrement
import fonctions.fonctions as fct


# importation des objects
import objects.demarrage as demarrage
import objects.menu_principal as menu_principal




def update():
    """ calcule ce qu'il y a afficher """
    # importation des variables
    global affichage, options_globales


    # tmp
    if pyxel.btn(pyxel.KEY_T):
        pyxel.quit()




    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        options_globales, affichage = demarrage.update(options_globales, affichage)

    elif options_globales["whereami"] == "menu_principal":
        options_globales = menu_principal.update(options_globales)

    return None



   


def draw() -> None:
    """ affiche les graphismes """
    # importation des variables
    global affichage, options_globales, liste_datas_cartes

    # clear
    pyxel.cls(0)

    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        demarrage.draw(affichage, options_globales)

    # si je suis sur l'ecran principal
    elif options_globales["whereami"] == "menu_principal":
        menu_principal.draw(liste_datas_cartes["menu_principal"])

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



# initialisation des images
pyxel.images[2].load(0, 0, "../resources/tiled/jeux_tuiles/UI.png")

global liste_datas_cartes
liste_datas_cartes = {
    "menu_principal" : fct.json_read("../resources/tiled/json/menu_principal.json"),
    "map" : fct.json_read("../resources/tiled/json/map.json")
}





pyxel.fullscreen(recup_option.param("fullscreen"))
pyxel.run(update, draw)