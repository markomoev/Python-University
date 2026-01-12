class Employee:
    def __init__(self, i_num, fname, Iname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.Iname = Iname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age

    def display_info(self):
        print(f"ID:{self.i_num}, Name:{self.fname} {self.Iname}, Exp:{self.work_experience}, Edu:{self.education_level}, Salary:{self.salary}, Age:{self.age}")

    def bonus(self):
        if self.education_level == "uni":
            self.salary *= 0.05
        if self.education_level == "high school":
            self.salary *= 0.02
        self.salary += (self.salary * self.work_experience) * (1.2/100)

employee_list = []
n = int(input("Enter the number of employees: "))

while len(employee_list) < n:
    emp = Employee(i_num=int(input("Enter a number: ")),
                   fname = str(input("Enter the first name: ")),
                   Iname = str(input("Enter the last name: ")),
                   work_experience= int(input("Enter a number: ")),
                   education_level=str(input("Enter a edu level: ")),
                   salary=float(input("Enter a number: ")),
                   age=int(input("Enter a number: "))
                   )
    emp.bonus()
    emp.display_info()
    employee_list.append(emp)

employee_list.sort(key=lambda a: a.age)
print("Sorted employee list (by age): ", employee_list)


def search_by_name(employee_list = employee_list, name = str(input("Enter a name: ")), Iname = str(input("Enter last name: "))):
    found = False
    for e in employee_list:
        if e.fname == name and e.Iname == Iname:
            e.display_info()
            found = True
    if not found: 
        print("Not found!")

def print_by_education_experience(employee_list = employee_list, education = str(input("Enter your education: ")), experience = int(input("Enter your experience: "))):
    found = False
    for e in employee_list:
        if e.education_level == education and e.work_experience == experience:
            e.display_info()
            found = True
    if not found:
        print("Not found!")

def remove_employee(employee_list = employee_list, i_num = int(input("Enter a number: "))):
    found = False
    for e in employee_list:
        if e.i_num == i_num:
            employee_list.remove(e)  
            found = True
    if found:
        print("Information deleted!")
    else:
        print("Wrong i_num!")
