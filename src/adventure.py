import gamestate
import random as rd

# Lists
People = []
# Variables
people_numb = 0


print('Hello Adventurer, welcome to the Terminal Adventure ')

# player set up
print('What is your name adventurer! ')
p_name = input('')

print('Okay ', p_name, " Would you like an introduction? ")
choise = input('')

if choise in gamestate.Yes:
    print('INSERT LORE HERE')
else:
    print('No problem ',p_name,''' If anything 
type Help to recive instructions''')

def dificulty():
    print('What will be the amount of people in your comunity? 3 to 6 ')
    choise = int(input(''))

    for i in range(0,choise):
        person = gamestate.Person(gamestate.Names[rd.randint(0,5)],4,10,2)
        People.append(person)
    
dificulty()

Alive = True

def Help():
    if choise == gamestate.Help:
        print('''You are a survior, leading a small comunity''')
    
print("Inster game here")
print(People)
print('\n')

while Alive:    
    print('What is your next move? ')
    choise = input('')

    if choise in gamestate.Help:
        print('''Comand list:
next day - next_day, skip, next
Interacting - interact, inspect, pick, look
Help - help, Help
Quit - end, terminate, quit''')
    elif choise in gamestate.Continue:
        print('Next day it is ', gamestate.Day)
        gamestate.Day = gamestate.Day + 1
    elif choise in gamestate.Inspect:
        print(People)
        print('Which person? ')
        choise = input('')
        # choise = the person whose number is in the list displayed
    elif choise in gamestate.Quit:
        print('Game over')
        Alive = False


    print('\n')