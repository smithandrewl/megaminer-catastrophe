
from games.catastrophe.tisbutasegfault.fuzzy_logic import *

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

        self.enemy_overlord_is_well_guarded = FuzzyValue(0.0) # soldiers close to overlord
        self.upkeep_income_ratio_is_high = FuzzyValue(0.0) # enemy upkeep / income

        # strategies:
        #   slash supply lines (kill the gatherers)
        #   Kill all humans (kill the fresh humans so they cannot be converted)
        #   Build shelters near bushes
        #   Guard bushes
        #   Guard fresh humans from missionaries
        #   Takeover (build shelters near enemy bushes and snipe them)

        # Tips:
        #   Disguise soldiers until they are near their target