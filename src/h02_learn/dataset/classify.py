from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
import os

# from h01_data.process import get_data_file_base as get_file_names
# from util import util


class ClassifyDataset(Dataset, ABC):
    # pylint: disable=too-many-instance-attributes

    def __init__(self, data_path, language, representation, embedding_size,
                 mode, classes=None, words=None):
        self.data_path = data_path
        self.language = language
        self.mode = mode
        self.representation = representation
        self.embedding_size = embedding_size

        # self.input_name_base = get_file_names(data_path, language)
        # self.process(classes, words)
        self.input_name_base = os.path.join(data_path, str(mode) + "-cls.pth")
        self.data = torch.load(self.input_name_base)
        self.x = torch.from_numpy(self.data['X']).float()
        self.y = torch.from_numpy(self.data['y']).long()

        assert len(self.x) == len(self.y)
        self.n_instances = len(self.x)
        self.classes = torch.from_numpy(np.array([0, 1]))
        self.n_classes = self.classes.shape[0]
        self.words = self.x
        self.n_words = None

    def __len__(self):
        return self.n_instances

    def __getitem__(self, index):
        return (self.x[index], self.y[index])