import player
import player_attribute
import turn


def main():
    # correct way to call return
    pl_name = player.player_name()
    pl_stat = player.player_job()
    pl_attr = ''

    print('\nNATURPG GAMES\n')
    print('Player name is ' + pl_name)
    print('Player job is ' + pl_stat + '\n')
    if pl_stat == 'fighter':
        pl_attr = player_attribute.player_fighter()
    elif pl_stat == 'swordsman':
        pl_attr = player_attribute.player_swordsman()
    elif pl_stat == 'mage':
        pl_attr = player_attribute.player_mage()
    elif pl_stat == 'healer':
        pl_attr = player_attribute.player_healer()
    else:
        print('Please enter as specified!\n')
        main()


if __name__ == "__main__":
    main()
