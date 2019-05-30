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
import fieldinfo as fi
import re


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


def load_data_sets():
    return load_data('datasets.csv')


def load_validate_sets():
    return load_data('validate_datasets.csv')


def load_data(filename):
    non_decimal = re.compile(r'[^\d.]+')
    module_path = dirname(__file__)
    print(module_path)

    fin = fi.params  # loadFinancialInfo()

    data_file_name = join(module_path, 'data', filename)
    with open(data_file_name) as f:
        # [each for each in csv.DictReader(f, delimiter='\t')]  #
        data_file = np.asarray(
            [each for each in csv.DictReader(f, delimiter='\t')])  # csv.DictReader(f, delimiter='\t')
        print('data_file.count', data_file.size)

        temp = data_file[0]  # data_file  #
        # temp.keys
        # print(temp)

        t = []
        for each in temp.keys():
            if each in fin:
                t.append(each)

        feature_names = np.asarray(t)  #
        n_samples = data_file.size
        n_features = feature_names.size
        # print(n_samples, n_features)
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples))
        names = np.empty((n_samples))
        # print(feature_names)

        for i, d in enumerate(data_file):
            t = []
            for k in feature_names:
                t.append(remoteNull(non_decimal.sub('', d[k])))

            data[i] = np.asarray(t, dtype=np.float64)
            score = d['B_INFO_CREDITRATING']
            # print(score)
            target[i] = np.asarray(cs.getRatingToScore(score), dtype=np.int)
            # names[i] = np.asarray(d['S_INFO_COMPNAME'])

        print(data)

        print(target)
    return Bunch(data=data, target=target, names=names)


def remoteNull(val):
    if val == '(null)':
        val = 0
    if val == '':
        val = 0
    return val
