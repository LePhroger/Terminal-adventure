from dataclasses import dataclass
from classes import Person, Resource
from typing import List

# Lists
Yes = ['y', 'yes']
No = ['n', 'no']
Continue = ['next day', 'next', 'skip']
Names = ['John', 'Kevin', 'Tom', 'Sheldon', 'Joel', 'Daren']
Help = ['help','Help']

# Variables
Day = 1


@dataclass
class GameState:
    people: List[Person]
    resources: List[Resource]
    morale: int
    heat: int
    day: int
