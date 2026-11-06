from course import Course
from graph import Graph

def get_valid_int(prompt_text: str) -> int:
    """Prompts until a valid positive integer is entered."""
    while True:
        try:
            val = int(input(prompt_text))
            if val <= 0:
                print("Error: Input must be a positive integer!")
                continue
            return val
        except ValueError:
            print("Error: Invalid numeric input! Please enter an integer.")

def get_valid_level(prompt_text: str) -> str:
    """Prompts until user inputs either 'core' or 'elective'."""
    while True:
        level = input(prompt_text).strip().lower()
        if level in ["core", "elective"]:
            return level
        print("Error: Level must be either 'core' or 'elective'.")

def build_sample_course_graph():
    """
    Populates the graph with 6 predefined university courses and prerequisites.
    Graph direction: Prerequisite ---> Advanced Course
    Example: SE101 (Intro Programming) -> SE201 (Data Structures)
    """
    graph = Graph()
    course_lookup = {}  # Map courseCode (str) -> Course object

    # Define 6 initial courses (Requirement: Minimum 5, Maximum 10)
    c1 = Course("SE101", "Fundamentals of Software Development", 3, "core", "C")
    c2 = Course("SE102", "Discrete Mathematics for Computing", 3, "core", "C")
    c3 = Course("SE201", "Data Structures & Algorithms", 4, "core", "B")
    c4 = Course("SE202", "Object-Oriented Software Design", 3, "elective", "C")
    c5 = Course("SE301", "Software Architecture & Design Patterns", 4, "core", "B")
    c6 = Course("SE302", "Cloud Computing", 3, "elective", "C")

    courses = [c1, c2, c3, c4, c5, c6]

    # Step 1: Add vertices to graph
    for course in courses:
        graph.addVertex(course)
        course_lookup[course.courseCode] = course

    # Step 2: Establish Prerequisite connections (addEdge: prerequisite -> unlocked_course)
    # SE101 unlocks SE201 and SE202
    graph.addEdge(course_lookup["SE101"], course_lookup["SE201"])
    graph.addEdge(course_lookup["SE101"], course_lookup["SE202"])

    # SE102 unlocks SE201
    graph.addEdge(course_lookup["SE102"], course_lookup["SE201"])

    # SE201 unlocks SE301
    graph.addEdge(course_lookup["SE201"], course_lookup["SE301"])

    # SE202 unlocks SE302
    graph.addEdge(course_lookup["SE202"], course_lookup["SE302"])

    return graph, course_lookup