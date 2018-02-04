from tkinter import *
from encode import encoder
from decode import decoder


#import en supplement du module filedialog de tkinter:
from tkinter.filedialog import askopenfilename,askdirectory

#import du module os qui permet d'avoir des commandes Unix dans python
import os

#repertoire courant dans une chaine de caractere
#cela permet d'exporter le programme sur d'autres ordinateurs sans
#changer les chemin dans le programme
chemin  = os.getcwd()   #Current Working Directory



class ValidatingEntry(Entry):
    # base class for validating entry widgets

    def __init__(self, master, value="", **kw):
        Entry.__init__(self, master, **kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(value)
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)

    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(self.newvalue)
        else:
            self.__value = value

    def validate(self, value):
        # override: return value, new value, or None if invalid
        return value

class MaxLengthEntry(ValidatingEntry):
    def __init__(self, master, value, maxlength, **kw):
        self.maxlength = maxlength
        ValidatingEntry.__init__(self, master, **kw)

    def validate(self, value):
        if len(value) <= self.maxlength:
            return value
        return None # new value too long

        


fenetre = Tk()
fenetre.title("Le stockage de l'information dans l'ADN")




def fichier_encodage():
    if var_mode.get()=="decode":
        entre_fichier = askopenfilename(multiple=False,filetypes=[("Fichier ADN", ".dna")], title="Sélectionnez le fichier .dna que vous voulez decoder")
    else:
        entre_fichier = askopenfilename(multiple=False, title="Sélectionnez le fichier que vous voulez encodez en ADN")
    entre_file.set(entre_fichier)


def fichier_decodage():
    sortie_file = askdirectory(title="Sélectionnez le dossier où les fichiers .dna vont être enregistrer")
    var_save.set(sortie_file)


def decodage():
    toutForget()

    var_fichier_texte.set("Sélectionnez le fichier .dna que vous voulez décodez :")
    var_button_save.set("Sélectionnez le dossier où le fichier va être enregistrer")
    
    label_file.pack()
    button_fichier.pack()
    label_fichier.pack()    

    label_choix.pack()
    choix_fichier.pack()
    choix_texte.pack()
    choix_texte.select()
    label_choix.config(state=DISABLED)
    choix_fichier.config(state=DISABLED)
    choix_texte.config(state=DISABLED)

    label_mode.pack()
    mode_encodage.pack()
    mode_decodage.select()
    mode_decodage.pack()
    correc_erreur.pack()


    mode_demo.pack()
    button_save.pack()
    label_save.pack()

    
    ecart.pack()
    var_start.set("Lancer le décodage du fichier .dna")
    bouton_start.pack()

def encodage():
    toutForget()
    var_fichier_texte.set("Sélectionnez le fichier que vous voulez encodez en ADN :")
    var_button_save.set("Sélectionnez le dossier où le fichier .dna va être enregistrer")
    
    label_texte.pack()
    entre_texte.pack()

    label_choix.pack()
    choix_fichier.pack()
    choix_texte.pack()
    choix_texte.select()
    
    label_choix.config(state=NORMAL)
    choix_fichier.config(state=NORMAL)
    choix_texte.config(state=NORMAL)
    
    label_mode.pack()
    mode_encodage.pack()
    mode_encodage.select()
    mode_decodage.pack()
    
    mode_demo.pack()
    button_save.pack()
    label_save.pack()

    ecart.pack()
    var_start.set("Lancer l'encodage en ADN")
    bouton_start.pack()

def modeDemonstration():
    toutForget()
    if var_demo.get()==0:
        var_texte_texte.set("Entrez le texte que vous voulez encoder en ADN (minimum 11 caractères) :")
        if var_choix.get()=="fichier":
            label_file.pack()
            button_fichier.pack()
            label_fichier.pack()
            
        elif var_choix.get()=="texte":
            label_texte.pack()
            entre_texte.pack()
            choix_texte.select()

        label_choix.pack()
        choix_fichier.pack()
        choix_texte.pack()
        
        if var_choix.get()=="texte":
            choix_texte.select()
        elif var_choix.get()=="fichier":
            choix_fichier.select()
        else:
            print("ERREUR")
        label_mode.pack()
        mode_encodage.pack()
        mode_encodage.select()
        mode_decodage.pack()

        label_choix.config(state=NORMAL)
        choix_fichier.config(state=NORMAL)
        choix_texte.config(state=NORMAL)

        label_mode.config(state=NORMAL)
        mode_encodage.config(state=NORMAL)
        mode_decodage.config(state=NORMAL)
        
        mode_demo.pack()
        button_save.pack()
        label_save.pack()

        ecart.pack()
        var_start.set("Lancer l'encodage en ADN")
        bouton_start.pack()
    else:
        var_texte_texte.set("Entrez le texte que vous voulez encoder pour la démonstration (entre 11 et 35 caractères) :")
        label_texte.pack()
        entre_texte_demo.pack()     
        
        label_explication_demo.pack()
        
        mode_demo.pack()
        button_save.pack()
        label_save.pack()

        ecart.pack()
        var_start.set("Lancer la démonstration d'encodage en ADN")
        bouton_start.pack()

def toutForget():
    label_texte.pack_forget()
    entre_texte.pack_forget()
    entre_texte_demo.pack_forget()
    label_file.pack_forget()
    button_fichier.pack_forget()
    label_file.pack_forget()
    button_fichier.pack_forget()
    label_fichier.pack_forget()
    label_choix.pack_forget()
    label_explication_demo.pack_forget()
    choix_fichier.pack_forget()
    choix_texte.pack_forget()
    label_mode.pack_forget()
    mode_encodage.pack_forget()
    mode_decodage.pack_forget()
    correc_erreur.pack_forget()
    mode_demo.pack_forget()
    button_save.pack_forget()
    label_save.pack_forget()
    ecart.pack_forget()
    bouton_start.pack_forget()
    
def choixFichier():
    toutForget()

    
    label_file.pack()
    button_fichier.pack()
    label_fichier.pack()

    label_choix.pack()
    choix_fichier.pack()
    choix_texte.pack()
    choix_fichier.select()

    label_mode.pack()
    mode_encodage.pack()
    mode_encodage.select()
    mode_decodage.pack()
    
    mode_demo.pack()

    button_save.pack()
    label_save.pack()

    ecart.pack()
    bouton_start.pack()
def choixTexte():

    toutForget()
    label_texte.pack()
    entre_texte.pack()

    label_choix.pack()
    choix_fichier.pack()
    choix_texte.pack()
    choix_texte.select()

    label_mode.pack()
    mode_encodage.pack()
    mode_encodage.select()
    mode_decodage.pack()

    mode_demo.pack()

    button_save.pack()
    label_save.pack()
    
    ecart.pack()
    bouton_start.pack()
    
        
def lancer():
    if var_demo.get() == 0:
        if var_mode.get()=="encode":
            if var_choix.get()=="fichier":
                valeur=entre_file.get()
            elif var_choix.get()=="texte":
                valeur=var_texte.get()
            encoder(var_choix.get(), valeur, var_save.get())
        else:
            valeur=entre_file.get()
            if var_correc.get() == 0:
                decoder(valeur, var_save.get(), True)
            else:
                print("sans correection")
                decoder(valeur, var_save.get(), False)
    else:
        valeur=entre_texte_demo.get()
        temps, s_bytes, s_trit1, len_Trit, nb0, s_trit3, s_trit4, s_dna, dicoDebut, dicoReverse, dicoI3, ID, dicoP, dicoIX, dicoIX_dna, dicoFinal, s_dna_final =encoder("texte", valeur, var_save.get())

        var_afficher = afficherEncodage(valeur, temps, s_bytes, s_trit1, len_Trit, nb0, s_trit3, s_trit4,s_dna, dicoDebut, dicoReverse, dicoI3, ID, dicoP, dicoIX,dicoIX_dna, dicoFinal, s_dna_final)
        fenetre_demo = Tk()
        fenetre_demo.title("Démonstration de l'encodage d'un texte vers de l'ADN")

        
        barre = Scrollbar(fenetre_demo)
        label_demo = Text(fenetre_demo, yscrollcommand=barre.set)
        
        barre.config(command=label_demo.yview)
        barre.pack(side="right", fill='y')
        label_demo.pack(expand=1, fill="both")
        label_demo.insert(0.0, var_afficher)
        

        




var_texte = StringVar()

var_fichier_texte=StringVar()
var_texte_texte=StringVar()
var_demo = IntVar()
var_correc = IntVar()
var_texte_demo= StringVar()
entre_file= StringVar()
var_save = StringVar()
var_mode = StringVar()
var_choix = StringVar()
var_start=StringVar()

var_button_save=StringVar()

#var_save.set("C:/Users/PC/Desktop")
#entre_file.set("C:/Users/PC/Desktop")

var_save.set(chemin)
entre_file.set(chemin)

var_start.set("Lancer l'encodage en ADN")
var_texte_texte.set("Entrez le texte que vous voulez encoder en ADN (minimum 11 caractères) :")
var_fichier_texte.set("Sélectionnez le fichier que vous voulez encodez en ADN :")
var_button_save.set("Sélectionnez le dossier où le fichier .dna va être enregistrer")

explication = "Bienvenue dans le mode démonstration ! \n Dans ce mode, vous allez pouvoir rentrez un texte, \n ayant une longueur entre 11 et 35 caractères pour \n des raisons de lisibité. Ce texte seras encoder et \n une explication de toutes les étapes seront afficher \n dans une nouvelle fenetre qui va s'ouvrir. \n Une fois que vous avez fini de lire ces explications,\nil vous suffit de fermer cette fenetre et vous pourrez\n continuer à utiliser le logiciel"
                



label_texte = Label(fenetre, textvariable=var_texte_texte)
entre_texte = Entry(fenetre, textvariable=var_texte, width=50)
label_file = Label(fenetre, textvariable=var_fichier_texte)
button_fichier = Button(fenetre, text="Sélectionner le fichier", command=fichier_encodage)
label_fichier = Label(fenetre, textvariable=entre_file)


label_choix = Label(fenetre, text="Que voulez-vous encodez en ADN ?")
choix_fichier = Radiobutton(fenetre, text="Fichier", variable=var_choix, value="fichier", command=choixFichier)
choix_texte = Radiobutton(fenetre, text="Texte", variable=var_choix, value="texte", command=choixTexte)

label_mode = Label(fenetre, text="Mode :")
mode_decodage = Radiobutton(fenetre, text="Décodage", variable=var_mode, value="decode", command=decodage)
mode_encodage = Radiobutton(fenetre, text="Encodage", variable=var_mode, value="encode", command=encodage)
correc_erreur = Checkbutton(fenetre, text="Enlever la correction d'erreur", variable = var_correc)


mode_demo = Checkbutton(fenetre, text="Mode démonstration", variable = var_demo, command=modeDemonstration)
label_explication_demo = Label(fenetre, text=explication)
entre_texte_demo = MaxLengthEntry(fenetre,"", 35, textvariable=var_texte_demo, width=50)
button_save=Button(fenetre, textvariable=var_button_save, command=fichier_decodage)
label_save= Label(fenetre, textvariable=var_save)

ecart = Frame(fenetre, width=10, height=50)
bouton_start=Button(fenetre, textvariable=var_start, width=50, height=5, command=lancer)



label_texte.pack()
entre_texte.pack()

label_choix.pack()
choix_fichier.pack()
choix_texte.pack()
choix_texte.select()

label_mode.pack()
mode_encodage.pack()
mode_encodage.select()
mode_decodage.pack()

mode_demo.pack()

button_save.pack()
label_save.pack()

ecart.pack()
bouton_start.pack()

fenetre.mainloop()



