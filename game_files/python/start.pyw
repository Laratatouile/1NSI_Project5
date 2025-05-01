import pyxel


# importation des fonctions
import fonctions.touches_param as recup_option
import fonctions.chiffrement as chiffrement
import fonctions.fonctions as fct


# importation des objects
import objects.demarrage as demarrage
import objects.menu_principal as menu_principal
import objects.curseur as curseur




def update():
    """ calcule ce qu'il y a afficher """
    # importation des variables
    global affichage, options_globales


    # tmp
    if pyxel.btn(pyxel.KEY_T):
        pyxel.quit()


    # affichage de la souris
    options_globales = curseur.update(options_globales)


    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        options_globales, affichage = demarrage.update(options_globales, affichage)

    elif options_globales["whereami"] == "menu_principal":
        options_globales = menu_principal.update(options_globales)

    return None



   


def draw() -> None:
    """ affiche les graphismes """
    # importation des variables
    global affichage, options_globales, liste_datas_cartes, liste_datas_objets

    # clear
    pyxel.cls(0)

    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        demarrage.draw(affichage, liste_datas_cartes)

    # si je suis sur l'ecran principal
    elif options_globales["whereami"] == "menu_principal":
        menu_principal.draw(liste_datas_cartes["menu_principal"])

    # affichage de la souris
    curseur.draw(options_globales, liste_datas_objets)

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
    "curseur" : {
        "x" : 0,
        "y" : 0
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



### ___ initialisation des images ___ ###
# lettres et chiffres
pyxel.images[0].load(0, 0, "../resources/tiled/jeux_tuiles/lettres1.png")
pyxel.images[1].load(0, 0, "../resources/tiled/jeux_tuiles/lettres2.png")



# liste des datas pour les cartes
global liste_datas_cartes
liste_datas_cartes = {
    "demarrage_1" : [
        fct.json_read("../resources/tiled/json/demarrage/demarrage1.json"),
        [
            "../resources/tiled/jeux_tuiles/lettres1.png",
            "../resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "demarrage_2" : [
        fct.json_read("../resources/tiled/json/demarrage/demarrage2.json"),
        [
            "../resources/tiled/jeux_tuiles/lettres1.png",
            "../resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "demarrage_3" : [
        fct.json_read("../resources/tiled/json/demarrage/demarrage3.json"),
        [
            "../resources/tiled/jeux_tuiles/lettres1.png",
            "../resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "demarrage_4" : [
        fct.json_read("../resources/tiled/json/demarrage/demarrage4.json"),
        [
            "../resources/tiled/jeux_tuiles/lettres1.png",
            "../resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "menu_principal" : [
        fct.json_read("../resources/tiled/json/menu_principal.json"),
        [
            "../resources/tiled/jeux_tuiles/decor.png",
        ]
    ],
    "map" : [
        fct.json_read("../resources/tiled/json/map.json"),
        [
            "../resources/tiled/jeux_tuiles/map.png",
        ]
    ]
}



# liste des data pour les objects
global liste_datas_objets
liste_datas_objets = {
    "curseur" : [
        "../resources/tiled/jeux_tuiles/objects.png",
        0
    ]
}



# lancement de l'instance pyxel
pyxel.fullscreen(recup_option.param("fullscreen"))
pyxel.run(update, draw)