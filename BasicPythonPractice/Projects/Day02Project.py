#Student performance analyzer.
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

class StudentAnalyzer:
    def __init__(self,fileName):
        self.fileName = fileName
        self.df = None
        self.subjects = []
        self.maxScores = []

    def ReadData(self):
        self.df = pd.read_csv(self.fileName)
        print("Data Retrieved Successfully")

    def CalculateResult(self):
        self.df["Result"] = (
            self.df["Maths"] +
            self.df["Physics"] + 
            self.df["Science"]
        )
        self.df["Average"] = self.df["Result"] / 3

    def MaxScores(self):
        max_maths = self.df["Maths"].max()
        max_physics = self.df["Physics"].max()
        max_science = self.df["Science"].max()

        self.subjects = ["Maths", "Physics", "Science"]
        self.maxScores = [max_maths, max_physics, max_science]
        
    def VisualizeResult(self):
        
        mp.figure() 
        mp.bar(self.df["Name"], self.df["Average"], color="skyblue")
        mp.title("Average Scores per Student")
        mp.show()

        mp.figure()
        mp.bar(self.subjects, self.maxScores, color="salmon")
        mp.title("Highest Score per Subject")
        mp.show()
        


SA = StudentAnalyzer("../StoreData/StudentAnalyzer.csv")
SA.ReadData()
SA.CalculateResult()
SA.MaxScores()
SA.VisualizeResult()

