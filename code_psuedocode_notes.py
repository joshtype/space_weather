#--------------------#
# Prof. A. Mostafa   #
# CompSci 1301k      #
# QEP Space Weather  #
# Joshua Gregory     #
#--------------------#

# QEP Group Project
# Space Weather Safety/Preparation Guide
# This file contains a mixture of code/psuedocode/notes for planning purposes
# Structure subject (likely to) change (significantly)
# Effort being made to display data stored on external files to shorten code

define function 1: welcome_user():
# print a welcome message, explain purpose of program
# no parameters, no return
    print("Welcome to FlarePrepare.py!")
    print("""This program is designed to provide you with a brief overview
of safety advice and preparation guidance to help you be better informed
about space weather and how to stay safe before, during, and after an event.
Included are links to important research and government agencies, as well as
examples of historical examples of harmful space weather.

The information provided in this program is for educational purposes only.
It is based on data from various research and government agencies.
Please refer to the links provided to access more detailed information,
important resources, and expert guidance.

Programmed by Joshua Gregory, Nov. 2022. Content is free to share. 
""")

define function 2: guide()
# display a table of contents, with input numbers for each topic,
# prompt user input for what kind of information to access,
# validate input with 'while: True', break loop & return valid input,
# provide exit option

    print("""
CONTENTS:
1) General information about space weather
2) Staying safe during a space weather event
3) Staying safe after a space weather event
4) Preparation for space weather events
5) Interesting examples of harmful space weather
6) Links to space weather conditions, tracking, predictins, guidance and more
7) Exit
""")
    
    while True:
        choice = input("What would you like to learn about?")
        if choice.isdigit == True:
            choice = int(choice)
            return choice
            break
        else:
            print("Pleae enter a valid option.")
        
define function 3: sw_data(choice):
# take choice returned from guide() as parameter, value of choice
# determines chosen data, provide exit option

    while True:
        if choice == 1:
            print("""
Brief Explanation of Space Weather
Space Weather refers to events conditions in space that may impact Earth.
One well-known and commonly seen example of space weather are the Northern and
Southern Lights. These are produced when ionized solar radiation waves are
deflected by Earth's magnetosphere. Similarly, most types of space weather
is harmless phenomena and topics of study. However, there are types of space
weather that can have significantly harmful impacts on Earth or human society.
The most common of these are Coronal Mass Ejections (CMEs) and Solar Flares.

What are CMEs and solar flares?
...
""")
        # during
        elif choice == 2:
            print("""
Staying Safe During an Event:
...
""")
        # after
        elif choice == 3:
            print("""
Staying Safe After an Event:
...
""")
        # prepare
        elif choice == 4:
            print("""
Preparation for Events:
...
""")
        # two examples harmful space weather
        elif choice == 5:
            print("""
Historical Examples of Harmful Space Weather:
...
""")
        # links
        elif choice == 6:
            print("""
Links:
...
""")
        # exit
        elif choice == 7:
            print("Stay safe and prepared!")
            break
            
define main() function:
# call helper functions,
# assign variables to functions so following functions can access parameters

    choice = guide()
    sw_data(choice)
    


    
