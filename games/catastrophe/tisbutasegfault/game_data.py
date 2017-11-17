from games.catastrophe.tisbutasegfault.fuzzy_data import *

class ExplorerData:
    def __init__(self):
        self.bushes = []
        self.structures = []
        self.visited_tiles = set()


class EnemyData:
    def __init__(self):
        self.enemySoldierCount = 0
        self.enemyMissionaryCount = 0
        self.gathererCount = 0
        self.constructorCount = 0

        self.food = 0
        self.cat_location = (0,0)

        self.cat_shelters = []
        self.missionaries = []


class GameData:
    def __init__(self):
        self.fuzzy_data = FuzzyData()
        self.explorer_data = ExplorerData()
        self.humans = []
        self.shelter_location = (0, 0)
        road = []
        x = 7
        y = 0
        while (y < 26):
            road.append((x, y))
            y += 1
        x = 8
        y = 0
        while (y < 26):
            road.append((x, y))
            y += 1

