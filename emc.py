'''
---------------------------------------
-- Created by:     Alireza Teimoori  --
-- Created on:     Feb 9 2019        --
-- Created for:    Unit 1-03         --
-- Course Code:    ICS4U             --
-- Teacher Name:   Chris Atkinson    --
---------------------------------------
'''

# Intro Constant:
LIGHTSPEED = 2.998 * 10**8
BOMB = 4.2 * 10**12

# Ask for and store data:
mass = input("What is the mass of the object in kilgrams? \n")


if float(mass) > 0: 
    # Calculations:
    energy = float(mass) * LIGHTSPEED**2
    bombEnergy = energy / BOMB

    # Output:
    print("The energy that is released is equal to:\n" + str(energy) + " joules.")
    print("This is equal to %d kiloton bomb" % bombEnergy)

else: # Eliminate invalid inputs
        print("Invalid input.")