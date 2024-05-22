from dataclasses import dataclass
from classes import Person, Resource
from typing import List

# Lists
Yes = ['y', 'yes']
No = ['n', 'no']
Names = ['John', 'Kevin', 'Tom', 'Sheldon', 'Joel', 'Daren']
# Variables
dificulty = 0

@dataclass
class GameState:
    people: List[Person]
    resources: List[Resource]
    morale: int
    heat: int
    day: int
