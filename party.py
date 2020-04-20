from src.building import Building
from src.participant import Participant
from src.room import Room

# a list of partygoers
partygoers = ['Casper', 'Abdesammad', 'Clyde', 'Saskia', 'Eline', 'Peter', 'Achraf', 'Ruben', 'Viktor', 'Joshua', 'Joca', 'Mystery guest', 'A stray cat']

# a list of empty rooms, fill them!
# max nr of people: 4
aws_classroom = []
# max nr of people: 3
cs_classroom = []
# max nr of people: 6
library = []

# Write your code below this line:
obs_osdorp_building = Building("OBS Osdorp", Room("AWS Classroom", 4), Room("CS Classroom", 3), Room("Library", 6))

for partygoer in partygoers:
    if partygoer is not Participant:
        partygoer = Participant(partygoer)
    obs_osdorp_building.let_in(partygoer)

aws_classroom = obs_osdorp_building.get_room("AWS Classroom")
cs_classroom = obs_osdorp_building.get_room("CS Classroom")
library = obs_osdorp_building.get_room("Library")

obs_osdorp_building.vibe_check()
obs_osdorp_building.shuffle()
obs_osdorp_building.vibe_check()