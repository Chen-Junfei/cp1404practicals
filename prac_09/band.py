class Band:

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def __str__(self):
        return f"{self.name} ({', '.join(str(member) for member in self.members)})"

    def play(self):
        for member in self.members:
            print(member.play())