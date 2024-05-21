from classes import Person, Resource, Status
from termcolor import colored, COLORS
import os, math

class Displayer:
    def __init__(self, witdh):
        self.witdh = witdh

    def safe_get(self, ls, idx, default=None):
        try:
            return ls[idx]
        except IndexError:
            return default
        
    def bold(self, text):
        return f"\033[1m{text}\033[0m"

    def heading(self, text):
        l = len(text)
        space = math.floor((self.witdh - l)/2)
        print(self.bold(f"{' ' * space}{text}"))

    def line(self):
        print("-" * self.witdh)

    def stat(self, name, color):
        text = f"{name}: {'■' * 7}{'□' * 3}"
        return (colored(text, color), len(text))

    def stats(self):
        string = ""
        (morale, len1) = self.stat("Morale", "light_green")
        (heat, len2) = self.stat("Heat", "yellow")

        space = math.floor((self.witdh - len1 - len2) / 3)
        spaces = ' ' * space

        string += f"{spaces}{morale}{spaces}{heat}{spaces}"

        print(string)

    def screen(self, people, resources):
        height = max(len(people), len(resources))
        string = ""

        os.system("clear")
        self.heading("Day 1")
        self.stats()
        self.line()

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