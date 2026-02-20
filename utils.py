import os

def ensure_directories():
    """Ensure necessary directories exist."""
    os.makedirs('data', exist_ok=True)
    os.makedirs('models', exist_ok=True)

def load_data(filepath):
    """Load data from CSV."""
    return pd.read_csv(filepath)

# Add more utilities as needed