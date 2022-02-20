class Date:
    def __init__(self, data):
        self.allData = data

        self.Year = []
        self.Month = []

        for i in range(int(len(data)/12) +1):
            entry = i * 12
            self.Year.append(data[entry][0])

        for i in range(len(data)):
            self.Month.append(data[i][1])

    def returnYears(self):
        return self.Year

    def returnMonths(self):
        return self.Month
