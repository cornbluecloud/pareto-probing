import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
x, y, z  = [], [], []

for p in range(10, 20, 10):
    filename = "../reduced_training_data/d0_" + str(p)+"_bert/all_results.tsv"

    reader = csv.reader(open(filename), delimiter = ",")
    representation = 'bert' # 22
    model = 'linear'
    language = 'english'
    x_axis = 'test_norm'
    y_axis = 'test_acc'


    for row in reader:
        order = len(row)
        ref = {row[i]: i for i in range(order)}
        break

    # save the test data in selected rows
    z0= []
    for row in reader:
        opt = True
 #      opt = (row[ref['representation']] == representation and row[ref['model']] == model and row[ref['language']] == language)
        if opt:
            # if float(row[ref[x_axis]]) < 500:   # drop the outliers
            #     continue
            x.append(float(row[ref[x_axis]]))
            y.append(p)
            z.append(float(row[ref[y_axis]]))

            # print (row[ref['test_rank']], row[ref['test_acc']])

    # draw with x, y
    # print x
# print(x)

# ax = plt.axes(projection='3d')
# ax.scatter(x, y, z)
# ax.set_title('Pareto Curves')
# ax.set_xlabel('complexity')
# ax.set_ylabel('Training size')
# ax.set_zlabel('Test accuracy')

plt.plot(x,z, marker = 'o')
plt.xlabel("Prob Complexity")
plt.ylabel("Test accuracy")
plt.title(("Train size  = 0.1"))
plt.show()
