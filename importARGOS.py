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

