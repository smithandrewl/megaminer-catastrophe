from games.catastrophe.fuzzy_data import *

class ExplorerData:
    def __init__(self):
        self.bushes = []
        self.structures = []
        self.visited_tiles = []




class GameData:
    def __init__(self):
        self.fuzzy_data = FuzzyData()
        self.explorer_data = ExplorerData()
        self.humans = []
        self.shelter_location = (0, 0)
