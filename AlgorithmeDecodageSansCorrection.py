# coding: utf-8

import time
from AlgorithmeDecodage import *

def decoderSansCorrection(valeur, fichier_save):
    """Fonction appelé lorsqu'on lance le décodage. Elle prend en paramètre le
    type (fichier ou texte), la valeur(texte, une séquence d'adn ou chemin de
    fichier .dna), ainsi que le chemin ou sauver le fichier décodé. Elle va
    décoder le fichier et l'enregistrer avec la bonne extension au chemin donné.
    Elle renvoi le temps écoulé pour le décodage. """
    
    time1=time.clock() #On calcule le temps au début du décodage
    
    #Si c'est un fichier on l'ouvre et on recupere le séquence d'ADN. 
    with open(valeur, "r") as ouverture:
        s_dna_final = ouverture.read()
    valeur = valeur[:-4] #On enleve les 4 derniers caractère du fichier (l'extension .dna)


    #On lance le décodage.
    s_dna_final = decodeSansCorrec(s_dna_final, valeur, fichier_save)
    
    time2=time.clock() #On calcule le temps à la fin du décodage
    temps=time2-time1  #On stocke le temps écoulé entre le début et la fin du décodage.

    return temps




          
def decodeSansCorrec(s_dna, fichier, fichier_save):
    """Fonction appelé lorsqu'on lance le décodage à partir de la fonction
    principale. Elle prend en paramètre le type (fichier ou texte), la séquence
    d'ADN, la valeur(texte ou chemin de fichier), ainsi que le chemin ou sauver
    le fichier décodé."""


    if len(s_dna)%117!=0: #On vérifie que la séquence est bien composé de segment de 117 nucléotides.
        print("Pas bonne longueur")
        
    segments = {}
    dicoSegment = {}
    segmentFinal = []
    dicoFinal = {}
    i=0
    i1=-1
    s_dna_f = [] #Liste qui contiendra la séquence d'ADN "final"
    while i < len(s_dna): #On recupere les segments de 117 dans un dictionnaire
        i1+=1
        segments[i1] = s_dna[i:i+117]
        i+=117

    
    for key, segment in segments.items(): #On va traiter chaque segment séparément
        
        segment = list(segment)
        
        del segment[116] #On supprime le premier nucléotides du segment
        del segment[0]   #On supprime le dernier nucléotides du segment
        
        IX = segment[100:115] #On recupere IX puis one le supprime du segment.
        del segment[100:115]

        #On transforme IX en trit.
        pre_nt = segment[99] 
        IX = DNAToTrit(IX, pre_nt=pre_nt)
        
        ID = IX[0:2] #On recupere ID.
        i3 = IX[2:14]#On recupere i3.

        
        p  = int(IX[-1]) #On recupere P, puis on le calcule à partir de ID et i3. On vérifie qu'ils sont bien égales.
        try:
            P = int(ID[0]) + int(i3[0]) + int(i3[2]) + int(i3[4]) + int(i3[6]) + int(i3[8]) + int(i3[10])
        except IndexError:
            print('ID : {}\ni3 : {}'.format(ID, i3))
        while P != 0 or P != 1 or P != 2:
            if P <0:
                P+=3
            elif P>2:
                P-=3
            else:
                break
        if P!=p:
            print("Erreur P")
            
        else:
            i = int("".join(str(v) for v in i3), 3) #On calcule i à partir de i3 et on vérifie qu'il est égale à la clé du segment ( pas obligatoire, juste pour mon programme).
        i = key
        #On regarde si i est impair, et si oui, on l'inverse et complemente
        if i%2!=0:
            segment=reverseDna(segment)
            
        dicoFinal[i] = "".join(segment) #On ajoute le segment a un dctionnaire avec comme clé i.

    
            
    s_dna_f = ""
    test = 0
    for i, segment in dicoFinal.items(): #On crée un dictionnaire qui va contenir, avec comme clé leur 'position' les 4 segments censés etre pareils pour les comparer.
        if i == 0: #Si c'est le premier segments, on défini les 4 premieres clé.
            s_dna_f += segment
        else:
            s_dna_f += segment[75:]
    if len(s_dna_f)%25!=0: #On vérifie que la séquence d'ADN final est bien un multiple de 25.
        print("Erreur !")

    
    s_dna_f = DNAToTrit(s_dna_f) #On transforme la liste d'ADN en une liste ternaire.
    
    for trit in s_dna_f:
        if not trit == "0":
            if not trit == "1":
                if not trit == "2":
                    print("wtf", trit)

    s2 = s_dna_f[len(s_dna_f)-20:len(s_dna_f)] #On recupere les 20 dernier trits de la séquence , donc S2.
    i=0
    time1_s4_s1=time.clock()
    for nb in s2: #On "enleve" le nombre de 0 permettant une longueur de 20
        if nb=="0":
            i+=1
        else:
            break
    longueur = int("".join(s2[i:len(s2)]),3) #On converti la olongueur en décimal.
    s1= s_dna_f[:longueur] #On recupere S1 grâce à la longueur calculé avant.
    del s_dna_f
    s_bytes = tritToByte(s1) #On transforme la séquence ternaire en une séquence d'octets. 
    #Si le type est un fichier, on recupere la position de l'extension et on rajoute _dna_decoded entre le nom et l'extension du fichier
    test = True
    i=-1
    while test:
        if fichier[i]==".":  
            test=False
        else:
            i-=1
    fichier= fichier[:i] + "_dna_decoded" + fichier[i:]

    #Enfin, on supprime le chemin du fichier pour ne garder que le nom et l'extension, puis on ajoute ce nom au chemin de sauvegarde.
    i=-1
    test=True
    if fichier.find("/") != -1 or fichier.find("\\") != -1:
        while test:
            if fichier[i]=="/" or fichier[i]=="\\":
                fichier=fichier[i:]
                test=False
            i-=1
    fichier=fichier_save+fichier

    with open(fichier, "wb") as ouverture: #On crée un fichier avec le chemin crée auparavant et on y écrit la séquence binaire.
        ouverture.write(s_bytes)
        
