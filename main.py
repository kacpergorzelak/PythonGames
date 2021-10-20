import turtle
from time import sleep

def get_number_of_participants():
    Participants = 0
    while True:
        participants = input("Enter the number of participants: (number must be greater than 2 and less than 10)\n")
        if participants.isdigit():
            participants = int(participants)
        else:
            print("Input must be a numeric value!")
            continue

        if 2 <= participants <= 10:
            return participants
        else:
            print("Number of participants must be in the range 2-10!")


def initialize_screen():
    WIDTH, HEIGHT = 500, 500
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("The Game")


Participants = get_number_of_participants()
print(Participants)
initialize_screen()
Participant_1 = turtle.Turtle()
Participant_1.forward(50)
sleep(10)