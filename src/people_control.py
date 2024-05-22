from dataclasses import dataclass

# List
players = []

for i in range(0, ):
    players.append(0)

@dataclass
class Controll:
    person: str
    time: int

    def __str__(self):
        return f"{self.person, 'is going for ', self.time, ' days'}"
        


p1 = Controll('josh', 4)

print(p1)
print(players)