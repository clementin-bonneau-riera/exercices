# res https://youtu.be/_AgUOsvMt8s

# --- exemple 1 ---

wallet = int(300)
computer_price = int(500)


def exemple_1():

    global wallet
    computer_price

    print(computer_price < 1000)  # renvoie si la condition est True ou False

    # vérifie une condition (d'autres opérateurs possibles : != ; <= ; >= ; == , etc.)
    if computer_price < 1000:
        # action effectuée si la première condition est remplie
        print("Prix de l'ordinateur ({}€) est inferieur à 1000€".format(computer_price))
    else:  # si la condition n'est pas remplie...
        print("Le prix de l'ordinateur ({}€) est supérieur à 1000€".format(
            computer_price))  # ... effectuer cette action


# --- exemple 2 ---

def exemple_2():

    global wallet
    computer_price

    if computer_price <= wallet:
        print("Achat possible")
        wallet -= computer_price
        print("Votre solde actuelle : {}€".format(wallet))
    else:
        dif = computer_price - wallet
        print("Achat impossible. Il manque {}€".format(dif))


# --- exemple 3 ---

def exemple_3():

    global wallet
    computer_price

    if computer_price <= wallet or computer_price > 450:  # vérifie plusieurs conditions. or => si la première n'est pas vérifiée mais la seconde oui, la condition est valide. "and" aussi possible, nécéssite que les 2 conditions soient vérif
        print("Achat raisonnable. Votre solde est de {}€".format(wallet))
    else:
        print("Pas d'achat.")


# --- exemple 4 --- conditions ternaires


def exemple_4():

    value_1 = int(30)
    value_2 = int(20)

    # renvoie une valeur en fonction de la condition à la fin de la syntaxe. la première valeur est celle renvoyée si la condition est vérifiée, la seconde est le else
    condition_tertiaire = ("Value 1 < Value 2", "Value 1 > Value 2")[
        value_1 > value_2]
    print("Value 1 = {}\nValue 2 = {}\n{}".format(
        value_1, value_2, condition_tertiaire))


# --- exemple 5 ---


def exemple_5():

    password = input("Mot de passe : ")
    password_lengt = len(password)

    if password_lengt <= 8:
        print("Mot de passe trop court : {} caractères".format(password_lengt))
    elif password_lengt > 8 and password_lengt < 12:  # condition intermédiaire à vérifier avant de passer au sinon
        print("Mot de passe moyen :  {} caractères".format(password_lengt))
    else:
        print("Mot de passe valide : {} caractères".format(password_lengt))


# --- exo ---


def exercice():

    # place de cinéma
    # récolter l'âge du client (en console)
    # si la personne est mineure -> 7€
    # si la personne est majeure -> 12€
    # demander si le client veut du pop corn
    # si oui, ajouter 5€ au prix à payer
    # afficher prix à payer

    age = int(input("ÂGE : "))
    price = 0
    
    if age < 18:
        price += 7
    elif age >= 18:
        price += 12

    popcorn_choice = input("Voulez vous du pop corn ? (yes/no) ")

    if popcorn_choice == "yes":
        price +=5

    print("prix : {}".format(price))


# --- exec --


if __name__ == '__main__':
    exercice()
