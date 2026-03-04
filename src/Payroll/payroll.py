#Phase 1: Setup

    # 1.1: Import Libraries
import csv
    # 1.2: Declare & Track Global Variables 
tax_rate = 0.2

    # 1.3: Initialize Classes Variables
class Payroll:
    def __init__(self, file_name):
        self.file_name = file_name
    # 1.4: Anything That Only Happens Once

#Phase 2: Loop

    # 2.1: Get Input from User
def get_user_input(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data
    # 2.2: Process User Input (Is the Guess Correct?)
        #2.2.1 Iterate through the input data
def process_user_input(data):
        #2.2.2 Calculate gross pay, taxes, and net pay for each employee
    row_counter = 0
    for row in data:
        row_counter += 1
        if row_counter == 1:
            continue
        name = row[0]
        hours_worked = float(row[1])
        hourly_rate = float(row[2])
        gross_pay = hours_worked * hourly_rate
        taxes = gross_pay * tax_rate
        net_pay = gross_pay - taxes
        #2.2.3 Print the results
        print(f"Employee: {name} Gross Pay: ${gross_pay:.2f} Taxes: ${taxes:.2f} Net Pay: ${net_pay:.2f}")
    # 2.3: Check Exit Conditions (Did the User Win? Are They Out of Guesses?)

    # 2.4: Give Feedback - Print a Message. Show updated game state. 

#Phase 3: End Game
    
    # 3.1: Announce the Result - Print a Message Congratulating the User or Telling Them They Lost. Reveal the Secret Word.

    # 3.2: Ask if They Want to Play Again. If so, Restart the Game Loop. If Not, Exit.


#Phase 4: House Keeping

    # 4.1: Any functions and methods that are used in the game loop but aren't part of the main game logic; e.g. main(), __name__ == "__main__", game = , and game.play; or display functions that show the current state of the game to the user. 
def main():
    payroll = Payroll("input.data")
    data = get_user_input(payroll.file_name)
    process_user_input(data)

if __name__ == "__main__":
    main()