# looks like not needed
'''
# pl_name = input("Enter player name: ")
def player(playern):
    print(playern)
'''


def player_name():
    global pl_name
    pl_name = str(input('Please enter your name: '))
    if (len(pl_name) < 3):
        print('Please enter more than 3 characters!')
        player_name()
    else:
        return pl_name
        # print('Player is : ' + pl_name)


def player_job():
    global pl_stat
    print('\nJob list:')
    print('1. Fighter')
    print('2. Swordsman')
    print('3. Mage')
    print('4. Healer')
    pl_stat = ''
    job_array = ['fighter', 'swordsman', 'mage', 'healer']
    pl_job = str(input('Please enter your job: '))
    if pl_job.lower() in ['1', '2', '3', '4', 'fighter', 'swordsman', 'mage', 'healer']:
        if pl_job.lower() in ['1', 'fighter']:
            pl_stat = job_array[0]
        elif pl_job.lower() in ['2', 'swordsman']:
            pl_stat = job_array[1]
        elif pl_job.lower() in ['3', 'mage']:
            pl_stat = job_array[2]
        elif pl_job.lower() in ['4', 'healer']:
            pl_stat = job_array[3]
        else:
            print('Please enter job as specified!')
            player_job()
    else:
        print('Please enter job as specified!')
        player_job()
    return pl_stat


# looks like not needed
'''

# Intial stat guide
# fighter:        attack:     best
#                 stamina:    best
#                 magic:      low

# swordsman:      attack:     best
#                 stamina:    mid
#                 magic:      mid

# mage:           attack:     best
#                 stamina:    low
#                 magic:      best

# healer:         attack:     mid
#                 stamina:    best
#                 magic:      mid



# def fighter_stat():
#     print('Player Stat')
#     print('Health: ')
#     print('Stamina: ')
#     print('Magic: ')


def main(pl_name, pl_stat):
    # player_name()     ->  salah
    # player_job()      ->  salah
    # print('Player name is ' + pl_name)
    # print('Player job is ' + pl_stat)
    print('Main executed')
    return pl_name, pl_stat


if __name__ == "__main__":
    pl_name = player_name()     # pemanggilan yg benar
    pl_stat = player_job()      # pemanggilan yg benar
    print('if main executed')
    main(pl_name, pl_stat)

'''
