import pandas as pd

def parse_metrics() -> pd.DataFrame :
    return pd.read_csv('data/metrics.csv', sep=',')
    
if __name__ == '__main__':
     parse_metrics()