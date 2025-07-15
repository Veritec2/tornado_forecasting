"""
Data loader module for tornado forecasting project
"""
import pandas as pd
import numpy as np

def load_tornado_data(filepath):
    """Load tornado data from CSV file"""
    print(f"Loading data from {filepath}")
    # Using pandas for better data handling
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def validate_data(data):
    """Validate loaded data"""
    if data is None:
        return False
    
    # Check if it's a DataFrame
    if hasattr(data,'columns'):
        required_columns = ['data','location','intensity']
    for col in required_columns:
        if col not in data.columns:
            print(f"Missing required column: {col}")
            return False
        
    return True    

def preprocess_data(data):
    """Preprocess the tornado data"""
    # New function added by colleague
    print("Preprocessing data...")
    return data
