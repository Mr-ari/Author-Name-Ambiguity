#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:29:56 2018

@author: ari
"""


import xlrd as xl
import time as tm
import numpy as nm
def coauth_yr(coauth,year):
    years.append(year)
    for auth in coauth:
        if auth in co_y :
            try:
                co_y[auth][year] = co_y[auth][year]+1
            except KeyError:
                co_y[auth][year] = 1

        else:
            co_y[auth]={year : 1}


def process(row):
    coauth_yr(row[9].split(","),int(row[11]))


co_y={}
years=[] 

for i in range (0,1):
    xl_filename = "m_auth_"+str(i)+".xlsx"
    wb = xl.open_workbook(xl_filename)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)

    for row in range (1,sheet.nrows):
        process(sheet.row_values(row))


    #print(co_y)
#print coauth vs year
    years = nm.unique(years)
    des_f = "m_auth_"+str(i)+"_co_yr.csv"
    tot_sum_hori = 0
    with open(des_f,"w") as csv_write:
        sum_hori=0
        sum_vert=[0]*len(years)
        header = "Name"
        for y in years:
            header = header + ','+str(y)
        csv_write.write(header+',sum'+'\n')
        for auth in co_y.keys():
            csv_write.write(auth)
            index = 0
            sum_hori=0
            for y in years:
                try:
                    csv_write.write(','+str(co_y[auth][y]))
                    sum_hori = sum_hori + co_y[auth][y]
                    sum_vert[index] = sum_vert[index] + co_y[auth][y]
                except KeyError:
                    csv_write.write(',0')   
                index = index+1
            csv_write.write(','+str(sum_hori)+'\n')
            tot_sum_hori = tot_sum_hori + sum_hori
        csv_write.write("sum")
        for val in sum_vert:
            csv_write.write(','+str(val))
            tot_sum_vert = tot_sum_vert + val    

    mean_hori = int(tot_sum_hori / len(co_y.keys()))        
    mean_vert = int(tot_sum_vert / len(years))
        