#!/usr/bin/env python3
# import matplotlib.pyplot as plt
# import numpy as np
import csv
import os
import sys
import pyexcel

# from openpyxl import Workbook

if os.name == 'nt':
    symbol = '\\'
if os.name == 'posix':
    symbol = '/'
# /home/me/PycharmProjects/velocity_vs acc001/data01/0.CSV
# print(os.environ)
dir_path = os.path.dirname(os.path.abspath(__file__)) + symbol

orig_stdout = sys.stdout
file_log = open(dir_path + 'log_file.txt', 'w')
# output_xlsx=dir_path + 'output.xlsx'

sys.stdout = file_log
csv_path = dir_path + 'csv'
# dir_path ='/media/me/data/doc-i/работа/india/SERCEL 508 XT/'
print('dir_path=', dir_path)

csv_files = []  # составляю общий список файлов csv
for root, dirs, files in os.walk(csv_path):
    for file in files:
        if (file.endswith(".csv")):
            csv_files.append(os.path.join(root, file))
print('file count = ', len(csv_files))
# начальные параметры для отображения данных о cx508
cx_sn_control = set()
keys_cx = ('Box Type', 'Serial Nb', 'Auto Test', 'Leakage Low (mA)', 'Leakage High (mA)', 'Version')
CX_508 = list()
CX_508.append(keys_cx)

# начальные параметры для отображения данных о cx508
fdu_sn_control = set()
keys_fdu = (
'Type', 'Serial Nb', 'Auto Test', 'Noise (μV)', 'Distortion (dB)', 'Phase(μs)', 'Gain (%)', 'CMRR (dB)', 'Version')
Fdu_508 = list()
Fdu_508.append(keys_fdu)
# print('keys fdu ', keys_fdu[0])


for file_name in csv_files:
    with open(file_name, encoding='utf-8-sig') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter=",")
        field_names = file_reader.fieldnames
        #        print(field_names)
        #        print(file_name)
        # count = 0
        if keys_cx[0] in field_names:
            for row in file_reader:
                if row['Box Type'] == 'CX_508':
                    # print('CX_508')
                    cx = list()
                    if not (row['Serial Nb'] in cx_sn_control):
                        cx_sn_control.add(row['Serial Nb'])
                        for indx in keys_cx:
                            cx.append(tuple(row[indx]))
                        CX_508.append(cx)
                        # if row['Box Type']=='SCI_508':
                    # print('SCI_508')
        if keys_fdu[0] in field_names:
            # print('FDU_508')
            for row in file_reader:
                fdu = list()
                if not (row['Serial Nb'] in fdu_sn_control):
                    fdu_sn_control.add(row['Serial Nb'])
                    for indx in keys_fdu:
                        fdu.append(tuple(row[indx]))
                    Fdu_508.append(fdu)
            # print(row['Box Type'] + ' ' + str(row['Serial Nb']))
        # count += 1

        r_file.close()

dat = {"CX_508": CX_508,
       "FDU_508": Fdu_508}
# print(cx_sn_control)
print('total nb cx508', len(cx_sn_control))
# print(fdu_sn_control)
print('total nb fdu508', len(fdu_sn_control))

# print(*dat)
my_dest_file_name = dir_path + "result.xls"
pyexcel.save_book_as(dest_file_name=my_dest_file_name, bookdict=dat)
# print(count)

file_log.close()
# Max. Distortion: -103 dB.
# Min. Common Mode Rejection (CMRR): 100 dB.
# Max. Gain error: 1.0%.
# Max. Phase error: 20 μs.
# Max. Noise (0 dB gain, 1600 mV scale): 1.0 μV.
# Max. Noise (12 dB gain, 400 mV scale): 0.25 μV.
# print(*file_reader.reader)

# SignalFileName = dir_path + 'data01'+symbol+'0.CSV'
# print(SignalFileName)
# with open(SignalFileName, 'r') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',')
#    data = np.array(list(reader)).astype(float)

# print(data[:][:, 1])
# print(data[:][:, 0])

# from openpyxl import Workbook
#
# reload(sys)
# sys.setdefaultencoding('utf8')
#
# if __name__ == '__main__':
#    workbook = Workbook()
#    worksheet = workbook.active
#    with open('input.csv', 'r') as f:
#        reader = csv.reader(f)
#        for r, row in enumerate(reader):
#            for c, col in enumerate(row):
#                for idx, val in enumerate(col.split(',')):
#                    cell = worksheet.cell(row=r+1, column=c+1)
#                    cell.value = val
#    workbook.save('output.xlsx')
