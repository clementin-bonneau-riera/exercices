"""
ask name to the user and print it
and ask it age
if age > 18 print "you can drink alcohol"
print if the user can drink alcohol
"""


name = input("What is your name? ")
age = int(input("How old are you? "))
print("Hello " + name)
if age > 18:
    print("You can drink alcohol")
else:
    print("You can't drink alcohol")