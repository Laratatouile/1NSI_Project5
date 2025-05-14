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
import objects.mort as mort
import objects.parametres as parametres
import objects.monstres as monstres




def update():
    """ calcule ce qu'il y a afficher """
    # importation des variables
    global affichage, options_globales, options_map, model, timer, mort_base
    if timer != 0:
        timer -= 1

    # detection de la mort et du compte a rebours pour la mort
    if timer == 0 :
        if options_globales["player"]["mort"] != False and mort_base == False:
            if options_globales["player"]["mort"] == "gagne":
                options_globales["whereami"] = "gagne"
            else:
                options_globales["whereami"] = "mort"
            mort_base = "retour_menu"
            timer = 5 * recup_option.param("fps")
            options_globales["player"] = {
                "x" : 450,
                "y" : 2450,
                "niveau" : 1,
                "puissance_boost" : 1,
                "attaque" : 0,
                "modif_terrain" : 1,
                "vie" : 100,
                "mort" : False
            }
            pyxel.camera(0, 0)

        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and mort_base == "retour_menu" :
            mort_base = False
            options_globales["whereami"] = "menu_principal"
        
    

    # quitter
    if pyxel.btn(recup_option.touche("arret")):
        sauvegarde.save(options_globales, model)


    # affichage de la souris
    options_globales = curseur.update(options_globales, model)

    
    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        options_globales, affichage = demarrage.update(options_globales, affichage)

    # si je suis sur le jeu
    elif options_globales["whereami"] == "jeu":
        options_globales, options_map = personnage.update(options_globales, options_map)
        options_globales = monstres.update(options_globales, model)

    elif options_globales["whereami"] == "parametres":
        options_globales = parametres.update(options_globales)

    return None



   


def draw() -> None:
    """ affiche les graphismes """
    # importation des variables
    global affichage, options_globales, liste_datas_cartes, liste_datas_objets


    # si je suis sur l'ecran de demarrage
    if options_globales["whereami"] == "start":
        # clear
        pyxel.cls(0)
        demarrage.draw(affichage, liste_datas_cartes)

    # si je suis sur l'ecran principal
    elif options_globales["whereami"] == "menu_principal":
        # clear
        pyxel.cls(0)
        menu_principal.draw(liste_datas_cartes["menu_principal"])

    # si je suis sur le jeu
    elif options_globales["whereami"] == "jeu":
        personnage.draw(options_globales, liste_datas_objets, liste_datas_cartes, options_map)
        monstres.draw(options_globales, liste_datas_objets)

    # si je suis mort
    elif options_globales["whereami"] == "mort":
        mort.draw(liste_datas_cartes["mort"])
    
    # si j'ai gagné
    elif options_globales["whereami"] == "gagne":
        mort.draw(liste_datas_cartes["gagne"])

    elif options_globales["whereami"] == "parametres":
        # clear
        pyxel.cls(0)
        parametres.draw(liste_datas_cartes)

    # affichage de la souris
    curseur.draw(options_globales, liste_datas_objets)

    return None






# variables
global options_globales, affichage, model, liste_datas_cartes, options_map, liste_datas_objets, mort_base, timer

timer = 0
mort_base = False
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
    ],
    "param" : {
        "btn" : -1,
        "start" : False
    }
}




# liste des datas pour les cartes
liste_datas_cartes = {
    "demarrage_1" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage1.json")
    ],
    "demarrage_2" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage2.json")
    ],
    "demarrage_3" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage3.json")
    ],
    "demarrage_4" : [
        fct.json_read("./resources/tiled/json/demarrage/demarrage4.json")
    ],
    "menu_principal" : [
        fct.json_read("./resources/tiled/json/menu_principal.json")
    ],
    "mort" : [
        fct.json_read("./resources/tiled/json/mort.json")
    ],
    "gagne" : [
        fct.json_read("./resources/tiled/json/gagne.json")
    ],
    "parametres" : [
        fct.json_read("./resources/tiled/json/parametres.json")
    ],
    "map" : [
        fct.json_read("./resources/tiled/json/map.json")
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
    fps=options_globales["fenetre"]["fps"],
    quit_key=pyxel.KEY_AC_BOOKMARKS
    )


# lancement de l'instance pyxel
pyxel.fullscreen(recup_option.param("fullscreen"))
pyxel.run(update, draw)