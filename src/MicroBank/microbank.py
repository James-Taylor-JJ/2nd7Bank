#Phase 1: Setup

    # 1.1: Import Libraries
import csv
    # 1.2: Declare & Track Global Variables 

    # 1.3: Initialize Classes Variables
class MicroBank:
    def __init__(self, file_name, balance=0.0):
        self.file_name = file_name
        self.balance = balance

    # 1.4: Anything That Only Happens Once

#Phase 2: The Loop

    # 2.1: Get Input from User
    def get_user_input(self):
        with open(self.file_name, 'r') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        return data
    # 2.2: Process User Input 
        # 2.2.1: Interate through the data 
    def process_user_input(self,data):
        # 2.2.2: Skip the first row of the data since it contains the column headers
        
        # 2.2.3: Determine whether the entry is a deposit or a withdrawal
        for row in data:
            transaction_date = row[0]
            transaction_type = row[1]
            transaction_amount = float(row[2])
        # 2.2.4: Add the corresponding amount if it's a deposit
            if transaction_type.strip().lower() == 'deposit':
                self.balance += transaction_amount
        # 2.2.5: Subtract it if it's a withdrawal
            elif transaction_type.strip().lower() == 'withdrawal':
                self.balance -= transaction_amount
    # 2.3: Give Feedback 
        # 2.3.1: Print the account balance.  
        print(f"Your current balance is: ${self.balance:.2f}")
#Phase 3: End Game
    
    # 3.1: Announce the Result - Print a Message Congratulating the User or Telling Them They Lost. Reveal the Secret Word.

    # 3.2: Ask if They Want to Play Again. If so, Restart the Game Loop. If Not, Exit.

#Phase 4: House Keeping

    # 4.1: Any functions and methods that are used in the game loop but aren't part of the main game logic; e.g. main(), __name__ == "__main__", game = , and game.play; or display functions that show the current state of the game to the user.

   

if __name__ == "__main__":
    microBank = MicroBank("input.data")
    data = microBank.get_user_input()
    microBank.process_user_input(data)