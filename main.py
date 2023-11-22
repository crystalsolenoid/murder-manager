



import keyboard

print("You are a crow in an acorn forest.")

class Murder:
    def __init__(self):
        self.acorns = 5
        self.orchard = 0
        self.population = 1

    def inventory(self, item):
        # returns Acorns: 5 as a string, for example
        pass

    def gather(self):
        self.acorns += 1
        print("You've got an acorn!")

    def plant(self):
        cost = 1 # this might increase with purchase
        if self.acorns >= cost:
            self.acorns -= cost
            self.orchard += 1
            print("You've grown an oak tree in the orchard.")
        else:
            print("Growing an oak costs %.2f acorns." % cost)

    def update(self):
        self.acorns += self.orchard * 0.1
        if self.acorns <= 0:
            self.die()
            # die
        else:
            # eat
            self.acorns -= self.population * 0.5
        print("Acorns: %.2f" % self.acorns)
        print("Oaks: %.2f" % self.orchard)
    
    def die(self):
        print("You die. :(")
        confirmQuit()

    def play(self):
        pass

    def listhelp(self):
        pass

def confirmQuit():
    global requestQuit
    confirm = input("Are you sure you want to quit? Your progress will not be saved? (y/N)")
    if confirm == "y":
        requestQuit = True

murder = Murder()

commands = {"gather": murder.gather,
            "plant": murder.plant,
            "play": murder.play,
            "help": murder.listhelp,
            "quit": confirmQuit}

requestQuit = False
while not requestQuit:
    raw = input("> ")
    if raw in commands:
        commands[raw]()
    murder.update()

# (The forest is a big park in a city.)
# (They take over the city.)
