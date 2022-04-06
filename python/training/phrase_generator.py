from random import randint
from random import shuffle
from rich import print as rprint


def generator():

    word_numbers = randint(1, 10)

    words = input("Entrez {} mots : \n".format(word_numbers)).split()

    num_check = len(words)

    if num_check == word_numbers:
        rprint("[green bold]Bon nombre de mots")
        shuffle(words)
        print(words)
    elif num_check > word_numbers:
        rprint("[red bold]Trop de mots\n {} > {}".format(
            num_check, word_numbers))
    elif num_check < word_numbers:
        rprint("[blue bold]Pas assez de mots\n {} < {}".format(
            num_check, word_numbers))


if __name__ == '__main__':
    generator()
