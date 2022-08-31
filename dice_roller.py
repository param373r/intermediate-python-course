import random
'''
Some later ideas for this project:
     - Add more inputs (like player or team name)
     - Store each player's roll totals in separate arrays
     - Choose a dice-based game that you can fully simulate using python.

'''
# Main method
def main():
     # Initializing Variables
     dice_sum = 0
     dice_rolls = int(input('How many dice would you like to roll?'))
     dice_size = int(input('How many sides is the dice of?'))
     
     # Loop for dice roll(s)
     for i in range(0,dice_rolls):
          roll = random.randint(1,dice_size) # Creating a dice roll

          # Some fun comments
          if roll == 1: 
               print(f'You rolled a {roll}! Critical Fail')
          elif roll == dice_size: #
               print(f'You rolled a {roll}! Critical Success!')
          else:
               print(f'You rolled a {roll}')
          
          # Finding the dice sum rolled
          dice_sum += roll
     print(f'You rolled a total of: {dice_sum}')

# Running the main function
if __name__== "__main__":
     main()