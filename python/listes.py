# res https://youtu.be/kyxF5eH3Kic

from statistics import mean
from random import shuffle


def list():

    members = ["Thom", "Jonny", "Colin", " Ed",
               "Phil"]  # définition de la liste

    # réaffecter des valeurs et en ajouter

    print(members)
    print(members[0])  # affiche le premier élement de la liste (commence à 0)
    # affiche le dernier élement de la liste (nombre d'éléments -1 vu que ça commence à 0)
    print(members[len(members)-1])

    # réaffectation de la première valeur de la liste
    members[0] = "Thom Yorke"
    members.insert(5, "Nigel")  # insère à la position x la valeur object
    members.insert(6, "Stanley")
    print(members[0])
    print(members)

    # ajoute un nouvel élement à la fin de la liste
    members.append("a surprise")
    # ajoute plusieurs élements à la fin de la liste
    members.extend(["The Karma", "The Police"])
    print(members)

    # supprimer des valeurs

    del members[7]  # supprime la valeur [x] de la liste
    print(members)

    members.pop(8)  # supprime la valeur (x) de la liste
    print(members)

    # supprime un élément de la liste à partir de son nom
    members.remove("The Karma")
    print(members)

    members.clear()  # vide la liste en entier
    print(members)


def exemple():
    notes = [20, 13, 12,
             14, 17, 7,
             9, 18, 15,
             11,
             ]
    print(notes)
    results = mean(notes)  # moyenne de la liste de notes
    shuffle(notes)  # met dans un ordre aléatoire les éléments de la liste
    print(notes)
    # .format convertit tout seul en string
    print("Moyenne de {} /20".format(results))


def exemple_2():
    # découpe une chaîne de caractères en éléments de liste à partir d'un caractère définia
    text = input("Entrer votre (nom|prenom|annee de naissance): ").split("|")
    print("Prénom : {} \n Nom : {} \n Année de naissance : {}".format(
        text[1], text[0], text[2]))


"""
générateur de phrases
demander une chaîne de mots de la forme mot1/mot2/mot3
transformer cette chaîne en liste
la mélanger
si le nombre d'élements de la liste < 10
    -> afficher les 2 premiers mots
si le nombre d'élements de la liste >= 10
    -> afficher les 3 derniers éléments de la liste
"""


def generateur():
    mots = input("liste de mots sous la forme mot1/mot2/mot3 : ").split("/")
    shuffle(mots)
    len_mots = len(mots)
    print(len_mots)
    if len_mots < 10:
        print(mots[0:1])
    else:
        print(mots[])


# list()
# exemple()
# exemple_2()
# generateur()

if __name__ == '__main__':
    generateur()
