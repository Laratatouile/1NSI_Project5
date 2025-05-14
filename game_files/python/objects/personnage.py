import pyxel
import objects.affichage_pyxel as affichage_pyxel
import fonctions.touches_param as recup_option
import math



def update(options_globales:dict, options_map:dict) -> dict:
    """ s'occupe de la getion du joueur et des affichages du jeu """
    # recuperation des variables
    vitesse_personnage = recup_option.param("vitesse_personnage") * options_globales["player"]["puissance_boost"]

    options_globales["player"], options_map = recup_terrain(options_globales["player"], options_map)

    # update des touches
    if options_globales["player"]["attaque"] == 0:
        if pyxel.btn(recup_option.touche("avancer")):
            options_globales["player"]["y"] = max(options_globales["player"]["y"] - vitesse_personnage * options_globales["player"]["modif_terrain"], 0)
        if pyxel.btn(recup_option.touche("reculer")):
            options_globales["player"]["y"] = min(options_globales["player"]["y"] + vitesse_personnage * options_globales["player"]["modif_terrain"], 2450)
        if pyxel.btn(recup_option.touche("gauche")):
            options_globales["player"]["x"] = max(options_globales["player"]["x"] - vitesse_personnage * options_globales["player"]["modif_terrain"], 0)
        if pyxel.btn(recup_option.touche("droite")):
            options_globales["player"]["x"] = min(options_globales["player"]["x"] + vitesse_personnage * options_globales["player"]["modif_terrain"], 850)
    else:
        options_globales["player"]["attaque"] -= 1

        

    # attaque
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        pass
        options_globales["player"]["attaque"] = recup_option.param("fps")

    # camera
    if 250 < options_globales["player"]["y"] < 2250:
        pyxel.camera(0, options_globales["player"]["y"] - 250)

    

    return options_globales, options_map





def draw(options_globales:dict, liste_datas_objets:dict, liste_datas_cartes:dict, options_map:dict) -> None:
    affichage_pyxel.draw_carte(liste_datas_cartes["map"], options_map)
    # si le joueur est en vie
    if options_globales["player"]["vie"] != 0:
        affichage_pyxel.draw_object(
            liste_datas_objets["joueur"],
            options_globales["player"]["x"],
            options_globales["player"]["y"]
        )
    # si il est mort brule
    elif options_globales["player"]["mort"] == "brule":
        affichage_pyxel.draw_object(
            liste_datas_objets["joueur_brule"],
            options_globales["player"]["x"],
            options_globales["player"]["y"]
        )
    # si il est mort tue par l'ia (t trop con c pas possible l'ia est nulle a chier)
    elif options_globales["player"]["mort"] == "zombie":
        affichage_pyxel.draw_object(
            liste_datas_objets["joueur_zombie"],
            options_globales["player"]["x"],
            options_globales["player"]["y"]
        )
    return None



def recup_terrain(player:dict, options_map:dict) -> tuple:
    """ recupere ou se trouve le joueur """
    case_eau = [[200, 200], [550, 600], [350, 650], [150, 850], [800, 1100], [100, 1150], [350, 1200], [150, 1450], [300, 1450], [750, 1450], [200, 1700], [750, 1800], [50, 1850], [550, 1950], [200, 2000], [100, 2100], [350, 2150], [300, 2300], [100, 2350], [300, 2400], [650, 2400]]
    case_lave = [[600, 150], [550, 200], [300, 300], [750, 300], [100, 400], [650, 450], [500, 500], [350, 550], [150, 700], [800, 700], [600, 850], [200, 900], [400, 950], [200, 1200], [500, 1250], [700, 1250], [650, 1500], [250, 1550], [50, 1600], [700, 1700], [500, 1750], [150, 1900], [400, 1950], [500, 2150], [750, 2150], [50, 2200], [250, 2400], [750, 2400]]
    case_pomme = options_map["listes_pommes"]["pommes_vierges"]

    # avec l'eau
    for case in case_eau:
        if case[0] - 30 < player["x"] < case[0] + 30 and case[1] - 30 < player["y"] < case[1] + 30:
            player["modif_terrain"] = 0.5
            return player, options_map
    # avec la lave
    for case in case_lave:
        if case[0] - 30 < player["x"] < case[0] + 30 and case[1] - 30 < player["y"] < case[1] + 30:
                player["vie"] = 0
                player["mort"] = "brule"
                player["modif_terrain"] = 0.5
                return player, options_map
    # avec les pommes
    for i in range(len(case_pomme)):
        if case_pomme[i][0] - 30 < player["x"] < case_pomme[i][0] + 30:
            if case_pomme[i][1] - 30 < player["y"] < case_pomme[i][1] + 30:
                player["vie"] += 50
                player["modif_terrain"] = 1
                options_map["listes_pommes"]["pommes_vierges"].pop(i)
                return player, options_map
    if math.hypot(player["x"] - 750, player["y"] - 200) < 50:
        player["mort"] = "gagne"
    player["modif_terrain"] = 1
    return player, options_map