print('Hello Adventurer, welcome to the Terminal Adventure ')

# player set up
print('What is your name adventurer! ')
p_name = input('')

print('Okay ', p_name, " Would you like an introduction? ")
choise = input('')

y = ['y', 'yes']
n = ['n', 'no']

if choise in y:
    print('INSERT LORE HERE')
else:
    print('''No problem ',p_name,' If anything 
type Help to recive instructions''')