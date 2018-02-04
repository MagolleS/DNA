import time
from random import randint
from values import TRITS

def decoder(valeur, fichier_save, correction):
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
    if correction:
        s_dna_final = decode(s_dna_final, valeur, fichier_save, correction)
    else:
        s_dna_final = decodeSansCorrec(s_dna_final, valeur, fichier_save)

    time2=time.clock() #On calcule le temps à la fin du décodage
    temps=time2-time1  #On stocke le temps écoulé entre le début et la fin du décodage.

    return temps
def convert(nombre, base = 2):
    """Fonction permettant de convertir un nombre en base 10 en une base défini.
    Elle prend en paramètre le nombre en base 10 ainsi que la base vers laquel
    le nombre doit etre converti, et qui par défaut est 2."""
    
    resultat = ''
    q = nombre // base
    r = nombre % base
    resultat = str(r) + resultat
    while q != 0:
        r = q % base
        resultat = str(r) + resultat
        q = q // base
    return resultat


def tritToByte(s_trit):
    """Fonction qui prend en paramètre une séquence de trits. Elle va transfomer
    cette séquence ternaire en un type bytes. Elle renvoi un objt de type bytes"""
    
    index = 0
    s_bytes = []#Liste qui va contenir les valeurs des octets et qui seras transformé en un bytes.
    while index < len(s_trit): #Tant que la liste de trit n'est pas vide, on continue à regarder les premier trit
        trit="".join(s_trit[index:index+6])
        if trit in TRITS:
            s_bytes.append(TRITS.index(trit))
            index+=6     
        else:
            trit = "".join(s_trit[index:index+5]) #Si on ne trouve pas de correspondance avec les 6 premier trits, on cherche avec les 5 premier.
            if trit in TRITS:
                s_bytes.append(TRITS.index(trit))
                index+=5                             
        
    s_bytes = bytes(s_bytes)#On transformer la liste en un bytes puis pn le renvoi.
    return s_bytes


def checkHomopolymere(segment1, segment2):
    """Fonction qui prend en paramètre deux segments de nucléotides et regarde si l'un des deux possède des
    homopolymères (répétition du même nucléotides). Si l'un des deux en possède, il va renvoyer celui qui n'en
    possède pas, si les deux ou aucun n'en possède, il renvoi un flottant (2,6)"""
    
    test1 = 0
    test2 = 0
    for i, nt in enumerate(segment1): #On vérifie le premier segment
        try: 
            if nt == segment1[i+1]: #On regarde si le nucléotides est égale a celui suivant
                test1+=1 #Si oui on ajoute 1 a 'test1'
        except IndexError: #Si, il y a un IndexError, cela signifie que c'est le dernier nucléotides du segment.
            break
    for i, nt in enumerate(segment2): #On vérifie le deuxième segment
        try:
            if nt == segment2[i+1]: #On regarde si le nucléotides est égale a celui suivant
                test2+=1  #Si oui on ajoute 1 a 'test2'
        except IndexError: #Si, il y a un IndexError, cela signifie que c'est le dernier nucléotides du segment.
            break
    if test1!=0 and test2!=0: #Les deux segments possèdent des homopolymères
        return 2,6
    elif test1==0 and test2==0: #Aucun des deux segments possèdent des homopolymères
        return 2,6
    elif test1!=0: #Le segment1 possèdent des homopolymères
        return segment2
    elif test2!=0: #Le segment2 possèdent des homopolymères
        return segment1 


    
def DNAToTrit(s_dna, pre_nt="A"):
    """Fonction qui transforme une séquence ADN en séquence trinaire.
    Elle prend en fonction la séquence d'ADN et, en paramtre faculatif,
    le nucléotide précedent, par défaut A, et renvoi une liste de trit."""
    
    s_trit = []#liste qui va accueillir la séquence trinaire
    a = "A"
    c = "C"
    g = "G"
    t = "T"
    longueur = len(s_dna)
    trits = ["0", "1", "2"]

    for index, nt in enumerate(s_dna):

        if s_trit != []:
            pre_nt = s_dna[index-1]
        if pre_nt == a:
            if nt == c:
                s_trit.append("0")
            elif nt == g:
                s_trit.append("1")
            elif nt == t:
                s_trit.append("2")
            else:
                s_trit.append(trits[randint(0, 2)])
  
        elif pre_nt == c:
            if nt == g:
                s_trit.append("0")
            elif nt == t:
                s_trit.append("1")
            elif nt == a:
                s_trit.append("2")
            else:
                s_trit.append(trits[randint(0, 2)])

        elif pre_nt == g:
            if nt == t:
                s_trit.append("0")
            elif nt == a:
                s_trit.append("1")
            elif nt == c:
                s_trit.append("2")
            else:
                s_trit.append(trits[randint(0, 2)])

        elif pre_nt == t:
            if nt == a:
                s_trit.append("0")
            elif nt == c:
                s_trit.append("1")
            elif nt == g:
                s_trit.append("2")
            else:
                print("pas nucléotides pr t : ", pre_nt)
                s_trit.append(trits[randint(0, 2)])
        	
        else:
            s_trit.append(trits[randint(0, 2)])
            
    if len(s_trit) != longueur:
    	print("Pas la même longueur : s_dna {} s_trit {}".format(longueur, len(s_trit)))
    return s_trit

def reverseDna(s_dna):
    """Fonction qui inverse une séquence d'ADN puis change chaque nucléotides
    par le nucléotide complémentaire. Elle prend en paramètre une séquence d'ADN et renvoi une autre séquence d'ADN"""
    
    if type(s_dna)!=list:
        s_dna = list(map(str, str(s_dna)))
        #Si c'est une chaine de caractere qui est recu en parametre, on la
        #transforme en liste
    a = "A"
    c = "C"
    g = "G"
    t = "T"
    s_dna_r = []#Liste qui va accueillir le nouvelle séquence d'adn
    for nt in s_dna:
        if nt == a:
            s_dna_r.append(t)
        elif nt == t:
            s_dna_r.append(a)
        elif nt == g:
            s_dna_r.append(c)
        elif nt == c:
            s_dna_r.append(g)

    s_dna_r.reverse()#On inverse la liste
    return s_dna_r

          
def decode(s_dna, fichier, fichier_save, correction):
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
        if len(IX) != 15 and correction:
        	print("erreur taille IX")
        IX = DNAToTrit(IX, pre_nt=pre_nt)

        ID = IX[0:2] #On recupere ID.
        i3 = IX[2:14]#On recupere i3.
        
        p  = int(IX[-1]) #On reœcupere P, puis on le calcule à partir de ID et i3. On vérifie qu'ils sont bien égales.

        try:
        	P = int(ID[0]) + int(i3[0]) + int(i3[2]) + int(i3[4]) + int(i3[6]) + int(i3[8]) + int(i3[10])
        except IndexError:
            print(len(IX), len(i3), len(ID))
            print('Erreur à la formation de P : \nID : {}\ni3 : {}'.format(ID, i3))

        while P != 0 or P != 1 or P != 2:
            if P <0:
                P+=3
            elif P>2:
                P-=3
            else:
                break
        if P!=p:
        	print("Erreur P : ", key )

        i = int("".join(str(v) for v in i3), 3) #On calcule i à partir de i3 et on vérifie qu'il est égale à la clé du segment ( pas obligatoire, juste pour mon programme).
        if i != key:
        	print("i et index différents")
        	print(i, "  ", key)
        i = key
        
        #On regarde si i est impair, et si oui, on l'inverse et complemente
        if i%2!=0:
            segment=reverseDna(segment)
        
        if correction:
            if len(segment) == 100:
            	dicoFinal[i] = "".join(segment) #On ajoute le segment a un dctionnaire avec comme clé i.
        else:
            dicoFinal[i] = "".join(segment) #On ajoute le segment a un dctionnaire avec comme clé i.

    s_dna_f = ""
    if correction:
        for i, segment in dicoFinal.items(): #On crée un dictionnaire qui va contenir, avec comme clé leur 'position' les 4 segments censés etre pareils pour les comparer.
            if i == 0: #Si c'est le premier segments, on défini les 4 premieres clé.
                dicoSegment[i] = [segment[:25]]
                dicoSegment[i+1] = [segment[25:50]]
                dicoSegment[i+2] = [segment[50:75]]
                dicoSegment[i+3] = [segment[75:]]
            else: #Sinon, on ajoute les 3 premiers segments et on défini le dernier.
                dicoSegment[i].append(segment[:25])
                dicoSegment[i+1].append(segment[25:50])
                dicoSegment[i+2].append(segment[50:75])
                dicoSegment[i+3] = [segment[75:]]
                
        for segment in dicoSegment.values():
            """Pour chaque segments, on va comparer tout les segments et procéder a un vote. Si on tombe sur des égalités,
            on utilise la fçonction checkHomopolymères et si elle renvoi un flottant, on défini le bon sgment aléatoirement."""
            i = len(segment)
            if i == 1:
                segmentFinal.append(segment[0])
            elif i == 2:
                if segment[0] != segment[1]:
                    test = checkHomopolymere(segment[0], segment[1])
                    if type(test) == float:
                        segmentFinal.append(segment[randint(0,1)])
                    else:
                        segmentFinal.append(test)
                else:
                    segmentFinal.append(segment[0])
            elif i == 3:
                if segment[0] == segment[1]:
                    segmentFinal.append(segment[0])
                elif segment[1] == segment[2]:
                    segmentFinal.append(segment[1])
                else:
                    test = checkHomopolymere(segment[0], segment[1])
                    if type(test) == float:
                        nbalea = randint(0,1)
                        segmentFinal.append(segment[nbalea])
                    else:
                        
                        segmentFinal.append(test)
            elif i == 4:
                if segment[0] == segment[1]:
                    if segment[2] == segment[3]:
                        if segment[2] == segment[1]:
                            segmentFinal.append(segment[0])
                        else:
                            test = checkHomopolymere(segment[1], segment[2])
                            if type(test) == float:
                                nbalea = randint(1,2)
                                segmentFinal.append(segment[randint(1,2)])
                            else:
                                segmentFinal.append(test)
                    else:
                        segmentFinal.append(segment[0])
                elif segment[1] == segment[2]:
                    if segment[0] == segment[3]:
                        test = checkHomopolymere(segment[0], segment[1])
                        if type(test) == float:
                            nbalea = randint(0,1)
                            segmentFinal.append(segment[nbalea])
                        else:
                            segmentFinal.append(test)
                    else:
                        segmentFinal.append(segment[1])
                elif segment[2] == segment[3]:
                    segmentFinal.append(segment[2])
        s_dna_f = "".join(segmentFinal)
    else:
        s_dna_f = ""
        for i, segment in dicoFinal.items(): #On crée un dictionnaire qui va contenir, avec comme clé leur 'position' les 4 segments censés etre pareils pour les comparer.
            if i == 0: #Si c'est le premier segments, on défini les 4 premieres clé.
                s_dna_f += segment
            else:
                s_dna_f += segment[75:]

    if len(s_dna_f)%25!=0: #On vérifie que la séquence d'ADN final est bien un multiple de 25.
        print("Erreur !")
        

    s_dna_f = DNAToTrit(s_dna_f) #On transforme la liste d'ADN en une liste ternaire.
    s2 = s_dna_f[len(s_dna_f)-20:len(s_dna_f)] #On recupere les 20 dernier trits de la séquence , donc S2.
    i=0
    time1_s4_s1=time.clock()
    for nb in s2: #On "enleve" le nombre de 0 permettant une longueur de 20
        if nb=="0":
            i+=1
        else:
            break
    longueur = int("".join(s2[i:len(s2)]),3) #On converti la olongueur en décimal.
    s1 = s_dna_f[:longueur]#On recupere S1 grâce à la longueur calculé avant.
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
        
# if __name__ == '__main__':
# 	decoder("image.jpg.dna", "")

