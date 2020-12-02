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
        x, y, z  = [], [], []
        s = 100 #range(10, 110, 10):
        if True:
    #   filename = "../reduced_training_data/d0_" + str(p)+"_bert/all_results.tsv"
            filename = "../inverse_power/B_" + r +"_d"+ str(d)+"_100_bert/all_results.tsv"
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
                    if float(row[ref[x_axis]]) > 500:   # drop the outliers
                        continue
                    # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                    #     continue
                    x.append(float(row[ref[x_axis]]))
                    y.append(s)
                    z.append(float(row[ref[y_axis]]))
        # print(x)
        # print(z)
        if d == 80:
            plt.scatter(x,z, label = "R"+ str(r)+"_"+ str(d) , marker = "*")
        else:
            plt.scatter(x,z, label = "R"+ str(r)+"_"+ str(d))


    #    ax.plot(x, y, z, label = "R1_"+ str(d) + "% d")
    #ax = plt.axes(projection='3d')
if True:
    for d in [00]: #range(0, 100, 10):

        for r in [0]: #ange(3, 11):
            x, y, z  = [], [], []
            filename = "../multiple_bijections/R0" + str(r) +"_d0_" + str(s)+"_bert/all_results.tsv"

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
                    if float(row[ref[x_axis]]) > 500:   # drop the outliers
                        continue
                    # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                    #     continue
                    x.append(float(row[ref[x_axis]]))
                    y.append(s)
                    z.append(float(row[ref[y_axis]]))

            if d==0:
                plt.scatter(x,z, label = "R0"+ str(r)+"_"+str(d))
            # # else:
            #     plt.scatter(x,z, label = "R0"+ str(r)+"_"+str(d), marker = "*")
  ##      ax.plot(x, y, z, label = "R0_"+ str(d) + "% d")
if True:
    for d in range(80, 100, 10):

        if True:
            x, y, z  = [], [], []
            filename = "../missing_data_pos_tag/d" +str(d)+"_bert/all_results.tsv"

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
                    if float(row[ref[x_axis]]) > 500:   # drop the outliers
                        continue
                    # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                    #     continue
                    x.append(float(row[ref[x_axis]]))
                    y.append(s)
                    z.append(float(row[ref[y_axis]]))

            plt.scatter(x,z, label = "R0_"+str(d), marker = "*")
    # print(x)


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
