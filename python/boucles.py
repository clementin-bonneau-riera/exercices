# res https://youtu.be/BrknhzrHm8w

from random import randint


# --- exemple 1 ---


def number():
    # créé une variable puis va effecue la boucle entre les deux valeurs annoncées.
    for position in range(1, 11):  # la dernière valeur est exclue
        print("Vous êtes le numéro", position)


# --- exemple 2 ---


blacklist = ["topsecret@gouv.fr", "manumacron@gmail.com"]
crash = "vladimirpoutine@gouv.ru"


def emails_example():
    emails = input("Entrez vos emails, séparés par / : ").split("/")
    # emails = ["bonjour@gmail.com", "bonsoir@gmail.com", "aurevoir@gmail.com"]
    for email in emails:  # pour chaque élément x dans la liste X

        if email in blacklist:  # regarde si l'élement est présent dans la X
            print("Envoi impossible à {}".format(email))
            continue  # passe au tour suivant

        if email in crash:  # regarde si l'élement est présent dans la X
            print("{} a fait planter le système. Reboot.".format(email))
            break  # fait cesser la bouclee de fonctionner. arrête tout même s'il reste des valeurs après

        print("Email envoyé à {}".format(email))


# --- exemple 3 ---


def stonks():
    salaire = int(input("Votre salaire : "))

    while salaire < 2000:  # tant que X est < à Y
        salaire += 120  # pareil que salaire = salaire + 120
        print("Salaire mensuel brut : {}€".format(salaire))


# --- exemple 4 ---


# nombre d'abonnés de base
suscribers_count = 2500

# il gagne 10% d'abonnés par moi
months = 0


def stonks_2():

    # rend les variables déf en dehors de la fonction utilisable à l'interieur
    global suscribers_count
    global months

    # au bout de 2 ans, combien d'abonnés ?
    while months <= 24:
        print("MOIS : {} \nABONNÉS : {}".format(months, suscribers_count))
        suscribers_count = suscribers_count * 1.1  # augmente l'audience
        months += 1


# --- TP ---


"""
consignes : Jeu du Juste Prix
- choisir un nombre entre 1 et 100
- tant que le jeu n'est pas fini:
    -> demander à l'utilisateur d'entrer un prix
    -> s'il trouve le prix, c'est gagné
    -> sinon donner des indications (+ ou -)

"""


def juste_prix():

    number = randint(1, 100)

    running = True

    while running:
        guess = int(input("Nombre entre 1 et 100 : "))

        if guess < number:  # possibilité d'utilser des elif
            print("c'est plus")

        if guess > number:
            print("c'est moins")

        if guess == number:
            print("c'est gagné")
            running = False  # break marche aussi mais là ça utilise running = True


# --- exec ---

if __name__ == '__main__':
    juste_prix()
