from datetime import datetime
from json import load, dump
import os

### ___ affichage dans la comsole simplifié ___ ###
def logs(Loader, Gravity, Text):
    """
        Loader, gravite, texte
    """
    decalage_max_texte, LenSpace = 20, ""
    if len(Loader) + len(Gravity) < decalage_max_texte:
        Space = decalage_max_texte - (len(Loader) + len(Gravity))
        for i in range(Space):
            LenSpace += " "
    print("[",str(datetime.now())[11:-7],"] [",Loader,"/",Gravity.upper(),"]",LenSpace," :",Text)






### ___ getion des fichiers json ___ ###
def json_read(path:str):
    """
        chargement du fichier a ouvrir et retour sous forme de dictionnaire
        Si data renvoie data
        Sinon renvoie None
    """
    while os.listdir()[0] != ".git":
        os.chdir("../")
    os.chdir("game_files")
    try:
        data = load(open(path, "r"))
    except:
        print(os.listdir())
        print(path)
        logs("JsonReader", "INFO", "Le fichier n'a pas été lu")
        return None
    return data



def json_save(data:dict, file:str) -> None:
    """
        sauvegarde du dictionnaire dans le fichier donne
        Si le fichier n'est pas sauvegarde
    """
    try:
        dump(data, open(file, "w"))
        logs("JsonReader", "INFO", "Le fichier a été enregistré")
    except Exception as e:
        logs("JsonReader", "FATAL", "Le fichier n'a pas pu être enregistré : "+str(e), 2)

    return None
