import numpy as np

class WeatherAnalyzer:
    def __init__(self, data, years):
        self.allData = data
        self.yearsArray = years

        self.minTempData = []
        self.maxTempData = []
        self.snowfallData = []
        self.averageList = []

        for i in data:
            self.maxTempData.append(i[2])
            self.minTempData.append(i[3])
            self.snowfallData.append(i[4])
            self.averageList.append(0)

    def getMinTemp(self):
        print(np.amin(self.minTempData))

    def getMaxTemp(self):
        print(np.amax(self.maxTempData))

    def arrayProcessor(self, arrayList, functionType):

        returnValues = []

        for i in range(int(len(arrayList) / 12) + 1):
            advance = i * 12
            start = 0 + advance
            end = 12 + advance
            while end > len(arrayList):
                end -= 1
            value = 0
            if functionType == "average":
                value = np.average(arrayList[start:end])
            elif functionType == "max":
                value = np.amax(arrayList[start:end])
            elif functionType == "min":
                value = np.amin(arrayList[start:end])
            returnValues.append(value)

        return returnValues

    def printResults(self, array):
        for i in range(len(array)):
            print(str(self.yearsArray[i]) + ": " + str(array[i]))


    def getMinTempAnnually(self):
        return self.arrayProcessor(self.minTempData, "min")

    def getMaxTempAnnually(self):
        return self.arrayProcessor(self.maxTempData, "max")

    def getAvgSnowfallAnnually(self):
        return self.arrayProcessor(self.snowfallData, "average")

    def getAvgTempAnnually(self):
        for i in range(len(self.minTempData)):
            self.averageList[i] = ((self.minTempData[i] + self.maxTempData[i])/2)
        return self.arrayProcessor(self.averageList, "average")

