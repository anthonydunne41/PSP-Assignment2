#
#   PSP Assignment 2 - Provided file (Part I - list_function.py).
#  
#   File:      dunap001_poker.py
#   Author:    Anthony Dunne
#   Email Id:  dunap001
#   Description:  Programming Assignment 2.
#       This is my own work as defined by the University's
#       Academic Misconduct policy.
#



def length(my_list):
    count = 0
    for item in my_list:
        count = count + 1

    return count


def to_string(my_list, sep=', '):
    new_string = ''
    index = 0
    for item in my_list:
        if index < length(my_list)-1:
            new_string = new_string + str(item) + sep
        elif index == length(my_list)-1:
            new_string = new_string + str(item)

        index = index + 1

    return new_string


def find(my_list, value):
    index = 0

    for num in my_list:
        if num == value:
            return index
        index = index + 1
        
    if num is not value:
        index = -1
        
    return index



def insert_value(my_list, value, insert_position):
    list_copy = []
    index = 0

    if insert_position <= 0:
        list_copy.append(value)
        for num in my_list:
            list_copy.append(num)

    elif insert_position > length(my_list):
        for num in my_list:
            list_copy.append(num)
        list_copy.append(value)

    elif insert_position < length(my_list):
        index = 0
        while index < insert_position:
            list_copy.append(my_list[index])
            index = index + 1
        if index == insert_position:
            list_copy.append(value)
        while index < length(my_list):
            list_copy.append(my_list[index])
            index = index + 1

    return list_copy


def remove_value(my_list, remove_position):
    new_list_copy = []
    
    index = 0
    if remove_position <= 0:
        index = 1
        while index < length(my_list):
            new_list_copy.append(my_list[index])
            index = index + 1

    elif remove_position > length(my_list):
        while index < length(my_list) - 1:
            new_list_copy.append(my_list[index])
            index = index + 1

    else:
        while index < length(my_list):
            if index != remove_position:
                new_list_copy.append(my_list[index])
            index = index + 1

    return new_list_copy


def reverse(my_list, number=-1):

    new_list = []

    if number >= length(my_list):
        number = length(my_list) - 1
    
    index = number
    if index == -1:
        index = length(my_list) - 1
        while index != -1:
            new_list.append(my_list[index])
            index = index - 1

    else:
        while index != -1:
            new_list.append(my_list[index])
            index = index - 1

        index = number + 1
        while index < length(my_list):
            new_list.append(my_list[index])
            index = index + 1

    if number < 2 and number != -1:
        new_list = my_list

    return new_list



