class Worker:
    def __init__(self, worker_num, fname, Iname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.Iname = Iname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        print(f"ID:{self.worker_num}, Names:{self.fname} {self.Iname}, Exp:{self.work_experience_company}, Salary:{self.salary}, Age:{self.age}")
    
    def salary_bonus(self):
        if 5 < self.work_experience_company < 10 :
            self.salary += self.salary * 0.015
        if self.work_experience_company < 5:
            self.salary += self.salary * 0.005
        if self.work_experience_company > 10:
            self.salary += self.salary * 0.02

workers_list = []
n = int(input("Enter the amount of workers: "))

while len(workers_list) < n:
    worker = Worker(worker_num=int(input("Enter a num: ")),
                    fname = str(input("Enter a first name: ")),
                    Iname = str(input("Enter a last name: ")),
                    work_experience_company=int(input("Enter a num: ")),
                    salary= float(input("Enter a num: ")),
                    age = int(input("Enter a num: "))
                    )
    worker.salary_bonus()
    worker.worker_information()
    workers_list.append(worker)


def search_by_num(workers_list = workers_list, worker_num = int(input("Enter a num: "))):
    found = False
    for w in workers_list:
        if w.worker_num == worker_num:
            found = True
            return True
    if not found:
        return False
    

def search_by_name_experience(workers_list = workers_list, fname = str(input("Enter the first name: ")), work_experience_company = int(input("Enter a num: "))):
    found = False
    for w in workers_list:
        if w.fname == fname and w.work_experience_company == work_experience_company:
            found = True
            li = [w.worker_info()]
            print(li)
    if not found:
        return False
    
def add_worker(workers_list = workers_list, worker = Worker(worker_num=int(input("Enter a num: ")),
                    fname = str(input("Enter a first name: ")),
                    Iname = str(input("Enter a last name: ")),
                    work_experience_company=int(input("Enter a num: ")),
                    salary= float(input("Enter a num: ")),
                    age = int(input("Enter a num: "))
                    )):
    worker.worker_information()
    workers_list.append(worker)

def remove_worker(worker_num = int(input("Enter a num: "))):
    found = False
    for w in workers_list:
        if w.worker_num == worker_num:
            found = True
            workers_list.remove(w)
            break
    if not found:
        print("Wrong worker_num!")
    else: 
        print("Information deleted!")
