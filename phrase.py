import pandas as pd
import os

def charge(fichier,mode):
    f=open(fichier,"r")
    taille=os.path.getsize(fichier)
    if taille>100000:
        print("Attention taille du fichier supérieure à 100ko: {}".format(taille))
        return -1
    else:
        print("Taille inférieure à 100ko: {}".format(taille))
        chargee=[]
    if mode=="L":
        for li in f:
            chargee.append(str.upper(str.strip(li,"\n")))
    else:
        # Version par caractère à construire
        return -1
    return chargee

def teste(tmot):
    if (str.upper(tmot) in prenoms and tmot!=""):
        return "Prénom",True,tmot
    elif str.upper(tmot) in lieux:
        return "Lieux", True,tmot
    elif str.upper(tmot) in exclusion:
        return "Exclusion", True,tmot
    else:
        return "Rien", False,''
    
class mot:
    def __init__(self,mo,pos):
        self.position=-1
        self.maj=False
        self.contenu=mo
        self.position=pos
        self.majuscule()

    def majuscule(self):
        lettre=self.contenu
        if str.isupper(lettre):
            self.maj=True
    
    def phrase(texte):
        # Recherche des points et fin de ligne
        texte=texte.replace("."," ")
        texte=texte.replace(","," ")
        texte=texte.replace(";"," ")
        texte=texte.replace("!"," ")
        texte=texte.replace(":"," ")
        texte=texte.replace("'"," ")
        # Cherche les mots c'est à dire les blocs après espace de texte
        i=0
        pos_mot=0
        phras=[]
        m=""
        while i<len(texte):
            if str.isalpha(texte[i]):
                m=m+texte[i]
            elif (texte[i]==" " or texte[i]=="\n"):
                pos_mot=pos_mot+1
                phras.append(mot(m,pos_mot))
                m=""
            else:
                while str.isnumeric(texte[i]):
                    i=i+1
            i=i+1
        return phras
    
    def distance(t_phrase,t_mot): # Distance entre un mot et les voisins majuscules
        index=t_mot.position-1
        distance=-1
        tab_phrase=[]
        # Mise en repère de la phrase
        for i in t_phrase:
            if i.maj:
                tab_phrase.append(True)
            else:
                tab_phrase.append(False)
        # Cas du mot en première position
        if index==0:
            if tab_phrase[1]:
                distance = 1
            else:
                distance = 0
        else:
            if tab_phrase[index-1]:
                distance = 1
            if tab_phrase[index+1]:
                distance = distance + 1
        return distance
#Initialisation des listes
prenoms=charge("/home/nnp/Documents/Python/bs/traitement/prenom-main/prenoms.csv","L")
lieux=["MOSCOW", "KIEV"]
exclusion=["PUTIN"]

# Ouverture fichier recherche
f=open("/home/nnp/Documents/Python/bs/nettoyage/moscow-shadows.txt")
match_prenoms=0
for i in f:
    texte_t=mot.phrase(i)
    for i in texte_t:
        res=teste(i.contenu)
        print(i.contenu)
        if res[1]:
            print(res)
            match_prenoms=match_prenoms+1
print(match_prenoms)
