## --------------------------------------------------------
## importARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line feature class from the [filtered] tracking points
##
## Usage: importARGOS <ARGOS folder> <Output feature class>
##
## Created: Oct 2018 (for ENV859)
## Author: Kendall DeLyser, kendall.delyser@duke.edu
## --------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (hard-wired)
inputFile = "V:/ARGOSTracking/data/ARGOSData/1997dg.txt"
outputFC = "V:/ARGOSTracking/scratch/ARGOSTrack.shp"

##Construct a while loop to iterate through all lines in the data file
# Open the ARGOS file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()
# print(lineString) # can print just to make sure code is working
while lineString:
    
    # Set code to run only if the line contains the string "Date :"
    if ("Date :" in lineString):

        # Parse the line into a list, split by spaces (default when we specify nothing in the split() function)
        lineData = lineString.split()

        # Extract attributes from the datum header line
        tagID = lineData[0]

        # Extract location info from the next line
        line2String = inputFileObj.readline()

        # Parse the line into a list
        line2Data = line2String.split()

        # Extract the data we need to variables
        obsLat = line2Data[2]
        obsLon = line2Data[5]

        # Print results to see how we're doing
        print(tagID,"Lat:"+obsLat," Long:"+obsLon)

    # Move to the next line so the while loop progresses
    lineString=inputFileObj.readline()

# Close the file object
inputFileObj.close()
        
    