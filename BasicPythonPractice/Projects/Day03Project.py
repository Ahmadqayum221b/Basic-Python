#Sales Data Analyzer.
import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

class DataAnalyzer:
    def __init__(self,fileName):
        self.fileName = fileName
        self.df = None
        self.products = []
        self.quantity = []
        self.topProduct = ""
        self.topSellingMonth = ""
        self.topQuantity = 0
        
    
    def analyzeData(self):
        self.df = pd.read_csv(self.fileName)
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        print("Analyzed Data successfully")

    #for selling the most, i would be using quantity over price.
    def TopSellingProduct(self):
        product_total = self.df.groupby("Product")["Quantity"].sum()
        self.topProduct = product_total.idxmax()
        print(self.topProduct)
    
    def TopQuantity(self):
        product_total = self.df.groupby("Product")["Quantity"].sum()
        self.topQuantity = product_total.max()
        print(self.topQuantity)

    def TopSellingMonth(self):
        month_HighestVal = self.df.groupby("Date")["Quantity"].max()
        self.topSellingMonth = month_HighestVal.idxmax()
        print(self.topSellingMonth)

    def TotalRevenue(self):
        total_revenue = (self.df["Quantity"] * self.df["Price"]).sum()
        print(f"Total Revenue: ${total_revenue:.2f}")
    
    def AverageSale(self):
        average_sale = (self.df["Quantity"] * self.df["Price"]).mean()
        print(f"Average Sale Value: ${average_sale:.2f}")

    def VisualizeTrends(self):
        #1.Monthly Trends
        monthly_sales = self.df.groupby(self.df["Date"].dt.to_period("M"))["Quantity"].sum()
        #Convert index periods to strings so matplotlib can display them easily
        monthly_sales.index = monthly_sales.index.astype(str)
        
        mp.plot(monthly_sales.index,monthly_sales.values,marker='o',color='b',linestyle='-')
        mp.title("Monthly Sales Trend (Quantity)")
        mp.xlabel("Month")
        mp.ylabel("Total Quantity Sold")
        mp.xticks(rotation=45)
        mp.tight_layout()  #Ensures no labels get cut off
        mp.savefig("../SavedPngs/monthly_sales_trend.png")
        mp.show()
        mp.clf()  #Clears the current plot to prepare for the next one
        
        #2.Product Sales Performance
        product_sales = self.df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
        
        mp.bar(product_sales.index, product_sales.values, color='skyblue')
        mp.title("Product Sales Breakdown")
        mp.xlabel("Product")
        mp.ylabel("Total Quantity Sold")
        mp.xticks(rotation=45)
        mp.tight_layout()
        mp.savefig("../SavedPngs/product_sales_comparison.png")
        mp.show()
        mp.clf()



DA = DataAnalyzer("../StoreData/Sales.csv")
DA.analyzeData()
DA.TopSellingProduct()
DA.TopQuantity()
DA.TopSellingMonth()
DA.TotalRevenue()
DA.AverageSale()
DA.VisualizeTrends()