#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:16:54 2018

@author: ari
"""
import time as tm
import os
import json as jsn
import sqlite3 as sql


conn = sql.connect("unique_auth.db")
cur = conn.cursor()
auth={}
comm_filename = "/home/ari/Documents/Ambiguity-Project/Dataset/mag_papers/mag_papers_"  
for i in range (18,22):
    start_time_file = tm.time()
    filename = comm_filename + str(i) + '.txt'
    des_filename = "auth_list_mag_"+str(i)
    print("Reading file mag_papers_"+str(i)+".txt")
    with open(filename,'r') as f:
        for line in f:
            data = jsn.loads(line)
            try:
                for d in data['authors']:
                    try:
                        auth[d['name']] = auth[d['name']] + 1
                    except KeyError:
                        auth[d['name']] = 1
            except KeyError:
                pass 

    if i%2 != 0:
        print("Writing to database")
        counter = 0
        for key in auth.keys():
            try:
                cur.execute("INSERT INTO authors VALUES(?,?)",(key,auth[key],))
            except sql.IntegrityError:
                cur.execute("UPDATE authors SET no_of_papers=no_of_papers+(?) WHERE name=(?)",(auth[key],key))
            counter = counter+1
            if counter == 20000:
                conn.commit()
                counter = 0
                print("------20,000 rows commited")

        auth.clear()
        print("commiting")
        conn.commit()
        with open("keep_track.txt",'w') as de:
            de.write(str(i))

    print("---------------------------------------------------------")
    print("In File " + filename + " Lines = " + " Time = " + str (tm.time() - start_time_file))