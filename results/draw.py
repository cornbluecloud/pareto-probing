import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

type = "pos_tag"
# type = "dep_label"
filename = "compiled_" + type + ".tsv"

reader = csv.reader(open(filename), delimiter = "\t")
representation = 'bert' # 22
model = 'linear'
language = 'english'
x_axis = 'test_rank'
y_axis = 'test_acc'


for row in reader:
    order = len(row)
    ref = {row[i]: i for i in range(order)}
    break

# save the test data in selected rows
x, y = [], []
for row in reader:

    opt = (row[ref['representation']] == representation and row[ref['model']] == model and row[ref['language']] == language)
    if opt:
        if float(row[ref[x_axis]]) > 300:   # drop the outliers
            continue
        x.append(row[ref[x_axis]])
        y.append(row[ref[y_axis]])
        # print (row[ref['test_rank']], row[ref['test_acc']])

# draw with x, y
# print x
plt.plot(x, y, marker = 'o', markersize = 5, label = "Original")

for p in range(10, 100, 10):
    filename = "../missing_data_pos_tag/d" + str(p)+"_bert/all_results.tsv"

    reader = csv.reader(open(filename), delimiter = ",")
    representation = 'bert' # 22
    model = 'linear'
    language = 'english'
    x_axis = 'test_rank'
    y_axis = 'test_acc'


    for row in reader:
    	order = len(row)
    	ref = {row[i]: i for i in range(order)}
    	break

    # save the test data in selected rows
    x, y = [], []
    for row in reader:
        opt = True
 #   	opt = (row[ref['representation']] == representation and row[ref['model']] == model and row[ref['language']] == language)
    	if opt:
    		if float(row[ref[x_axis]]) > 300:	# drop the outliers
    			continue
    		x.append(row[ref[x_axis]])
    		y.append(row[ref[y_axis]])
    		# print (row[ref['test_rank']], row[ref['test_acc']])

    # draw with x, y
    # print x
    plt.plot(x, y, marker = 'o', markersize = 5, label = str(p) + " percent dimension deleted")
plt.title('Pareto Curves')
plt.xlabel('complexity')
plt.ylabel('accuracy')
plt.legend()
plt.show()

