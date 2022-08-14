import pygame
import random
import math
import psutil
import os

screenX = 800
screenY = 600



def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
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

def processSize(vms):
    return vms / screenX

def getSizes():
    listOfRunningProcess = getListOfProcessSortedByMemory()
    adjustedSizes = []
    sizes = []
    numberOfAsteroids = 20
    for elem in listOfRunningProcess[:numberOfAsteroids] :
        print(elem['name'])
        
        #print(elem['pid'])
        adjustedSizes.append(processSize(elem['vms']))

    difference = max(adjustedSizes) - min(adjustedSizes)
    print(difference)
    for i in adjustedSizes:
        j = math.log2(i)
        #j = (i / difference) * 100
        sizes.append([j,j])
    print(sizes)
    print(adjustedSizes)

getSizes()