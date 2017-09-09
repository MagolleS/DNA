#!/usr/bin/python3.5
# coding: utf-8

from string import digits, ascii_uppercase
from random import randint
import time

list_ID = ["00", "01","02","10","11","12","20","21","22"] #Liste conteant les 9 possibilités pour ID.
listInsert = ["A", "T"]#Liste qui accueille les 2 nucléotides possibles a ajouter au début d'un segment
listAppend = ["C", "G"]#Liste qui accueille les 2 nucléotides possibles a ajouter à la fin d'un segment

def print_erreur(message):
    print("/!\ ERREUR /!\ : \n"+message)

def encoder(tipe, valeur, fichier_save):
    """Fonction appelé lorsqu'on lance l'encodage. Elle prend en paramètre le
    type (fichier ou texte), la valeur(texte ou chemin de fichier), ainsi que
    le chemin ou sauver le fichier .dna. Elle renvoi une série de variable
    nécessaire au mode démonstration"""

    print("Lancement de l'encodage")
    
    time1 = time.clock() #Calcule le temps au début de la fonction
    
    #Fonction qui récupere la séquence binaire du fichier/texte et la transforme en ternaire. Elle renvoie la séquence binaire et la séquence ternaire.
    s_trit1, s_bytes = byteToTrit(tipe, valeur)

    
    #Fonction qui crée S4 et renvoi S4, S2 (len_Trit et nb0) et S3.
    s_trit4, len_Trit, nb0, s_trit3 = tritToFinalTrit(s_trit1)

    
    #Fonction qui transforme une séquence ternaire en séquence de nucléotides. Renvoi une liste comportant les bases.
    s_dna = TritToDNA(s_trit4)

    
    #Fonction qui crée tout les segments et l'indexation propore à chacun d'eux. Renvoi la séquence d'ADN final, plusieurs dictionnaire comportant en clé i et en valeur différents états du segment ou de son indexation.
    s_dna_final, dicoDebut, dicoReverse, dicoI3, ID, dicoP, dicoIX, dicoIX_dna, dicoFinal = DnaToDnaFinal(s_dna)

    
    #Fonction qui enregistre la séquence d'ADN dans un fichier .dna. Elle prend en paramètre le type (tipe), la valeur (le chemin, si le type est un fichier), la séquence d'ADN, et le chemin ou sauver le fichier.
    enregistrement(tipe, valeur, s_dna_final, fichier_save)
    
    time2=time.clock() #Calcule le temps à la fin de la fonction.
    temps=time2-time1  #Stocke le temps écoulé entre le début et la fin de la fonction.
    #Toutes les variables nécessaire au mode démonstration sont renvoyé par cette fonction
    return temps, s_bytes, s_trit1, len_Trit, nb0, s_trit3, s_trit4, s_dna, dicoDebut, dicoReverse, dicoI3, ID, dicoP, dicoIX, dicoIX_dna, dicoFinal, s_dna_final
    



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


def enregistrement(tipe, valeur, s_dna, fichier_save):
    """Fonction qui récupere une séquence d'adn et un emplacement de fichier et
    enregistre un fichier en .dna contenant cette séquence"""
    
    if tipe=="fichier":
        #Si le type est un fichier, on efface tout le chemin afin de ne laisser plus que le nom du fichier ainsi que son extension
        i=-1
        test=True
        while test:
            if valeur[i]=="/":
                valeur=valeur[i:]
                test=False
            i-=1
        valeur+=".dna" #On ajoute ensuite l'extension .dna
        fichier_save+="/"+valeur #enfin, on l'ajoute au chemin de sauvegarde défini auparavant.
        with open(fichier_save, "w") as ouverture:
            ouverture.write(s_dna)#On crée un fichier à l'emplacement crée auparavant et on y écrit la séquence d'ADN.
    
    else:
        #Si le type est un texte, on ajoute au chemin de sauvegarde texte_ suivi d'un nombre entre 0 et 1000 (aléatoire) puis l'extension .txt et enfin .dna.
        fichier_save+="/texte_"+str(randint(0,1000))+".txt"+".dna"
        with open(fichier_save, "x") as ouverture:
            ouverture.write(s_dna)#On crée un fichier à l'emplacement crée auparavant et on y écrit la séquence d'ADN.
        
def tritToFinalTrit(s_trit1):
    """Fonction qui prend en paramètre une liste contenant des str de 5 ou 6 caractere
    (0,1 ou 2) et la transforme de sorte qu'on puisse y connaitre sa longueur ainsi que
    la longueur totale soit un multiple de 25. Elle renvoi également S2 (len_Trit et nb0) et S3."""
    
    s_trit1 = "".join(s_trit1)
    #On crée s_trit2 qui mesure 20 trit et qui donne la longueur de s1 en ternaire
    len_Trit = convert(len(s_trit1), base=3)
    nb0 = 20 - len(convert(len(s_trit1), base=3))
    s_trit2 = nb0*"0" + len_Trit
    #On crée s_trit3 en fonction de s_trit1 et s_trit2 pour que ces 3 derniers ait comme longueur un multiple de 25
    len_trit_1_2 = len(s_trit1) + 20
    s_trit3 = 0
    while (len_trit_1_2 + s_trit3)%25 != 0:
        s_trit3+=1
    s_trit3 = s_trit3*"0"
    #On crée S4 : S1 + S3 + S2
    s_trit4 = str(s_trit1) + s_trit3 + s_trit2
    return s_trit4, len_Trit, nb0*"0", s_trit3
    




def TritToDNA(s_trit, pre_nt = "A"):
    """Fonction qui transforme une séquence ternaire en séquence ADN.
    Elle prend en fonction la séquence de trit et, en paramtre faculatif,
    le nucléotide précedent, par défaut A, et renvoi une liste de nucléotides."""
    
    
    s_t = list(map(int, str(s_trit)))  # Liste qui contient la séquence en trinaire
    s_dna = []  # Liste qui va acceuillir les nucléotides transformés
    for trit in s_t:
        if s_dna == []:
            pre_trit = pre_nt
        else:
            pre_trit = s_dna[-1]
            
        if pre_trit == "A":
            if trit == 0:
                s_dna.append("C")
            elif trit == 1:
                s_dna.append("G")
            elif trit == 2:
                s_dna.append("T")
        elif pre_trit == "C":
            if trit == 0:
                s_dna.append("G")
            elif trit == 1:
                s_dna.append("T")
            elif trit == 2:
                s_dna.append("A")
        elif pre_trit == "G":
            if trit == 0:
                s_dna.append("T")
            elif trit == 1:
                s_dna.append("A")
            elif trit == 2:
                s_dna.append("C")
        elif pre_trit == "T":
            if trit == 0:
                s_dna.append("A")
            elif trit == 1:
                s_dna.append("C")
            elif trit == 2:
                s_dna.append("G")

    return s_dna


def DnaToDnaFinal(s_dna):
    
    """"Fonction qui crée les segments de longueur 117. Elle prend en paramètre une séquence
    d'ADN et renvoi une autre séquence d'ADN"""
    
    ID = list_ID[randint(0,8)]#On determine ID qui reste le même pour toute la séquence donné en paramètre.
    #Création de dictionnaires qui vont contenir des infomations nécessaires au mode démonstration.
    dicoDebut = {}
    dicoReverse = {}
    dicoI3 = {}
    dicoP = {}
    dicoIX = {}
    dicoIX_dna = {}
    dicoFinal = {}
    
    maxNt = 100
    minNt = 0
    i=0
    segment = []
    s_dna_final = ""
    while i != (len(s_dna)/25)-3:
        #Boucle qui traite chaque segment séparement
        #On crée le segment de longueur 100. 
        if minNt == 0:
            segment=s_dna[:maxNt]        
        else:
            segment=s_dna[minNt:maxNt] 
        dicoDebut[i]="".join(segment)

        #Si i est impair, on inverse et complémente le segment
        if not i%2==0:
            segment = reverseDna(segment)
        dicoReverse[i] = "".join(segment)


        #On crée i3 de longueur 12
        i_trit = str(convert(i, base=3))
        i3 = (12 - len(i_trit))*"0" + i_trit
        dicoI3[i]=i3


        #On calcule P, d'abord "normalement" puis, tant que P est différent de 0, 1 ou 2, on retranche 3 si il est superieur a 2 ou ajoute 3 si il est inferieur à 0
        P = int(ID[0]) + int(i3[0]) + int(i3[2]) + int(i3[4]) + int(i3[6]) + int(i3[8]) + int(i3[10])
        
        while P != 0 or P != 1 or P != 2:
            if P <0:
                P+=3
            elif P>2:
                P-=3
            else:
                break
        dicoP[i]=P
        #On crée IX : ID + i3 + P. On le converti ensuite en ADN en précisant le nucléotide précedent avec le dernier nucléotide du segment
        IX = str(ID) + str(i3) + str(P)
        dicoIX[i] = IX
        IX_dna = TritToDNA(IX, pre_nt=segment[-1])
        dicoIX_dna[i] = IX_dna
        
        segment.extend(IX_dna)#On ajoute IX au segment.


        #On ajoute un nucléotide au début et un à la fin du segment, aléatoirement si possible mais en prenant en compte les nucléotides suivant ou précedent.
        if segment[0] == "A":
            segment.insert(0, "T")
        elif segment[0] == "T":
            segment.insert(0, "A")
        else:
            segment.insert(0, listInsert[randint(0,1)])

        if segment[-1]=="C":
            segment.append("G")
        elif segment[-1]=="G":
            segment.append("C")
        else:
            segment.append(listAppend[randint(0,1)])
        s_dna_final += "".join(segment)#On ajoute le segment à la séquence d'ADN final.
        dicoFinal[i]=segment
        
        i+=1
        maxNt+=25
        minNt+=25


        
        #Test si le segment a la bonne longueur
        if len(segment)<117:
            print_erreur("Le segment {} a une taille plus petite que 117 ({}).".format(i-1, len(segment)))
        elif len(segment)>117:
            print_erreur("Le segment {} a une taille plus grande que 117 ({}).".format(i-1, len(segment)))
    return s_dna_final, dicoDebut, dicoReverse, dicoI3, ID, dicoP, dicoIX, dicoIX_dna, dicoFinal #On renvoi la séquence d'ADN final ainsi que des variables nécessaires au mode décodage.
        
           
        
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
            
    
    
            
def byteToTrit(tipe, valeur):
    """Fonction qui prend en parametre un emplacement de fichier sous forme de
    string(str), va récuperer sous forme de d'un bytes la séquence binaire du
    fichier, puis le transformer en une séquence de trit. Cette séquence est s_trit
    et est represente en une liste contenant des str de 5 ou 6 caractere (0,1 ou 2)
    """
    
    if tipe=="fichier":
        with open(valeur, "rb") as ouverture:
            octets = ouverture.read()
    else:
        octets=valeur.encode()
    #Le fichier est ouvert et la séquence binaire est dans le bytes octets
        
    s_trit = []
    #Pour chaque octets, la valeur correspond à 5 ou 6 trits qu'on ajoute à s_trit
    for oct in octets:
        if oct == 0:
            s_trit.append("22201")
        elif oct == 1:
            s_trit.append("00100")   
        elif oct == 2:      
            s_trit.append("11220")  
        elif oct == 3:
            s_trit.append("00211")
        elif oct == 4:
            s_trit.append("20222")
        elif oct == 5:
            s_trit.append("00222")
        elif oct == 6:
            s_trit.append("02211") 
        elif oct == 7:
            s_trit.append("222110")
        elif oct == 8:
            s_trit.append("22002")                        
        elif oct == 9:
            s_trit.append("02100")                        
        elif oct == 10:
            s_trit.append("22001")                        
        elif oct == 11:
            s_trit.append("222122")                      
        elif oct == 12:
            s_trit.append("12001")
        elif oct == 13:
            s_trit.append("02021")
        elif oct == 14:
            s_trit.append("10100")
        elif oct == 15:
            s_trit.append("02010")
        elif oct == 16:
            s_trit.append("20101")
        elif oct == 17:
            s_trit.append("12211")
        elif oct == 18:
            s_trit.append("12120")
        elif oct == 19:
            s_trit.append("11111")
        elif oct == 20:
            s_trit.append("21211")
        elif oct == 21:
            s_trit.append("21221")
        elif oct == 22:
            s_trit.append("20220")
        elif oct == 23:
            s_trit.append("00122")
        elif oct == 24:
            s_trit.append("20022")
        elif oct == 25:
            s_trit.append("12121")
        elif oct == 26:
            s_trit.append("21111")
        elif oct == 27:
            s_trit.append("00221")
        elif oct == 28:
            s_trit.append("00202")
        elif oct == 29:
            s_trit.append("222202")
        elif oct == 30:
            s_trit.append("222102")
        elif oct == 31:
            s_trit.append("00010")
        elif oct == 32:
            s_trit.append("02212")
        elif oct == 33:
            s_trit.append("10011")
        elif oct == 34:
            s_trit.append("22011")
        elif oct == 35:
            s_trit.append("02221")
        elif oct == 36:
            s_trit.append("21212")
        elif oct == 37:
            s_trit.append("21021")
        elif oct == 38:
            s_trit.append("11211")
        elif oct == 39:
            s_trit.append("10111")
        elif oct == 40:	
            s_trit.append("12220")   
        elif oct == 41:
            s_trit.append("22110")
        elif oct == 42:    
            s_trit.append("22101")
        elif oct == 43:
            s_trit.append("11122")
        elif oct == 44:    
            s_trit.append("22022")
        elif oct == 45:    
            s_trit.append("01210")
        elif oct == 46:    
            s_trit.append("00210")
        elif oct == 47:    
            s_trit.append("02122")
        elif oct == 48:    
            s_trit.append("10122")
        elif oct == 49:    
            s_trit.append("01011")
        elif oct == 50:    
            s_trit.append("11101")
        elif oct == 51:    
            s_trit.append("01102")		
        elif oct == 52:    
            s_trit.append("22112")
        elif oct == 53:    
            s_trit.append("12122")
        elif oct == 54:    
            s_trit.append("11012")	
        elif oct == 55:
            s_trit.append("222112")
        elif oct == 56:    
            s_trit.append("02201")
        elif oct == 57:    
            s_trit.append("02011")
        elif oct == 58:    
            s_trit.append("20021")
        elif oct == 59:    
            s_trit.append("222021")	
        elif oct == 60:    
            s_trit.append("00022")
        elif oct == 61:    
            s_trit.append("222200")
        elif oct == 62:    
            s_trit.append("222120")
        elif oct == 63:    
            s_trit.append("21010")
        elif oct == 64:    
            s_trit.append("00121")
        elif oct == 65:    
            s_trit.append("02022")
        elif oct == 66:    
            s_trit.append("20100")
        elif oct == 67:    
            s_trit.append("10211")
        elif oct == 68:
            s_trit.append("21001")
        elif oct == 69:    
            s_trit.append("21210")
        elif oct == 70:    
            s_trit.append("10212")
        elif oct == 71:    
            s_trit.append("222212")
        elif oct == 72:    
            s_trit.append("20110")
        elif oct == 73:
            s_trit.append("20010")
        elif oct == 74:    
            s_trit.append("21220")
        elif oct == 75:    
            s_trit.append("21022")
        elif oct == 76:    
            s_trit.append("21000")
        elif oct == 77:    
            s_trit.append("01211")
        elif oct == 78:    
            s_trit.append("10220")
        elif oct == 79:    
            s_trit.append("12002")
        elif oct == 80:    
            s_trit.append("12011")
        elif oct == 81:    
            s_trit.append("11212")
        elif oct == 82:    
            s_trit.append("21100")
        elif oct == 83:    
            s_trit.append("12210")
        elif oct == 84:
            s_trit.append("20112")
        elif oct == 85:
            s_trit.append("22200")
        elif oct == 86:    
            s_trit.append("22102")
        elif oct == 87:    
            s_trit.append("21222")
        elif oct == 88:    
            s_trit.append("21012")
        elif oct == 89:    
            s_trit.append("12101")
        elif oct == 90:    
            s_trit.append("10120")
        elif oct == 91:    
            s_trit.append("01202")
        elif oct == 92: 
            s_trit.append("10200")
        elif oct == 93:    
            s_trit.append("02210")
        elif oct == 94:    
            s_trit.append("222211")
        elif oct == 95:    
            s_trit.append("11201")
        elif oct == 96:    
            s_trit.append("00102")
        elif oct == 97:    
            s_trit.append("01112")
        elif oct == 98:    
            s_trit.append("22010")
        elif oct == 99:    
            s_trit.append("00012")
        elif oct == 100:    
            s_trit.append("22100")
        elif oct == 101:    
            s_trit.append("20001")
        elif oct == 102:    
            s_trit.append("20202")
        elif oct == 103:    
            s_trit.append("02102")
        elif oct == 104:    
            s_trit.append("20200")
        elif oct == 105:    
            s_trit.append("20210")
        elif oct == 106:    
            s_trit.append("20012")
        elif oct == 107:    
            s_trit.append("11100")
        elif oct == 108:    
            s_trit.append("02101")
        elif oct == 109:    
            s_trit.append("11021")
        elif oct == 110:    
            s_trit.append("00021")
        elif oct == 111:    
            s_trit.append("02110")
        elif oct == 112:    
            s_trit.append("12102")
        elif oct == 113:    
            s_trit.append("01012")
        elif oct == 114:   
            s_trit.append("10101")
        elif oct == 115:    
            s_trit.append("10222")
        elif oct == 116:    
            s_trit.append("10221")
        elif oct == 117:    
            s_trit.append("10002")
        elif oct == 118:    
            s_trit.append("01120")
        elif oct == 119:    
            s_trit.append("00201")
        elif oct == 120:    
            s_trit.append("10020")
        elif oct == 121:    
            s_trit.append("222111")
        elif oct == 122:    
            s_trit.append("222220")
        elif oct == 123:    
            s_trit.append("02111")
        elif oct == 124:    
            s_trit.append("222222")
        elif oct == 125:    
            s_trit.append("00000")
        elif oct == 126:    
            s_trit.append("10112")
        elif oct == 127:    
            s_trit.append("22121")
        elif oct == 128:    
            s_trit.append("02000")
        elif oct == 129:    
            s_trit.append("10000")
        elif oct == 130:    
            s_trit.append("20111")
        elif oct == 131:    
            s_trit.append("00212")
        elif oct == 132:    
            s_trit.append("22021")
        elif oct == 133:    
            s_trit.append("21112")
        elif oct == 134:    
            s_trit.append("11022")
        elif oct == 135:    
            s_trit.append("01220")
        elif oct == 136:    
            s_trit.append("11102")
        elif oct == 137:    
            s_trit.append("20011")
        elif oct == 138:    
            s_trit.append("22111")
        elif oct == 139:    
            s_trit.append("10021")
        elif oct == 140:    
            s_trit.append("12212")
        elif oct == 141:    
            s_trit.append("11202")
        elif oct == 142:    
            s_trit.append("10201")
        elif oct == 143:    
            s_trit.append("02200")
        elif oct == 144:    
            s_trit.append("02002")
        elif oct == 145:    
            s_trit.append("11120")
        elif oct == 146:    
            s_trit.append("20102")
        elif oct == 147:    
            s_trit.append("11110")
        elif oct == 148:    
            s_trit.append("11002")
        elif oct == 149:    
            s_trit.append("22000")
        elif oct == 150:    
            s_trit.append("21002")
        elif oct == 151:    
            s_trit.append("21102")
        elif oct == 152:    
            s_trit.append("222221")
        elif oct == 153:    
            s_trit.append("11020")
        elif oct == 154:    
            s_trit.append("20221")
        elif oct == 155:    
            s_trit.append("01002")
        elif oct == 156:    
            s_trit.append("11001")
        elif oct == 157:    
            s_trit.append("00120")
        elif oct == 158:    
            s_trit.append("02202")
        elif oct == 159:    
            s_trit.append("10202")
        elif oct == 160:    
            s_trit.append("10012")
        elif oct == 161:    
            s_trit.append("22012")
        elif oct == 162:    
            s_trit.append("20211")
        elif oct == 163:    
            s_trit.append("21201")
        elif oct == 164:    
            s_trit.append("00220")
        elif oct == 165:    
            s_trit.append("11222")
        elif oct == 166:    
            s_trit.append("21011")
        elif oct == 167:
            s_trit.append("10110")
        elif oct == 168:
            s_trit.append("20002")
        elif oct == 169:
            s_trit.append("20122")
        elif oct == 170:
            s_trit.append("22122")
        elif oct == 171:
            s_trit.append("20201")
        elif oct == 172:
            s_trit.append("10022")
        elif oct == 173:
            s_trit.append("21101")
        elif oct == 174:
            s_trit.append("12110")
        elif oct == 175:
            s_trit.append("12222")
        elif oct == 176:
            s_trit.append("00200")
        elif oct == 177:
            s_trit.append("21202")
        elif oct == 178:
            s_trit.append("10210")
        elif oct == 179:
            s_trit.append("10010")
        elif oct == 180:
            s_trit.append("02012")
        elif oct == 181:
            s_trit.append("12221")
        elif oct == 182:
            s_trit.append("12022")
        elif oct == 183:
            s_trit.append("02222")
        elif oct == 184:
            s_trit.append("01100")
        elif oct == 185:
            s_trit.append("02121")
        elif oct == 186:
            s_trit.append("01122")
        elif oct == 187:
            s_trit.append("00112")
        elif oct == 188:
            s_trit.append("01020")
        elif oct == 189:
            s_trit.append("222100")
        elif oct == 190:
            s_trit.append("01222")
        elif oct == 191:
            s_trit.append("21020")
        elif oct == 192:
            s_trit.append("01201")
        elif oct == 193:
            s_trit.append("00001")
        elif oct == 194:
            s_trit.append("12021")
        elif oct == 195:
            s_trit.append("12010")
        elif oct == 196:
            s_trit.append("20121")
        elif oct == 197:
            s_trit.append("21120")
        elif oct == 198:
            s_trit.append("00002")
        elif oct == 199:
            s_trit.append("222201")
        elif oct == 200:
            s_trit.append("00011")
        elif oct == 201:
            s_trit.append("01010")
        elif oct == 202:
            s_trit.append("12112")
        elif oct == 203:
            s_trit.append("11112")
        elif oct == 204:
            s_trit.append("02120")
        elif oct == 205:
            s_trit.append("11010")
        elif oct == 206:
            s_trit.append("01110")
        elif oct == 207:
            s_trit.append("01212")
        elif oct == 208:
            s_trit.append("20120")
        elif oct == 209:
            s_trit.append("12000")
        elif oct == 210:
            s_trit.append("12100")
        elif oct == 211:
            s_trit.append("11210")
        elif oct == 212:
            s_trit.append("11011")
        elif oct == 213:
            s_trit.append("21200")
        elif oct == 214:
            s_trit.append("12200")
        elif oct == 215:
            s_trit.append("01111")
        elif oct == 216:
            s_trit.append("01200")
        elif oct == 217:
            s_trit.append("12012")
        elif oct == 218:
            s_trit.append("10121")
        elif oct == 219:
            s_trit.append("10102")
        elif oct == 220:
            s_trit.append("222210")
        elif oct == 221:
            s_trit.append("00020")
        elif oct == 222:
            s_trit.append("01000")
        elif oct == 223:
            s_trit.append("20020")
        elif oct == 224:
            s_trit.append("11121")
        elif oct == 225:
            s_trit.append("10001")
        elif oct == 226:
            s_trit.append("02001")
        elif oct == 227:
            s_trit.append("01101")
        elif oct == 228:
            s_trit.append("222121")
        elif oct == 229:
            s_trit.append("21121")
        elif oct == 230:
            s_trit.append("02220")
        elif oct == 231:
            s_trit.append("01001")
        elif oct == 232:
            s_trit.append("222101")
        elif oct == 233:
            s_trit.append("01022")
        elif oct == 234:
            s_trit.append("20212")
        elif oct == 235:
            s_trit.append("00101")
        elif oct == 236:
            s_trit.append("222022")
        elif oct == 237:
            s_trit.append("01021")
        elif oct == 238:
            s_trit.append("00111")
        elif oct == 239:
            s_trit.append("11200")
        elif oct == 240:
            s_trit.append("12201")
        elif oct == 241:
            s_trit.append("11000")
        elif oct == 242:
            s_trit.append("02112")
        elif oct == 243:
            s_trit.append("01221")
        elif oct == 244:
            s_trit.append("00110")
        elif oct == 245:
            s_trit.append("11221")
        elif oct == 246:
            s_trit.append("01121")
        elif oct == 247:
            s_trit.append("12111")
        elif oct == 248:
            s_trit.append("12020")
        elif oct == 249:
            s_trit.append("02020")
        elif oct == 250:
            s_trit.append("22020")
        elif oct == 251:
            s_trit.append("20000")
        elif oct == 252:
            s_trit.append("21110")
        elif oct == 253:
            s_trit.append("22120")
        elif oct == 254:
            s_trit.append("12202")
        elif oct == 255:
            s_trit.append("21122")

    #On retourne la liste
    return s_trit, octets

    

def afficherEncodage(texte, temps, s_bytes, s_trit1, len_Trit, nb0, s_trit3, s_trit4, s_dna, dicoDebut, dicoReverse, dicoI3, ID, dicoP, dicoIX, dicoIX_dna, dicoFinal, s_dna_final):
    """Fonction qui prend en paramètre ce que retourne la fonction encode.
    Il retourne un string contenant un affichage lisible des etapes de
    l'encodage. """

    s = ""
    for index, trit in enumerate(s_trit1):
        octet = convert(s_bytes[index], 2)
        s += "{}  {}  {} \n\n".format(texte[index], int(8-len(octet))*"0"+str(octet), trit)
    s += "".join(s_trit1)
    s += "{} convertit en base 3 -> {}\n".format(int(len_Trit, 3), len_Trit)
    s += "La longueur du nombre est de {}, on rajoute donc 20-{} = {} :\n {} {}\n".format(len(len_Trit),len(len_Trit),len(nb0), nb0, len_Trit)
    s += "La longueur des deux séquences est de {}. Le plus proche multiple de 25 est {} on rajoute donc {} 0 : \n {}\n".format(
        str(int(len_Trit, 3)+20), str(len(s_trit4)), str(len(s_trit3)), str(s_trit3))
    s += "Cela nous donne : \n {} {} {} de longueur {}\n".format("".join(s_trit1), str(s_trit3), nb0+len_Trit, len(s_trit4))
    s += "On converti le tout en ADN : \n {}\n".format("".join(s_dna))


    s += "N est égal à {longueur}. Il y aura donc ({longueur}/25)-3 = {truc} segment.\n".format(longueur=len("".join(s_dna)), truc=int((len("".join(s_dna))/25)-3))
    ecart=""
    for cle, valeur in dicoDebut.items():
        
        s += "Segment {} : {}{} {} {} {}\n".format(cle, ecart, "".join(valeur[:25]), "".join(valeur[25:50]), "".join(valeur[50:75]), "".join(valeur[75:100]))
        ecart+= " " +" "*25
        

    s += "Pour chaque segment, on regarde si i est impair : \n"
    s += str(len(dicoI3)) + str( len(dicoReverse)) + "\n"
    for cle, valeur in dicoReverse.items():
        s += "Segment {}\n".format(cle)
        if cle%2==0:
            s += "i = {}, et est donc pair, on laisse le segment comme il est : \n {}\n".format(cle, "".join(valeur))
        else:
            s += "i = {}, et est impair, on inverse puis complemente donc le segment : \n {}\n".format(cle, "".join(valeur))

    s += "\n\n On défini ensuite i3 : \n\n"
    for i, i3 in dicoI3.items():
        s += "Segment {} :  \n".format(i)
        s += "On converti i = {} en base 3 : {} puis on le fait préceder d'assez de 0 pour que sa longueur soit 12 : {}\n\n".format(i, convert(i, 3), i3)

    s += "\n\nOn va ensuite calculer P à partir de ID et i3 :\n\n"
    for i, i3 in dicoI3.items():
        s += "Segment {} :   ID : {}, i3 : {}\n".format(i, ID, i3)
        s += "P est égal à {} + {} + {} + {} + {} + {} + {} modulo 3 = {} \n\n".format(ID[0] , i3[0] ,i3[2], i3[4],i3[6], i3[8], i3[10], dicoP[i])

    s += "\n Et enfin, on forme IX : \n"
    for i, IX in dicoIX_dna.items():
        s += "IX = {} {} {}. Transforme en ADN en prenant en compte le dernier nucléotide du segment, IX nous donne : {} de longueur 15 \n\n".format(ID, dicoI3[i], dicoP[i], "".join(IX))

    s += "On ajoute cela au segment : \n\n"
    for i, segment in dicoReverse.items():
        s += "Segment {} : \n {} {}\n\n".format(i, segment, "".join(dicoIX_dna[i]))

    s += "On ajoute deux nucléotides aux extremités ce qui forme un segment de 117 nt : \n\n"
    for i, segment in dicoFinal.items():
        s += "Segment {} :  {} {} {}\n \n".format(i, segment[0], "".join(segment[1:-1]), segment[-1])
    return s


