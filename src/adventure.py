
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

print('What will be the amount of people in your comunity? 3 to 6 ')
choise = int(input(''))

for i in range(0,choise):
    print('Asing people here')

Alive = True

def Help():
    print('''You are a survior, leading a small comunity''')
    

while Alive:
    print("Inster game here")
    Alive = False
