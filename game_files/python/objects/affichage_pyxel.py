import pyxel


def draw_carte(datas_carte:dict) -> None:
    """ Affiche la carte à l'écran en utilisant les données de Tiled et Pyxel """

    data_carte = (datas_carte[0] if len(datas_carte) == 2 else datas_carte)


    for i in range(len(data_carte["layers"])):
        # calcul des differentes variables pour l'affichage
        layer = data_carte["layers"][i]
        width, height = layer["width"], layer["height"]
        tile_width, tile_height = data_carte["tilewidth"], data_carte["tileheight"]

        decalage_x = (data_carte["layers"][i]["offsetx"] if "offsetx" in data_carte["layers"][i].keys() else 0)
        decalage_y = (data_carte["layers"][i]["offsety"] if "offsety" in data_carte["layers"][i].keys() else 0)

        # detection du type de tuile a afficher
        objects = data_carte["layers"][i]["name"]
        img = 2
        if objects == "textes":
            img = 0
        elif objects == "UI":
            pyxel.images[2].load(0, 0, datas_carte[1])


        # affichage des tuiles une par une
        for y in range(height):
            for x in range(width):
                tuile = layer["data"][y * width + x]
                if tuile == 0:
                    continue
                tuile -= 1

                tuile %= 25


                u = tuile % 5 * tile_width
                v = tuile // 5 * tile_height

                pyxel.blt(
                    x * tile_width + decalage_x,
                    y * tile_height + decalage_y,
                    (img if tuile < 25 else img+1),
                    u,
                    (v if tuile < 25 else v-25),
                    tile_width,
                    tile_height)
    return None



def draw_object(data_carte:dict, id_tuile:int, x:int, y:int) -> None:
    pyxel.images[2].load(0, 0, data_carte)
    pyxel.blt(x, y, id_tuile % 5, id_tuile // 5, 2, 50, 50)
    return None