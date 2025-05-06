import pyxel


def draw_carte(data_carte:dict) -> None:
    """ Affiche la carte à l'écran en utilisant les données de Tiled et Pyxel """
    for i in range(len(data_carte[0]["layers"])):
        # calcul des differentes variables pour l'affichage
        layer = data_carte[0]["layers"][i]
        width, height = layer["width"], layer["height"]
        tile_width, tile_height = data_carte[0]["tilewidth"], data_carte[0]["tileheight"]

        decalage_x = (data_carte[0]["layers"][i]["offsetx"] if "offsetx" in data_carte[0]["layers"][i].keys() else 0)
        decalage_y = (data_carte[0]["layers"][i]["offsety"] if "offsety" in data_carte[0]["layers"][i].keys() else 0)


        ### ___ detection du type de tuile a afficher ___ ###
        objects = data_carte[0]["layers"][i]["name"]
        
        # si c un texte
        if objects == "textes":
            pyxel.images[0].load(0, 0, "../resources/tiled/jeux_tuiles/lettres1.png")
            pyxel.images[1].load(0, 0, "../resources/tiled/jeux_tuiles/lettres2.png")
        # si c'est une partie de L'UI
        elif objects == "UI":
            pyxel.images[0].load(0, 0, "../resources/tiled/jeux_tuiles/UI.png")
        elif objects == "decor":
            pyxel.images[0].load(0, 0, "../resources/tiled/jeux_tuiles/decor.png")


        # affichage des tuiles une par une
        for y in range(height):
            for x in range(width):
                tuile = layer["data"][y * width + x]
                if tuile == 0:
                    continue
                tuile -= 1
                tuile -= i*25

                u = tuile % 5 * tile_width
                v = tuile // 5 * tile_height

                pyxel.blt(
                    x * tile_width + decalage_x,
                    y * tile_height + decalage_y,
                    (0 if tuile < 25 else 1),
                    u,
                    (v if tuile < 25 else v-250),
                    tile_width,
                    tile_height,
                    colkey=0
                    )
    return None



def draw_object(data_objet:dict, x:int, y:int) -> None:
    pyxel.images[2].load(0, 0, data_objet[0])
    pyxel.blt(x, y, 2, data_objet[1] % 5, data_objet[1] // 5, 50, 50, colkey=0)
    return None

