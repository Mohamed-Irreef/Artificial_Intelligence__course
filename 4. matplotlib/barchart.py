import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits","Vegetables","Meat"])
label = np.array([3,4,5,2])

plt.title("Food")
plt.bar(categories,label, color="orange")
plt.xlabel("Items")
plt.ylabel("Ratings")
plt.show()