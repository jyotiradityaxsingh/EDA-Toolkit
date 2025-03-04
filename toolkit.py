import os
import pandas as pd
import numpy as np
from scipy.stats import trim_mean, mode

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

    def centralTendency(self):
        """Returns All The Measures In Measure of Central Tendency Applied On Each Column of The Data"""
        data = self.loadData()  # Load data here
        results = {}

        for column in data.columns:
            columnData = data[column].dropna()  # Drop NaN values For Calculations
            # Mean
            MeanValue = columnData.mean()
            # Trimmed Mean (Default Trimming Percentage: 10%)
            trimmedMeanValue = trim_mean(columnData, proportiontocut=0.1)
            # Median
            medianValue = columnData.median()
            # Mode
            modeResult = mode(columnData)
            modeValue = modeResult[0]
            results[column] = {
                'Mean': MeanValue,
                'Trimmed Mean': trimmedMeanValue,
                'Median': medianValue,
                'Mode': modeValue
            }

        resultsDataFrame = pd.DataFrame(results).T
        print(resultsDataFrame)