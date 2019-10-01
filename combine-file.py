#!/usr/local/bin/python
#@author : Chiranjeevi Borra
#Date: 9/24/2019
import os
import sys
import re

file1= sys.argv[1]
file2= sys.argv[2]
print(file1)
print(file2)

### open both files f1 and f2 
f1=open(file1).readlines()
f2=open(file2).readlines()
#f1f2=open('f1f2.txt','w')


# Define keys and Variables for each line from each file
# keys and values from file1

f1_keys=[]
f1_vals=[]
for i in f1:                           
  f1_keys+=[i.split("|")[0].strip().replace("~/t", "")]              
  f1_vals+=[i.split("|")[1].strip().replace("~/t", "")]           

# keys and values from file2

f2_keys=[]
f2_vals=[]

for i in f2: 
  f2_keys+=[i.split("|")[0].strip().replace("~/t", "")]              
  f2_vals+=[i.split("|")[1].strip().replace("~/t", "")]


# loop with file1 keys, file2 keys and check file1 keys are matching with file2 keys , if it matches print it in file by adding f2_vals.
# keep missing entries in f2 info to add those lines in end  

for i in range(len(f1_keys)):
    isKeyFoundInF2 = "false"
    for j in range(len(f2_keys)):
        if f1_keys[i] == f2_keys[j]:
            temp = f1_keys[i] + " | " + f1_vals[i] + ";" + f2_vals[j]
            print(temp)
           #f1f2.write("%s \n" %(temp))
            del f2_keys[j:j+1]
            del f2_vals[j:j+1]
            isKeyFoundInF2 = "true"
            break
    
    if isKeyFoundInF2 == "false":
        temp = f1_keys[i] + " | " + f1_vals[i] + ";,,,,,"
        print(temp)
       #f1f2.write("%s \n" %(temp))

#add missing keys and values in file2 with commas.

for i in range(len(f2_keys)):
    temp = f2_keys[i] + " | " + ",,,,,;" + f2_vals[i]
    print(temp)
   #f1f2.write("%s \n" %(temp))

# close all files
#fef2.close()
#f1.close()
#f2.close()
