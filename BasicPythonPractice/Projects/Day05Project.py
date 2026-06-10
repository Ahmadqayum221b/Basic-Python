#Steam Game Analytics Dashboard.
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb

class SteamGame:
    def __init__(self,fileName):
        self.fileName = fileName
        self.df = None
        self.highestRevGame = ""
        self.highestRatedGame = ""
        self.AvgRating = 0
        self.TotalRev = 0
        self.BestGenre = ""
        self.BestPlatform = ""

    def AnalyzeData(self):
        self.df = pd.read_csv(self.fileName)
        print("Data Analyzed Successfully")
        self.RevenueColumn()
    
    #Revenue Column Creation.
    def RevenueColumn(self):
        self.df["Revenue"] = self.df["CopiesSold"] * self.df["Price"]
        
    #Finding Highest Revenue Game.
    def HighestRevenueGame(self):
        highestRev = self.df.groupby("Game")["Revenue"].max()
        self.highestRevGame = highestRev.idxmax()
        self.MakeAFile(f"Highest Revenue Game : {self.highestRevGame}\n")
    
    #Finding Highest Rated Game.
    def HighestRatedGame(self):
        highestRated = self.df.groupby("Game")["Rating"].max()
        self.highestRatedGame = highestRated.idxmax()
        self.MakeAFile(f"Highest Rated Game : {self.highestRatedGame}\n")

    #Calculating the Average Rating.
    def CalculateAvgRating(self):
        avgRating = self.df.groupby("Game")["Rating"].sum()
        self.AvgRating = np.mean(avgRating)
        self.MakeAFile(f"Average Rating : {self.AvgRating:.2f}\n")

    #Calculating total revenue
    def CalculateTotalRevenue(self):
        self.TotalRev = np.sum(self.df["Revenue"])
        self.MakeAFile(f"Total Revenue : {self.TotalRev}\n")

    #finding the best genre
    def FindBestGenre(self):
        bestGen = self.df.groupby("Genre")["Revenue"].max()
        self.BestGenre = bestGen.idxmax()
        self.MakeAFile(f"Best Genre : {self.BestGenre}\n")
    
    #finding the best platform
    def FindBestPlatform(self):
        bestplat = self.df.groupby("Platform")["Revenue"].max()
        self.BestPlatform = bestplat.idxmax()
        self.MakeAFile(f"Best Platform : {self.BestPlatform}\n")

    #Creating visualization.
    def Visualization(self):
        #revenue per game.
        sb.barplot(data=self.df,x="Revenue",y="Game")
        mp.xlabel("Revenue")
        mp.ylabel("Game")
        mp.title("Revenue Per Game")
        mp.savefig("../SavedPngs/RevenuePerGame.png")
        mp.show()

        #Rating Distribution.
        sb.barplot(data=self.df,x="Rating",y="Game")
        mp.xlabel("Rating")
        mp.ylabel("Game")
        mp.title("Rating Per Game")
        mp.savefig("../SavedPngs/RatingPerGame.png")
        mp.show()

        #Genre Revenue
        sb.barplot(data=self.df,x="Revenue",y="Genre")
        mp.xlabel("Revenue")
        mp.ylabel("Genre")
        mp.title("Genre Revenue")
        mp.savefig("../SavedPngs/GenreRevenue.png")
        mp.show()

        #Rating Vs Copies Sold.
        sb.scatterplot(data=self.df,x="Rating",y="CopiesSold")
        mp.xlabel("Rating")
        mp.ylabel("CopiesSold")
        mp.title("Rating vs Copies Sold")
        mp.savefig("../SavedPngs/RatingVCopiesSold.png")
        mp.show()

    def MakeAFile(self,data):
        with open("../OtherFiles/SteamGameData.txt","a") as file:
            file.write(data)

SG = SteamGame("../StoreData/SteamGameData.csv")
SG.AnalyzeData()
SG.HighestRevenueGame()
SG.HighestRatedGame()
SG.CalculateAvgRating()
SG.CalculateTotalRevenue()
SG.FindBestGenre()
SG.FindBestPlatform()
SG.Visualization()