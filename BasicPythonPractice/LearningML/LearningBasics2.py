from sklearn.preprocessing import LabelEncoder #this will be for converting string into numbers.
from sklearn.model_selection import train_test_split #for splitting data in test and train.
from sklearn.linear_model import LinearRegression #importing linear Regression.
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score,root_mean_squared_error
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

class EvaluateModel:
    def __init__(self,fileName):
        self.fileName = fileName
        self.df = None
        self.x = self.y = None
        self.x_test = self.y_test = self.x_train = self.y_train = None
        self.prediction = None
        self.model = None
        self.mae = None
        self.mse = None
        self.r2 = None
        self.rmse = None

    def LoadData(self):
        self.df = pd.read_csv(self.fileName)
        print("-------Data Loaded Sucessfully---------")

    def CleanData(self):
        self.df = self.df.dropna() #we are dropping those data that have null references.
        print("------Data Cleaned Successfully--------")
        print(self.df.head(10))

    def InitializeInputOutput(self):
        #for input date,product,quantity.
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df["Day"] = self.df["Date"].dt.day
        self.df["Month"] = self.df["Date"].dt.month
        self.df["Year"] = self.df["Date"].dt.year
        print(self.df.head(20))
        self.CleanCurrencyColumn("Unit Price")
        self.CleanCurrencyColumn("Revenue")
        self.CleanCurrencyColumn("Shipping Cost")
        self.CleanCurrencyColumn("Profit")
        self.CleanPercentageColumn("Discount %")
        
        self.x = self.df[
        [
            "Day",
            "Month",
            "Year",
            "Quantity",
            "Unit Price",
            "Discount %",
            "Shipping Cost"
        ]]
        self.y = self.df["Profit"]

    def ModelFitting(self):
        self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(
            self.x,
            self.y,
            test_size=0.2, #80% train, 20% test.
            random_state=42 #for locking to not be random.
        )
        self.model = LinearRegression()
        print(self.x.dtypes)
        print(self.x.head())
        self.model.fit(self.x_train,self.y_train) #fitting the training data into the linear regression model.

    def Prediction(self):
        self.prediction = self.model.predict(self.x_test) #for predicting we use testing input data.
        print(self.prediction)

    def EvaluatingTheModel(self):
        #MAE and MSE.
        #for evaluating the model the parameters are the y testing data.
        #and the prediction result.
        self.mae = mean_absolute_error(self.y_test,self.prediction)
        self.mse = mean_squared_error(self.y_test,self.prediction)
        self.r2 = r2_score(self.y_test,self.prediction)
        self.rmse = root_mean_squared_error(self.y_test,self.prediction)
        self.DisplayData()

    def CleanCurrencyColumn(self, columnName):
        self.df[columnName] = (
            self.df[columnName]
            .str.replace("$","",regex=False)
            .str.replace(",","",regex=False)
            .astype(float)
        )
        
    def CleanPercentageColumn(self, columnName):
        self.df[columnName] = (
            self.df[columnName]
            .str.replace("%","",regex=False)
            .str.replace(",","",regex=False)
            .astype(float)
        )

    def DisplayData(self):
        print(f"MAE : {self.mae:.2f}")
        print(f"MSE : {self.mse:.2f}")
        print(f"R2 Score : {self.r2:.2f}")
        print(f"RMSE : {self.rmse:.2f}")
        


EM = EvaluateModel("../StoreData/SalesData.csv")

EM.LoadData() #First step is to load data.
EM.CleanData() #Second step is to clean data.
EM.InitializeInputOutput() #third step is to Initialize the inputs and outputs (features)
EM.ModelFitting() #fourth step is to fit the features and the output into the model, the test data.
EM.Prediction() #fifth step is to do the prediction.
EM.EvaluatingTheModel() #sixth step is to evaluate the model.