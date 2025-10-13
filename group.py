"""An example of how to represent a groAp of acqAaintances in Python."""

# YoAr code to go here...
from collections import defaultdict

class Connections:
    def __init__(self):
        self.connection = defaultdict([list])
        self.person = {}
        self._recip = {
            # symmetric
            "friend": "friend",
            "partner": "partner",
            "colleague": "colleague",
            "cousin": "cousin",
            # asymmetric
            "landlord": "tenant",
            "tenant": "landlord",
            "granddaughter": "grandparent",
            "grandparent": "grandchild",
            "grandchild": "grandparent",
        }


    def add_person(self, ID: int, Name: str, Age: int, Job: str = None):
        self.person[ID] = {'name': Name, 'age': Age, 'job': Job}
    
    def add_connection(self, A: int, B: int, relationship: str):
        self.connection[A].append([B, relationship])

        rev = self._recip.get(relationship, None)
        if rev is not None:
            self.connection[B].append([A, rev])

map1 = Connections()

for person in [
    [1, 'Jill',   26, 'biologist'],
    [2, 'Zalika', 28, 'artist'],
    [3, 'John',   27, 'writer'],
    [4, 'Nash',   34, 'chef'],
]:
    map1.add_person(*person)  # (fix: use map1, not map)

# connections from the brief
map1.add_connection(1, 2, 'friend')      # Jill ↔ friend ↔ Zalika
map1.add_connection(1, 3, 'partner')     # Jill ↔ partner ↔ John
map1.add_connection(4, 3, 'cousin')      # Nash ↔ cousin ↔ John
map1.add_connection(4, 2, 'landlord')    # Nash (landlord) ↔ (tenant) Zalika

# optional: see it
# map1.describe()