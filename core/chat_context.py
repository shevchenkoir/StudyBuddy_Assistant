class ConversationHistory:
    def __init__(self):
        self.history = []

    def add_turn(self, question, answer):
        self.history.append((question, answer))

    def get_history(self, max_turns=5):
        return self.history[-max_turns:]

    def clear(self):
        self.history = []