import random





def get_computer_choice(choices):
    
    return choices [random.randint (0,2)]


def get_user_choice ():
    print ("Choose your weapon: Rock, Paper or Scissors?")
    return input().lower()


def get_winner ():
    choices = ["rock", "paper", "scissors"] #in this list index 0 beats 1 beats 2 beats 0
    user = get_user_choice ()
    computer = get_computer_choice (choices)
    print (f"Computer chose {computer}!")
    if user == computer:
        print ("Draw! Don't give up!")
        get_winner ()
    if choices.index (user) +1 == choices.index (computer) or choices.index(user)-2 == choices.index (computer): #describes the relationship in comment on line 18
        return "User wins!"
    else:
        return "Computer Wins!" #should this be a print line?

def play_game():
    return get_winner()
