# turn function for counting encounter

import player_attribute


def turn_counter():
    count = 100
    while count != 0:
        print('Count: ' + str(count))
        count -= 1


pl_health = ''
turn_counter()
print(player_attribute.player_fighter(pl_health))
health = player_attribute.player_fighter(pl_health)
print(health)
# def dec_health():
