from enum import Enum


class State(Enum):
    IDLE = 1
    FIND_FOOD = 2
    FIND_STRUCTURE = 3
    FIND_SHELTER = 4
    FIND_CAT = 5
    FIND_HUMAN = 6
    ATTACK = 7
    DEFEND_SHELTER = 8
    DEFEND_CAT = 9


def gatherer_update(state):
    if state == State.IDLE:
        if energy.low:
            this.state = State.FIND_SHELTER
        else:
            this.state = State.FIND_FOOD
    elif state == State.FIND_SHELTER:
        if energy.high and not capacity.full:
            this.state = FIND_FOOD
    elif state == State.FIND_FOOD:
        if capacity.full or energy.low:
            this.state = State.FIND_SHELTER


def constructor_update(state):
    if state == State.IDLE:
        if energy.low:
            this.state = State.FIND_SHELTER
        else:
            this.state = State.FIND_STRUCTURE
    elif state == State.FIND_SHELTER:
        if energy.high and not capacity.full:
            this.state = FIND_STRUCTURE
    elif state == State.FIND_STRUCTURE:
        if capacity.full or energy.low:
            this.state = State.FIND_SHELTER


def evangelist_update(state):
    if state == State.IDLE:
        if energy.low:
            this.state = State.FIND_SHELTER
        else:
            this.state = State.FIND_HUMAN
    elif state == State.FIND_SHELTER:
        if energy.high:
            this.state = FIND_HUMAN
    elif state == State.FIND_HUMAN:
        if energy.low:
            this.state = State.FIND_SHELTER


def soldier_update(state):
    if state == State.IDLE:
        if cat.energy.low:
            this.state = State.DEFEND_CAT
        elif energy.low:
            this.state = State.FIND_SHELTER
        else:
            this.state = State.ATTACK
    elif state == State.FIND_SHELTER:
        if cat.energy.low:
            this.state = State.DEFEND_CAT
        elif energy.high:
            this.state = State.ATTACK
    elif state == State.ATTACK:
        if cat.energy.low:
            this.state = State.DEFEND_CAT
        elif energy.low:
            this.state = State.FIND_SHELTER
    elif state == State.DEFEND_CAT:
        if cat.energy.high:
            if energy.low:
                this.state = State.FIND_SHELTER
            else:
                this.state = State.ATTACK


def human_update(self):
    self.state = State.FIND_CAT

