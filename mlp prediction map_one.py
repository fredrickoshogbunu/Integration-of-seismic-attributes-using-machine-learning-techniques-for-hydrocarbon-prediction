import csv
import matplotlib.pyplot as plt

highs_x = []
highs_y = []

lows_x = []
lows_y =[]

with open("H1_MLP_Data_label.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        if(row[2] == "1"):
            highs_x.append(float(row[0]))
            highs_y.append(float(row[1]))
            # print(row[2])

        else:
            lows_x.append(float(row[0]))
            lows_y.append(float(row[1]))
            # print(row[2])


lows = plt.scatter(lows_x, lows_y, c='red', s=35)

highs = plt.scatter(highs_x, highs_y, c='green' ,s=35)


plt.legend((lows, highs),
           ('Non Hydrocarbon', 'Hydrocarbon'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=12)


plt.title('MLP MODEL PREDICTION MAP')
plt.xlabel('x-coordinates')
plt.ylabel('y-coordinates')
plt.show()

