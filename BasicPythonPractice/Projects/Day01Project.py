#Student Marks Manager (Mini Data system)

#Properties.

#Takes student names and marks
#Stores them using classes
#Uses loops to enter multiple students
#Handles wrong input using try/except
#Saves data into a file
#Reads and displays saved data

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        self._StoreData()
    def _init_(self):
        self
    
    def _StoreData(self):
        with open("../StoreData/StudentData.txt","a") as file:
            file.write(f"Student Name : {self.name}  And Student Marks : {self.marks}\n")

try:
    numberofstudents = int(input("Enter Number of Students : "))
    for i in range(numberofstudents):
        try:
            name = str(input("Enter Name : "))
            marks = float(input("Enter Marks : "))
            Std = Student(name,marks)
        except:
            print("Invalid Name or marks")
        wannaContinue = input("Wanna Continue : Y/N => ").strip().upper()
        if wannaContinue == 'Y':
            continue
        else:
            break
except:
    print("Invalid Credentials Entered")


with open("../StoreData/StudentData.txt","r") as file:
    print(file.read())
