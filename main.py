#!/usr/bin/env python
# Author: Gary Hooks
# Web: http://www.garyspassage.co.uk
# Email: garyhooks@gmail.com
# Publish Date: 19th August 2018
# Licence: GNU GPL
#
# Usage: python3 ./main.py

import random
import time

__PASSWORD__ = "password123"
__PHONENUMBER__ = "07554112335"

def count_lines(filename):

    count = 0
    with open(filename, "r") as file:
            for line in file:
                count+=1

    return count

def get_random(filename, maxlines):

    randomnumber = random.randint(0,maxlines)

    stop = 0
    counter = 0
    while stop == 0:
        with open(filename, "r") as file:
                for line in file:
                    if counter == randomnumber:
                        stop = 1
                        result = line
                    counter += 1

    return result

def main():

    _OLDEST_BIRTH_YEAR = 1970
    _YOUNGEST_BIRTH_YEAR = 2005

    firstname_lines = count_lines("firstnames.txt")
    lastnames_lines = count_lines("lastnames.txt")
    passwords_lines = count_lines("passwords.txt")
    towns_lines = count_lines("towns.txt")

    random_firstname = get_random("firstnames.txt", firstname_lines).capitalize().strip()
    random_lastname = get_random("lastnames.txt", lastnames_lines).capitalize().strip()
    random_password = get_random("passwords.txt", passwords_lines).strip()
    random_town = get_random("towns.txt", towns_lines).capitalize().strip()

    birthmonth = random.randint(1,12)
    day = random.randint(1,28)
    year = random.randint(_OLDEST_BIRTH_YEAR, _YOUNGEST_BIRTH_YEAR)

    print("Name: " + random_firstname + " " + random_lastname)
    print("Location: " + random_town)
    print("Date of Birth: " + str(day) + "/" + str(birthmonth) + "/" + str(year))
    print("Password: " + random_password)
    print("Phone Number: " + __PHONENUMBER__)

    print("\n")
    print("===================================")
    print("\n")


if __name__ == "__main__":
    flag = 0
    while flag < 20:
        main()
        flag+=1
        time.sleep(1)