import time

def decoder(valeur, fichier_save):
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
    s_dna_final = decode(s_dna_final, valeur, fichier_save)
    
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
        if trit=="222110": #Si on trouve une correspondance, on ajoute l'octet correspondant à s_bytes, puis on supprime de la liste de trit les trits correspondants.
            s_bytes.append(7)
            index+=6
        elif trit=="222122":
            s_bytes.append(11)
            index+=6
        elif trit=="222202":
            s_bytes.append(29)
            index+=6
        elif trit=="222102":
            s_bytes.append(30)
            index+=6
        elif trit=="222112":
            s_bytes.append(55)
            index+=6
        elif trit=="222021":
            s_bytes.append(59)
            index+=6
        elif trit=="222200":
            s_bytes.append(61)
            index+=6
        elif trit=="222120":
            s_bytes.append(62)
            index+=6
        elif trit=="222212":
            s_bytes.append(71)
            index+=6
        elif trit=="222211":
            s_bytes.append(94)
            index+=6
        elif trit=="222111":
            s_bytes.append(121)
            index+=6
        elif trit=="222220":
            s_bytes.append(122)
            index+=6
        elif trit=="222222":
            s_bytes.append(124)
            index+=6
        elif trit=="222221":
            s_bytes.append(152)
            index+=6
        elif trit=="222100":
            s_bytes.append(189)
            index+=6
        elif trit=="222201":
            s_bytes.append(199)
            index+=6
        elif trit=="222210":
            s_bytes.append(220)
            index+=6
        elif trit=="222121":
            s_bytes.append(228)
            index+=6
        elif trit=="222101":
            s_bytes.append(232)
            index+=6
        elif trit=="222022":
            s_bytes.append(236)
            index+=6
        else:
            trit = trit="".join(s_trit[index:index+5]) #Si on ne trouve pas de correspondance avec les 6 premier trits, on cherche avec les 5 premier.
            if trit == "22201":
                s_bytes.append(0)
                index+=5
            elif trit == "00100":
                s_bytes.append(1)
                index+=5
            elif trit == "11220":      
                s_bytes.append(2)
                index+=5
            elif trit == "00211":
                s_bytes.append(3)
                index+=5
            elif trit == "20222":
                s_bytes.append(4)
                index+=5
            elif trit == "00222":
                s_bytes.append(5)
                index+=5
            elif trit == "02211":
                s_bytes.append(6)
                index+=5
            elif trit == "22002":
                s_bytes.append(8)
                index+=5
            elif trit == "02100":
                s_bytes.append(9)
                index+=5
            elif trit == "22001":
                s_bytes.append(10)
                index+=5
            elif trit == "12001":
                s_bytes.append(12)
                index+=5
            elif trit == "02021":
                s_bytes.append(13)
                index+=5
            elif trit == "10100":
                s_bytes.append(14)
                index+=5
            elif trit == "02010":
                s_bytes.append(15)
                index+=5
            elif trit == "20101":
                s_bytes.append(16)
                index+=5
            elif trit == "12211":
                s_bytes.append(17)
                index+=5
            elif trit == "12120":
                s_bytes.append(18)
                index+=5
            elif trit == "11111":
                s_bytes.append(19)
                index+=5
            elif trit == "21211":
                s_bytes.append(20)
                index+=5
            elif trit == "21221":
                s_bytes.append(21)
                index+=5
            elif trit == "20220":
                s_bytes.append(22)
                index+=5
            elif trit == "00122":
                s_bytes.append(23)
                index+=5
            elif trit == "20022":
                s_bytes.append(24)
                index+=5
            elif trit == "12121":
                s_bytes.append(25)
                index+=5
            elif trit == "21111":
                s_bytes.append(26)
                index+=5
            elif trit == "00221":
                s_bytes.append(27)
                index+=5
            elif trit == "00202":
                s_bytes.append(28)
                index+=5
            elif trit == "00010":
                s_bytes.append(31)
                index+=5
            elif trit == "02212":
                s_bytes.append(32)
                index+=5
            elif trit == "10011":
                s_bytes.append(33)
                index+=5
            elif trit == "22011":
                s_bytes.append(34)
                index+=5
            elif trit == "02221":
                s_bytes.append(35)
                index+=5
            elif trit == "21212":
                s_bytes.append(36)
                index+=5
            elif trit == "21021":
                s_bytes.append(37)
                index+=5
            elif trit == "11211":
                s_bytes.append(38)
                index+=5
            elif trit == "10111":
                s_bytes.append(39)
                index+=5
            elif trit == "12220":	
                s_bytes.append(40)
                index+=5
            elif trit == "22110":
                s_bytes.append(41)
                index+=5
            elif trit == "22101":    
                s_bytes.append(42)
                index+=5
            elif trit == "11122":
                s_bytes.append(43)
                index+=5
            elif trit == "22022":    
                s_bytes.append(44)
                index+=5
            elif trit == "01210":    
                s_bytes.append(45)
                index+=5
            elif trit == "00210":    
                s_bytes.append(46)
                index+=5
            elif trit == "02122":    
                s_bytes.append(47)
                index+=5
            elif trit == "10122":    
                s_bytes.append(48)
                index+=5
            elif trit == "01011":    
                s_bytes.append(49)
                index+=5
            elif trit == "11101":    
                s_bytes.append(50)
                index+=5
            elif trit == "01102":    
                s_bytes.append(51)
                index+=5
            elif trit == "22112":    
                s_bytes.append(52)
                index+=5
            elif trit == "12122":    
                s_bytes.append(53)
                index+=5
            elif trit == "11012":    
                s_bytes.append(54)
                index+=5
            elif trit == "02201":    
                s_bytes.append(56)
                index+=5
            elif trit == "02011":    
                s_bytes.append(57)
                index+=5
            elif trit == "20021":    
                s_bytes.append(58)
                index+=5
            elif trit == "00022":    
                s_bytes.append(60)
                index+=5
            elif trit == "21010":    
                s_bytes.append(63)
                index+=5
            elif trit == "00121":    
                s_bytes.append(64)
                index+=5
            elif trit == "02022":    
                s_bytes.append(65)
                index+=5
            elif trit == "20100":    
                s_bytes.append(66)
                index+=5
            elif trit == "10211":    
                s_bytes.append(67)
                index+=5
            elif trit == "21001":
                s_bytes.append(68)
                index+=5
            elif trit == "21210":    
                s_bytes.append(69)
                index+=5
            elif trit == "10212":    
                s_bytes.append(70)
                index+=5
            elif trit == "20110":    
                s_bytes.append(72)
                index+=5
            elif trit == "20010":
                s_bytes.append(73)
                index+=5
            elif trit == "21220":    
                s_bytes.append(74)
                index+=5
            elif trit == "21022":    
                s_bytes.append(75)
                index+=5
            elif trit == "21000":    
                s_bytes.append(76)
                index+=5
            elif trit == "01211":    
                s_bytes.append(77)
                index+=5
            elif trit == "10220":    
                s_bytes.append(78)
                index+=5
            elif trit == "12002":    
                s_bytes.append(79)
                index+=5
            elif trit == "12011":    
                s_bytes.append(80)
                index+=5
            elif trit == "11212":    
                s_bytes.append(81)
                index+=5
            elif trit == "21100":    
                s_bytes.append(82)
                index+=5
            elif trit == "12210":    
                s_bytes.append(83)
                index+=5
            elif trit == "20112":
                s_bytes.append(84)
                index+=5
            elif trit == "22200":
                s_bytes.append(85)
                index+=5
            elif trit == "22102":    
                s_bytes.append(86)
                index+=5
            elif trit == "21222":    
                s_bytes.append(87)
                index+=5
            elif trit == "21012":    
                s_bytes.append(88)
                index+=5
            elif trit == "12101":    
                s_bytes.append(89)
                index+=5
            elif trit == "10120":    
                s_bytes.append(90)
                index+=5
            elif trit == "01202":    
                s_bytes.append(91)
                index+=5
            elif trit == "10200": 
                s_bytes.append(92)
                index+=5
            elif trit == "02210":    
                s_bytes.append(93)
                index+=5
            elif trit == "11201":    
                s_bytes.append(95)
                index+=5
            elif trit == "00102":    
                s_bytes.append(96)
                index+=5
            elif trit == "01112":    
                s_bytes.append(97)
                index+=5
            elif trit == "22010":    
                s_bytes.append(98)
                index+=5
            elif trit == "00012":    
                s_bytes.append(99)
                index+=5
            elif trit == "22100":    
                s_bytes.append(100)
                index+=5                
            elif trit == "20001":    
                s_bytes.append(101)
                index+=5
            elif trit == "20202":    
                s_bytes.append(102)
                index+=5
            elif trit == "02102":    
                s_bytes.append(103)
                index+=5
            elif trit == "20200":    
                s_bytes.append(104)
                index+=5
            elif trit == "20210":    
                s_bytes.append(105)
                index+=5
            elif trit == "20012":    
                s_bytes.append(106)
                index+=5
            elif trit == "11100":    
                s_bytes.append(107)
                index+=5
            elif trit == "02101":    
                s_bytes.append(108)
                index+=5
            elif trit == "11021":    
                s_bytes.append(109)
                index+=5
            elif trit == "00021":    
                s_bytes.append(110)
                index+=5
            elif trit == "02110":    
                s_bytes.append(111)
                index+=5
            elif trit == "12102":    
                s_bytes.append(112)
                index+=5
            elif trit == "01012":    
                s_bytes.append(113)
                index+=5
            elif trit == "10101":   
                s_bytes.append(114)
                index+=5
            elif trit == "10222":    
                s_bytes.append(115)
                index+=5
            elif trit == "10221":    
                s_bytes.append(116)
                index+=5
            elif trit == "10002":    
                s_bytes.append(117)
                index+=5
            elif trit == "01120":    
                s_bytes.append(118)
                index+=5
            elif trit == "00201":    
                s_bytes.append(119)
                index+=5
            elif trit == "10020":    
                s_bytes.append(120)
                index+=5
            elif trit == "02111":    
                s_bytes.append(123)
                index+=5
            elif trit == "00000":    
                s_bytes.append(125)
                index+=5
            elif trit == "10112":    
                s_bytes.append(126)
                index+=5
            elif trit == "22121":    
                s_bytes.append(127)
                index+=5
            elif trit == "02000":    
                s_bytes.append(128)
                index+=5
            elif trit == "10000":    
                s_bytes.append(129)
                index+=5
            elif trit == "20111":    
                s_bytes.append(130)
                index+=5
            elif trit == "00212":    
                s_bytes.append(131)
                index+=5
            elif trit == "22021":    
                s_bytes.append(132)
                index+=5
            elif trit == "21112":    
                s_bytes.append(133)
                index+=5
            elif trit == "11022":    
                s_bytes.append(134)
                index+=5
            elif trit == "01220":    
                s_bytes.append(135)
                index+=5
            elif trit == "11102":    
                s_bytes.append(136)
                index+=5
            elif trit == "20011":    
                s_bytes.append(137)
                index+=5
            elif trit == "22111":    
                s_bytes.append(138)
                index+=5
            elif trit == "10021":    
                s_bytes.append(139)
                index+=5
            elif trit == "12212":    
                s_bytes.append(140)
                index+=5
            elif trit == "11202":    
                s_bytes.append(141)
                index+=5
            elif trit == "10201":    
                s_bytes.append(142)
                index+=5
            elif trit == "02200":    
                s_bytes.append(143)
                index+=5
            elif trit == "02002":    
                s_bytes.append(144)
                index+=5
            elif trit == "11120":    
                s_bytes.append(145)
                index+=5
            elif trit == "20102":    
                s_bytes.append(146)
                index+=5
            elif trit == "11110":    
                s_bytes.append(147)
                index+=5
            elif trit == "11002":    
                s_bytes.append(148)
                index+=5
            elif trit == "22000":    
                s_bytes.append(149)
                index+=5
            elif trit == "21002":    
                s_bytes.append(150)
                index+=5
            elif trit == "21102":    
                s_bytes.append(151)
                index+=5
            elif trit == "11020":    
                s_bytes.append(153)
                index+=5
            elif trit == "20221":    
                s_bytes.append(154)
                index+=5
            elif trit == "01002":    
                s_bytes.append(155)
                index+=5
            elif trit == "11001":    
                s_bytes.append(156)
                index+=5
            elif trit == "00120":    
                s_bytes.append(157)
                index+=5
            elif trit == "02202":    
                s_bytes.append(158)
                index+=5
            elif trit == "10202":    
                s_bytes.append(159)
                index+=5
            elif trit == "10012":    
                s_bytes.append(160)
                index+=5
            elif trit == "22012":    
                s_bytes.append(161)
                index+=5
            elif trit == "20211":    
                s_bytes.append(162)
                index+=5
            elif trit == "21201":    
                s_bytes.append(163)
                index+=5
            elif trit == "00220":    
                s_bytes.append(164)
                index+=5
            elif trit == "11222":    
                s_bytes.append(165)
                index+=5
            elif trit == "21011":    
                s_bytes.append(166)
                index+=5
            elif trit == "10110":
                s_bytes.append(167)
                index+=5
            elif trit == "20002":
                s_bytes.append(168)
                index+=5
            elif trit == "20122":
                s_bytes.append(169)
                index+=5
            elif trit == "22122":
                s_bytes.append(170)
                index+=5
            elif trit == "20201":
                s_bytes.append(171)
                index+=5
            elif trit == "10022":
                s_bytes.append(172)
                index+=5
            elif trit == "21101":
                s_bytes.append(173)
                index+=5
            elif trit == "12110":
                s_bytes.append(174)
                index+=5
            elif trit == "12222":
                s_bytes.append(175)
                index+=5
            elif trit == "00200":
                s_bytes.append(176)
                index+=5
            elif trit == "21202":
                s_bytes.append(177)
                index+=5
            elif trit == "10210":
                s_bytes.append(178)
                index+=5
            elif trit == "10010":
                s_bytes.append(179)
                index+=5
            elif trit == "02012":
                s_bytes.append(180)
                index+=5
            elif trit == "12221":
                s_bytes.append(181)
                index+=5
            elif trit == "12022":
                s_bytes.append(182)
                index+=5
            elif trit == "02222":
                s_bytes.append(183)
                index+=5
            elif trit == "01100":
                s_bytes.append(184)
                index+=5
            elif trit == "02121":
                s_bytes.append(185)
                index+=5
            elif trit == "01122":
                s_bytes.append(186)
                index+=5
            elif trit == "00112":
                s_bytes.append(187)
                index+=5
            elif trit == "01020":
                s_bytes.append(188)
                index+=5
            elif trit == "01222":
                s_bytes.append(190)
                index+=5
            elif trit == "21020":
                s_bytes.append(191)
                index+=5
            elif trit == "01201":
                s_bytes.append(192)
                index+=5
            elif trit == "00001":
                s_bytes.append(193)
                index+=5
            elif trit == "12021":
                s_bytes.append(194)
                index+=5
            elif trit == "12010":
                s_bytes.append(195)
                index+=5
            elif trit == "20121":
                s_bytes.append(196)
                index+=5
            elif trit == "21120":
                s_bytes.append(197)
                index+=5
            elif trit == "00002":
                s_bytes.append(198)
                index+=5
            elif trit == "00011":
                s_bytes.append(200)
                index+=5
            elif trit == "01010":
                s_bytes.append(201)
                index+=5
            elif trit == "12112":
                s_bytes.append(202)
                index+=5
            elif trit == "11112":
                s_bytes.append(203)
                index+=5
            elif trit == "02120":
                s_bytes.append(204)
                index+=5
            elif trit == "11010":
                s_bytes.append(205)
                index+=5
            elif trit == "01110":
                s_bytes.append(206)
                index+=5
            elif trit == "01212":
                s_bytes.append(207)
                index+=5
            elif trit == "20120":
                s_bytes.append(208)
                index+=5
            elif trit == "12000":
                s_bytes.append(209)
                index+=5
            elif trit == "12100":
                s_bytes.append(210)
                index+=5
            elif trit == "11210":
                s_bytes.append(211)
                index+=5
            elif trit == "11011":
                s_bytes.append(212)
                index+=5
            elif trit == "21200":
                s_bytes.append(213)
                index+=5
            elif trit == "12200":
                s_bytes.append(214)
                index+=5
            elif trit == "01111":
                s_bytes.append(215)
                index+=5
            elif trit == "01200":
                s_bytes.append(216)
                index+=5
            elif trit == "12012":
                s_bytes.append(217)
                index+=5
            elif trit == "10121":
                s_bytes.append(218)
                index+=5
            elif trit == "10102":
                s_bytes.append(219)
                index+=5
            elif trit == "00020":
                s_bytes.append(221)
                index+=5
            elif trit == "01000":
                s_bytes.append(222)
                index+=5
            elif trit == "20020":
                s_bytes.append(223)
                index+=5
            elif trit == "11121":
                s_bytes.append(224)
                index+=5
            elif trit == "10001":
                s_bytes.append(225)
                index+=5
            elif trit == "02001":
                s_bytes.append(226)
                index+=5
            elif trit == "01101":
                s_bytes.append(227)
                index+=5
            elif trit == "21121":
                s_bytes.append(229)
                index+=5
            elif trit == "02220":
                s_bytes.append(230)
                index+=5
            elif trit == "01001":
                s_bytes.append(231)
                index+=5
            elif trit == "01022":
                s_bytes.append(233)
                index+=5
            elif trit == "20212":
                s_bytes.append(234)
                index+=5
            elif trit == "00101":
                s_bytes.append(235)
                index+=5
            elif trit == "01021":
                s_bytes.append(237)
                index+=5
            elif trit == "00111":
                s_bytes.append(238)
                index+=5
            elif trit == "11200":
                s_bytes.append(239)
                index+=5
            elif trit == "12201":
                s_bytes.append(240)
                index+=5
            elif trit == "11000":
                s_bytes.append(241)
                index+=5
            elif trit == "02112":
                s_bytes.append(242)
                index+=5
            elif trit == "01221":
                s_bytes.append(243)
                index+=5
            elif trit == "00110":
                s_bytes.append(244)
                index+=5
            elif trit == "11221":
                s_bytes.append(245)
                index+=5
            elif trit == "01121":
                s_bytes.append(246)
                index+=5
            elif trit == "12111":
                s_bytes.append(247)
                index+=5
            elif trit == "12020":
                s_bytes.append(248)
                index+=5
            elif trit == "02020":
                s_bytes.append(249)
                index+=5
            elif trit == "22020":
                s_bytes.append(250)
                index+=5
            elif trit == "20000":
                s_bytes.append(251)
                index+=5
            elif trit == "21110":
                s_bytes.append(252)
                index+=5
            elif trit == "22120":
                s_bytes.append(253)
                index+=5
            elif trit == "12202":
                s_bytes.append(254)
                index+=5
            elif trit == "21122":
                s_bytes.append(255)
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
        elif pre_nt == c:
            if nt == g:
                s_trit.append("0")
            elif nt == t:
                s_trit.append("1")
            elif nt == a:
                s_trit.append("2")
        elif pre_nt == g:
            if nt == t:
                s_trit.append("0")
            elif nt == a:
                s_trit.append("1")
            elif nt == c:
                s_trit.append("2")
        elif pre_nt == t:
            if nt == a:
                s_trit.append("0")
            elif nt == c:
                s_trit.append("1")
            elif nt == g:
                s_trit.append("2")

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

          
def decode(s_dna, fichier, fichier_save):
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


    for segment in segments.values(): #On va traiter chaque segment séparément
        
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
        P = int(ID[0]) + int(i3[0]) + int(i3[2]) + int(i3[4]) + int(i3[6]) + int(i3[8]) + int(i3[10])
        while P != 0 or P != 1 or P != 2:
            if P <0:
                P+=3
            elif P>2:
                P-=3
            else:
                break
        if P!=p:
            print("Erreur P")

            
        i = int("".join(str(v) for v in i3), 3) #On calcule i à partir de i3 et on vérifie qu'il est égale à la clé du segment ( pas obligatoire, juste pour mon programme).

        #On regarde si i est impair, et si oui, on l'inverse et complemente
        if i%2!=0:
            segment=reverseDna(segment)
            
        dicoFinal[i] = "".join(segment) #On ajoute le segment a un dctionnaire avec comme clé i. 

        

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
            dicoSegment[i+3]= [segment[75:]]
            
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

if __name__ == '__main__':
    decoder("image.jpg.dna", "")
