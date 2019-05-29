import os
import csv
import sys
import numpy as np
import shutil
from collections import namedtuple
from os import environ, listdir, makedirs
from os.path import dirname, exists, expanduser, isdir, join, splitext
import hashlib
import credit_score as cs


class Bunch(dict):
    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass


def load_data():
    module_path = dirname(__file__)
    print(module_path)

    # fdescr_name = join(module_path, 'datasets.csv')
    # print(fdescr_name)
    # with open(fdescr_name) as f:
    #     descr_text = f.read()
    # print(descr_text)

    # csvfile = open(cwd + '/datasets.csv', 'r')
    #
    # reader = [each for each in csv.DictReader(csvfile, delimiter='\t')]

    data_file_name = join(module_path, 'datasets.csv')
    with open(data_file_name) as f:
        # [each for each in csv.DictReader(f, delimiter='\t')]  #
        data_file = np.asarray(
            [each for each in csv.DictReader(f, delimiter='\t')])  # csv.DictReader(f, delimiter='\t')
        print('data_file.count', data_file.size)

        temp = data_file[0]  # data_file  #
        # temp.keys
        # print(temp)
        feature_names = np.asarray([each for each in temp.keys()])
        n_samples = data_file.size
        n_features = feature_names.size
        # print(n_samples, n_features)
        data = np.empty((n_samples, 2))
        target = np.empty((n_samples))

        for i, d in enumerate(data_file):
            q = remoteNull(d['TOT_ASSETS'])
            q1 = remoteNull(d['OTHER_CASH_PAY_RAL_INV_ACT'])
            # print('p', i, q, q1)
            data[i] = np.asarray([q, q1], dtype=np.float64)
            score = d['B_INFO_CREDITRATING']
            # print(score)
            target[i] = np.asarray(cs.getRatingToScore(score), dtype=np.int)

        # print(n_samples)
        # print(n_features)

        print(data)

        print(target)
    return Bunch(data=data, target=target)


def remoteNull(val):
    if val == '(null)':
        val = 0
    return val