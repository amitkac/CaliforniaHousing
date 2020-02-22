
import os
from six.moves import urllib
import tarfile
import pandas as pd


class LoadData():

    def __init__(self, url):
        self.url = url
        self.housing_path = os.path.join("datasets", "housing")
        self.fetch_housing_data()
        # self.load_housing_data()

    def fetch_housing_data(self):
        housing_url = self.url
        if not os.path.isdir(self.housing_path):
            housing_path = self.housing_path
            os.makedirs(housing_path)
            tgz_path = os.path.join(housing_path, "housing.tgz")
            urllib.request.urlretrieve(housing_url, tgz_path)
            housing_tgz = tarfile.open(tgz_path)
            housing_tgz.extractall(path=housing_path)
            housing_tgz.close()
        else:
            pass

    @classmethod
    def load_housing_data(cls, self):
        csv_path = os.path.join(self.housing_path, "housing.csv")
        housingData = pd.read_csv(csv_path)
        self.housingData = housingData
