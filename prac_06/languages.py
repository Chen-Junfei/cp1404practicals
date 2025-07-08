"""
Word Occurrences
Estimate: 5 minutes
Actual:   13 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create some ProgrammingLanguage objects and display their information."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print()

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()