
import gamestate

print('Hello Adventurer, welcome to the Terminal Adventure ')

# player set up
print('What is your name adventurer! ')
p_name = input('')

print('Okay ', p_name, " Would you like an introduction? ")
choise = input('')

if choise in gamestate.y:
    print('INSERT LORE HERE')
else:
    print('''No problem ',p_name,' If anything 
type Help to recive instructions''')
    

Alive = True

def Help():
    print('''You are a survior, leading a small comunity''')
    

while Alive:
    print("Inster game here")
