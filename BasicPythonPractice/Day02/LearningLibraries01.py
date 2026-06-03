#In this we will be learning three kinds of libraries.
#Numpy.
#Pandas.
#Matplotlib.

#Numpy => Used for mathematical operations.
import numpy as np
arrayofNumbers = np.array([1,2,3,4])
print(arrayofNumbers.min())
print(arrayofNumbers.mean())
print(arrayofNumbers.max())


#Pandas => Data analysis.
import pandas as pd
data = {
    "Names" : ["Ahmad","Hassan","Faizan"],
    "Age" : [20,15,21]
}
dataset = pd.DataFrame(data)
print(dataset)
#Dataframe is basically used to convert the data into the excel form.
#most of the dataset use this.


#matplotlib => used for visualization (graphs or charts or plots or histograms)
import matplotlib.pyplot as mp
import numpy as np
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
y *= 2
mp.plot(x,y)
mp.show()
#that's basically line graph.
#for a bar graph look below.
names = ["Ahmad","Hamza","Asad"]
marks = [20,25,15]
mp.bar(names,marks)
mp.show()
