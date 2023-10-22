class Staff:
    def __init__(self, name, surname, pnumber, salary, langs):
        print("Staff init func")
        self.name = name
        self.surname = surname
        self.pnumber = pnumber
        self.salary = salary
        self.langs = langs

class Personal(Staff):
    def __init__(self, name, surname, pnumber, salary, langs, age, city):
        super().__init__(name, surname, pnumber, salary, langs)
        print("Personal init func")
        self.age = age
        self.city = city
class Editor(Staff):
    def editName(self,c_Name):
        print("Staff name changed!")
        self.name = c_Name
    def editSname(self,c_Sname):
        print("Staff name changed!")
        self.surname = c_Sname
    def editPnumber(self,c_Pnumber):
        print("Staff name changed!")
        self.pnumber = c_Pnumber
    def editSalary(self,c_Salary):
        print("Staff name changed!")
        self.salary = c_Salary
    def editLangs(self,c_Langs):
        print("Staff name changed!")
        self.langs.append(c_Langs)
    def updtSalary(self,u_Salary):
        print("Staff name changed!")
        self.salary += u_Salary

class manager(Editor,Personal,Staff):
    def __init__(self,name, surname, pnumber, salary, langs, age, city, deparment, position, workers):
        super().__init__(name, surname, pnumber, salary, langs, age,city)
        print("Manager init func")
        self.department = deparment
        self.position = position
        self.workers = workers

    def show(self):
        print("""
        < Staff DATA >

        Name :{}

        Surname :{}

        Phone Number :{}

        Salary :{}

        Languages :{}
        
        Age :{}
        
        City :{}
        
        Department :{}
        
        Position :{}
        
        Workers :{}
        """.format(self.name, self.surname, self.pnumber, self.salary, self.langs,self.age,self.city,self.department,self.position,self.workers))
