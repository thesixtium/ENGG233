import numpy as np

class FileIO:
    def __init__(self, filePath):
        self.filePath = filePath
        self.dataTable = np.loadtxt(self.filePath, delimiter=",", skiprows=1,
                                    usecols=(0,1,2,3,4), dtype=np.float)

    def readFile(self):
        return self.dataTable
