from src.participant import Participant
from src.room import Room

class Building:
    
    def __init__(self, name, *rooms):
        self.name = name
        if rooms:
            self.rooms = list(rooms)
        else:
            self.rooms = []
        self._next_room = 0

    def let_in(self, partygoer):
        while not self.rooms[self._next_room].being_walked_in_by(partygoer):
            self._next_room += 1
            if self._next_room >= len(self.rooms):
                self._next_room = 0

    def get_room(self, room_name):
        try:
            return self.rooms[self.rooms.index(room_name)]
        except:
            print("No such {} in my building!".format(room_name))
            return None

    def where_is(self, participant):
        print("Where is {}?".format(str(participant)))
        for room in self.rooms:
            room.where_is(participant)

    def shuffle(self):
        print("All right people! Get out! We are going to mix things up!")
        got_out = []
        for room in self.rooms:
            got_out += room.guests

    def vibe_check(self):
        print("Okay everybody! Vibe-Check!")
        for room in self.rooms:
            print(room)