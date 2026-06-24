from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("../StoreData/Sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
encode = LabelEncoder()
df["Product"] = encode.fit_transform(df["Product"])
X = df[["Product","Quantity"]]
Y = df["Price"]
df.dropna()
x_train,x_test,y_train,y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42 #acts like a randomness locker, if we dont use this every loop will have randomvalue.
)
model = LinearRegression()
model.fit(x_train,y_train)
predictions = model.predict(x_test)
#The above one is the learning step.
#For Evaluation we do the following things.

mae = mean_absolute_error(y_test,predictions)
r2 = r2_score(y_test,predictions)
print(df.head())
print(df.info())
print("MAE : ",mae)
print("R2 : ",r2)