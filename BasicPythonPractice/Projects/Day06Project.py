#Data Analyst for Car dealership company.

import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
class CarDataAnalyst:
    def __init__(self,brandMostCar,citymostExpCars,highestAvgPrice,modelMostFreq):
        self.brandMostCar = brandMostCar
        self.citymostExpCars = citymostExpCars
        self.highestAvgPrice = highestAvgPrice
        self.modelMostFreq = modelMostFreq

        self.BMC = None
        self.CMEC = None
        self.HAP = None
        self.MMF = None

        self.file = None

    def AnalyzeData(self):
        with open("../OtherFiles/CarDataReport.txt","w") as file2:
            file2.write("")
        self.BMC = pd.read_csv(self.brandMostCar)
        self.CMEC = pd.read_csv(self.citymostExpCars)
        self.HAP = pd.read_csv(self.highestAvgPrice)
        self.MMF = pd.read_csv(self.modelMostFreq)

    def VisualizeAndReportData(self):
        #Keep everything inside the 'with' block so the file stays open while writing
        with open("../OtherFiles/CarDataReport.txt","a") as file:
            file.write("Car Data Analyst Report\n")
            
            #1.Visualizing the Most Brand Cars
            mp.figure() # Creates a clean, separate figure for each plot
            mp.bar(x=self.BMC["brand"], height=self.BMC["mostcars"])
            mp.title("Cars per Brand")
            mp.show()
            
            #Find the row with the maximum cars to log it properly
            max_cars_idx = self.BMC["mostcars"].idxmax()
            max_brand = self.BMC.loc[max_cars_idx, "brand"]
            max_cars_count = self.BMC.loc[max_cars_idx,"mostcars"]
            file.write(f"Most Cars: {max_cars_count} | Brand: {max_brand}\n")
            
            #2.Visualizing the Most expensive cars in a city
            mp.figure()
            mp.bar(x=self.CMEC["city"],height=self.CMEC["expensivecars"])
            mp.title("Expensive Cars per City")
            mp.show()
            
            max_city_idx = self.CMEC["expensivecars"].idxmax()
            max_city = self.CMEC.loc[max_city_idx,"city"]
            max_city_count = self.CMEC.loc[max_city_idx,"expensivecars"]
            file.write(f"City with the most expensive Cars: {max_city} ({max_city_count} cars)\n")
            
            #3.Visualizing the Highest Average Price
            mp.figure()
            mp.bar(x=self.HAP["year"].astype(str),height=self.HAP["averageprices"]) 
            mp.title("Average Price per Year")
            mp.show()
            avg_price = self.HAP.groupby("year")["averageprices"].max()
            year = avg_price.idxmax()
            file.write(f"Year with Highest Average Price : {year} and the Average Price : {avg_price.max():.2f}\n")
            #4.Visualizing the Most Frequent Model
            mp.figure()
            mp.bar(x=self.MMF["model"],height=self.MMF["mostfrequentmodel"])
            mp.title("Most Frequent Models")
            mp.show()
            most_freq_model = self.MMF.groupby("model")["mostfrequentmodel"].max()
            max_model = most_freq_model.idxmax()
            file.write(f"Most Frequent Model : {max_model} and the Quantity : {most_freq_model.max()}\n")
            
            file.write("\n")
CarData = CarDataAnalyst("../StoreData/CarDataAnalystDatas/brandSellMostCars","../StoreData/CarDataAnalystDatas/citymostexpensivecars","../StoreData/CarDataAnalystDatas/highestaverageprices","../StoreData/CarDataAnalystDatas/modelmostfrequent")
CarData.AnalyzeData()
CarData.VisualizeAndReportData()
