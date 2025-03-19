import csv
import time
import getpass 
class Student:
    def __init__(self, first_name, last_name, email_address, courses=None, grades=None, marks=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.courses = courses if courses is not None else []
        self.grades = grades if grades is not None else []
        self.marks = marks if marks is not None else []
    def display_records(self):
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"Email: {self.email_address}")
        print("Courses and Grades:")
        for course, grade in zip(self.courses, self.grades):
            print(f"Course: {course}, Grade: {grade}")
    def add_new_student(self, student_list):
        if any(student.email_address == self.email_address for student in student_list):
            print(f"Student with email {self.email_address} already exists.")
        else:
            student_list.append(self)
            write_students_to_csv("students.csv", student_list)
            print(f"Student record for {self.first_name} {self.last_name} has been added successfully.") 
    def delete_new_student(self, student_list):
        student_list.remove(self)
        write_students_to_csv("students.csv", student_list)
        print(f"Student record for {self.first_name} {self.last_name} has been deleted successfully.") 
    def update_student_record(self, student_list, first_name=None, last_name=None, email_address=None, courses=None, grades=None, marks=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email_address:
            self.email_address = email_address
        if courses:
            self.courses = courses
        if grades:
            self.grades = grades
        if marks:
            self.marks = marks
        write_students_to_csv("students.csv", student_list)
    def check_my_grades(self):
        print(f"Grades for {self.first_name} {self.last_name}: {', '.join(map(str, self.grades))}")

    def check_my_marks(self):
        print(f"Marks for {self.first_name} {self.last_name}: {', '.join(map(str, self.marks))}")
class Course:
    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name
    def display_courses(self):
        print(f"Course ID: {self.course_id}, Course Name: {self.course_name}, Credits: {self.credits}")
    def add_new_course(self, course_list):
        if any(course.course_id == self.course_id for course in course_list):
            print(f"Course with ID {self.course_id} already exists.")
        else:
            course_list.append(self)
            write_courses_to_csv("courses.csv", course_list)
            print(f"Course {self.course_name} (ID: {self.course_id}) added successfully.")
    def delete_new_course(self, course_list):
        if self in course_list:
            course_list.remove(self)
            write_courses_to_csv("courses.csv", course_list)
            print(f"Course {self.course_name} (ID: {self.course_id}) deleted successfully.")
        else:
            print(f"Course with ID {self.course_id} not found.")
class Professor:
    def __init__(self, name, email_address, rank, course_id):
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id
    def professors_details(self):
        print(f"Professor: {self.name}, Rank: {self.rank}, Email: {self.email_address}")
        print(f"Teaches Course ID: {self.course_id}")
    def add_new_professor(self, professor_list):
        if any(professor.email_address == self.email_address for professor in professor_list):
            print(f"Professor with email {self.email_address} already exists.")
        else:
            professor_list.append(self)
            write_professors_to_csv("professors.csv", professor_list)
            print(f"Professor {self.name} (Email: {self.email_address}) added successfully.")
    def delete_professor(self, professor_list):
        if self in professor_list:
            professor_list.remove(self)
            write_professors_to_csv("professors.csv", professor_list)
            print(f"Professor {self.name} (Email: {self.email_address}) deleted successfully.")
        else:
            print(f"Professor with email {self.email_address} not found.")
    def modify_professor_details(self, professor_list, name=None, rank=None, course_id=None):
        if name:
            self.name = name
        if rank:
            self.rank = rank
        if course_id:
            self.course_id = course_id
        write_professors_to_csv("professors.csv", professor_list)
        print(f"Professor {self.name}'s details updated successfully.") 
    def show_course_details_by_professor(self, course_list):
        print(f"Courses taught by Professor {self.name}:")
        for course in course_list:
            if course.course_id == self.course_id:
                print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")
class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range
    def display_grade_report(self):
        print(f"Grade ID: {self.grade_id}, Grade: {self.grade}, Marks Range: {self.marks_range}")
    def add_grade(self, grade_list):
        if any(g.grade_id == self.grade_id for g in grade_list):
            print(f"Grade with ID {self.grade_id} already exists.")
        else:
            grade_list.append(self)
            write_grades_to_csv("grades.csv", grade_list)
            print(f"Grade {self.grade} (ID: {self.grade_id}) added successfully.")
    def delete_grade(self, grade_list):
        # Check if the grade exists by grade_id
        if self in grade_list:
            grade_list.remove(self)
            write_grades_to_csv("grades.csv", grade_list)
            print(f"Grade {self.grade} (ID: {self.grade_id}) deleted successfully.")
        else:
            print(f"Grade with ID {self.grade_id} not found.")
            
    def modify_grade(self, grade_list, new_grade, new_marks_range):
        self.grade = new_grade
        self.marks_range = new_marks_range
        write_grades_to_csv("grades.csv", grade_list)
        print(f"Grade {self.grade_id} has been modified successfully.")


# --- 5. LoginUser Class ---
class LoginUser:
    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def Login(self):
        print(f"User with email {self.email_id} logged in.")

    def Logout(self):
        print(f"User with email {self.email_id} logged out.")

    def Change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully.")

    def Encrypt_password(self):
        self.password = self.password[::-1]

    def Decrypt_password(self):
        self.password = self.password[::-1]
        
        
# Define the TextSecurity class
class TextSecurity:
    def __init__(self, shift):
        self.shift = shift
    
    def encrypt(self, text):
        """Simple Caesar cipher encryption"""
        result = ""
        for char in text:
            # Shift each character by the specified amount
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
            elif char.isdigit():
                # For digits, use a simple shift within 0-9
                result += str((int(char) + self.shift) % 10)
            else:
                # Keep non-alphanumeric characters as is
                result += char
        return result
    
    def decrypt(self, text):
        """Simple Caesar cipher decryption"""
        # For decryption, we use the negative of the shift value
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
            elif char.isdigit():
                # For digits, use a simple shift within 0-9
                result += str((int(char) - self.shift) % 10)
            else:
                # Keep non-alphanumeric characters as is
                result += char
        return result



# --- Utility Functions for Writing Data to CSV ---
def write_students_to_csv(file_name, student_list):
    with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\students.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Email", "Courses", "Grades", "Marks"])
        for student in student_list:
            writer.writerow([student.first_name, student.last_name, student.email_address, 
                             ', '.join(student.courses), ', '.join(map(str, student.grades)), 
                             ', '.join(map(str, student.marks))])

def write_courses_to_csv(file_name, course_list):
    with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\courses.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Course ID", "Course Name", "Credits"])
        for course in course_list:
            writer.writerow([course.course_id, course.course_name, course.credits])

def write_professors_to_csv(file_name, professor_list):
    with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\professors.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Professor Name", "Email", "Rank", "Course ID"])
        for professor in professor_list:
            writer.writerow([professor.name, professor.email_address, professor.rank, professor.course_id])

def write_grades_to_csv(file_name, grade_list):
    with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\grades.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Grade ID", "Grade", "Marks Range"])
        for grade in grade_list:
            writer.writerow([grade.grade_id, grade.grade, grade.marks_range])
            
def write_login_to_csv(file_name, user_list):
    """Write login information to CSV file"""
    with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User ID", "Password", "Role"])
        for user in user_list:
            writer.writerow([user["user_id"], user["password"], user["role"]])


# --- Utility Functions for Reading Data from CSV ---
def read_students_from_csv(file_name):
    student_list = []
    try:
        with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\students.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                first_name, last_name, email_address, courses_str, grades_str, marks_str = row
                courses = courses_str.split(", ") if courses_str else []
                
                # If grades are letters (like 'A', 'B', 'C'), leave them as strings
                grades = grades_str.split(", ") if grades_str else []  # No need to convert to int if they are letters
                marks = list(map(int, marks_str.split(", "))) if marks_str else []  # Marks should remain integers
                
                student_list.append(Student(first_name, last_name, email_address, courses, grades, marks))
    except FileNotFoundError:
        print(f"{file_name} not found, starting with an empty list.")
    return student_list


def read_courses_from_csv(file_name):
    course_list = []
    try:
        with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\courses.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                course_id, course_name, credits = row
                course_list.append(Course(course_id, credits, course_name))
    except FileNotFoundError:
        print(f"{file_name} not found, starting with an empty list.")
    return course_list

def read_professors_from_csv(file_name):
    professor_list = []
    try:
        with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\professors.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                name, email_address, rank, course_id = row
                professor_list.append(Professor(name, email_address, rank, course_id))
    except FileNotFoundError:
        print(f"{file_name} not found, starting with an empty list.")
    return professor_list

def read_grades_from_csv(file_name):
    grade_list = []
    try:
        with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\grades.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                grade_id, grade, marks_range = row
                grade_list.append(Grades(grade_id, grade, marks_range))
    except FileNotFoundError:
        print(f"{file_name} not found, starting with an empty list.")
    return grade_list

# Functions for reading/writing login data
def read_login_from_csv(file_name):
    """Read login information from CSV file"""
    user_list = []
    try:
        with open(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                user_id, password, role = row
                user_list.append({"user_id": user_id, "password": password, "role": role})
    except FileNotFoundError:
        print(f"{file_name} not found, starting with an empty list.")
    return user_list

# Mapping letter grades to numeric values
GRADE_MAP = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0
}

def get_numeric_grade(grade):
    """Convert letter grade to numeric grade."""
    return GRADE_MAP.get(grade.upper(), 0)  # Default to 0 if grade is not recognized


# --- Main Program ---
def main():
    # Read data from CSV files
    students = read_students_from_csv("student.csv")
    professors = read_professors_from_csv("professors.csv")
    courses = read_courses_from_csv("courses.csv")
    grades = read_grades_from_csv("grades.csv")
    user_list = read_login_from_csv(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv")  # Load existing users from file
    logged_in_user = None  # Keep track of the logged-in user
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Student")
        print("2. Professor")
        print("3. Exit")
        role = input("Choose your role: ")
        
        if role == "1":
            while True:  # Keep inside the student menu until the user chooses to go back
                print("\n--- Student Menu ---")
                print("1. Register")
                print("2. Login")
                print("3. Display My Records")
                print("4. Check My Grades")
                print("5. Check My Marks")
                print("6. Display Courses")
                print("7. show_course_details_by_professor")
                print("8. Back to Main Menu")
                
                student_choice = input("Enter your choice: ")
                
                if student_choice == "1":
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")
                    email = input("Enter your email address: ")

                    # Check if the email is already registered
                    if any(user['user_id'] == email for user in user_list):
                        print("Email is already registered. Please log in.")
                    else:
                        # Use getpass to mask the password input
                        password = getpass.getpass("Enter your password: ")  # Masked input: *************

                        # Encrypt the password before saving it
                        cipher = TextSecurity(4)
                        encrypted_password = cipher.encrypt(password)

                        # Register the user
                        user_list.append({"user_id": email, "password": encrypted_password, "role": "student"})
                        write_login_to_csv(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv", user_list)  # Write the updated list to the CSV file
                        print(f"Registration successful for student {first_name} {last_name} with email {email}.")
                elif student_choice == "2":
                    email = input("Enter your email: ")

                    # Use getpass to mask the password input
                    password = getpass.getpass("Enter your password: ")  # Masked input: *************

                    # Reload the user list from CSV to ensure it has the latest data
                    user_list = read_login_from_csv(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv")

                    # Check if the user exists
                    user = next((u for u in user_list if u['user_id'] == email), None)
                    if user:
                        # Decrypt the stored password and check if it matches
                        cipher = TextSecurity(4)
                        decrypted_password = cipher.decrypt(user['password'])
                        
                        if decrypted_password == password:
                            print(f"Student {email} logged in successfully.")
                            # Set a flag for the logged-in state
                            logged_in = True
                            logged_in_email = email
                            
                        else:
                            print("Incorrect password.")
                            # For debugging
                            print(f"Stored encrypted password: {user['password']}")
                            print(f"Decrypted password: {decrypted_password}")
                            print(f"Entered password: {password}")
                            
                    else:
                        print("User not found.")
                   
                            
                
                
                elif student_choice == "3":
                    
                    student_email = input("Enter your email to display records: ")
                    student_obj = next((s for s in students if s.email_address == student_email), None)
                    if student_obj:
                        student_obj.display_records()
                    else:
                        print("Student not found.")
                        
                elif student_choice == "4":
                    student_email = input("Enter your email to check grades: ")
                    student_obj = next((s for s in students if s.email_address == student_email), None)
                    if student_obj:
                        student_obj.check_my_grades()
                    else:
                        print("Student not found.")
                        
                elif student_choice == "5":
                    student_email = input("Enter your email to check marks: ")
                    student_obj = next((s for s in students if s.email_address == student_email), None)
                    if student_obj:
                        student_obj.check_my_marks()
                    else:
                        print("Student not found.")
                        
                elif student_choice == "6":
                    print("All available courses are:")
                    for course in courses:
                        course.display_courses()  # This will call the display_courses method
                        
                elif student_choice == "7":
                    # Display all professors with courses they teach
                    print("\n--- Professors and their Courses ---")
                    for professor in professors:
                        print(f"\nProfessor: {professor.name} (Email: {professor.email_address})")
                        # Display courses taught by the professor
                        professor.show_course_details_by_professor(courses)
                        
                elif student_choice == "8":  # Back to Main Menu
                    print("Returning to main menu...")
                    break  # Break the inner loop to go back to the Main Menu
                    
        elif role == "2":  # Professor Menu
            while True:  # Keep inside the professor menu until the user chooses to go back
                print("\n--- Professor Menu ---")
                print("1. Register")
                print("2. Login")
                print("3. Display Professor Details")
                print("4. Display Student Records")
                print("5. Display Grade Report")
                print("6. Add New Student")
                print("7. Delete Student")
                print("8. Update Student Record")
                print("9. Add New Course")
                print("10. Delete Course")
                print("11. Add Grade")
                print("12. Delete Grade")
                print("13. Modify Grade")
                print("14. Add New Professor")
                print("15. Delete Professor")
                print("16. Modify Professor Details")
                print("17. Search by Student")
                print("18. Sort by Student Marks")
                print("19. Back to Main Menu")
                
                professor_choice = input("Enter your choice: ")
                
                if professor_choice == "1":
                    name = input("Enter your name: ")
                    email = input("Enter your email address: ")

                    # Check if the email is already registered
                    if any(user['user_id'] == email for user in user_list):
                        print("Email is already registered. Please log in.")
                    else:
                        rank = input("Enter your rank: ")
                        course_id = input("Enter course ID: ")

                        # Use getpass to mask the password input
                        password = getpass.getpass("Enter your password: ")  # Masked input: *************

                        # Encrypt the password before saving it
                        cipher = TextSecurity(4)
                        encrypted_password = cipher.encrypt(password)

                        # Register the user
                        user_list.append({"user_id": email, "password": encrypted_password, "role": "professor"})
                        write_login_to_csv(r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv", user_list)  # Write the updated list to the CSV file
                        print(f"Registration successful for professor {name} with email {email}.")
                        
                elif professor_choice == "2":
                    email = input("Enter your email: ")
                    password = getpass.getpass("Enter your password: ")  # Masked input
    
                    # Define the login file path
                    login_file = r"C:\Users\anura\OneDrive\Desktop\Data 200\lab1\login.csv"
    
                    # Reload the user list from CSV to ensure it has the latest data
                    user_list = read_login_from_csv(login_file)

                    # Check if the user exists
                    user = next((u for u in user_list if u['user_id'] == email), None)
                    if user:
                        # Decrypt the stored password and check if it matches
                        cipher = TextSecurity(4)
                        decrypted_password = cipher.decrypt(user['password'])
                        if decrypted_password == password:
                            print(f"Professor {email} logged in successfully.")
                            # Set a flag for the logged-in state
                            logged_in = True
                            logged_in_email = email
                        else:
                            print("Incorrect password.")
                            # For debugging
                            print(f"Stored encrypted password: {user['password']}")
                            print(f"Decrypted password: {decrypted_password}")
                            print(f"Entered password: {password}")
                    else:
                        print("User not found.")
                
                elif professor_choice == "3":
                    professor_email = input("Enter email to display professor details: ")
                    professor_obj = next((p for p in professors if p.email_address == professor_email), None)
                    if professor_obj:
                        professor_obj.professors_details()
                    else:
                        print("Professor not found.")
                        
                elif professor_choice == "4":
                    # Display student records (for the professor)
                    #if logged_in_professor:
                        # Filter and display records for students associated with the logged-in professor
                    for student in students:
                            #if student.professor_email == logged_in_professor.email_address:
                        student.display_records()
                    #else:
                        #print("No professor logged in.")
                        
                elif professor_choice == "5":
                    student_email = input("Enter the student's email to view their grade report: ")
                        
                    # Find the student based on email
                    student_obj = next((s for s in students if s.email_address == student_email), None)
                    if student_obj:
                        print(f"\nGrade Report for {student_obj.first_name} {student_obj.last_name}:")
                        for course, grade, mark in zip(student_obj.courses, student_obj.grades, student_obj.marks):
                            print(f"Course: {course}, Grade: {grade}, Marks: {mark}")
                    else:
                        print("Student not found.")
                        
                elif professor_choice == "6":
                    first_name = input("Enter student's first name: ")
                    last_name = input("Enter student's last name: ")
                    email_address = input("Enter student's email: ")
                    new_student = Student(first_name, last_name, email_address)
                    new_student.add_new_student(students)
                    
                elif professor_choice == "7":
                    student_email = input("Enter student's email to delete: ")
                    student_obj = next((s for s in students if s.email_address == student_email), None)
                    if student_obj:
                        student_obj.delete_new_student(students)
                    else:
                        print("Student not found.")
                        
                elif professor_choice == "8":
                    student_email = input("Enter email to update student record: ")
                    student_obj = next((s for s in students if s.email_address == student_email), None)
                    if student_obj:
                        first_name = input("Enter new first name (or leave blank to keep current): ")
                        last_name = input("Enter new last name (or leave blank to keep current): ")
                        email_address = input("Enter new email (or leave blank to keep current): ")
                        courses = input("Enter new courses (comma separated): ").split(", ")

                        # Handling grades input (if they are numeric or letter grades)
                        grades_input = input("Enter new grades (comma separated): ").split(", ")
                        grades = []
                        for grade in grades_input:
                            grade = grade.strip()  # Remove leading/trailing whitespace
                            if grade.isnumeric():  # If it's numeric, convert to integer
                                grades.append(int(grade))
                            else:
                                grades.append(grade)  # Otherwise, keep as a string (for letter grades like 'A', 'B')

                        # Handling marks input (convert to integers)
                        marks_input = input("Enter new marks (comma separated): ").split(", ")
                        marks = list(map(int, marks_input))

                        # Update student record
                        student_obj.update_student_record(
                            students, 
                            first_name or student_obj.first_name,
                            last_name or student_obj.last_name,
                            email_address or student_obj.email_address,
                            courses or student_obj.courses,
                            grades or student_obj.grades,
                            marks or student_obj.marks
                        )
                        print(f"Student record for {student_obj.first_name} {student_obj.last_name} updated successfully.")

                    else:
                        print("Student not found.")
                    
                elif professor_choice == "9":
                    course_id = input("Enter course ID: ")
                    credits = input("Enter credits for the course: ")
                    course_name = input("Enter course name: ")
                    new_course = Course(course_id, credits, course_name)
                    new_course.add_new_course(courses)
                    
                elif professor_choice == "10":
                    course_id = input("Enter course ID to delete: ")
                    course_obj = next((c for c in courses if c.course_id == course_id), None)
                    if course_obj:
                        course_obj.delete_new_course(courses)
                    else:
                        print("Course not found.")
                        
                elif professor_choice == "11":
                    grade_id = input("Enter grade ID: ")
                    grade = input("Enter grade: ")
                    marks_range = input("Enter marks range: ")
                    new_grade = Grades(grade_id, grade, marks_range)
                    new_grade.add_grade(grades)
                    
                elif professor_choice == "12":
                    grade_id = input("Enter grade ID to delete: ")
                    grade_obj = next((g for g in grades if g.grade_id == grade_id), None)
                    if grade_obj:
                        grade_obj.delete_grade(grades)
                    else:
                        print("Grade not found.")
                        
                elif professor_choice == "13":
                    grade_id = input("Enter grade ID to modify: ")
                    grade_obj = next((g for g in grades if g.grade_id == grade_id), None)
                    if grade_obj:
                        new_grade = input("Enter new grade: ")
                        new_marks_range = input("Enter new marks range: ")
                        grade_obj.modify_grade(grades, new_grade, new_marks_range)
                    else:
                        print("Grade not found.")
                        
                elif professor_choice == "14":
                    name = input("Enter professor's name: ")
                    email_address = input("Enter professor's email: ")
                    rank = input("Enter professor's rank: ")
                    course_id = input("Enter course ID: ")
                    new_professor = Professor(name, email_address, rank, course_id)
                    new_professor.add_new_professor(professors)
                    
                elif professor_choice == "15":
                    professor_email = input("Enter professor's email to delete: ")
                    professor_obj = next((p for p in professors if p.email_address == professor_email), None)
                    if professor_obj:
                        professor_obj.delete_professor(professors)
                    else:
                        print("Professor not found.")
                        
                elif professor_choice == "16":
                    professor_email = input("Enter professor's email to modify details: ")
                    professor_obj = next((p for p in professors if p.email_address == professor_email), None)
                    if professor_obj:
                        name = input("Enter new name (leave blank to keep current): ")
                        rank = input("Enter new rank (leave blank to keep current): ")
                        course_id = input("Enter new course ID (leave blank to keep current): ")
                        professor_obj.modify_professor_details(professors, name or professor_obj.name,
                                                           rank or professor_obj.rank,
                                                           course_id or professor_obj.course_id)
                    else:
                        print("Professor not found.")
                        
                elif professor_choice == "17":
                    student_email = input("Enter student email to search: ")
                    # Start measuring time
                    start_time = time.time()

                    student_obj = next((s for s in students if s.email_address == student_email), None)
    
                    # Stop measuring time
                    end_time = time.time()

                    # Calculate the time taken
                    time_taken = end_time - start_time

                    if student_obj:
                        student_obj.display_records()
                    else:
                        print("Student not found.")
    
                    # Print the time taken for the search operation
                    print(f"Time taken to search: {time_taken * 1000:.6f} milliseconds")
                        
                elif professor_choice == "18":
                    # Sorting students by their average numeric grade (converted from letter grade)
                    students.sort(key=lambda x: sum(get_numeric_grade(grade) for grade in x.grades) / len(x.grades), reverse=True)
                    print("Students sorted by marks.")
                    for student in students:
                        avg_grade = sum(get_numeric_grade(grade) for grade in student.grades) / len(student.grades)
                        print(f"{student.first_name} {student.last_name} - Average Grade: {avg_grade:.2f}")
                        
                elif professor_choice == "19":  # Back to Main Menu
                    print("Returning to main menu...")
                    break  # Go back to the main menu
                
        elif role == "3":
            print("Exiting system.")
            break
        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
       
                        
                


# In[ ]:





# In[ ]:





# In[ ]:




