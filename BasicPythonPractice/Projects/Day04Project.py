#Employee Salary Analyzer.

#Find:
#Highest paid employee
#Lowest paid employee
#Average salary
#Department with highest average salary
#Visualize:
#Salary per employee
#Average salary per department
#Practice:
#Pandas GroupBy
#NumPy mean/max/min
#Bar charts
#OOP

import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

class EmpSalaryAnalyzer:
    def __init__(self,fileName):
        self.fileName = fileName
        self.df = None
        self.highestPaidEmployee = ""
        self.lowestPaidEmployee = ""
        self.AvgSalary = 0
        self.highestAvgDepSalary = 0
        self.Emps = []
        self.Salaries = []
        self.Deps = []
    
    def FetchData(self):
        self.df = pd.read_csv(self.fileName)
        self.Emps = self.df["Name"]
        self.Salaries = self.df["Salary"]
        self.Deps = self.df["Department"]
        print("Data Read Successfully")

    def Calculation(self):
        self.HighestPaidEmp()
        self.LowestPaidEmp()
        self.AverageSalary()
        self.DepartmentHighestAvgSalary()
        
    def HighestPaidEmp(self):
        highestPaidEmp = self.df.groupby("Name")["Salary"].max()
        self.highestPaidEmployee = highestPaidEmp.idxmax()
        print(self.highestPaidEmployee)

    def LowestPaidEmp(self):
        lowestPaidEmp = self.df.groupby("Name")["Salary"].min()
        self.lowestPaidEmployee = lowestPaidEmp.idxmin()
        print(self.lowestPaidEmployee)

    def AverageSalary(self):
        avgSalary = self.df.groupby("Name")["Salary"].sum()
        self.AvgSalary = np.mean(avgSalary)
        print(self.AvgSalary)

    def DepartmentHighestAvgSalary(self):
        
        depAvgSalary = self.df.groupby("Department")["Salary"].sum()
        self.highestAvgDepSalary = np.max(depAvgSalary)
        print(self.highestAvgDepSalary)
    
    def Visualization(self):
        self.SalaryPerEmp()
        self.AvgSalaryPerDep()
    
    def SalaryPerEmp(self):
        x = self.Emps
        y = self.Salaries
        mp.plot(x,y)
        mp.xlabel("Employees")
        mp.ylabel("Salaries")
        mp.title("Salary Per Employee")
        mp.savefig("../SavedPngs/SalaryPerEmployee.png")
        mp.show()
    
    def AvgSalaryPerDep(self):
        avg_salary_per_dep = self.df.groupby("Department")["Salary"].mean()
        x2 = avg_salary_per_dep.index   
        y2 = avg_salary_per_dep.values  
        
        mp.figure(figsize=(6,4))
        mp.bar(x2,y2,color='salmon')
        mp.xlabel("Department")
        mp.ylabel("Average Salaries")
        mp.title("Average Salary Per Department")
        mp.tight_layout()
        mp.savefig("../SavedPngs/AvgSalaryPerDepartment.png")
        mp.show()

try:
    E1 = EmpSalaryAnalyzer("../StoreData/EmployeeSalary.csv")
    E1.FetchData()
    E1.Calculation()
    E1.Visualization()

except:
    print("Invalid Data Getting Analyzed")
