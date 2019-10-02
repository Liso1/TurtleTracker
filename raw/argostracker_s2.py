# -*- coding: utf-8 -*-
#-------------------------------------------------------------
# ARGOSTrackerTool.py
#
# Description: Parses a line of ARGOS tracking data 
# Step 2
#
# Created by: Shawn Li (soxiang.li@duke.edu)
# Created on: Fall 2019
#--------------------------------------------------------------
# Create a variable pointing to the file with no header
fileName = "V:/TurtleTracker/raw/saranoheader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineStrings = fileObj.readlines()
print ("There are {} records in the file".format(len(lineStrings)))

# Close the file object
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}

# Use a for loop to read each line, one at a time, until the list is exhausted
for lineString in lineStrings:
    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")
    
    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    #filter out record
    if obsLC in ("1","2","3"):
            
        # Add values to dictionary
        dateDict[recordID] = obsDate
        locationDict[recordID] = (obsLat, obsLon)

# Ask the user for a date, specifying the format
userDate = input("Enter a date (M/D/YYYY):")

#collect keys matching user date
keyList = []
for k,v in dateDict.items():
    if v == userDate:
        keyList.append(k)
        
# report if no keys are found
if len(keyList) == 0:
    print ("No observations recorded for {}".format(userDate))
# Loop through each key and report the associated date location
else:
     for k in keyList:
        theDate = dateDict[k]
        theLocation = locationDict[k]
        theLat = theLocation[0]
        theLon = theLocation[1]
        print("Record {0}: Sara was see at {1}N-{2}W, on {3}".format(k,theLat,theLon,theDate))

    