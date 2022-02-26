#
#  PSP Assignment 2 - Provided file (part2_dunp001.py).
#
#   File:      dunap001_poker.py
#   Author:    Anthony Dunne
#   Email Id:  dunap001
#   Description:  Programming Assignment 2.
#       This is my own work as defined by the University's
#       Academic Misconduct policy.
#


import character
import random

def read_file(filename):

    # List to store information on heroes and villains
    character_list = []
    
    infile = open(filename, "r")

    index = 0

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':

        # Get name
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Get secret_identity
        secret_id = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Split line into no battles, no won, no lost, etc.
        info_list = line.split()
        is_hero = info_list[0]
        if is_hero == 'h':
            is_hero = True
        else:
            is_hero = False
        no_battles = int(info_list[1])
        no_won = int(info_list[2])
        no_lost = int(info_list[3])
        no_drawn = int(info_list[4])
        health = int(info_list[5])        
        
        # Create new Character object with character (hero and villain) info
        new_character = character.Character(name, secret_id, is_hero, no_battles, no_won,
                                              no_lost, no_drawn, health)
        
        # Add new character to character_list
        character_list.append(new_character)
        
        # Read next line of file.
        line = infile.readline()
    
    return character_list


def display_characters(character_list, display_type):
    
    hero_list = []
    villian_list = []
    
    print(51*'=')
    print('-     Character (heroes and villains) Summary     -')
    print(51*'=')
    print('-                             P  W  L  D   Health -')
    print(51*'-')

    for char in character_list:
        hero = char.get_is_hero()

        if hero == True:
            hero_list.append(char)

        else:
            villian_list.append(char)

    if display_type == 0:
        for char in character_list:
            print('- ', char, ' -')
            print(51*'-')

    elif display_type == 1:
        for char in hero_list:
            print('- ', char, ' -')
            print(51*'-')

    elif display_type == 2:
        for char in villian_list:
            print('- ', char, ' -')
            print(51*'-')

    print(51*'=')


def write_to_file(filename, character_list):

    outfile = open("new_characters.txt", "w")

    index = 0
    while index < len(character_list):
        outfile.write(character_list[index].get_name() + '\n')
        outfile.write(character_list[index].get_secret_identity() + '\n')

        true_false = character_list[index].get_is_hero()

        if true_false == True:
            outfile.write('h ')
        else:
            outfile.write('v ')

        outfile.write(str(character_list[index].get_no_battles()) + ' ')
        outfile.write(str(character_list[index].get_no_won()) + ' ')
        outfile.write(str(character_list[index].get_no_lost()) + ' ')
        outfile.write(str(character_list[index].get_no_drawn()) + ' ')
        outfile.write(str(character_list[index].get_health()) + '\n')

        index = index + 1
    
    outfile.close()
    

def find_character(character_list, name):

    index = 0
    for person_name in character_list:
        if person_name != name:
            index = index + 1

        elif person_name == name:
            return index

    if index >= len(character_list):
        return -1
        

def add_character(character_list, name, secret_id, is_hero):

    new_heroVillan = find_character(character_list, name)

    if new_heroVillan != -1:
        print('')
        print(name, 'already exits in character list')
        print('')
        print('')

    else:
        new_character = character.Character(name, secret_id, is_hero)
        character_list.append(new_character)
        print('Successfully added', name, 'to the character list')
        print('')
        print('')

    return character_list
        
    
def remove_character(character_list, name):

    remove_char = find_character(character_list, name)
    
    if remove_char == -1:
        print('')
        print(name, 'is not found in characters.')
        print('')

    
    else:
        new_list_copy = []
    
        index = 0
        if remove_char <= 0:
            index = 1
            while index < len(character_list):
                new_list_copy.append(character_list[index])
                index = index + 1
            print('Successfully removed ', name, 'from character list.')
            print('')
            print('')

        elif remove_char > len(character_list):
            while index < len(character_list) - 1:
                new_list_copy.append(character_list[index])
                index = index + 1
            print('Successfully removed ', name, 'from character list.')
            print('')
            print('')

        else:
            while index < len(character_list):
                if index != remove_char:
                    new_list_copy.append(character_list[index])
                index = index + 1
            print('Successfully removed ', name, 'from character list.')
            print('')
            print('')

        

        character_list = new_list_copy

    return character_list


def do_battle (character_list, opponent1_pos, opponent2_pos):

    player1_name = character_list[opponent1_pos].get_name()
    player2_name = character_list[opponent2_pos].get_name()

    player1_health = character_list[opponent1_pos].get_health()
    player2_health = character_list[opponent2_pos].get_health()

    
    battle_rounds = int(input('Please enter number of battle rounds: '))
    while battle_rounds > 5 or battle_rounds <= 0:
        print('Must be between 1-5 inclusive.')
        print('')
        battle_rounds = int(input('How many rounds do you want to play? '))

    print('')
    print('')
    print('-- Battle --')
    print('')
    print(player1_name, 'verus', player2_name, '-', battle_rounds, 'rounds')
    index = 0
    while index < battle_rounds and player1_health > 0 and player2_health > 0:
        player1_dmg = random.randint(0,50)
        player2_dmg = random.randint(0,50)

        character_list[opponent1_pos].update_health(player1_dmg)
        character_list[opponent2_pos].update_health(player2_dmg)

        player1_health = character_list[opponent1_pos].get_health()
        player2_health = character_list[opponent2_pos].get_health()

        print('')
        print('Round: ', index + 1)
        print('> ', player1_name, ' - Damage: ', player1_dmg, ' - Current health: ', player1_health)
        print('> ', player2_name, ' - Damage: ', player2_dmg, ' - Current health: ', player2_health)
        
        index = index + 1

    print('')
    print('-- End of battle --')
    print('')
    
    if index == battle_rounds:
        if player1_health > player2_health:
            print('** ', player1_name, 'wins! **')
            print('')
            print('')
            character_list[opponent1_pos].increment_no_won()
            character_list[opponent2_pos].increment_no_lost()

            
        elif player2_health < player1_health:
            print('** ', player2_name, 'wins! **')
            print('')
            print('')
            character_list[opponent1_pos].increment_no_lost()
            character_list[opponent2_pos].increment_no_won()

        elif player1_health == 0 and player2_health == 0:
            print('Both players have killed each other ayy lmao')
            print('')
            print('')
            print('')
            character_list[opponent1_pos].increment_no_drawn()
            character_list[opponent2_pos].increment_no_drawn()

    elif player1_health <= 0 and player2_health > 0:
        print('-- ', player1_name, ' has died!  :(')
        print('')
        print('** ', player2_name, 'wins! **')
        print('')
        print('')
        character_list[opponent1_pos].increment_no_lost()
        character_list[opponent2_pos].increment_no_won()

    elif player2_health <= 0 and player1_health > 1:
        print('-- ', player2_name, ' has died!  :(')
        print('')
        print('** ', player1_name, 'wins! **')
        print('')
        print('')
        character_list[opponent1_pos].increment_no_won()
        character_list[opponent2_pos].increment_no_lost()
        

    elif player1_health == 0 and player2_health == 0:
        print('Both players have killed each other ayy lmao')
        print('')
        print('')
        character_list[opponent1_pos].increment_no_drawn()
        character_list[opponent2_pos].increment_no_drawn()

    character_list[opponent1_pos].increment_no_battles()
    character_list[opponent2_pos].increment_no_battles()

    return character_list


print('File     : Part2_dunap001.py')
print('Author   : Anthony Dunne')
print('Stud ID  : 110117963')
print('Email ID : dunap001@mymail.unisa.edu.au')
print('This is my own work as defined by the University\'s Academic Misconduct Policy.')
print('')
print('')
 
character_list = []
character_list = read_file('characters.txt')

write_to_file('new_characters.txt', character_list)

choice = 'y'
while choice != 'quit':

    choice_list = ['list', 'heroes', 'villains', 'search', 'reset', 'add', 'remove', 'battle', 'quit']

    print('Please enter choice')
    choice = input('[list, heroes, villains, search, reset, add, remove, battle, quit]: ')
    print('')

    while choice not in choice_list:
        print('Not a valid command - please try again.')
        print('')
        print('')
        print('Please enter choice')
        choice = input('[list, heroes, villains, search, reset, add, remove, battle, quit]: ')
        print('')

    if choice == 'quit':
        print("\n\n-- Program terminating --\n")
        write_to_file('new_characters.txt', character_list)

    elif choice == 'list':
        print('')
        display_characters(character_list, 0)
        print('')

    elif choice == 'heroes':
        print('')
        display_characters(character_list, 1)
        print('')

    elif choice == 'villains':
        print('')
        display_characters(character_list, 2)
        print('')

    elif choice == 'search':
        search_name = input('Please enter name: ')
        print('')
        name_pos = find_character(character_list, search_name)
        if name_pos == -1:
            print(search_name, 'is not found in character (heroes and villians) list.')
            print('')
            
        else: 
            searched_person = character_list[name_pos]
            
            vil_or_hero = ''
            true_false = character_list[name_pos].get_is_hero()
            if true_false == True:
                vil_or_hero = 'HERO'
            else:
                vil_or_hero = 'VILLIAN'

            
            print('All about', search_name, '-->', vil_or_hero)
            print('')
            print('Secret identity: ', searched_person.get_secret_identity())
            print('')
            print('Battles fought:', searched_person.get_no_battles())
            print('  > No won:', searched_person.get_no_won())
            print('  > No lost:', searched_person.get_no_lost())
            print('  > No drawn:', searched_person.get_no_drawn())
            print('')
            print('Current Health: ', searched_person.get_health(), '%', sep='')
            print('')
            print('')

    elif choice == 'reset':
        reset_name = input('Please enter name: ')
        reset_pos = find_character(character_list, reset_name)
        if reset_pos == -1:
            print('')
            print(reset_name, ' is not found in character (heroes and villians) list.')
            print('')

        else:
            character_list[reset_pos].set_health(100)
            print('')
            print('Successfully updated ', reset_name, '\'s healths to 100')
            print('')
        

    elif choice == 'add':
        add_name = input('Please enter name: ')
        add_secretid = input('Please enter secret_indentity: ')
        h_or_v_list = ['h', 'v']
        h_or_v = input('Is this character a hero or a villian [h|v]? ')
        while h_or_v not in h_or_v_list:
            h_or_v = input('Is this character a hero or a villian [h|v]? ')
        print('')

        add_character(character_list, add_name, add_secretid, h_or_v)
        

    elif choice == 'remove':
        remove_name = input('Please enter name: ')
        print('')
        character_list = remove_character(character_list, remove_name)


    elif choice == 'battle':
        opponent1 = input('Please enter opponent one\'s name: ')
        opponent1_pos = find_character(character_list, opponent1)
        while opponent1_pos == -1:
            print(opponent1, ' is not found in character list - please enter another opponent!')
            print('')
            opponent1 = input('Please enter opponent one\'s name: ')
            opponent1_pos = find_character(character_list, opponent1)

        opponent2 = input('please enter opponent two\'s name: ')
        opponent2_pos = find_character(character_list, opponent2)
        while opponent2_pos == -1:
            print(opponent2, ' is not found in character list - please enter another opponent!')
            print('')
            opponent2 = input('Please enter opponent one\'s name: ')
            opponent2_pos = find_character(character_list, opponent2)
        
        do_battle (character_list, opponent1_pos, opponent2_pos)



