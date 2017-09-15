# coding: utf-8


# file1 = input("Fichier 1 : ")
# file2 = input("Fichier 2 : ")

file1 = "image_dna_decoded_normal.jpg"
file2 = "image_dna_decoded.jpg"

with open(file1, "r", encoding='latin-1') as ouverture:
    s1 = ouverture.read()

with open(file2, "r", encoding="latin-1") as ouverture:
    s2 = ouverture.read()

nbErreur = 0

for index, char in enumerate(s1, start=0):
    if char != s2[index]:
        nbErreur+=1
        print("erreur à : ", index)
print(nbErreur/len(s1), "% d'erreurs")