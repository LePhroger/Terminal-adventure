from dataclasses import dataclass
from termcolor import colored
from enum import Enum
import random as rd

class Status(Enum):
    NONE = 0
    FREEZING = 1
    STARVING = 2

@dataclass
class Person:
    name: str
    health: int
    status: Status
    status_left: int

    LENGTH = 10 + 3 + 5 + 3 + 5

    def __repr__(self):
        string = f"{self.name.ljust(10, ' ')} | {('♥' * self.health).ljust(5, ' ')}"
        string += f" | "
        
        if self.status != Status.NONE:
            string += colored(f"{'■' * self.status_left}{'□' * (5 - self.status_left)}", "red")
        else:
            string += ' ' * 5

        return string

@dataclass
class Resource:
    name: str
    amount: int
    color: str
    
    LENGTH = 3 + 3 + 6

    def __repr__(self):
        string = colored(f"{str(self.amount).rjust(3, ' ')}", self.color)
        string += " | "
        string += colored(f"{self.name.rjust(6, ' ')}", self.color)
        return string
    

class Chest:
    def __init__(self, numb_1, numb_2):
        self.slot_1 = numb_1
        self.slot_2 = numb_2
        self.item = rd.randint(numb_1, numb_2)
    
    def __repr__(self):
        return f"{self.item}"

p1 = Chest()

print(p1)