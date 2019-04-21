#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:29:56 2018

@author: ari
"""

import time as tm
import csv as cv
import json as jsn
import os 
import copy as cp

def process(line):
    coAuthList=[]
    authInList = [] 
    data = jsn.loads(line)
    try:
        t = data['authors']
    except KeyError:
        return

    for names_dict in t:
        coAuthList.append(names_dict['name'])
        if names_dict['name'] in hashAuth:
            authInList.append(names_dict['name'])

    if len(authInList)>0:
        temp = {}
        try:
            temp['id'] = data['id']
        except KeyError:
            return

        try:
            temp['title'] = data['title']
        except KeyError:
            temp['title'] = 'None'

        try:
            temp['venue'] = data['venue']
        except KeyError:
            temp['venue']='None'

        try:
            temp['year'] = data['year']
        except KeyError:
            temp['year']='None'

        try:
            temp['fos'] = data['fos']
        except KeyError:
            temp['fos'] = 'None'

        try:
            temp['references']=data['references']
        except KeyError:
            temp['references'] = 'None'

        try:
            temp['keywords'] = data['keywords']
        except KeyError:
            temp['keywords'] = 'None'   

        try:
            temp['n_citation'] = data['n_citation']
        except KeyError:
            temp['n_citation'] = 'None'

        try:
            temp['lang'] = data['lang']
        except KeyError:
            temp['lang'] = 'None'

        try:
            temp['abstract'] = data['abstract']
        except KeyError:
            temp['abstract'] = 'None'     

        try:
            temp['publisher'] = data['publisher']
        except KeyError:
            temp['publisher'] = 'None'       

        
        for word in authInList:
           # prisnt(coAuthList)
            tempDict = cp.copy(temp)           
            tempList = cp.copy(coAuthList)
            tempList.remove(word)
            tempDict['CoAuthors'] = cp.copy(tempList)
            if word in authData:
                authData[word].append(tempDict)
            else:
                authData[word] = []
                authData[word].append(tempDict)    
            
        
    
#----------------------------------------------

hashAuth = {}
authData = {}
with open("get_authors.txt",'r') as f:
    index=0
    for line in f:
        hashAuth[line.replace('\n','')] = 'auth_'+str(index)
        index=index+1



tot_time = tm.time()

#for reading the mag_papers
for i in range(0,2):
    filename ="mag_papers_"+str(i)+'.txt'
    with open(filename,'r') as f:
        start_time = tm.time()
        print("Reading file "+ filename)
        for line in f:
            process(line)
        print("Reading completed in = "+str(tm.time()-start_time)+' sec')

with open("/home/ari/Desktop/result/Author_Map.csv",'w') as csvfile:
    for key in hashAuth.keys():
        csvfile
        csvfile.write(key+','+hashAuth[key]+'\n')


#printing dictionary to the csv file
fieldnames = authData[key][0].keys()
for key in authData.keys():
    filename = "/home/ari/Desktop/result/"+hashAuth[key]+'.csv'
    with open(filename, 'w') as output_file:
        dict_writer = cv.DictWriter(output_file,fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(authData[key])

print("Writing complete to csv file")
print("Total time = " + str(tm.time()-tot_time))
