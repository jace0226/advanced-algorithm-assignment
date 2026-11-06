class Course:
    """
    Represents a single University Course entity.
    Attributes:
        courseCode (str): Unique code identifier (e.g., 'SE101')
        courseName (str): Full title of the course
        creditHours (int): Number of credit units (e.g., 3, 4)
        level (str): Classification - 'core' or 'elective'
        passingGrade (str): Required grade to complete course (e.g., 'C', 'B')
    """
    def __init__(self, courseCode: str, courseName: str, creditHours: int, level: str, passingGrade: str = "C"):
        self.courseCode = courseCode.upper()
        self.courseName = courseName
        self.creditHours = creditHours
        self.level = level.lower()  # 'core' or 'elective'
        self.passingGrade = passingGrade

    def get_details(self, force_show_all: bool = False) -> str:
        """
        Advanced Feature b: For elective courses, standard profile displays only name/code,
        hiding internal details. For core courses (or when forced), shows all attributes.
        """
        if self.level == "elective" and not force_show_all:
            return (f"Course Code : {self.courseCode}\n"
                    f"Course Name : {self.courseName}\n"
                    f"Category    : Elective (Detailed stats hidden)")
        # Detailed output for core courses or forced full view
        return (f"Course Code   : {self.courseCode}\n"
                f"Course Name   : {self.courseName}\n"
                f"Credit Hours  : {self.creditHours}\n"
                f"Category      : {self.level.capitalize()}\n"
                f"Passing Grade : {self.passingGrade}")

    def __str__(self):
        return f"{self.courseCode} - {self.courseName}"
