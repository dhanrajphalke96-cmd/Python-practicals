class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = 0

    def set_name(self,name):
        if name == "":
            print("name connot be empty")
        else :
            self.name = name       
    def get_name(self):
        return self.name
    def set_roll_no(self,roll_no):
        if roll_no <=0 and roll_no >= 101:
            print("Roll no has to be between 1 & 100")
        else :
            self.roll_no = roll_no


    def get_roll_no(self): 
        return self.roll_no

    def set_marks(self , marks):
        if marks < 0 :
            print("Marks connot be negative")
    def get_marks(self):
       return self.marks               

std1= Student()
print(std1.set_name("Dhanraj"))
print(std1.set_roll_no(69))
print(std1.set_marks(88))
print(std1.get_name())
print(std1.get_roll_no())
print(std1.get_marks())
