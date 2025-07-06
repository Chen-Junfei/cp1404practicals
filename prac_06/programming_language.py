"""
Word Occurrences
Estimate: 10 minutes
Actual:   3 minutes
"""

class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""


    def __init__(self, name, typing, reflection, year):
        """Construct a programming language with given name, typing, reflection and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"

