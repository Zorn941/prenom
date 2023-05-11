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
            chargee.append(str.strip(li,"\n"))
    else:
        # Version par caractère à construire
        return -1
    return chargee

list_pre=charge("C:/Users/nicolas.philippotin/Documents/python/charge/prenoms.csv","L")
if "Petrov" in list_pre:
    print("Trouvé")