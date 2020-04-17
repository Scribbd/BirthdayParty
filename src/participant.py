class Participant:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hi, my name is " + str(self.name)

    def __eq__(self, other):
        if other is Participant:
            return self.name == other.name
        return self.name == str(other)