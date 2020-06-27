import os
import pickle
import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms


default_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])


class MNISTSlice(MNIST):

    def __init__(
            self, root, data, labels, train=True, transform=None, download=True):

        super(MNISTSlice, self).__init__(
            root, train=train, transform=transform, download=download)

        data_ = data.clone()
        labels_ = labels.clone()

        if train:
            self.train_node_data = data_
            self.train_node_labels = labels_
        else:
            self.test_node_data = data_
            self.test_node_labels = labels_

    def dump(self, path):
        pickle.dump(self, open(path, 'wb'))

    @staticmethod
    def load(path):
        return pickle.load(open(path, 'rb'))