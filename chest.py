class Chest:
    def __init__(self, item):
        self.item = item
    
    def __str__(self):
        return f"{self.item}"

p1 = Chest('Help')

print(p1)