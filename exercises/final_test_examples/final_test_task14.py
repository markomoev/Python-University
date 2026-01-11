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
        return f"ID: {self.i_num} Name: {self.fname}, {self.Iname} Work experience: {self.work_experience} Education level: {self.education_level} Salary: {self.salary} Age: {self.age}"
    
    def __repr__(self):
        return self.display_info()
    
    def bonus(self):
        self.salary += (self.salary * 1.012) * self.work_experience
        if self.education_level == "University":
            self.salary *= 1.05
        if self.education_level == "High School":
            self.salary = self.salary * (102/100)

employee_list = []
n = int(input("Enter a number for the employees: "))

while len(employee_list) < n:
    emp = Employee(
        i_num = int(input("Enter the ID: ")),
        fname = str(input('Enter the first name: ')),
        Iname = str(input("Enter the last name: ")),
        work_experience = int(input("Enter the years of work exp: ")),
        education_level = str(input("Enter your education level: ")),
        salary = int(input("Enter your initial salary: ")),
        age = int(input("Enter your age: "))
    )
    emp.bonus()
    employee_list.append(emp)
print(employee_list)

def sort_employee(employee_list = employee_list):
    employee_list.sort(key=lambda x: x.age)
    print("Sorted by age:", employee_list)

def search_by_name(employee_list = employee_list,
                    name = str(input("Enter the first name: ")),
                    Iname = str(input("Enter the last name: "))):
    for e in employee_list:
        if e.fname == name and e.Iname == Iname:
            print(e)
        else:
            print("Not found!!!")

def print_by_education_experience(employee_list = employee_list,
                                  education = str(input("Enter the education level: ")),
                                  experience = int(input("Enter the years of experience"))):
    for e in employee_list:
        if e.education_level == education and e.work_experience == experience:
            print(e)

def remove_employee(employee_list = employee_list, i_num = int(input("Enter the id number: "))):
    for e in employee_list:
        if e.i_num == i_num:
            employee_list.remove(e)
        else: 
            print("Wrong i_num !!!")