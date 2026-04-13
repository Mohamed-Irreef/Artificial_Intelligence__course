import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,0,1,1,2,3,3,4,5,8])
y1 = np.array([56,57,60,39,79,60,49,29,29,95])

x2=np.array([0,1,1,2,3,5,3,5,5,9])
y2=np.array([48,28,62,58,53,29,38,18,58,38])

plt.scatter(x1,y1, color="blue", s=100, alpha=0.5, label="Class A")
plt.scatter(x2,y2, color="green", s=100, alpha=0.5, label="Class B")
plt.legend()
plt.show()