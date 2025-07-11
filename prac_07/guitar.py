"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

class Guitar:
    """Represent a guitar object."""


    def __init__(self, name="", year=0, cost=0):
        """Construct a Guitar with given name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self, current_year):
        """Return age of a guitar object"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return ture if age of guitar greater than 50, False otherwise"""
        return self.get_age(current_year) >= 50
