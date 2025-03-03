# Libraries
import os
import pandas as pd
import numpy as np

class EDAToolkit:

    def __init__(self, filePath, fileType):
        self.filePath = filePath
        self.fileType = fileType

    def loadData(self):
        """Loads The Data Based On The File Type"""
        if self.fileType == 'csv' or self.fileType == 'CSV' or self.fileType == '.csv':
            return pd.read_csv(self.filePath)
        elif self.fileType == 'excel' or self.fileType == 'Excel' or self.fileType == '.xlsx':
            return pd.read_excel(self.filePath)
        elif self.fileType == 'json' or self.fileType == 'JSON' or self.fileType == '.json':
            return pd.read_json(self.filePath)
        else:
            raise ValueError("Unsupported File Type")

    def peek(self):
        """Returns The First 5 Rows And Last 5 Rows of The Data"""
        data = self.loadData()
        print("FIRST 5 ROWS")
        print(data.head())
        print()
        print("Last 5 ROWS")
        print(data.tail())

    def info(self):
        """Returns The Info of The Dataset"""
        data = self.loadData()
        print("INFO")
        print(data.info())
        print()
        print("DESCRIPTION")
        print(data.describe())