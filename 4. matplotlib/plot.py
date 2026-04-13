import matplotlib.pyplot as plt
x=[2022,2023,2024,2025,2026]
y =[12,45,18,39,28]

plt.grid(linewidth=2, color="orange", linestyle="dashed") # by defualt it includes both x and y
# plt.grid(axis='x') 
# plt.grid(axis='y') 

plt.title("Population",fontsize=20, family="Arial",fontweight="bold",color="green")

plt.xlabel("Year", fontsize=10, family="Arial",fontweight="bold",color="red")
plt.ylabel("Numbers", fontsize=10, family="Arial",fontweight="bold",color="red")

plt.xticks(x) # instead the 0.5 increament in x axis, use the same x vlaue in the x axis
plt.tick_params(axis="both", colors="blue")

plt.plot(x,y, marker="*", markersize=10, markerfacecolor="red", markeredgecolor="black", linestyle="solid",linewidth=5, color="orange")
plt.show()