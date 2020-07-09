# print('hello world!')

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def display(playername, hpoint):
#     print(playername + " " + str(hpoint) + " left")

# playername = input("playername ")

# hpoint = 100

# display(playername, hpoint)

import player

playern = input(str("Enter player name: "))

if (len(playern) < 3):
    print("Name invalid, enter 3 or more letter")
else:
    player.player(playern)

# temp
print("Simple RPG")
print("Player name: " + playern)
print("Attribute: ")
print("Health:  " + ("#" * 1))
print("Magic:   " + ("#" * 10))
print("Stamina: " + ("#" * 10))

