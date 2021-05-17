import numpy as np
import pandas as pd
from pandas import DataFrame
# URL
url_winequality_data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

# working place. everything 
def homework(url_winequality_data, n):
    import requests
    from io import StringIO
    import io

    data = requests.get(url_winequality_data,stream=True)
    df = pd.read_csv(io.BytesIO(data.content),sep=";")
    df_pH = df["pH"]
    df_dioxide_n = pd.qcut(df["total sulfur dioxide"],n)
    mean = pd.concat([df_pH, df_dioxide_n], axis=1).groupby("total sulfur dioxide")["pH"].mean()
    my_result = max(mean) + min(mean)

    return my_result

homework(url_winequality_data, 20)