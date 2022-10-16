import pandas as pd
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation


#Loading the excel file
path = 'Insert File Path here'
df = pd.read_excel(path)
#Renaming the Column
df.rename(columns = {'Unnamed: 0':'Year'}, inplace = True)

#Getting Data ready for Animation

year = df['Year']
cols = df.columns.to_list()

counter = count(0,1)

#X is for X axis and Y is for Y axis
x = []
y = []

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

#making the animation function
def animate(i):
    idx = next(counter)
    if idx < len(df):
        x.append(year[idx])
        y.append(df.iloc[idx, 1])
        
        #clearing the axis
        plt.cla()
        
        #Plotting and Plot editing
        ax.plot(x , y, label = cols[1])
        ax.set_title('GINI Index Mean', weight = 'bold')
        ax.set_xlabel('Time (Years)')
        ax.set_ylabel('GINI Index')
        ax.legend(loc = 'upper right')
        ax.set_ylim((0,50))

#Showing the animation
ani = FuncAnimation(fig = fig, func = animate, frames= 100)
plt.show()
