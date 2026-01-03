class AgentMemory:
    def __init__(self):
        self.logs = []

    def add(self, message):
        self.logs.append(message)

    def show(self):
        return self.logs
