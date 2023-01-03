from trieur import clean
def compte_ligne(nom_fichier):
    '''Compte les lignes et les mots d'un fichier'''
    with open(nom_fichier, "r") as fd :
        content = fd.read()
        lignes = content.rstrip('\n').split('\n')
        result = []
        mot = []
        nombredeligne = len(lignes)
        for i in range(nombredeligne):
            
            mot += lignes[i].split(" ")
        
        result.append(nombredeligne)
        result.append(len(mot))
        return result

def compte_dans_fichiers(liste_fichiers):
    '''Compte les lignes et les mots dans une liste de fichier'''
    resultat = []
    for i in liste_fichiers :
        resultat.append(compte_ligne(i))
    return resultat

def mots_fichier(nom_fichier): 
    '''renvoie les mots d'un fichier et leurs nombre d'occurence dans une liste sous le format [mot, occurence] (aurait etait beacoup plus simple avec un dico ...)'''
    with open(nom_fichier, "r") as fd :
        content = fd.read()
        lignes = content.rstrip('\n').split('\n')
        mot = []
        resultat = []
        resultat2 = []
        sansdoub = []
        lignes = clean(lignes)
        # separe les lignes en mots
        for i in range(len(lignes)) :
            mot += lignes[i].split(" ")
        #Passe tous les mots en majuscule
        for i in range(len(mot)):
            mot[i] = mot[i].upper()
            resultat.append([])
        #On ajoute tous les mots en majuscule dans une autre liste
        for i in range(len(resultat)):
            resultat[i].append(mot[i])
        #On ajoute dans une autre liste le nombre d'occurence et le mot
        for k in resultat :
             resultat2.append([k, resultat.count(k)])
        #On enleve les doublons
        for element in resultat2 :
            if element not in sansdoub :
                sansdoub.append(element)
        # ON enleve les ' ' 
        for element in sansdoub :
            if element[0][0] == '':
                sansdoub.pop(sansdoub.index(element))
            
                 
       
        return sansdoub

def classement(liste):
    '''classe les 15 premiers mots qui apparaissent le plus'''
    indexoccu = []
    result = []
    for element in liste :
        indexoccu.append((element[0][0],element[1]))
        
    indexoccu.sort(key=clef, reverse=True)
    
    for i in range(0,15):
        result.append(indexoccu[i])
    return result 
        


def clef(elem):
    return elem[1]

       

# --------------------------------------------------
# Programme principal
# --------------------------------------------------
def main():
   # print(compte_ligne("/amuhome/k22005807/src/Prog/SAE105/Donnees/Donnees brute/fichiers/fichier_0.txt"))
   # liste = []
   # for i in range(0,50):
      
   #     liste.append("/amuhome/k22005807/src/Prog/SAE105/Donnees/Donnees brute/fichiers/fichier_" + str(i) +".txt")   
   # print(compte_dans_fichiers(liste))
   #print(mots_fichier("/amuhome/k22005807/src/Prog/SAE105/Donnees/Donnees brute/fichiers/fichier_0.txt"))
   #print(classement(mots_fichier("/amuhome/k22005807/src/Prog/SAE105/Donnees/Donnees brute/fichiers/fichier_0.txt")))
         
if __name__ == "__main__":
    main()