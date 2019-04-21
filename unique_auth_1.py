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


comm_filename = "/home/ari/Documents/Ambiguity-Project/Dataset/mag_papers/mag_papers_"
auth={}  
for i in range (60,80):
    start_time_file = tm.time()
    filename = comm_filename + str(i) + '.txt'
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
        des_f = "unique_auth_mag_" + str(int(i/10)) + ".db"
        with sql.connect(des_f) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS authors (name VARCHAR PRIMARY KEY,no_of_papers int NOT NULL)")
            print("Writing to database")
            for key in auth.keys():
                try:
                    cur.execute("INSERT INTO authors VALUES(?,?)",(key,auth[key],))
                except sql.IntegrityError:
                    cur.execute("UPDATE authors SET no_of_papers=no_of_papers+(?) WHERE name=(?)",(auth[key],key))

            print("commiting")
            auth.clear()
            conn.commit()
            with open("keep_track.txt",'w') as de:
                de.write(str(i))
                   

    print("---------------------------------------------------------")
    print("In File " + filename + " Lines = " + " Time = " + str (tm.time() - start_time_file))        