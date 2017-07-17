blanks = ["__1__", "__2__", "__3__", "__4__"]

# The following is the level_easy string to pass in to the play_game function. 
level_easy = "__1__ is a __2__ used general-purpose, __3__ programming __4__."

# A list of replacement words for the level_easy to be passed in to the play game function. 
easy_answers = ["Python", "widely", "high-level", "language"]

# The following the level_medium string to pass in to the play_game function.
level_medium = "__1__ is a __2__ level, __3__, untyped, and __4__ programming language."

# A list of replacement words for the level_medium to be passed in to the play game function. 
medium_answers = ["Javascript", "high", "dynamic", "interpreted"]

# The following is the level_hard string to pass in to the play_game function.
level_hard = "__1__ is a __2__ __3__ __4__."

# A list of replacement words for the level_hard to be passed in to the play game function. 
hard_answers = ["C++", "general-purpose", "programming", "language"]

def choose_level():

#Checks if the player will choose which level
#raw_input is for the user_input
    prompt = raw_input ("Select your level : easy, medium or hard ")
    
#If the player choose easy then mad_libs_game will be played with level_easy & easy_
#answers 
    if prompt == "easy":
        mad_libs_game(level_easy, easy_answers)
    if prompt == "medium":
        mad_libs_game(level_medium, medium_answers)
    if prompt == "hard":
        mad_libs_game(level_hard, hard_answers)

# Plays a full game of mad_libs. A player is prompted to replace words in level_string, 
# which appear in answers with the words.
# Checks if a answer in answers is a substring of the word passed in.  
def mad_libs_game(level_string, answers):
    print level_string
    for answer in answers:
        user_input = raw_input("Fill the blank: ")
        while user_input != answer:
            user_input = raw_input("Incorrect, fill the blank: ")
        level_string = level_string.replace(blanks[answers.index(answer)], user_input)
        print level_string
    return ""
print choose_level()
