import numpy as np
import pandas as pd

# idata
idataraw = pd.read_csv("idata.csv")
idatawavelength = idataraw["wavelength (nm)"].tolist()
idataintensity = idataraw["intensity (counts)"].tolist()
idata = [idatawavelength, idataintensity]

# tdata
tdataraw = pd.read_csv("tdata.csv")
tdatawavelength = tdataraw["wavelength (nm)"].tolist()
tdatatransmission = tdataraw["transmission (int)"].tolist()
tdata = [tdatawavelength, tdatatransmission]

peakrange = [425, 500]
#peakrange = [600, 675]

def transmissionFraction(idata = idata, tdata = tdata, peakrange = peakrange):
    """
    takes in intensity data (idata), transmission data (tdata), and wavelength range of interest (peakrange) and calculates the total approx. expected fraction of light to pass through
    idata = ["wavelength (nm)" list, "intensity (counts)" list]
    tdata = ["wavelength (nm)" list, "transmission (int)" list]
    peakrange = [minimum wavelength int, maximum wavelength int]
    """
    totalintensity = 0
    weightedSum = 0
    for n in range(len(idata[0])):
        if peakrange[0] <= idata[0][n] <= peakrange[1]:
            totalintensity += idata[1][n]
            weightedSum += idata[1][n]*findTransmissionVal(tdata, idata[0][n])
    return [weightedSum/totalintensity, totalintensity]

def findTransmissionVal(tdata, wavelength):
    """
    takes in transmission data (tdata) and a given wavelength and finds the approx. transmission based on drawing a line between the two points the wavelength splits between
    tdata = ["wavelength (nm)" list, "transmission (int)" list]
    wavelength = int
    """
    lowerWavelength = min(tdata[0])
    while lowerWavelength + 5 < wavelength:
        lowerWavelength += 5
    lowerWavelengthindex = tdata[0].index(lowerWavelength)
    lowerT = tdata[1][lowerWavelengthindex]
    upperT = tdata[1][lowerWavelengthindex + 1]
    deltaT = upperT - lowerT
    cutoffFraction = (wavelength - lowerWavelength)/5
    totalT = lowerT + deltaT*cutoffFraction
    return totalT
    
## RESULTS:
# Red peak: Y% = 47.37
  # count total = 16044003
  # %counts = 55.55%
# Blue peak: Y% = 48.51
  # count total = 12837721
  # %counts = 44.45%