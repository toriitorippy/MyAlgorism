# common
import pandas as pd
import numpy as np

# init part(データの読み込みと前処理)
file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
online_retail_data = pd.ExcelFile(file_url)
online_retail_data_table = online_retail_data.parse('Online Retail')

# 採点の都合上、文字列型に変換
online_retail_data_table['cancel_flg'] = online_retail_data_table.InvoiceNo.map(lambda x:str(x)[0])

# InvoiceNoの先頭が5であるものとIDがNullでないものが対象
target_online_retail_data_tb = online_retail_data_table[(online_retail_data_table.cancel_flg == '5') 
                                                        & (online_retail_data_table.CustomerID.notnull())]

target_online_retail_data_tb = target_online_retail_data_tb.assign(TotalPrice=target_online_retail_data_tb.Quantity * target_online_retail_data_tb.UnitPrice)

def homework(target_online_retail_data_tb, n):
    df = target_online_retail_data_tb
    df = df.groupby("CustomerID", as_index = False)["TotalPrice"].sum()
    df = df.sort_values('TotalPrice', ascending=False)
    df['index'] = np.arange(1, df['CustomerID'].count() + 1)
    df["Group"] = pd.qcut(df['index'], n)
    df = df.groupby("Group", as_index = False)["TotalPrice"].sum()
    Total = df["TotalPrice"].sum()
    df["Percentage"] = df["TotalPrice"]/Total
    my_result = df["Percentage"]
    return pd.Series(my_result)

homework(target_online_retail_data_tb, 10)