import pandas as pd

def load_and_clean_data(filepath):
    """
    Load the reactor performance data from a CSV file and clean it.
    """
    
    data = pd.read_csv(filepath)

    # Basic data cleaning (handling missing values, if necessary)
    if data.isnull().values.any():
        data = data.fillna(method='ffill')  

    return data

if __name__ == "__main__":
    data = load_and_clean_data('data/reactor_performance.csv')
    print(data.head())
