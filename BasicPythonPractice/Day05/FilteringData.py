import pandas as pd
import matplotlib.pyplot as mp
class Filteration:
    def __init__(self,fileName):
        self.fileName = fileName
        self.df = None
    
    def FilterData(self):
        self.df = pd.read_csv(self.fileName)
        print(self.df)

    def VisualizeData(self):
        brandcounts = self.df["brand"].value_counts() #in here the brand column gets stored into brandcounts variable.
        #brandcounts.index gives you the names like Suzuki, Honda etc.
        #brandcounts.value gives you how much number do they have.
        mp.bar(x=brandcounts.index,height=brandcounts.values)
        mp.show()

F = Filteration("../StoreData/filteredcardata.csv")
F.FilterData()
F.VisualizeData()