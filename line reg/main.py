import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\wilsen\OneDrive\Desktop\self made models\line reg\data_corr.csv")

def linear_regression(x_train,y_train):
    x = df.iloc[:,0].sum()
    y = df.iloc[:,1].sum()
    df["x2"]  = (df.iloc[:,0]**2).sum()
    df["xy"] = (df.iloc[:,0] * df.iloc[:,1]).sum()
    print(df)
    

linear_regression(df,df)