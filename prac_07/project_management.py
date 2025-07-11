"""
Word Occurrences
Estimate: 120 minutes
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
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        choice = input(MENU).lower()
    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save in ['yes', 'y']:
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


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
    out_file.close()


def display_projects(projects):
    print("Incomplete projects: ")
    for project in sorted([part for part in projects if not part.is_complete()]):
        print(f"  {project}")
    print("Completed projects: ")
    for project in sorted([part for part in projects if part.is_complete()]):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.start_date > filter_date]
    filtered.sort(key=get_start_date)
    for project in filtered:
        print(project)


def get_start_date(project):
    return project.start_date


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    i = 0
    for project in projects:
        print(f"{i} {project}")
        i += 1
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    new_completion_percentage = input("New Percentage: ")
    if new_completion_percentage != "":
        project.completion_percentage = int(new_completion_percentage)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


main()