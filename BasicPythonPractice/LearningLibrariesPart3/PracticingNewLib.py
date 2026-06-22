#here i will be learning the new library.
#Seaborn.
#it is built on top of matplotlib.
#it is used for statistical Visualization.

#it makes good graphs with less code.

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as mp
data = {
    "Names": ["Ahmad","Dua","Ali","Sana","Zain","Fatima"],
    "Marks": [30, 40, 30, 50, 40, 30]
}
dataset = pd.DataFrame(data)
sb.histplot(data = dataset,x="Names",y="Marks")
mp.show()

#Why Seaborn.
#Seaborn is used to find patterns,trends and stories in your data through pictures.
#it is built specifically for data science and stats.