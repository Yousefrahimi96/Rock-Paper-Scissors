import random

class RockPaperScissors:
    def __init__(self):
        choice_list = ["rock", "paper", "scissors"]
        
    def computer_choice(self, cchoice):
        self.cchoice = cchoice
        self.cchoice = random.choice(choice_list)
        
    def user_choice(self, uchoice):
        self.uchoice = uchoice
        self.uchoice = input("Please inter your choice from (rock, paper, scissors) : ")
        while True:
            for i in choice_list:
                if i == uchoice:
                    break
                elif uchoice == "q":
                    break
                else:
                    uchoice = input("Please inter your choice from (rock, paper, scissors) : ")
                    continue
            break
               
    def decision(self):
        if (self.uchoice == self.cchoice) :
            print("withdraw")
            pass
        elif (self.uchoice == "rock" and self.cchoice == "scissors") or \
            (self.uchoice == "paper" and self.cchoice == "rock") or \
            (self.uchoice == "scissors" and self.cchoice == "paper"):
            print("You won")
            pass
        else :
            print("You lose")
            pass
        return(f"computer choice is {self.cchoice}")
            
            