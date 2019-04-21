#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:29:56 2018

@author: ari
"""

import xlrd as xl
import time as tm
import math as mt

def fill_coauth(coauth_list):
    for auth in coauth_list:
        count[count_coauth]=count[count_coauth]+1
        try:
            coauth[auth] = coauth[auth]+1
        except KeyError:
            coauth[auth] = 1

def fill_keywords(keywords_list):
    for keyword in keywords_list:
        count[count_keywords]=count[count_keywords]+1
        try:
            keywords[keyword] = keywords[keyword]+1
        except KeyError:
            keywords[keyword] = 1
"""
def fill_institute(ins):
    count[count_ins]= count[count_ins] + 1
    try:
        institute[ins] = institute[ins] + 1
    except KeyError:
        institute[ins] = 1

def fill_year(year):
    count[count_years]=count[count_years]+1
    try:
        years[year] = years[year] + 1
    except KeyError:
        years[year] = 1

def fill_journal(jour):
    count[count_journal] = count[count_journal]+1
    try:
        journal[jour] = journal[jour] + 1
    except KeyError:
        journal[jour] = 1    

 """

def process(row):
    fill_coauth(row[9].split(","))
    #fill_year(row[11])
    #fill_journal(row[16])
    fill_keywords(row[12].split(","))
    #fill_institute(row[15])

def mean_count():
    temp = {}
    temp['coauth'] = int(count[count_coauth]/len(coauth.keys()))
    #temp['year']=int(count[count_years]/len(years.keys()))
    temp['keywords']=int(count[count_keywords]/len(keywords.keys()))
    #temp['institute']=int(count[count_ins]/len(institute.keys()))
    #temp['journal']=int(count[count_journal]/len(journal.keys()))
    return temp

    

coauth={}
#years={}
keywords={}
#journal={}
#institute={}

count=[0]*5
count_coauth=0
#count_years=1
count_keywords=2
#count_journal=3
#count_ins=4

for i in range (0,1):
    xl_filename = "m_auth_"+str(i)+".xlsx"
    wb = xl.open_workbook(xl_filename)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)

    for row in range (1,sheet.nrows):
        process(sheet.row_values(row))

    means =  mean_count()
    A_coauth = set()
    B_coauth = set()
    for auth in coauth.keys():
        if coauth[auth] <= means['coauth']:
            A_coauth.add(auth)
        else :
            B_coauth.add(auth)

    coauth.clear()
    """
    A_years=set()
    B_years=set()
    for year in years.keys():
        if years[year] <= means['year']:
            A_years.add(year)
        else:
            B_years.add(year)

    years.clear()
    """
    A_keywords =set()
    B_keywords = set()
    for key in keywords.keys():
        if keywords[key] <= means['keywords']:
            A_keywords.add(key)
        else:
            B_keywords.add(key)

    keywords.clear()
    """
    A_journal = set()
    B_journal = set()
    for jour in journal.keys():
        if journal[jour] <= means['journal']:
            A_journal.add(jour)
        else :
            B_journal.add(jour)

    journal.clear()
    A_institute = set()
    B_institute = set()
    for ins in institute.keys():
        if institute[ins] <= means['institute']:
            A_institute.add(ins)
        else :
            B_institute.add(ins)

    institute.clear()
    """
    result = {'coauth':{'nca':0,'ncb':0,'ncom':0},'keywords':{'nca':0,'ncb':0,'ncom':0}}
    author_name = sheet.cell_value(1,1)
    N = sheet.nrows - 1
    for index in range (1,sheet.nrows):
        row = sheet.row_values(index)
        coauth_set = set(row[9].split(","))
        keywords_set = set(row[12].split(","))
        # coauth
        if coauth_set.issubset(A_coauth):
            result['coauth']['nca'] = result['coauth']['nca']+1
        elif coauth_set.issubset(B_coauth):
            result['coauth']['ncb'] = result['coauth']['ncb']+1   
        else :
            result['coauth']['ncom'] = result['coauth']['ncom']+1

        if keywords_set.issubset(A_keywords):
            result['keywords']['nca'] = result['keywords']['nca']+1
        elif keywords_set.issubset(A_keywords):     
            result['keywords']['ncb'] = result['keywords']['ncb']+1
        else :
            result['keywords']['ncom'] = result['keywords']['ncom']+1

    print(result)
    """
    des_f = "result_m_auth_"+str(i)+".csv"
    header = "Feature,Author,N,CnA,CnB,CnCom,idfSumCA,idfSumCB,idfSumCom,idfSumCnorm1,idfSumCnorm2,Similarity"
    with open(des_f,"w") as csv_file:
        for field in result.keys():
            idfSumCA=mt.log10(N/result[field]['nca']) 
            idfSumCB=mt.log10(N/result[field]['ncb'])
            idfSumCom=mt.log10(N/result[field]['ncom'])
            idfSumCnorm1 = mt.log10(result[field]['ncom']/result[field]['nca'])
            idfSumCnorm2 = mt.log10(result[field]['ncom']/result[field]['ncb'])
            Similarity = (idfSumCnorm1+idfSumCnorm2)/2
            csv_file.write(field+","+author_name+","+str(N)+","+str(result[field]['nca'])+","+str(result[field]['ncb'])+","+str(result[field]['ncom'])+","+str(idfSumCA)+","+str(idfSumCB)+","+str(idfSumCom)+","+str(idfSumCnorm1)+","+str(idfSumCnorm2)+","+str(Similarity)+"\n")

    print(xl_filename+" Complete !")
    """