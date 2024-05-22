from classes import Person, Resource, Status
from displayer import Displayer
from gamestate import GameState
from getch import getch

class GameLoop:
    def __init__(self, gamestate):
        self.state = gamestate
        self.displayer = Displayer(80, gamestate)

    def do_day(self):
        # Morning Phase
        self.displayer.prompt("Hello\nYou had some event happen!\n\nPress any key to continue...")

    def choose_person(self):
        self.state.people[0].selected = True
        self.displayer.screen()

        i = 0
        while True:
            chr = getch()

            self.state.people[i].selected = False

            if chr == 'w':
                i -= 1
            if chr == 's':
                i += 1

            if i < 0:
                i = 0
            if i >= len(self.state.people):
                i = len(self.state.people) - 1

            self.state.people[i].selected = True

            # Break if enter pressed
            if ord(chr) == 13:
                break

            self.displayer.screen()

        return self.state.people[i]
    
    def choose_resource(self):
        self.state.resources[0].selected = True
        self.displayer.screen()

        i = 0
        while True:
            chr = getch()

            self.state.resources[i].selected = False

            if chr == 'w':
                i -= 1
            if chr == 's':
                i += 1

            if i < 0:
                i = 0
            if i >= len(self.state.resources):
                i = len(self.state.resources) - 1

            self.state.resources[i].selected = True

            # Break if enter pressed
            if ord(chr) == 13:
                break

            self.displayer.screen()

        return self.state.resources[i]


p = Person("Jack", 4, Status.FREEZING, 4)
p2 = Person("Ana", 5, Status.NONE, 0)
r2 = Resource("Heat", 10, "yellow")
r = Resource("Wood", 10, "green")

g = GameState([p, p2], [r, r2], 9, 3, 1)
gl = GameLoop(g)
gl.do_day()