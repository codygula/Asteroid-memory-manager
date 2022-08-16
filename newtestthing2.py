import pygame
import random
import math
import psutil
import os

def getListOfProcessSortedByMemory():
    #Get list of running processes by memory
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects
# print(getListOfProcessSortedByMemory())
bigdict = getListOfProcessSortedByMemory()



duplicates = []
newNames = []
for i in bigdict:
    if i['name'] not in duplicates: 
        duplicates.append(i['name'])
        newNames.append({'name':i['name'], 'size':0})
    combinedSize = newNames[i['size'] + bigdict[i['vms']]]
    newNames['name'].update(combinedSize)
print(newNames)


# duplicates = {'name':[]}
# newNames = {'name':[], 'vms':[]}
# for i in bigdict:
#     if i['name'] not in duplicates['name']: 
#         duplicates['name'].append(i['name'])
#         newNames['name'].append(i['name'])
#         newNames['vms'].append(i['vms'])
# print(newNames)



# newNames = []
# newSizes = []
# duplicates = []
# print()
# def deduplicate(list1):
    
#     i = 0
#     while i <= len(list1)-1:
#         if list1[i] not in duplicates:
#             newNames.append(list1[i])
#             newSizes.append(sizes[i])
#             duplicates.append(list1[i])
#         # elif i in duplicates:
#         #     duplicates.append(i)
#         i += 1
        


# deduplicate(list1)
