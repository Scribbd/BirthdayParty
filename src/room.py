from src.participant import Participant

class Room:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.guests = []

    def being_walked_in_by(self, guest):
        if len(self.guests) < self.size:
            self.guests.append(guest)
            return True
        else:
            print("\t{} is full!".format(self.name))
        return False

    def where_is(self, guest_name):
        if guest_name in self.guests:
            print("\t{} is here! In the {}!".format(guest_name, self.name))
        else:
            print("\tNobody here in {} with that name.".format(self.name))
    
    def clear(self):
        self.guests.clear()

    def __str__(self):
        out = "\tThis is {}, I got room for {}. Guests, introduce yourselves!\n".format(self.name, self.size)
        for guest in self.guests:
            out += "\t\t{}\n".format(str(guest))
        return out
    
    def __eq__(self, other):
        if other is Room:
            return self.name == other.name
        return self.name == str(other)