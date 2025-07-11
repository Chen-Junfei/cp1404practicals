"""
Word Occurrences
Estimate: 60 minutes
Actual:    minutes
"""

from project import  Project
import datetime

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> """

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)


def load_projects(filename):
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        if len(parts) == 5:
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    in_file.close()
    return projects


def save_projects(filename, projects):
    out_file = open(filename, 'w')
    out_file.write("Name    Start Date	Priority	Cost Estimate	Completion Percentage")
    for project in projects:
        out_file.write(project + '\n')
