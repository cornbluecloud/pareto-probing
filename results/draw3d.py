import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# ax = plt.axes(projection='3d')
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#for train_size in range(10, 100, 10):
prob_acc = 5
#for prob_complexity in range(40, 310, 10):
for r in [ "power3"]: #[0.01, 0.1, 1, 10 ]:
    for d in [0]: #range(0, 100, 10):

        for s in range(10, 110, 10): #s = 100 #range(10, 110, 10):
            x, y, z  = [], [], []
            filename = "../B_bert/B_power3_d0_" +str(s) +"_bert/all_results.tsv"
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

            for row in reader:
                opt = True
         #      opt = (row[ref['representation']] == representation and row[ref['model']] == model and row[ref['language']] == language)
                if opt:
                    # if float(row[ref[x_axis]]) > 500:   # drop the outliers
                    #     continue
                    # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                    #     continue
                    x.append(float(row[ref[x_axis]]))
                    y.append(s)
                    z.append(float(row[ref[y_axis]]))

            plt.scatter(x,z, label = "Rpower3_"+ "training_size_"+str(s) )


    #    ax.plot(x, y, z, label = "R1_"+ str(d) + "% d")
    #ax = plt.axes(projection='3d')


    # ax.set_title('Pareto Curves')
    # ax.set_xlabel('complexity')
    # ax.set_ylabel('Training size')
    # ax.set_zlabel('Test accuracy')


    # plt.xlabel("train_size")
    # plt.ylabel("Test accuracy")
    # plt.title("prob complexity = " +str(prob_complexity))
plt.xlabel("prob norm")
plt.ylabel("Test accuracy")
plt.legend()
plt.show()
