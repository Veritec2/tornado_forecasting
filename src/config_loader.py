"""
Configuration loader - bug fixes applied
"""
import json

def load_config(config_path):
    """Load configuration file"""
    # FIXED: Added encoding parameter and proper error handling
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        
        # FIXED: Return correct variable name
        return config_data
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}
