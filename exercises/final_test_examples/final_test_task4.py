# main class
class Student:
    def __init__(self, first_name, last_name, faculty_number, grade, enroll_year):
        self.first_name = first_name
        self.last_name = last_name
        self.faculty_number = faculty_number
        self.grade = grade
        self.enroll_year = enroll_year

    def display_info(self):
        return f"The student {self.first_name} {self.last_name} with faculty number: {self.faculty_number} ended with grade {self.grade} in year {self.enroll_year}"

# defining the list with students
students_list = []

student1 = Student("Petko", "Karaivanov", "123", 5, 2026)
student2 = Student("Ilia", "Ivanov", "102", 4.7, 2029)
student3 = Student("Milcho", "Kalaidjiev", "206", 5.99, 2030)

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

# operations
def sort_by_grade():
    students_list.sort(key = lambda student: student.grade, reverse = True)
    for student in students_list:
        print(student.display_info())

def list_by_year(year = 2026):
    for student in students_list:
        if student.enroll_year == year:
            print(student)

def best_students():
    students_list.sort(key = lambda student: student.grade, reverse = True)
    print(students_list[0])

def average_grade():
    sum_grades = 0
    for student in students_list:
        current_grade = float(student.grade)
        sum_grades += current_grade
    print(sum_grades / len(students_list))

def remove_lowest():
    students_list.sort(key = lambda student: student.grade, reverse = True)
    students_list.remove(students_list[-1])