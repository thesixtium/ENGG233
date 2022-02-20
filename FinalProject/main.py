'''
Created by
Aleksander Berezowski
and
Xavier Champagne

Last modified:
2020-11-24
'''


# I M P O R T S
import Chart
import Date
import FileIO
import TemperatureData
import WeatherAnalyzer

weather = FileIO.FileIO("CalgaryWeather.csv")
dates = Date.Date(weather.dataTable)
analyzer = WeatherAnalyzer.WeatherAnalyzer(weather.dataTable, dates.returnYears())
charts = Chart.Chart()

def selection(n):

    selections = ['analyzer.getMinTemp()',
                  'analyzer.getMaxTemp()',
                  'analyzer.printResults(analyzer.getMinTempAnnually())',
                  'analyzer.printResults(analyzer.getMaxTempAnnually())',
                  'analyzer.printResults(analyzer.getAvgSnowfallAnnually())',
                  'analyzer.printResults(analyzer.getAvgTempAnnually())',
                  'charts.drawLineChart(dates.returnYears(), analyzer.getMinTempAnnually(), "Minimum Temperature of 1990-2019 Annually", "Year", "Degrees (Celsius)")',
                  'charts.drawLineChart(dates.returnYears(), analyzer.getMaxTempAnnually(), "Maximum Temperature of 1990-2019 Annually", "Year", "Degrees (Celsius)")',
                  'charts.drawBarChart(dates.returnYears(), analyzer.getAvgSnowfallAnnually(), "Average Snowfall of 1990-2019 Annually", "Year", "Amount (cm)")',
                  'charts.drawBarChart(dates.returnYears(), analyzer.getAvgTempAnnually(), "Average Temperature of 1990-2019 Annually", "Year", "Degrees (Celsius)")'
                  ]

    try:
        x = int(n) - 1
        exec(str(selections[x]))
    except:
        print("Invalid Input")


def menu():
    print()
    print("1- Get Minimum Temperature of 1990-2019")
    print("2- Get Maximum Temperature of 1990-2019")
    print("3- Get Minimum Temperature of 1990-2019 Annually")
    print("4- Get Maximum Temperature of 1990-2019 Annually")
    print("5- Get Average Snowfall between 1990-2019 Annually")
    print("6- Get Average Temperature between 1990-2019 Annually")
    print("7- LineChart Minimum Temperature of 1990-2019 Annually")
    print("8- LineChart Maximum Temperature of 1990-2019 Annually")
    print("9- BarChart Average Snowfall between 1990-2019 Annually")
    print("10- BarChart Average Temperature between 1990-2019 Annually")
    selection(input("Selection: "))

def main():
    while True:
        menu()

if __name__ == '__main__':
    main()
