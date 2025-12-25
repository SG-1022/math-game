import random

class MathGame:

    def __init__(self, digits):
        self.emoji_number = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣",
            4: "4️⃣",
            5: "5️⃣",
            6: "6️⃣",
            7: "7️⃣",
            8: "8️⃣",
            9: "9️⃣",
            0: "0️⃣"
        }

        self.emoji_symbol = {
            "+": "➕",
            "-": "➖",
            "*": "✖️",
            "/": "➗",
        }

        if digits == 2:
            num = 99
        elif digits == 1:
            num = 9
        else:
            print("It looks like you haven't provided anything, so we will go by default.")
            num = 9

        self.first_number = random.randint(0, num)
        self.second_number = random.randint(1, num)

        self.symbols = ["+", "-", "*", "/"]
        self.random_symbol = random.choice(self.symbols)
        self.display_symbols = {
            "+": "+",
            "-": "-",
            "*": "×",
            "/": "÷"
        }
        self.emoji_on_or_off = input("Do you want emoji numbers on or off? (On, Off)\n").lower()


    def refresh_question(self):
        self.first_number = random.randint(0, 9)
        self.second_number = random.randint(0, 9)
        self.random_symbol = random.choice(self.symbols)

        if self.second_number == 0 and self.random_symbol == "/":
            self.refresh_question()
        checking = eval(f"{self.first_number}{self.random_symbol}{self.second_number}")
        checking = float(checking)
        checking = str(checking)
        if checking[-1] != "0":
            self.refresh_question()



    def get_questions(self) -> dict[str, str]:
        self.refresh_question()
        real_equation = f"{self.first_number}{self.random_symbol}{self.second_number}"

        if self.emoji_on_or_off == "on":
            display_equation = f"{self.emoji_number[self.first_number]}{self.emoji_symbol[self.random_symbol]}{self.emoji_number[self.second_number]}"
        else:
            display_equation = f"{self.first_number} {self.display_symbols[self.random_symbol]} {self.second_number}"

        display_text = f"What is the answer to the question '{display_equation}'?"

        # FIXME - Make the display_text look better. DO NOT USE RANDOM MODULE!


        equation_dictionary = {
            "real_equation": real_equation,
            "display_equation": display_equation,
            "display_text": display_text,
            "answer": eval(real_equation)
        }

        return equation_dictionary

    def email_feedback(self, feedback):
        """Emails back to owner of the game."""
        import smtplib
        import os

        EMAIL = os.environ.get("EMAIL")
        PASSWORD = os.environ.get("PASSWORD")


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr = EMAIL,
                                to_addrs = EMAIL,
                                msg = f"Subject:Feedback For Math_Game\n\n{feedback}\n*This is sent from Python.")

    def save_feedback(self, feedback):
        """Saves into a txt."""
        with open("feedback.txt", "a") as feed:
            feed.write("\n" + feedback)
            print("Saved feedback!")