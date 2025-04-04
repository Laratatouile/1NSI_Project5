def fichier_ouvrir(nom_sauvegarde:str, clef:int) -> dict:
    """ essaye d'ouvrir le fichier avec la clef definie """
    def decode(texte:str, decalage:int) -> str:
        """ dechiffre le texte avec le decalage """
        def cree_dictionnaire_decalage(decalage:int) -> dict:
            """ crée un dictionnaire avec un decalage de decalage """
            symboles_dans_dictionnaire = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [" ", "{", "}", ":", ",", "[", "]", '"', "'", "_"]
            return {i[1] : symboles_dans_dictionnaire[i[0]+decalage if i[0]+decalage < len(symboles_dans_dictionnaire) else i[0] - len(symboles_dans_dictionnaire) + decalage] for i in enumerate(symboles_dans_dictionnaire)}
        decode = ""
        dictionnaire_decalage = cree_dictionnaire_decalage(-decalage)
        for i in texte:
            try:
                decode += dictionnaire_decalage.get(i)
            except:
                pass
        return decode
    # ouvrir et lire le fichier chiffre
    with open(f"../sauvegardes/{nom_sauvegarde}.zmb", "r") as read_file:
        data_chiff = read_file.read()
    # renvoier le fichier  dechiffre et tranforme en dictionnaire
    data = decode(data_chiff, clef)
    if (data[:9+len(nom_sauvegarde)] == "{'nom': '"+nom_sauvegarde) or (data[:9+len(nom_sauvegarde)] == '{"nom": "'+nom_sauvegarde):
        return eval(data)
    return None
    



def fichier_sauvegarder(nom_sauvegarde:str, clef:int, sauvegarde:dict) -> None:
    """ essaye d'ouvrir le fichier avec la clef definie """
    def code(texte:str, decalage:int) -> str:
        """ chiffre le texte avec le decalage """
        def cree_dictionnaire_decalage(decalage:int) -> dict:
            """ crée un dictionnaire avec un decalage de decalage """
            symboles_dans_dictionnaire = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [" ", "{", "}", ":", ",", "[", "]", '"', "'", "_"]
            return {i[1] : symboles_dans_dictionnaire[i[0]+decalage if i[0]+decalage < len(symboles_dans_dictionnaire) else i[0] - len(symboles_dans_dictionnaire) + decalage] for i in enumerate(symboles_dans_dictionnaire)}
        code = ""
        for i in texte:
            code += cree_dictionnaire_decalage(decalage).get(str(i))
        return code
    # ouvrir et lire le fichier chiffre
    sauvegarde = str(sauvegarde)
    with open(f"../sauvegardes/{nom_sauvegarde}.zmb", "w", encoding="utf-8") as write_file:
        write_file.write(code(sauvegarde, int(clef)))
    return None


