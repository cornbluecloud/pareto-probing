from sklearn import datasets
import pathlib
import os
import numpy as np
import torch

X, y = datasets.make_classification(n_samples = 1000, n_features = 10, n_informative = 2, n_classes = 2)
# print(X[10])

train_cls_dict = {"X":X[:700], "y":y[:700]}
val_cls_dict = {"X":X[700:850], "y":y[700:850]}
test_cls_dict = {"X":X[850:], "y":y[850:]}

torch.save(train_cls_dict, "./data/cls/train-cls.pth")
torch.save(val_cls_dict, "./data/cls/dev-cls.pth")
torch.save(test_cls_dict, "./data/cls/test-cls.pth")