# https://youtu.be/kyxF5eH3Kic

members = ["Thom", "Jonny", "Colin", " Ed", "Phil"]  # définition de la liste

print(members)
print(members[0])  # affiche le premier élement de la liste (commence à 0)
# affiche le dernier élement de la liste (nombre d'éléments -1 vu que ça commence à 0)
print(members[len(members)-1])

members[0] = "Thom Yorke"  # réaffectation de la première valeur de la liste
members.insert(5, "Nigel")  # insère à la position x la valeur object
members.insert(6, "Stanley")
print(members[0])
print(members)
