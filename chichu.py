# Tools

# -- Imported Modules
import datetime

# -- Realm of the Known

known_modules = list()
known_functions = list()
known_concepts = list()

# -- Axioms

class Module:

    defintion = "collection of functions"
    notes = ["use import statement to access module"]

    def __init__(self, name, defintion):
        self.name = name
        self.function = list()
        self.defintion = defintion

class Function:

    definition = "named operation"

    def __init__(self, name, arguments=[], takes="", returns=""):
        self.name = name
        self.arguments = arguments
        self.takes = takes
        self.returns = returns

class Concept:

    defintion = "an abstract idea"

    def __init__(self, name, definition):
        self.name = name
        self.defintion = definition

#  Data Entry

# -- Modules

# -- -- Math
known_modules.append(Module("Math", "collection of basic mathematical functions"))

# -- Functions

# -- Concepts
known_modules.append(Concept("percent difference", "100 times the absolute value of the difference between the values, divided by their average    "))

print(datetime.datetime.date(all))
