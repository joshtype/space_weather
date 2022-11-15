#-------------------------#
# Professor A. Mostafa    #
# Computer Science 1301k  # 
# Natural Disaster Prep   #
# Space Weather           #
#-------------------------#

# FlarePrepare.py <v.1.0>
# Programmer: Joshua Gregory
# Publsihed Nov.2022
# Open License: free to use/share/edit

# Space Weather Preparation and Safety
# [15 pts]: addresses problem; provides a solution
# [15 pts]: includes name of programmer; purpose summary; descriptive comments 
# [15 pts]: no syntax/runtime/logic errors; no global code
# [15 pts]: includes structures learned in course:
#           - print, str, int, list, inputs, functions, bool conditionals,
#             for/while loops, if blocks, files, main(), etc

#<---------------------------------(80 chars)--------------------------------->#

def welcome_msg():
    msg = """
Welcome to FlarePrepare.py by Joshua Gregory!
This is a guide to help you learn about space weather and how to stay safe
during potentially harmful space weather events.

The content of this program is provided for educational purposes only. It is
based on information provided by ready.gov. See 'Links' for more information.
"""
    print(msg)
    
#<---------------------------------(80 chars)--------------------------------->#

def main_contents():
    topics = """
Content Topics:
1) General Information
2) Safety During Events
3) Safety After Events
4) Preparation for Events
5) Links to Resources
6) Space Weather Quiz
7) Exit
"""
    print(topics)

def access_data():
    '''prompt/validate/repeat user input w/ while loop and if blocks;
       data subsets stored in external files accessed via input value;
       read and display data from external files; break loop for exit input'''
    
    while True:
        print(sep="/n")  # new lines can improve readability & user experience
        choice = int(input("Your choice: "))  # convert input from str to int
        
        if choice == 1:                     # if input has same value as 1
            try:                            # try to: open file, assign the
                with open("file-info.txt") as i:  # opened file to 'i', then
                    info = i.read()         # read 'i', store content as 'info'
            except FileNotFoundError:       # if try = filenotfound, then,
                print("Under construction...")  # display str instead of error
            print(info)                     # displays the stored file reading

        elif choice == 2:
            try:
                with open("file-during.txt") as d:
                    during = d.read()
            except FileNotFoundError:
                print("Under construction...")
            print(during)

        elif choice == 3:
            try:
                with open("file-after.txt") as a:
                    after = a.read()
            except FileNotFoundError:
                print("Under construction...")
            print(after)

        elif choice == 4:
            try:
                with open("file-prepkit.txt") as p:
                    prepkit = p.read()
            except FileNotFoundError:
                print("Under construction...")
            print(prepkit)

        elif choice == 5:
            try:
                with open("file-links.txt") as l:
                    links = l.read()
            except FileNotFoundError:
                print("Under construction...")
            print(links)

        elif choice == 6:  # if input = 6, return 'quiz' to main
            return "quiz"
        elif choice == 7:  # goodbye message
            print("Stay safe and prepared! Goodbye!")
            break          # break loops to terminate further execution
        else:
            print("Invalid option. Please choose again.")
            
#<---------------------------------(80 chars)--------------------------------->#

def space_weather_quiz():
    ''' prompts = multiple choice space weather questions; inputs = answers; 
        use while loop/if blocks to validate input; allow reentry if invalid;
        initiate a variable for accumulation; add 1 for correct answers;
        display score after 10 prompts; break loop if user exits '''
    
    # ten quiz questions, each assigned to a variable to keep code organized:
    que1 = """
1. The term 'space weather' refers to:
A) Extraplanetary storms, such as Jupiter's 'Red Spot'
B) Thunder-like frequencies studied by astrometeorologists 
C) Conditions in space that can impact Earth, such as solar wind or auroras
D) Static discharge from lunar surfaces to Earth's surfaces ('moon lightning')
"""
    que2 = """
2. Which of these Earth phenomena is caused by space weather?
A) Aurora Borealis
B) red tides
C) tectonic shifting
D) El Nino
"""
    que3 = """
3. Which of these is more likely to damage satellite systems like GPS?
A) space debris
B) comet off-gassing
C) geomagnetic fluctuation
D) Coronal Mass Ejection
"""
    que4 = """
4. The 1989 Canadian Blackout was caused by solar wind. Solar wind refers to:
A) fluctuations in charged particles resulting from solar rotation 
B) a constant stream of ionized particles emitted by the sun
C) bursts of solar plasma that appear 'windswept' in photos
D) photon dispersal through upper atmosphere air currents
"""
    que5 = """
5. Which of these is a trusted resource for information during natural disasters?
A) National Oceanic and Atmosphere Administration
B) Wireless Emergency Alert System
C) Emergency Alert System
D) All of the above
"""
    que6 = """
6. A communication plan does NOT include:
A) evacuation routes and contact information
B) how to continue livestreaming disaster effects
C) meeting place if household becomes separated
D) considerations for special needs and disabilities
"""
    que7 = """
7. 
A)
B)
C)
D)
"""
    que8 = """
8.
A)
B)
C)
D)
"""
    que9 = """
9.
A)
B)
C)
D)
"""
    que10 = """
10.
A)
B)
C)
D)
"""

    score = 0  # 'score' variable is an accumulator to store number of correct inputs
    
    # begin input prompts for quiz questions:
    print(que1)                                    # question 1
    ans1 = input("Choose A, B, C, or D: ")         # store input as 'ans1'
    if ans1 == "A" or ans1 == "B" or ans1 == "D":  # if ans1 is wrong, then
        score += 0                                 # score = score + 0
    elif ans1 == "C":                              # if ans1 is right, then
        score += 1                                 # score = score + 1

    print(que2)


#<---------------------------------(80 chars)--------------------------------->#

def main():
    ''' call helper functions '''
    welcome_msg()
    main_contents()
    access_data()

    if access_data() == "quiz":
        space_weather_quiz()

#<---------------------------------(80 chars)--------------------------------->#

if __name__ == "__main__":
    main()
    
#<---------------------------------(80 chars)--------------------------------->#

# end of file
