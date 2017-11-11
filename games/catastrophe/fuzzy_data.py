
from games.catastrophe.fuzzy_logic import *

class FuzzyData:
    """
    A class to hold global fuzzy values.  The values should be updated/replaced every game update.
    """
    def __init__(self):
        """

        """
        self.decent_resources = FuzzyValue(0.0)
        self.decent_population = FuzzyValue(0.0)
        self.high_overlord_health = FuzzyValue(0.0)