import json
import math
import hashlib
from random import choice, shuffle

with open('namelist.json', 'r') as jsonFile:
    name_list = json.load(jsonFile)

    first_names = name_list['first_name']
    last_names = name_list['last_name']

    shuffle(first_names)
    shuffle(last_names)


def getRandomFirstName():
    return choice(first_names)


def getRandomLastName():
    return choice(last_names)


def getEmail(first_name, last_name):
    return ''.join([first_name, '_', last_name, '@domain.com']).lower()


def getID(first_name, last_name):
    '''
    Function that hashes a given string combination, and takes the 8
    least-significant decimals to simulate a 'unique' ID number.
    '''
    return int(hashlib.md5(''.join([first_name, last_name]).encode('utf-8')).hexdigest(), 16) % int(math.pow(10, 8))


def generateSample(size):
    user_list = []
    for i in range(size):
        user_dict = {}
        first_name = getRandomFirstName()
        last_name = getRandomLastName()
        user_dict['name'] = ' '.join([first_name, last_name])
        user_dict['user_id'] = getID(first_name, last_name)
        user_dict['email_address'] = getEmail(first_name, last_name)

        user_tuple = (user_dict['name'], user_dict['user_id'], user_dict['email_address'])

        user_list.append(user_tuple)

    return user_list
