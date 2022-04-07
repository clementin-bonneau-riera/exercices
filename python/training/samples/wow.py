"""
generate a random number between 1 and 100
ask the user for a number between 1 and 100
if the user number is greater than the random number
    print "you guessed too high"
if the user number is less than the random number
    print "you guessed too low"
if the user number is equal to the random number
    print "you guessed correctly"
do not finish the program whil the user number is not equal to the random number
"""
import random
import string

def main():
    random_number = random.randint(1, 100)
    user_number = int(input("Guess a number between 1 and 100: "))
    while user_number != random_number:
        if user_number > random_number:
            print("You guessed too high")
        else:
            print("You guessed too low")
        user_number = int(input("Guess a number between 1 and 100: "))
    print("You guessed correctly")


"""
create a function named friend
create a list of friends
ask the user for a name
if the name is in the list of friends
    print "you are a friend"
else
    print "you are not a friend"
"""

def friend():
    friends = ["Thalia", "Raph", "Alice", "Hugo", "Antho", "Gab", "Ainhoa"]
    name = input("Enter a name: ")
    if name in friends:
        print("You are a friend")
    else:
        print("You are not a friend")


"""
create a function strange_word
ask the user for a word
count number of letters in the word
replace all the letters with a random letter
print the word
"""

def strange_word():
    word = input("Enter a word: ")
    count = 0
    for letter in word:
        count += 1
    for i in range(count):
        word = word.replace(word[i], random.choice(string.ascii_letters))
    print(word)


"""
create a function "albums_rates"
ask the user for 5 albums name
rate them from 1 to 5
class the albums by rate
print the albums with their rate
"""

def albums_rates():
    albums = []
    for i in range(5):
        album = input("Enter an album: ")
        rate = int(input("Enter a rate: "))
        albums.append((album, rate))
    albums.sort(key=lambda album: album[1])
    for album in albums:
        print(album[0], album[1])
    with open("albums.txt", "w") as file:
        for album in albums:
            file.write(album[0] + " " + str(album[1]) + "\n")



"""
create a function mean
ask the user for 5 numbers
calculate the mean
print the mean
"""

def mean():
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)
    mean = sum(numbers) / len(numbers)
    print(mean)

"""
create a function names_to_txt
ask for the user 5 name
write these 5 name in a file named names.txt in the same folder
"""

def names_to_txt():
    names = []
    for i in range(5):
        name = input("Enter a name: ")
        names.append(name)
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")


"""
creer une fonction amis
creer une liste d'amis à partir des entrées de l'utilisateur
demander pour chaque ami son age
arreter quand l'utilisateur le demande
afficher les amis avec leur age et enregistrer dans un fichier
"""

def amis():
    friends = []
    for i in range(3):
        friend = input("Enter a friend: ")
        age = int(input("Enter an age: "))
        friends.append((friend, age))
    for friend in friends:
        print(friend[0], friend[1])
    with open("friends.txt", "w") as file:
        for friend in friends:
            file.write(friend[0] + " " + str(friend[1]) + "\n")



if __name__ == "__main__":
    amis()