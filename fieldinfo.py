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
import xlrd

eliminate = ['OBJECT_ID', 'S_INFO_COMPNAME', 'NOTES_RCV', 'S_INFO_COMPCODEB', 'ANN_DTB', 'REPORT_PERIODB',
             'STATEMENT_TYPE', 'CRNCY_CODE', 'B_INFO_CREDITRATING', 'B_RATE_RATINGOUTLOOK',
             'B_INFO_CREDITRATINGAGENCY', 'S_INFO_COMPCODEC', 'S_INFO_COMPCODEI', 'S_INFO_COMPCODEB', 'S_INFO_COMPCODE',
             'ACTUAL_ANN_DT', 'BUSINESSSCOPE', 'ANN_DT', 'REPORT_PERIODI', 'ANN_DTI', 'AUDIT_AM', 'ANN_DTC',
             'REPORT_PERIODC', 'COMP_TYPE_CODE', 'MEMO', 'ASSET_DISPOSAL_INCOME', 'CONTINUED_NET_PROFIT']

params = ['TOT_ASSETS', 'CAP_RSRV', 'CAP_STK']


def load_basic_info():
    data = _getXlsxInfo('basic_info.xlsx')
    tables = data.sheets()[0]
    nrows = tables.nrows
    print(nrows)
    ncols = tables.ncols
    print(ncols)
    rows = tables.row_values(0)
    print(rows)
    rows = tables.row_values(1)
    print(rows)


def loadFinancialInfo():
    data = _getXlsxInfo('financial_reports.xlsx')
    tables = data.sheets()[0]
    # nrows = tables.nrows
    # print(nrows)
    # ncols = tables.ncols
    # print(ncols)
    # rows = tables.row_values(0)
    # print(rows)
    rows = np.array(tables.col_values(1)[7:])
    # print(rows)
    return rows


def _getXlsxInfo(name):
    module_path = dirname(__file__)
    print('module_path', module_path)

    basic_info_path = join(module_path, 'data', name)

    data = xlrd.open_workbook(basic_info_path)
    return data
