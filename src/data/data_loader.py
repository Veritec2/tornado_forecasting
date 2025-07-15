"""
Data loader module for tornado forecasting project
"""
import numpy as np

def load_tornado_data(filepath):
    """Load tornado data from CSV file"""
    print(f"Loading data from {filepath}")
    # Using numpy for numerical operations
    data = np.loadtxt(filepath, delimiter=',')
    return data

def validate_data(data):
    """Validate loaded data"""
    print("Validating data shape and type...")
    if not isinstance(data, np.ndarray):
        return False
    return True

def preprocess_data(data):
    """Preprocess the tornado data"""
    # New function added by colleague
    print("Preprocessing data...")
    return data
