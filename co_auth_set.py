#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:29:56 2018

@author: ari
"""


import csv as cv
import time as tm
import ast
import re
import numpy as nm

for i in range (0,1):
    data = {}
    years = []
    filename = "auth_"+str(i)+".csv"
    with open(filename,"r") as csvfile:
        print("Reading File : " + filename)
        reader = cv.reader(csvfile)
        next(reader, None) #skipping the header
        for row in reader:
            year = int(row[3])
            years.append(year)
            for auth in row[11].split("'"):
                if auth != '[' and auth != ', ' and auth !=']':
                    if auth in data :
                        try:
                            data[auth][year] = data[auth][year]+1
                        except KeyError:
                            data[auth][year] = 1

                    else:
                        data[auth]= {year : 1}    

        years_uni = nm.unique(years)        
    #    print(data)


        des_f = "co_auth_set_"+str(i)+".csv"
        with open(des_f,"w") as csv_write:
            header = "Name"
            for y in years_uni:
                header = header + ','+str(y)
            csv_write.write(header+'\n')
            for d in data.keys() :
                if d != '[]':
                    csv_write.write(d)
                    for y in years_uni:
                        try:
                            csv_write.write(','+str(data[d][y]))
                        except KeyError:
                            csv_write.write(',0')   
                    csv_write.write('\n')

        
        print("Complete !")
        data.clear()                
