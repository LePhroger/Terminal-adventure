from dataclasses import dataclass
from classes import Person, Resource
from typing import List

@dataclass
class GameState:
    people: List[Person]
    resources: List[Resource]
    morale: int
    heat: int
    day: int
