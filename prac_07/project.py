"""
Word Occurrences
Estimate: 5 minutes
Actual:   10 minutes
"""
import datetime

class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a project from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        return self.completion_percentage == 100

    def __lt__(self, other):
        return self.priority < other.priority

    def convert_to_string(self):
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"