import pyxel

def update(options_principales:dict) -> dict:
    """ met a jour le menu principal """
    return options_principales


def draw(data_carte) -> None:
    """ Affiche la carte à l'écran en utilisant les données de Tiled et Pyxel """
    layer = data_carte["layers"][0]
    width = layer["width"]
    height = layer["height"]
    tile_width = data_carte["tilewidth"]
    tile_height = data_carte["tileheight"]


    for y in range(height):
        for x in range(width):
            tuile = layer["data"][y * width + x]
            if tuile == 0:
                continue
            tuile -= 1

            u = tuile % 5 * tile_width
            v = tuile // 5 * tile_height

            pyxel.blt(x * tile_width, y * tile_height, 2, u, v, tile_width, tile_height)
    return None