import random
# import player     looks like not needed for now

'''
Intial stat guide
fighter:        attack:     best    90 - 100
                stamina:    best    90 - 100
                magic:      low     40 - 50

swordsman:      attack:     best    90 - 100
                stamina:    mid     70 - 80
                magic:      mid     70 - 80

mage:           attack:     best    90 - 100
                stamina:    low     40 - 50
                magic:      best    90 - 100

healer:         attack:     mid     70 - 80
                stamina:    best    90 - 100
                magic:      mid     70 - 80
'''

pl_health = ''


def player_fighter(pl_health):
    print('Player Stat: Fighter')
    pl_health = 100
    print('Health:  ' + str(pl_health))
    pl_attack = random.randint(90, 100)
    print('Attack:  ' + str(pl_attack))
    pl_stamina = random.randint(90, 100)
    print('Stamina: ' + str(pl_stamina))
    pl_magic = random.randint(40, 50)
    print('Magic:   ' + str(pl_magic))
    print('')
    return pl_health, pl_attack, pl_stamina, pl_magic


def player_swordsman():
    print('Player Stat: Swordsman')
    pl_health = 100
    print('Health:  ' + str(pl_health))
    pl_attack = random.randint(90, 100)
    print('Attack:  ' + str(pl_attack))
    pl_stamina = random.randint(70, 80)
    print('Stamina: ' + str(pl_stamina))
    pl_magic = random.randint(70, 80)
    print('Magic:   ' + str(pl_magic))
    print('')
    return pl_health, pl_attack, pl_stamina, pl_magic


def player_mage():
    print('Player Stat: Mage')
    pl_health = 100
    print('Health:  ' + str(pl_health))
    pl_attack = random.randint(90, 100)
    print('Attack:  ' + str(pl_attack))
    pl_stamina = random.randint(40, 50)
    print('Stamina: ' + str(pl_stamina))
    pl_magic = random.randint(90, 100)
    print('Magic:   ' + str(pl_magic))
    print('')
    return pl_health, pl_attack, pl_stamina, pl_magic


def player_healer():
    print('Player Stat: Healer')
    pl_health = 100
    print('Health: ' + str(pl_health))
    pl_attack = random.randint(70, 80)
    print('Attack: ' + str(pl_attack))
    pl_stamina = random.randint(90, 100)
    print('Stamina: ' + str(pl_stamina))
    pl_magic = random.randint(70, 80)
    print('Magic: ' + str(pl_magic))
    print('')
    return pl_health, pl_attack, pl_stamina, pl_magic


# looks like not needed
'''
def main():
    # global pl_health
    # global pl_attack
    # global pl_stamina
    # global pl_magic
    player_stat = player.pl_stat()
    if player_stat == 'fighter':
        return player_fighter
    elif player_stat == 'swordsman':
        return player_swordsman
    elif player_stat == 'mage':
        return player_mage
    elif player_stat == 'healer':
        return player_healer
    else:
        print('Please enter as specified!\n')
        main()
'''
