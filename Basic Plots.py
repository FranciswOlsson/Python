#Basic Plots
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,50)
sinus = np.sin(x)

plt.plot(x,sinus)
plt.show()

plt.plot(x, sinus, "o")
plt.show()  #use plt.plot to get color / marker abbreviations


#Rapid multiplot
cosinus = np.cos(x)
plt.plot(x, sinus, "-b", x, sinus, "ob", x, cosinus, "-r", x, cosinus, "or")
plt.xlabel('this is x!')
plt.ylabel('this is y!')
plt.title('My First Plot')
plt.show()

#Step by step
plt.plot(x, sinus, label='sinus', color='blue', linestyle='--', linewidth=2)
plt.plot(x, cosinus, label='cosinus', color='red', linestyle='-', linewidth=2)
plt.legend()
plt.show()

#Scatter plots

