class StateMachine:
    def __init__(self, initial_state, game_data):
        self.game_data = game_data
        self.current_state = initial_state

    def update(self):
        new_state = self.current_state.update(self.game_data)

        self.current_state = new_state
