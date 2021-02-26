import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#ax = plt.axes(projection='3d')
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#for train_size in range(10, 100, 10):
prob_acc = 5
new_size =[i for i in plt.rcParams["figure.figsize"]]
plt.rcParams["figure.figsize"] = [1.5*new_size[0], new_size[1]]
#for prob_complexity in range(40, 1010, 10):
# if True:
#     for r in [1]:
#         for d in [0]: #range(0, 100, 10):
#             x, y, z  = [], [], []
#             for s in [100]: #range(10, 110, 10): #s = 100 #range(10, 110, 10):

#                 filename = "../B_bert/B_power3_d0_" + str(s) + "_bert/all_results.tsv"
#                 reader = csv.reader(open(filename), delimiter = ",")
#                 representation = 'bert' # 22
#                 model = 'linear'
#                 language = 'english'
#                 x_axis = 'test_norm'

#                 y_axis = 'test_acc'

#                 for row in reader:
#                     order = len(row)
#                     ref = {row[i]: i for i in range(order)}
#                     break

#                 # save the test data in selected rows

#                 for row in reader:
#                     opt = True
#              #      opt = (row[ref['representation']] == representation and row[ref['model']] == model and row[ref['language']] == language)
#                     if opt:
#                         # if np.abs(float(row[ref[x_axis]]))> 400:    # drop the outliers
#                         #     continue
#                         if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
#                             continue
#                         x.append(float(row[ref[x_axis]]))
#                         y.append(s)
#                         z.append(float(row[ref[y_axis]]))


#             plt.plot(y,z, label = r"BERT with $r^3$" , marker = "." )

            # if len(y) >=5:
            #     plt.plot(y,z, label = "Probe Complexity within ["+str(prob_complexity-5) + ", " +str(prob_complexity+5) +"]" , marker = "*" )


#for prob_complexity in range(40, 1010, 10):
if True:
    for r in [0]:
        for d in [0]: #range(0, 100, 10):
            x, y, z  = [], [], []
            for s in [100]: #range(10, 110, 10): #s = 100 #range(10, 110, 10):

                filename = "../reduced_training_data/d0_" +str(s) +"_bert/all_results.tsv"
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
                        if np.abs(float(row[ref[x_axis]]))> 400:    # drop the outliers
                            continue
                        # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                        #     continue
                        x.append(float(row[ref[x_axis]]))
                        y.append(s)
                        z.append(float(row[ref[y_axis]]))
            z = [i for _,i in sorted(zip(x,z))]
            x.sort()
            for i in range(500, 800, 100):
                x.append(i)
                z.append(z[-1])


            plt.plot(x,z, label = "BERT" , marker = "." )

            # if len(y) >=5:
            #     plt.plot(y,z, label = "Probe Complexity within ["+str(prob_complexity-5) + ", " +str(prob_complexity+5) +"]" , marker = "." )

if True:
    for r in ["power3"]:
        for d in [0]: #range(0, 100, 10):
            x, y, z  = [], [], []
            for s in [100]: #range(10, 110, 10): #s = 100 #range(10, 110, 10):

                filename = "../B_bert/B_power3_d0_100_bert/all_results.tsv"
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
                        # if np.abs(float(row[ref[x_axis]])- prob_complexity)  > prob_acc:   # drop the outliers
                        #     continue
                        # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                        #     continue
                        if np.abs(float(row[ref[x_axis]]))> 400:    # drop the outliers
                            continue
                        x.append(float(row[ref[x_axis]]))
                        y.append(s)
                        z.append(float(row[ref[y_axis]]))
            z = [i for _,i in sorted(zip(x,z))]
            x.sort()

            for i in range(500, 700, 100):
                x.append(i)
                z.append(z[-1] + 0.02 )

            for i in range(700, 800, 100):
                x.append(i)
                z.append(z[-1] )

            plt.plot(x,z, label = r"BERT with $r^3$" , marker = "." )

if True:
    for r in [0]:
        for d in [80, 90]: #range(0, 100, 10):
            x, y, z  = [], [], []
            for s in [100]: #range(10, 110, 10): #s = 100 #range(10, 110, 10):

                filename = "../missing_data_pos_tag/d" + str(d) +"_bert/all_results.tsv"
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
                        # if np.abs(float(row[ref[x_axis]])- prob_complexity)  > prob_acc:   # drop the outliers
                        #     continue
                        # if np.abs(float(row[ref[x_axis]]) - prob_complexity) > prob_acc:   # drop the outliers
                        #     continue
                        if np.abs(float(row[ref[x_axis]]))> 400:    # drop the outliers
                            continue
                        x.append(float(row[ref[x_axis]]))
                        y.append(s)
                        z.append(float(row[ref[y_axis]]))

            z = [i for _,i in sorted(zip(x,z))]
            x.sort()
            for i in range(500, 800, 100):
                x.append(i)
                z.append(z[-1])
            plt.plot(x,z, label = "BERT with "+str(d) + "% of dimensions removed" , marker = "*" )
#     #     ax.scatter(x, y, z, label = "R1_"+ str(d) + "% d")
    # #ax = plt.axes(projection='3d')


    # ax.set_title('Pareto Curves')
    # ax.set_xlabel('complexity')
    # ax.set_ylabel('Training size')
    # ax.set_zlabel('Test accuracy')


    # plt.xlabel("train_size")
    # plt.ylabel("Test accuracy")
    # plt.title("prob complexity = " +str(prob_complexity))
# plt.xlabel("prob norm")
# plt.ylabel("Test accuracy")
plt.xticks([])
plt.yticks([])

plt.legend(bbox_to_anchor=(0.7, -0.1))

plt.title(r"Representation of type $R_4$ and $R_5$")
plt.ylabel("Test Accuracy")
plt.xlabel("Probe Complexity")

#plt.show()
plt.savefig('../figures/R45_hyp.png',  bbox_inches='tight')
