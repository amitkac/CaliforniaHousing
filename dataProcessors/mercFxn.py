
import numpy as np
import pandas as pd


class MercFx():
    ''' Calculates the mercator cordinates'''

    def __init__(self, x):
        self.lat = x.latitude
        self.lon = x.longitude

        # self.mercatorCoord()

    def mercatorCord(self):

        lat = self.lat
        lon = self.lon

        r_major = 6378137.000
        x = r_major * np.radians(lon)
        scale = x/lon
        y = 180.0/np.pi * np.log(np.tan(np.pi/4.0 +
                                        lat * (np.pi/180.0)/2.0)) * scale
        return x, y
