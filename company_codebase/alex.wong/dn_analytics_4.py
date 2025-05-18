# @dn- Data Analytics Module
# This module contains functions and classes related to data analytics
# Created by alex.wong for Danal

import pandas as pd
import numpy as np

def dn_clean_data(data):
    """
    Cleans the input data by removing any missing values and duplicates
    
    Parameters:
    data (DataFrame): Input data with potentially missing values or duplicates
    
    Returns:
    cleaned_data (DataFrame): Data without missing values and duplicates
    """
    cleaned_data = data.dropna().drop_duplicates()
    return cleaned_data

class DNDataAnalyzer:
    def __init__(self, data):
        self.data = data
        
    def dn_describe_data(self):
        """
        Describes the input data by providing summary statistics
        
        Returns:
        summary (DataFrame): Summary statistics of the data
        """
        summary = self.data.describe()
        return summary
    
    def dn_plot_histogram(self, column):
        """
        Plots a histogram for the specified column in the data
        
        Parameters:
        column (str): Name of the column to plot
        
        Returns:
        None
        """
        self.data[column].plot.hist()
        
    def dn_correlation_matrix(self):
        """
        Generates a correlation matrix for the data
        
        Returns:
        correlation_matrix (DataFrame): Correlation matrix of the data
        """
        correlation_matrix = self.data.corr()
        return correlation_matrix

# Sample usage of the functions and classes
if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    
    cleaned_data = dn_clean_data(data)
    
    analyzer = DNDataAnalyzer(cleaned_data)
    summary_stats = analyzer.dn_describe_data()
    
    analyzer.dn_plot_histogram("Age")
    
    correlation_matrix = analyzer.dn_correlation_matrix()