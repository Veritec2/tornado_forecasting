"""
Configuration loader with an intentional bug
"""

def load_config(config_path):
    """Load configuration file"""
    # BUG: This will fail - missing 'encoding' parameter
    with open(config_path, 'r') as f:
        config = f.read()
    
    # BUG: Wrong variable name
    return configuration  # Should be 'config'
