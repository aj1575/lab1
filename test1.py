import csv
import time

# Class Definitions

class Student:
    def __init__(self, first_name, last_name, email, course_id, grade, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def display_records(self):
        print(f"{self.first_name} {self.last_name} | {self.email} | {self.course_id} | {self.grade} | {self.marks}")

    def check_my_grades(self):
        print(f"Grade: {self.grade}, Marks: {self.marks}")

    def update_student_record(self, grade, marks):
        self.grade = grade
        self.marks = marks

class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def display_courses(self):
        print(f"{self.course_id} | {self.course_name} | {self.description}")

class Professor:
    def __init__(self, name, email, rank, course_id):
        self.name = name
        self.email = email
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        print(f"{self.name} | {self.email} | {self.rank} | {self.course_id}")

class LoginUser:
    def __init__(self, email_id, password, role):
        self.email_id = email_id
        self.password = password
        self.role = role

    def Login(self, password):
        return self.password == password

    def Encrypt_password(self):
        cipher = TextSecurity(4)
        self.password = cipher.encrypt(self.password)

    def Decrypt_password(self):
        cipher = TextSecurity(4)
        return cipher.decrypt(self.password)

class TextSecurity:
    def __init__(self, shift):
        self.shifter = shift
        self.s = self.shifter % 26

    def _convert(self, text, s):
        result = ""
        for i, ch in enumerate(text):
            if ch.isupper():
                result += chr((ord(ch) + s - 65) % 26 + 65)
            else:
                result += chr((ord(ch) + s - 97) % 26 + 97)
        return result

    def encrypt(self, text):
        return self._convert(text, self.shifter)

    def decrypt(self, text):
        return self._convert(text, 26 - self.s)

# File Handling Functions

def load_students(file_path):
    students = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:
                students.append(Student(row[1], row[2], row[0], row[3], row[4], int(row[5])))
    return students

def load_courses(file_path):
    courses = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:
                courses.append(Course(row[0], row[1], row[2]))
    return courses

def load_professors(file_path):
    professors = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:
                professors.append(Professor(row[0], row[1], row[2], row[3]))
    return professors

def load_logins(file_path):
    logins = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:
                logins.append(LoginUser(row[0], row[1], row[2]))
    return logins

# Search Functionality

def search_students(students, search_term):
    start_time = time.time()
    found = [student for student in students if search_term.lower() in student.first_name.lower() or search_term.lower() in student.last_name.lower()]
    end_time = time.time()
    print(f"Search completed in {end_time - start_time} seconds.")
    return found

def search_courses(courses, search_term):
    start_time = time.time()
    found = [course for course in courses if search_term.lower() in course.course_name.lower()]
    end_time = time.time()
    print(f"Search completed in {end_time - start_time} seconds.")
    return found

# Sorting Functionality

def sort_students(students, sort_by="email"):
    return sorted(students, key=lambda student: getattr(student, sort_by))

def sort_courses(courses, sort_by="course_name"):
    return sorted(courses, key=lambda course: getattr(course, sort_by))

# Login Functionality

def login_user(logins, email, password):
    for login in logins:
        if login.email_id == email:
            if login.Login(password):
                print("Login successful!")
                return login
    print("Invalid login credentials.")
    return None

# Main Function

def main():
    # Load Data
    students = load_students(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\students.csv")
    courses = load_courses(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\courses.csv")
    professors = load_professors(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\professors.csv")
    logins = load_logins(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv")
    
    # Ask user for their role
    role = input("Are you a student or professor? (Enter 'student' or 'professor'): ").strip().lower()
    email = input(f"Enter your {role} email ID: ").strip()
    password = input(f"Enter your {role} password: ").strip()

    # Validate Login
    user = login_user(logins, email, password)
    
    if user is None:
        return  # Exit if login fails

    # Check Role and Proceed
    if user.role == "student":
        print("\nStudent Dashboard")
        student_found = False
        for student in students:
            if student.email == email:
                student_found = True
                student.check_my_grades()
                break
        if not student_found:
            print("Student not found.")

    elif user.role == "professor":
        print("\nProfessor Dashboard")
        professor_found = False
        for professor in professors:
            if professor.email == email:
                professor_found = True
                professor.professors_details()
                break
        if not professor_found:
            print("Professor not found.")
    
    # Example functionality for searching and sorting
    print("\nSearch for Students with term 'Sam':")
    found_students = search_students(students, "Sam")
    for student in found_students:
        student.display_records()

    print("\nSorted Students by Email:")
    sorted_students = sort_students(students, "email")
    for student in sorted_students:
        student.display_records()

    print("\nSearch for Courses with term 'Data Science':")
    found_courses = search_courses(courses, "Data Science")
    for course in found_courses:
        course.display_courses()

    print("\nSorted Courses by Name:")
    sorted_courses = sort_courses(courses, "course_name")
    for course in sorted_courses:
        course.display_courses()

if __name__ == '__main__':
    main()
