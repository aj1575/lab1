import csv
import hashlib
from datetime import datetime
import os  # Import the os module

class Student:
    def __init__(self, email, first_name, last_name, course_id, grade, marks):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grade = grade
        self.marks = int(marks)

    def to_list(self):
        return [self.email, self.first_name, self.last_name, self.course_id, self.grade, self.marks]

class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def to_list(self):
        return [self.course_id, self.course_name, self.description]

class Professor:
    def __init__(self, professor_id, name, rank, course_id):
        self.professor_id = professor_id
        self.name = name
        self.rank = rank
        self.course_id = course_id

    def to_list(self):
        return [self.professor_id, self.name, self.rank, self.course_id]

class LoginUser:
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    def to_list(self):
        return [self.email, self.password, self.role]

class CheckMyGrade:
    def __init__(self):
        self.students = []
        self.courses = []
        self.professors = []
        self.users = []
        self.base_path = "C:\\Users\\anura\\OneDrive\\Desktop\\Data 200\\lab1"  # Store the base path

        self.load_data()

    def load_data(self):
        self.load_students()
        self.load_courses()
        self.load_professors()
        self.load_users()

    def load_students(self):
        file_path = os.path.join(self.base_path, 'students.csv')  # Construct the full file path
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    self.students.append(Student(*row))
        except FileNotFoundError:
            print(f"Warning: 'students.csv' not found at {file_path}.  Creating an empty student list.")
            self.students = []

    def load_courses(self):
        file_path = os.path.join(self.base_path, 'courses.csv')
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    self.courses.append(Course(*row))
        except FileNotFoundError:
            print(f"Warning: 'courses.csv' not found at {file_path}.  Creating an empty course list.")
            self.courses = []

    def load_professors(self):
        file_path = os.path.join(self.base_path, 'professors.csv')
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    self.professors.append(Professor(*row))
        except FileNotFoundError:
            print(f"Warning: 'professors.csv' not found at {file_path}. Creating an empty professor list.")
            self.professors = []

    def load_users(self):
         file_path = os.path.join(self.base_path, 'login.csv')
         try:
             with open(file_path, 'r') as file:
                 reader = csv.reader(file)
                 next(reader, None)
                 for row in reader:
                     self.users.append(LoginUser(*row))
         except FileNotFoundError:
             print(f"Warning: 'login.csv' not found at {file_path}. Creating an empty user list.")
             self.users = []

    def add_student(self, student):
        self.students.append(student)
        # self.save_students() # Implement save_students later

    # def save_students(self):  #Implement save_students later

    def search_student(self, email):
        for student in self.students:
            if student.email == email:
                return student
        return None

    def get_average_score(self):
        if not self.students:
            return 0
        total = sum(student.marks for student in self.students)
        return total / len(self.students)

    def get_median_score(self):
        if not self.students:
            return 0
        sorted_marks = sorted(student.marks for student in self.students)
        mid = len(sorted_marks) // 2
        if len(sorted_marks) % 2 == 0:
            return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
        return sorted_marks[mid]

    def display_menu(self):
        while True:
            print("\nCheckMyGrade System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Add Professor")
            print("4. Display Students")
            print("5. Search Student")
            print("6. Show Statistics")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student_interactive()
            elif choice == '2':
                self.add_course_interactive()
            elif choice == '3':
                self.add_professor_interactive()
            elif choice == '4':
                self.display_students()
            elif choice == '5':
                email = input("Enter student email to search: ")
                student = self.search_student(email)
                if student:
                    print("Student Found:", student.to_list())
                else:
                    print("Student not found.")
            elif choice == '6':
                print("Average Score:", self.get_average_score())
                print("Median Score:", self.get_median_score())
            elif choice == '7':
                print("Exiting application...")
                break
            else:
                print("Invalid choice, please try again.")
                continue # Return to start of loop

    def add_student_interactive(self):
        email = input("Enter Email: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        course_id = input("Enter Course ID: ")
        grade = input("Enter Grade: ")
        marks = input("Enter Marks: ")
        self.add_student(Student(email, first_name, last_name, course_id, grade, marks))
        print("Student added successfully!")

    def add_course_interactive(self):
        course_id = input("Enter Course ID: ")
        course_name = input("Enter Course Name: ")
        description = input("Enter Description: ")
        self.add_course(Course(course_id, course_name, description))
        print("Course added successfully!")

    def add_professor_interactive(self):
        professor_id = input("Enter Professor ID: ")
        name = input("Enter Name: ")
        rank = input("Enter Rank: ")
        course_id = input("Enter Course ID: ")
        self.add_professor(Professor(professor_id, name, rank, course_id))
        print("Professor added successfully!")

    def add_course(self, course):
        self.courses.append(course)

    def add_professor(self, professor):
        self.professors.append(professor)

    def display_students(self):
        for student in self.students:
            print(student.to_list())

if __name__ == "__main__":
    app = CheckMyGrade()
    app.display_menu()
