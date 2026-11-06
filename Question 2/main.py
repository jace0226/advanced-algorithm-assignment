from course import Course
from utils import get_valid_int, get_valid_level, build_sample_course_graph


def main():
    graph, course_lookup = build_sample_course_graph()

    while True:
        print("\n==== University Course Prerequisite System ====")
        print("1. View All Courses")
        print("2. View Course Details")
        print("3. View Prerequisites of a Course")
        print("4. View Courses Unlocked by a Course")
        print("5. Add a New Course On-Demand")
        print("6. View Course Profile")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        # 1. View All Courses
        if choice == "1":
            print("\nAvailable Courses:")
            all_courses = graph.getAllVertices()
            if not all_courses:
                print("No courses currently registered.")
            else:
                for idx, course in enumerate(all_courses, start=1):
                    print(f"{idx}. {course.courseCode} - {course.courseName} [{course.level.capitalize()}]")

        # 2. View Full Course Details
        elif choice == "2":
            code = input("Enter Course Code: ").strip().upper()
            if code in course_lookup:
                print("\n=== Course Details (Full View) ===")
                print(course_lookup[code].get_details(force_show_all=True))
            else:
                print(f"Error: Course code '{code}' not found!")

        # 3. View Prerequisites
        elif choice == "3":
            code = input("Enter Course Code: ").strip().upper()
            if code in course_lookup:
                target_course = course_lookup[code]
                prereqs = graph.listIncomingAdjacentVertex(target_course)

                print(f"\nPrerequisites for {target_course.courseCode} ({target_course.courseName}):")
                if prereqs:
                    for p in prereqs:
                        print(f" - {p.courseCode} ({p.courseName})")
                else:
                    print(" - None (No prerequisite courses required)")
            else:
                print(f"Error: Course code '{code}' not found!")

        # 4. View Unlocked Courses
        elif choice == "4":
            code = input("Enter Course Code: ").strip().upper()
            if code in course_lookup:
                source_course = course_lookup[code]
                unlocked = graph.getOutgoingAdjacentVertices(source_course)

                print(f"\nCourses unlocked by {source_course.courseCode} ({source_course.courseName}):")
                if unlocked:
                    for u in unlocked:
                        print(f" - {u.courseCode} ({u.courseName})")
                else:
                    print(" - None (Does not unlock any further courses)")
            else:
                print(f"Error: Course code '{code}' not found!")

        # 5. Add Course On-Demand
        elif choice == "5":
            code = input("Enter New Course Code (e.g., SE401): ").strip().upper()
            if code in course_lookup:
                print(f"Error: Course code '{code}' already exists!")
                continue

            name = input("Enter Course Name: ").strip()
            while not name:
                print("Error: Course name cannot be empty!")
                name = input("Enter Course Name: ").strip()

            credits = get_valid_int("Enter Credit Hours: ")
            level = get_valid_level("Enter Course Level (core/elective): ")
            grade = input("Enter Passing Grade (e.g., C, B): ").strip().upper() or "C"

            new_course = Course(code, name, credits, level, grade)
            graph.addVertex(new_course)
            course_lookup[code] = new_course
            print(f"Success: Course '{code}' added to graph successfully as a vertex!")

        # 6. Core / Elective Profile View
        elif choice == "6":
            code = input("Enter Course Code: ").strip().upper()
            if code in course_lookup:
                print("\n=== Course Profile View ===")
                # Standard view hides details for electives, shows full for core
                print(course_lookup[code].get_details(force_show_all=False))
            else:
                print(f"Error: Course code '{code}' not found!")

        # 7. Exit
        elif choice == "7":
            print("Exiting Course Prerequisite System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a choice between 1 and 7.")

if __name__ == "__main__":
    main()