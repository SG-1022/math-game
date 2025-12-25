import random

import math_game as mg

# TODO - Make a proper introduction.

input("Welcome to the math game! Press enter to continue.")
a = input("In this game, we will question your math skills with easy questions. With one digit numbers by default. So we hope you enjoy the game!"
      "\nThis game is still in beta mode. To make it better, please give good feedback when asked."
      "\nImmediately when you press enter, the game will start. Have fun!"
      "\nIf you want to see our growth and our goals, than type \"history\"\n")

if a.lower() == "history":
    with open("Version History.txt") as version_history:
        version_history = version_history.read()
        print(version_history)
    version_history = None

# a = input("\nIf you want to have like bigger numbers, please type it here."
#           "\nThe only available numbers are listed in parenthesis. (1, 2)"
#           "\nYou do not have to answer this question.\n")

# if a == "1":
#     digits = 1
# elif a == "2":
#     digits = 2
# else:
#     digits = 1
# TODO - Fix this code and make it so that it actually works.

digits = 1

math_game = mg.MathGame(digits)



while True:

    equations_dictionary = math_game.get_questions()
    equation_dictionary_key = ["real_equation", "display_equation", "display_text", "answer"]

    user_input = input(equations_dictionary["display_text"] + "\n")
    print(equations_dictionary["answer"])

    try:
        user_input = float(user_input)
        h = False
    except ValueError:

        if user_input == "exit":
            feedback = input("Thank you so much for playing the Math Game! What is your feedback of this game?\n")
            math_game.email_feedback(feedback=feedback)
            print("Thank you so much and we hope you enjoyed the game!")
            raise SystemExit
        else:
            print("You made a mistake. You didn't provide the answer in the correct format.")
            h = True

    if user_input == float(equations_dictionary["answer"]):
        with open("correct_statement.txt") as state:
            statement = state.read()
            my_list = statement.split("\n")
            print(random.choice(my_list))


    else:
        if not h:
            print(f"It looks like you got it incorrect😭. The correct answer is {equations_dictionary['answer']}.")