#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 14:29:56 2018

@author: ari
"""

import csv as cv

def count_authors(li):
    if li == '[]':
        return 0
    count = 0    
    for auth in li.split("'"):
        if auth != '[' and auth != ', ' and auth !=']':
            count = count + 1
    return count

for i in range(0,1):
    data = {}
    filename = "auth_"+str(i)+".csv"
    with open(filename,"r") as f:
        print("Reading File : " + filename)
        reader = cv.reader(f)
        next(reader, None) #skipping the header
        for row in reader:
            num_of_coauthors = count_authors(row[11])
            try:
                data[num_of_coauthors] = data[num_of_coauthors] + 1
            except KeyError:
                data[num_of_coauthors] = 1


    #writing to csv file
    des_f = "count_co_auth"+str(i)+".csv"
    with open(des_f,"w") as csvfile:
        csvfile.write("Multi_coauth_set_paper,count")
        for key in data.keys():
            csvfile.write(str(key)+","+str(data[key])+"\n")
