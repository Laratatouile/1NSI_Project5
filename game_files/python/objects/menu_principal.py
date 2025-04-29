import pyxel
import objects.affichage_pyxel as affichage_pyxel

def update(options_principales:dict) -> dict:
    """ met a jour le menu principal """
    return options_principales


def draw(data_carte) -> None:
    """ Affiche la carte à l'écran en utilisant les données de Tiled et Pyxel """
    affichage_pyxel.draw_carte(data_carte)
    return None