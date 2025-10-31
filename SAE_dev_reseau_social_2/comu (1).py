#!/usr/bin/env python

def cree_reseau(amis): 
    """Cette fonction crée un dictionnaire modélisant un réseau d'amis  
    dont les clés sont les membres du réseau et les valeurs le tableau
    de leurs amis à partir d'un tableau 'amis' de couples d'amis. 
     
    Argument : 
    amis -- tableau de couple d'amis (liste)""" 
    reseau={} 
    i=0 
    while i<len(amis): 
        if amis[i][0] not in reseau: #teste si le premier ami du couple d'amis à l'indice i est déjà défini dans le dictionnaire 
            reseau[amis[i][0]]=[] #ajoute le premier ami du couple d'amis au dictionnaire avec un tableau vide comme valeur, que l'on remplira au fur et à mesure 
        if amis[i][1] not in reseau: #même chose avec le second ami du couple d'amis 
            reseau[amis[i][1]]=[] 
        if amis[i][1] not in reseau[amis[i][0]]: #teste si le second ami du couple d'amis est dans la liste d'amis du premier ami 
            reseau[amis[i][0]].append(amis[i][1]) 
        if amis[i][0] not in reseau[amis[i][1]]: #même chose avec le premier ami 
            reseau[amis[i][1]].append(amis[i][0]) 
        i+=1 
    return(reseau) 


def liste_personnes(reseau):
    """Cette fonction crée une liste des membres
    d'un dictionnaire de réseau d'amis.
     
    Argument : 
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    liste=[] 
    for cle in reseau.keys(): #affecte la valeur d'une clé à 'cle' à chaque tour de boucle 
        liste.append(cle) 
    return liste 
  
  
def sont_amis(reseau,nom1,nom2):
    """Cette fonction teste si deux membres
    d'un réseau sont amis. 
     
    Arguments : 
    reseau -- dictionnaire de réseau d'amis (dictionnaire)
    nom1 -- premier membre du réseau (chaine de caractères) 
    nom2 -- deuxième membre du réseau (chaine de caractères)""" 
    if nom1 not in reseau or nom2 not in reseau: #teste si un des deux noms n'est pas présent dans le réseau 
        return False #si l'un des deux noms n'est pas dans le réseau, il n'existe pas de relation entre les deux personnes 
    return nom1 in reseau[nom2] #si le nom1 est dans la liste des amis de nom2, c'est aussi le cas dans le sens inverse, une relation allant dans les deux sens 


def sont_amis_de(reseau,nom,groupe):
    """Cette fonction teste si tous les
    membres d'un groupe sont amis avec une
    personne passée en paramètre. 
     
    Arguments : 
    reseau -- dictionnaire de réseau d'amis (dictionnaire)
    nom -- membre d'un réseau (chaine de caractères) 
    groupe -- tableau de personnes (liste)""" 
    i=0 
    while i<len(groupe) and sont_amis(reseau,groupe[i],nom): #interromp la boucle si la personne en position i n'est pas ami avec 'nom' 
        i+=1 
    return i==len(groupe) #si la boucle a parcouru tout le tableau 'groupe', c'est qu'il n'y a eu aucune interruption et qu'ils sont tous amis de nom 
  
  
def sont_amis_de_bis(reseau,nom,groupe):
    """Cette fonction est une autre version
    de la fonction sont_amis_de ci-dessus.
    Elle teste si tous les membres d'un
    groupe sont amis avec une personne
    passée en paramètre. 
     
    Arguments : 
    reseau -- dictionnaire de réseau d'amis (dictionnaire)
    nom -- membre d'un réseau (chaine de caractères) 
    groupe -- tableau de personnes (liste)""" 
    i=0 
    while i<len(groupe): 
        if not sont_amis(reseau,groupe[i],nom): #teste si la personne à l'indice i est ami avec 'nom'
            return False 
        i+=1 
    return True 
  
  
def est_comu(groupe,reseau):
    """Cette fonction teste si tous les
    membres d'un groupe sont tous amis entre eux. 
     
    Arguments :
    groupe -- tableau de personnes (liste)
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    i=0 
    while i+1<len(groupe) and sont_amis(reseau,groupe[i],groupe[i+1]): #interromp la boucle si la personne en position i n'est pas ami avec celle en position i+1 
        i+=1 
    return i+1==len(groupe) #si la boucle a parcouru tout le tableau 'groupe', c'est qu'il n'y a eu aucune interruption et qu'ils sont tous amis de nom 
  

def est_comu_bis(groupe,reseau):
    """Cette fonction est une autre version
    de la fonction est_comu ci-dessus.
    Elle teste si tous les
    membres d'un groupe sont tous amis entre eux. 
     
    Arguments :
    groupe -- tableau de personnes (liste)
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    i=0 
    while i+1<len(reseau): 
        if not sont_amis(reseau,groupe[i],groupe[i+1]): #teste si la personne à l'indice i est ami avec celle à l'indice i+1
            return False 
        i+=1 
    return True 
  
  
def comu(groupe,reseau):
    """Cette fonction crée une communauté (liste)
    qui regroupe toutes les personnes amis entre
    elles d'un groupe passé en paramètre. 
     
    Arguments :
    groupe -- tableau de personnes (liste)
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    comun=[] 
    for nom in groupe: 
        if sont_amis_de(reseau,nom,comun): #teste si 'nom' est ami avec toutes les personnes dans le tableau 'comun' 
            comun.append(nom) 
    return comun 


def tri_popu(groupe,reseau): #tri par insertion
    """Cette fonction trie un groupe par
    popularité (nombre d'amis) décroissante. 
     
    Arguments :
    groupe -- tableau de personnes (liste)
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    i=0
    while i<len(groupe)-1:
        maxi=i 
        j=i+1 
        while j<len(groupe): 
            if len(reseau[groupe[j]])>len(reseau[groupe[maxi]]): 
                maxi=j 
            j+=1 
        sup=groupe.pop(maxi) 
        groupe.insert(i,sup) 
        i+=1 
    return groupe 
  
  
def comu_dans_reseau(reseau):
    """Cette fonction trie les membres d'un
    réseau par popularité décroissante et utilise
    le groupe ainsi créé pour créer une communauté. 
     
    Argument :
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    groupe=liste_personnes(reseau) #affecte la liste des personnes qui appartiennent au réseau à 'groupe'
    tri_popu(groupe,reseau) #tri cette liste de personnes
    return comu(groupe,reseau) #crée une communauté à partir de la liste triée
  

def comu_dans_amis(comun,reseau):
    """Cette fonction crée une communauté (liste)
    réduite à une personne avant d'y ajouter
    toutes ses amis s'ils sont également amis
    avec toutes les personnes de la communauté. 
     
    Arguments :
    comun -- communauté d'une seule personne (liste)
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    groupe=reseau[comun[0]] #affecte la liste d'ami de la personne à l'indice i à 'groupe'
    tri_popu(groupe,reseau) #tri cette liste d'ami
    for ami in groupe: 
        if sont_amis_de(reseau,ami,comun): #teste si 'ami' est ami avec toutes les personnes du tableau 'comun'
            comun.append(i) 
    return comun 


def comu_max(reseau):
    """Cette fonction renvoie la plus
    grande communauté trouvée à partir
    de communautés de chaque membre du
    réseau passé en paramètre.
     
    Argument :
    reseau -- dictionnaire de réseau d'amis (dictionnaire)""" 
    liste=liste_personnes(reseau) #affecte la liste des personnes qui appartiennent au réseau à 'liste'
    comun_max=comu_dans_amis([liste[0]],reseau) #affecte une communauté crée à partir de la personne à l'indice i à 'comun_max'
    i=1 
    while i<len(tab): 
        comun_tmp=comu_dans_amis([liste[i]],reseau) #affecte une communauté crée à partir de la personne à l'indice i à 'comun_tmp'
        if len(comun_max)<len(comun_tmp): #teste si le nombre de personnes dans la communauté temporaire est supérieur à celui de 'comun_max'
            comun_max=comun_tmp 
        i+=1 
    return comun_max
