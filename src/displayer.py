from classes import Person, Resource, Status
import os

class Displayer:
    def __init__(self, witdh):
        self.witdh = witdh

    def safe_get(self, ls, idx, default=None):
        try:
            return ls[idx]
        except IndexError:
            return default

    def screen(self, people, resources):
        height = max(len(people), len(resources))
        string = ""

        os.system("clear")

        for i in range(height):
            person = self.safe_get(people, i)
            resource = self.safe_get(resources, i)
            space = self.witdh
            string = ""

            if person != None:
                space -= Person.LENGTH
                string += str(person)

            if resource != None:
                space -= Resource.LENGTH
                string += ' ' * space
                string += str(resource)

            print(string)

        print("-" * self.witdh)

d = Displayer(80)
p = Person("Jack", 4, Status.FREEZING, 4)
r2 = Resource("Heat", 10, "yellow")
r = Resource("Wood", 10, "green")

d.screen([p], [r, r2])