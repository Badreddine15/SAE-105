#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import json 
import matplotlib.pyplot as plt



#-------------------------------------Partie01---------------------------------------------#
import csv 



import string
def clean(carac):
    '''Fonction qui ne garde que notre definition de mot '''
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
    '''Compte les mots dans une liste de fichiers '''
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
    '''Ecrit dans un fichier le nombre dappartition d'un mot dans une liste de fichier'''
    result=[]
    for i in liste_fichier :
        result.append([classement(i)])
    with open("res", "w",) as csv_file :
        ecrit = csv.writer(csv_file, delimiter=",")
        for i in result :
            for n in i :
                ecrit.writerow(n)
    return result

def apparition_mots_sans(liste_fichier):
    
    result=[]
    for i in liste_fichier :
        result.append([classement(i)])
    return result

def clef(elem):
    '''Aide a trier '''
    return elem[1]


#--------------------------------------------------------------------Partie2--------------------------#


def lecture_solo(rep) :
    '''Ne lis qu'un seul fichier '''
    with open(rep) as re :
        lecture = re.read()
    
    js = json.loads(lecture)
    res = []
    for i in range(len(js["data"])):
        texte = js["data"][i]['text']
        if "RT" in texte :
            texte = texte.split(":")
            texte.pop(0)
            if len(texte) >= i :
                js["data"][i]['text'] = texte[0]
    for i in range(len(js["data"])) :
        res.append([js["data"][i]['created_at'],js["data"][i]['text']])
    
    return res

def lecture_tweet(rep):
    '''Lis les tweets dans une liste de fichier et renvoie tweet + date de creation '''
    liste_fichiers_rep = [f for f in listdir(rep) if isfile(join(rep, f))]
    res = []
    resfinal = []
    for i in liste_fichiers_rep :
        res.append(lecture_solo(str(rep)+"/"+i))
    for i in res :
        for n in i :
            resfinal.append(n)
        
    return resfinal
        


def mots_dans_fichiers_rep(rep) :
    ''' premier élément est le nom du fichier, le deuxième élément
est un dictionnaire dont les clés sont les mots utilisés et les valeurs sont nombre
d’utilisation de ces mots dans le fichier correspondant.'''
    liste_fichiers_rep = [f for f in listdir(rep) if isfile(join(rep, f))]
    
    chemin = []
    res = []
    for i in liste_fichiers_rep :
        res.append([i])
    for i in liste_fichiers_rep :
        chemin.append(rep+"/"+i)
    m = mots_dans_fichiers(chemin)
    for i in res :
        i.append(dict())
    for n in m:
        for i in res:           
            i[1][n[0]] = n[res.index(i)+1]
    return res
    
def apparition_mots_rep(rep) :
    '''cule la fréquence d’apparition
des 15 mots apparaissant le plus fréquemment dans chacun des fichiers contenus dans
le répertoire rep'''
    liste_fichiers_rep = [f for f in listdir(rep) if isfile(join(rep, f))]
    chemin = []
    resulat = []
    final = []
    
    for i in liste_fichiers_rep :
        chemin.append(rep+"/"+i)
    for i in chemin :
        resulat.append(classement(i))
    for n in resulat : 
        final.append(dict())
    for n in resulat:
        for m in n :
            final[resulat.index(n)][m[0]]=m[1]
    with open("res", "w") as res :
        res.write(str(final))
    return final



def compte_tweet(rep):
    tweets = lecture_tweet(rep)
    res = []
    date = []
    date_sansdoub = []
    inter = {}
    for i in tweets :
        res.append(i[0].split(" "))
    for i in res :
        date.append(i[0])
    for i in date :
        if i not in date_sansdoub :
            date_sansdoub.append(i)
    for i in date_sansdoub :
        inter[i] = date.count(i)
    
    date2 = list(inter.keys())
    tweet = list(inter.values())
    plt.bar(range(len(inter)), tweet, tick_label=date2) 
    plt.show()
    
    
    


def compte_mot_rep(mot, rep):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    fichier = [f for f in listdir(rep) if isfile(join(rep, f))]
    freq =[]
    result = {}
    for i in apparition_mots_rep(rep) :
        if str(mot).upper() in i :
            freq.append(i[str(mot).upper()])
        else :
            freq.append(0)
    for i in range(len(fichier)) :
        result[fichier[i]] = freq[i]
    ax.bar(fichier,freq)
    plt.show()
    return result




def compte_mot_tweet_rep(mot, rep):
    tweets = lecture_tweet(rep)
    date_tweet = []
    intermediare = []
    resultat = dict()
    for i in tweets :
        i[0] = i[0].split(" ")
        i[0].pop(1)
        i[0] = i[0][0]
    for i in tweets : 
        if [i[0]] not in date_tweet :
            date_tweet.append([i[0]])
    for i in date_tweet :
        for n in tweets :
            if i[0] in n :
                i.append(n[1].lower())
    for i in date_tweet :
        cont = 0
        intermediare.append([i[0]])
        for n in range(1,len(i)) :
            cont += i[n].count(mot.lower())
        intermediare[intermediare.index([i[0]])].append(cont)
    for i in intermediare :
        resultat[i[0]] = i[1]
    print(resultat)
    
    
    



def main():
    print(mots_dans_fichiers_rep("rep1"))
    print(apparition_mots_rep("rep1"))
    print(compte_mot_rep("de", "rep1"))
    print(lecture_tweet("rep2"))
    print(compte_tweet("rep2"))
    print(compte_mot_tweet_rep("je", "rep2"))
if __name__ == "__main__":
    main()