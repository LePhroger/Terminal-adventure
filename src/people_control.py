from dataclasses import dataclass

@dataclass
class Control:
    person: str
    time: int

    def __repr__(self):
        return f"{self.person, 'is going for ', self.time, ' days'}"
        


p1 = Control('josh', 4)

print(p1)
print(players)