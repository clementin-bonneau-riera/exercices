# res https://youtu.be/_AgUOsvMt8s

# --- exemple 1 ---

wallet = 200
computer_price = 999.99


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


# --- exec --

if __name__ == '__main__':
    exemple_3()
