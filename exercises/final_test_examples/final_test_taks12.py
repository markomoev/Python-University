class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades
    
    def add_grade(self):
        self.grades = int(input("Enter grade (whole number): "))

        if self.grades < 2 or self.grades > 6:
            print("The grade should be between 2 and 6!")

    def average(self):
        sum = 0
        for x in students_list:
            sum += x.grades
        if len(students_list) == 0:
            print("There are not grades!")
        else: 
            avg = sum / len(students_list)
            return avg

    def student_info(self):
        return f"ID:{self.student_id}, Name:{self.name}, Grade:{self.grades}"

    def __repr__(self):
        return self.student_info()

students_list = []
for i in range(2):
    s = Student(student_id=int(input("Enter id: ")), name=str(input("Enter name: ")), grades=0)
    s.add_grade()
    students_list.append(s)
print(students_list)

def add_student(students_list = students_list):
    for y in range(1):
        s = Student(student_id=int(input("Enter id: ")), name=str(input("Enter name: ")), grades=0)
        s.add_grade()
        students_list.append(s)
    print(students_list)

def add_grade_to_student(students_list = students_list, student_id = int(input("Enter the student id: "))):
    for s in students_list:
        if s  == student_id:
            s.grades = s.add_grade()
        else: 
            print("Student id could not be found!")

def print_all_students(students_list = students_list):
    for s in students_list:
        print(s)

def best_student(students_list = students_list):
    if not students_list:
        print("No students in the list.")
        return

    best_s = students_list[0]

    for s in students_list:
        if s.grades > best_s.grades:
            best_s = s
            
    print(f"The best student is: {best_s.name} with grade: {best_s.grades}")
