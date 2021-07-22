import pandas as pd
import statistics
import plotly_express as px
import math
import numpy as np

df1 = pd.read_csv("./CSV Files/IceCream.csv")
temp = df1["Temperature"].tolist()
ice = df1["Ice-cream Sales( ₹ )"].tolist()
graph1 = px.scatter(x = temp, y = ice, title = "Ice-cream")
#graph1.show()

correlations1 = np.corrcoef(temp, ice)
print(correlations1[0,1])

df2 = pd.read_csv("./CSV Files/Coffee.csv")
coffee = df2["Coffee in ml"].tolist()
sleep = df2["sleep in hours"].tolist()
graph2 = px.scatter(x = coffee, y = sleep, title = "COFFEE")
#graph2.show()

correlations2 = np.corrcoef(coffee, sleep)
print(correlations2[0,1])

df3 = pd.read_csv("./CSV Files/TV.csv")
size = df3["Size of TV"].tolist()
time = df3["Average time spent watching TV in a week (hours)"].tolist()
graph3 = px.scatter(x = size, y = time, title = "TV")
#graph3.show()

correlations3 = np.corrcoef(size, time)
print(correlations3[0,1])

df4 = pd.read_csv("./CSV Files/School.csv")
marks = df4["Marks In Percentage"].tolist()
present = df4["Days Present"].tolist()
graph4 = px.scatter(x = marks, y = present, title = "School")
graph4.show()

correlations4 = np.corrcoef(marks, present)
print(correlations4[0,1])