#Rock Scissors Paper version 2.0
#Rock Scissors Paper
#Programmer: Dimitris theodoropoulos
#Use it in code Skulptor
import random
import simplegui

#Let's Go

COMPUTER = 0
HUMAN = 0
human_choice = ""
computer_choice = ""


def choice_to_number(choice):
    return {'rock':0,'paper':1,'scissors':2}[choice]
    


def number_to_choice(number):
     return {0:'rock',1:'paper',2:'scissors'} [number]
   
def random_computer_choice():
    """Choose randomly for computer."""
    computer_choice = ['rock', 'paper', 'scissors']
    return random.choice(computer_choice)

def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""
    
    global COMPUTER
    global HUMAN	
   
    #Project Ace 
    computerchoice = choice_to_number(computer_choice)
    humanchoice = choice_to_number(human_choice)
    
    
    
    if (humanchoice - computerchoice) % 3 == 1:
        print("HaHaHa")
        COMPUTER=COMPUTER+1
        
    else:
        print("Beginners Luck")
        HUMAN=HUMAN+1
        
    if (human_choice==computer_choice):
        print("Lucky")
        HUMAN=HUMAN-1

def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
    
def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'
    
def test_all():
    test_choice_to_number()
    test_number_to_choice()
    print"Enjoy"

test_all()

def rock():
    global human_choice, computer_choice
    global HUMAN, COMPUTER
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN, COMPUTER
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


def draw(canvas):
    
    try:
        
        canvas.draw_text("I Chose: " + human_choice, [70,130], 74, "yellow")
        canvas.draw_text("CPU Chose: " + computer_choice, [70,200], 74, "red")
        

        canvas.draw_text("My Score: " + str(HUMAN), [70,370], 60, "yellow")
        canvas.draw_text("CPU Score: " + str(COMPUTER), [70,430], 60, "red")
        canvas.draw_text("Created by Jim Theodoropoulos " , [19,610], 9, "White") 
    
    except TypeError:
        pass
    
def play_rps():
    frame = simplegui.create_frame("home", 1090, 627)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)
    frame.start()
 
play_rps()
