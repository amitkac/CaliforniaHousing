from dataRead.loadData import LoadData
import pandas as pd
from dataProcessors import mercFxn
from Plotting import plots


URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"


def main():

    dat = LoadData(URL)
    LoadData.load_housing_data(dat)
    df = dat.housingData

    #  data cleaning

    

    mercCordObj = mercFxn.MercFx(df)
    x, y = mercCordObj.mercatorCord()
    z = plots.Plots(df, x, y)
    z.holoViewPlot()


if __name__ == '__main__':
    main()


# print(x[1:10])
