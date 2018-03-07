# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:27:50 2018

@author: chenxizhang
"""

import re
import csv

#read data to file data.csv
f = open('data.csv','rb')
reader = csv.reader(f)

#write to a new file data2.csv
g = open('data2.csv','wb')
writer = csv.writer(g)

#remove whitespace
rows = [row.strip() for row in f]

header = ['First','M.I.','Last','Phone']
writer.writerow(header)

#generate line expression
regex_last = re.compile(r'(\w+)\,\s(\w+)\s?(\w+?\.?)?.*\(?(\d{3})\)?[\s\.\-]?(\d{3})[\s\.\-]?(\d{4})')
regex_first = re.compile(r'(\w+)\s?(\w?\.?)\s(\w{2,}).*\(?(\d{3})\)?[\s\.\-]?(\d{3})[\s\.\-]?(\d{4})')

#write data into the file data2.csv
for row in rows:
    data_last = re.search(regex_last, row)
    if data_last:
        phone_format = '(' + data_last.group(4) + ')' + ' ' + data_last.group(5) + '-' + data_last.group(6)
        data = [data_last.group(2), data_last.group(3), data_last.group(1), phone_format]
        writer.writerow(data)

    data_first = re.search(regex_first, row)
    if data_first:
        phone_format = '(' + data_first.group(4) + ')' + ' ' + data_first.group(5) + '-' + data_first.group(6)
        data = [data_first.group(1), data_first.group(2), data_first.group(3), phone_format]
        writer.writerow(data)
        
    
f.close()
g.close()
