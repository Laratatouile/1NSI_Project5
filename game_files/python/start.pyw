import pyxel


# importation des fonctions
import fonctions.touches_param as recup_option
import fonctions.fonctions as fct
import fonctions.sauvegarde  as sauvegarde


# importation des objects
import objects.demarrage as demarrage
import objects.menu_principal as menu_principal
import objects.curseur as curseur
import objects.personnage as personnage
import objects.monstres as monstres




def update():
    """ calcule ce qu'il y a afficher """
    # importation des variables
    global affichage, options_globales, options_map, model, timer
    timer = 0
    timer = max(timer-1, 0)

    # detection de la mort et du compte a rebours
    if timer == 0 and options_globales["player"]["mort"] != False:
        timer = 5 * recup_option.param("fps")

    elif timer == 0 and options_globales["player"]["mort"] != False:
        sauvegarde.save(options_globales, model)
    

    # quitter
    if pyxel.btn(recup_option.touche("arret")):
        sauvegarde.save(options_globales, model)


    # affichage de la souris
    options_globales = curseur.update(options_globales)

    # si je suis sur le menu principal
    if options_globales["whereami"] == "menu_principal":
        options_globales = menu_principal.update(options_globales)
    
    # si je suis sur l'ecran de demarrage
    elif options_globales["whereami"] == "start":
        options_globales, affichage = demarrage.update(options_globales, affichage)

    # si je suis sur le jeu
    elif options_globales["whereami"] == "jeu":
        options_globales, options_map = personnage.update(options_globales, options_map)
        options_globales = monstres.update(options_globales, model)

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

    # si je suis sur le jeu
    elif options_globales["whereami"] == "jeu":
        personnage.draw(options_globales, liste_datas_objets, liste_datas_cartes, options_map)
        monstres.draw(options_globales, liste_datas_objets)

    # affichage de la souris
    curseur.draw(options_globales, liste_datas_objets)

    return None






# variables
global options_globales, affichage, model, liste_datas_cartes, options_map, liste_datas_objets

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
    "player" : {
        "x" : 450,
        "y" : 2450,
        "niveau" : 1,
        "puissance_boost" : 1,
        "attaque" : 0,
        "modif_terrain" : 1,
        "vie" : 100,
        "mort" : False
    },
    "monstres": [
        {
            "etat": [1, 2, 1, 2, 30, 10],  # [x_perso, y_perso, dir_lave, dist_lave, x_joueur, y_joueur]
            "position": {"x": 800, "y": 2300},
            "recompense": 0
        }
    ]
}




# liste des datas pour les cartes
liste_datas_cartes = {
    "demarrage_1" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage1.json"),
        [
            "./resources/tiled/jeux_tuiles/lettres1.png",
            "./resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "demarrage_2" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage2.json"),
        [
            "./resources/tiled/jeux_tuiles/lettres1.png",
            "./resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "demarrage_3" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage3.json"),
        [
            "./resources/tiled/jeux_tuiles/lettres1.png",
            "./resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "demarrage_4" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage4.json"),
        [
            "./resources/tiled/jeux_tuiles/lettres1.png",
            "./resources/tiled/jeux_tuiles/lettres2.png"
        ]
    ],
    "menu_principal" : [
        fct.json_read("./resources/tiled/json/menu_principal.json"),
        [
            "./resources/tiled/jeux_tuiles/decor.png",
        ]
    ],
    "map" : [
        fct.json_read("./resources/tiled/json/map.json"),
        [
            "./resources/tiled/jeux_tuiles/map.png",
        ]
    ]
}



# liste des data pour les objects
liste_datas_objets = {
    "curseur" : [
        "./resources/tiled/jeux_tuiles/objects.png",
        0
    ],
    "joueur" : [
        "./resources/tiled/jeux_tuiles/patates.png",
        0
    ],
    "joueur_brule" : [
        "./resources/tiled/jeux_tuiles/patates.png",
        1
    ],
    "joueur_zombie" : [
        "./resources/tiled/jeux_tuiles/patates.png",
        3
    ],
    "monstre" : [
        "./resources/tiled/jeux_tuiles/patates.png",
        5, 6
    ]
}

options_map = {
    "listes_pommes" : {
        "liste_de_base" : [
            [100, 150],
            [750, 850],
            [100, 1350],
            [800, 1950]
        ],
        "pommes_vierges": [
            [100, 150],
            [750, 850],
            [100, 1350],
            [800, 1950]
        ]
    }
}

model = monstres.initialiser()


# parametres de la fenetre
pyxel.init(
    recup_option.param("taille_fenetre_x"),
    recup_option.param("taille_fenetre_y"),
    "La pomme de terre c'est super",
    fps=240,#options_globales["fenetre"]["fps"],
    quit_key=pyxel.KEY_AC_BOOKMARKS
    )


# lancement de l'instance pyxel
pyxel.fullscreen(recup_option.param("fullscreen"))
pyxel.run(update, draw)