from enum import Enum


class State(Enum):
    IDLE = 1
    FIND_FOOD = 2
    FIND_STRUCTURE = 3
    FIND_SHELTER = 4
    FIND_CAT = 5
    FIND_HUMAN = 6
    ATTACK = 7
    DEFEND_CAT = 8


def update(self, job):
    if job == "gatherer":
        if state == State.IDLE:
            if energy.low:
                self.state = State.FIND_SHELTER
            else:
                self.state = State.FIND_FOOD
        elif state == State.FIND_SHELTER:
            if energy.high and not capacity.full:
                self.state = FIND_FOOD
        elif state == State.FIND_FOOD:
            if capacity.full or energy.low:
                self.state = State.FIND_SHELTER
    elif job == "constructor":
        if state == State.IDLE:
            if energy.low:
                self.state = State.FIND_SHELTER
            else:
                self.state = State.FIND_STRUCTURE
        elif state == State.FIND_SHELTER:
            if energy.high and not capacity.full:
                self.state = FIND_STRUCTURE
        elif state == State.FIND_STRUCTURE:
            if capacity.full or energy.low:
                self.state = State.FIND_SHELTER
    elif job == "missionary":
        if state == State.IDLE:
            if energy.low:
                self.state = State.FIND_SHELTER
            else:
                self.state = State.FIND_HUMAN
        elif state == State.FIND_SHELTER:
            if energy.high:
                self.state = FIND_HUMAN
        elif state == State.FIND_HUMAN:
            if energy.low:
                self.state = State.FIND_SHELTER
    elif job == "soldier":
        if state == State.IDLE:
            if cat.energy.low:
                self.state = State.DEFEND_CAT
            elif energy.low:
                self.state = State.FIND_SHELTER
            else:
                self.state = State.ATTACK
        elif state == State.FIND_SHELTER:
            if cat.energy.low:
                self.state = State.DEFEND_CAT
            elif energy.high:
                self.state = State.ATTACK
        elif state == State.ATTACK:
            if cat.energy.low:
                self.state = State.DEFEND_CAT
            elif energy.low:
                self.state = State.FIND_SHELTER
        elif state == State.DEFEND_CAT:
            if cat.energy.high:
                if energy.low:
                    self.state = State.FIND_SHELTER
                else:
                    self.state = State.ATTACK
    elif job == "fresh human":
        self.state = State.FIND_CAT

