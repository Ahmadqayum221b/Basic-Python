#Learning other libraries.
#1)-Plotly.
#plotly creates interactive graphs.
import plotly.express as px
data = {
    "Students" : ["Ahmad","Dua"],
    "Marks" : [40,80]
}

fig = px.bar(
    data,
    x="Students",
    y="Marks"
)
fig.show()

#2)-SciPy => it is used for scientific computing.
#it is basically an extended version of Numpy.
#heavily used in reasearch and M.L.
#it provides advanced mathematical tools.

from scipy import stats
data = [4,5,3,1,55]
print(stats.cauchy(data))

