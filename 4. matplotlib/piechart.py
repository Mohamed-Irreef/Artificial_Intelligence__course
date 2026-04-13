import matplotlib.pyplot as plt
import numpy as np

categories = ["9th","10th", "11th","12th"]
values = [300,200,400,100] 
colors =["red","green","blue","yellow"]

plt.title("Pie Chart")
plt.pie(values, labels=categories, colors=colors, autopct="%1.1f%%", explode=[0,0,0,0.5], shadow=True, startangle=180)
plt.show()