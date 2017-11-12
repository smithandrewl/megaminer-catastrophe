# This is where you build your AI for the Catastrophe game.

from joueur.base_ai import BaseAI
from games.catastrophe.tile import *

import random



from games.catastrophe.fuzzy_data import *
from games.catastrophe.fuzzy_logic import *
from games.catastrophe.state_machine import *
from games.catastrophe.game_data import *

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The basic AI functions that are the same between games. """

    def get_name(self):
        """ This is the name you send to the server so your AI will control the player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Tis But a Segfault" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its playerID and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        self.game_data = GameData()

        self.random = random.random()
        # <<-- /Creer-Merge: start -->>

        self.game_data.humans = [human for human in self.player.units if human.job.title == 'fresh human']

        self.first_run = True



    def game_updated(self):
        """ This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic



        self.game_data.fuzzy_data.high_overlord_health = grade_membership(self.player.cat.energy, 50, 100)
        self.game_data.fuzzy_data.decent_population = grade_membership(len(self.player.units), 0, 3)
        self.game_data.fuzzy_data.decent_resources = grade_membership(self.player.food, 30, 100)

        protect_the_king = self.game_data.fuzzy_data.decent_population.\
            fuzzyAnd(self.game_data.fuzzy_data.decent_resources).\
            fuzzyAnd(self.game_data.fuzzy_data.high_overlord_health.fuzzyNot())

        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why you won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn

        if self.first_run:
            self.game_data.humans[0].change_job("soldier")
            self.game_data.humans[1].change_job("missionary")
            self.game_data.humans[2].change_job("gatherer")

            self.first_run = False

        neighbors = self.game_data.humans[2].tile.get_neighbors()


        free_neighbors = []

        for neighbor in neighbors:
            not_a_unit_or_a_structure = (neighbor.unit is None) and (neighbor.structure is None)
            is_a_road = (neighbor.structure != None) and (neighbor.structure.type == "road")
            unexplored = neighbor not in self.game_data.explorer_data.visited_tiles
            can_occupy = not_a_unit_or_a_structure or is_a_road and unexplored

            if can_occupy:
                free_neighbors.append(neighbor)


        if len(free_neighbors) == 0:
            self.game_data.explorer_data.visited_tiles = []
        else:
            dest = free_neighbors[random.randint(0, len(free_neighbors) - 1)]


            if dest.harvest_rate != 0:
                self.game_data.explorer_data.bushes.append((dest.x, dest.y))
                print("Bush found at (" + str(dest.x) + ", " + str(dest.y) + ")")

            self.game_data.explorer_data.visited_tiles.append((dest.x, dest.y))
            self.game_data.humans[2].move(dest)

        return True
        # <<-- /Creer-Merge: runTurn -->>

    def find_path(self, start, goal):
        """A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.
        Args:
            start (Tile): the starting Tile
            goal (Tile): the goal Tile
        Returns:
            list[Tile]: A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.
        """

        if start == goal:
            # no need to make a path to here...
            return []

        # queue of the tiles that will have their neighbors searched for 'goal'
        fringe = []

        # How we got to each tile that went into the fringe.
        came_from = {}

        # Enqueue start as the first tile to have its neighbors searched.
        fringe.append(start)

        # keep exploring neighbors of neighbors... until there are no more.
        while len(fringe) > 0:
            # the tile we are currently exploring.
            inspect = fringe.pop(0)

            # cycle through the tile's neighbors.
            for neighbor in inspect.get_neighbors():
                # if we found the goal, we have the path!
                if neighbor == goal:
                    # Follow the path backward to the start from the goal and return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's neighbors to be inspected

                # if the tile exists, has not been explored or added to the fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and neighbor.is_pathable():
                    # add it to the tiles to be explored and add where it came from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where you want to go.
        #   in that case, we'll just return an empty path.
        return []

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
