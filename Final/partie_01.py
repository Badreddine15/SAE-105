#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import csv 



import string
def clean(carac):
    cleaned = []
    interdit = []
    passable = ["é","à","'","_","è", '"']
    for k in carac:
        for lettre in k :       
            if lettre not in string.digits and lettre not in string.ascii_lowercase and lettre not in string.ascii_uppercase and lettre not in passable and lettre not in interdit:
                interdit.append(lettre)
        for i in interdit :
            if i in k :
                k = k.replace(i," ")
        if k not in cleaned:
            cleaned.append(k)
    return cleaned



def compte_ligne_mot(nom_fichier):
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
        resultat.append(compte_ligne_mot(i))
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
        sansdoub2 = []
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
                sansdoub.append([element[0][0],element[1]])
        for element in sansdoub : 
            if element not in sansdoub2 :
                sansdoub2.append(element)
        # ON enleve les ' ' 
        for element in sansdoub2 :
            if element[0] == '':
                sansdoub2.pop(sansdoub2.index(element))
           
            
                 
       
        return sansdoub2
    



def mots_dans_fichiers(liste_fichiers):
    resultat = []
    final = []
    affichage = []
    finalv2 = []
    finalv3 = []
    for i in liste_fichiers :
        resultat.append(mots_fichier(i))
    for elemen in resultat : 
        for i in elemen : 
            if i not in final :
                final.append(i[0])
    for i in final :
        if i not in finalv3:
            finalv3.append(i)            
    for i in final :
        if [i] not in finalv2:
            finalv2.append([i])
    for i in range(len(liste_fichiers)):
        for j in range(len(finalv2)):
            finalv2[j].append(0)
        affichage = mots_fichier(liste_fichiers[i])
        for k in range(len(affichage)):
            ind = finalv3.index(affichage[k][0])
            finalv2[ind][i+1] = affichage[k][1]
    return finalv2
        

def classement(liste):
    '''classe les 15 premiers mots qui apparaissent le plus'''
    comptage = mots_fichier(liste)
    motfich = compte_ligne_mot(liste)
    motfich = motfich[1]
    resultat = []
    #Calcule frequance du mot :
    listefreq = []
    for i in comptage :
        listefreq.append([i[0],i[1]/motfich])
    listefreq.sort(key=clef, reverse=True)
    
    if len(listefreq) > 15 :
        for i in range(0,15) :
            resultat.append(listefreq[i])
    else :
        resultat = listefreq
    return resultat
   
   
        

def apparition_mots(liste_fichier):
    result=[]
    for i in liste_fichier :
        result.append([classement(i)])
    with open("res", "w",) as csv_file :
        ecrit = csv.writer(csv_file, delimiter=",")
        for i in result :
            for n in i :
                ecrit.writerow(n)
    return result

def clef(elem):
    return elem[1]

       

# --------------------------------------------------
# Programme principal
# --------------------------------------------------
def main():
   print(compte_ligne_mot("rep1/texte_01.txt"))
   print(compte_dans_fichiers(["rep1/texte_01.txt","rep1/texte_02.txt","rep1/texte_03.txt","rep1/texte_04.txt","rep1/texte_05.txt","rep1/texte_06.txt"]))
   print(mots_fichier("rep1/texte_02.txt"))
   print(mots_dans_fichiers(["rep1/texte_01.txt","rep1/texte_02.txt","rep1/texte_03.txt","rep1/texte_04.txt","rep1/texte_05.txt","rep1/texte_06.txt"]))
   print(apparition_mots(["rep1/texte_01.txt","rep1/texte_02.txt","rep1/texte_03.txt","rep1/texte_04.txt","rep1/texte_05.txt","rep1/texte_06.txt"]))
         
if __name__ == "__main__":
    main()
