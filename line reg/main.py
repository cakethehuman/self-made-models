import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\wilsen\OneDrive\Desktop\self made models\line reg\data_corr.csv")


    
def a_calculation(n,x,y,x2,xy):
    a_top = ((y*x2) - (x*xy))
    a_bottom = ((n*x2) - (x**2))
    a = a_top/a_bottom
    print(a)

def b_calculation(n,x,y,x2,xy):
    print("ho")

def linear_regression(data_frame,x_train,y_train):
    n = data_frame.shape[0]
    x = data_frame[x_train].sum()
    y = data_frame[y_train].sum()
    data_frame["x2"]  = (data_frame[x_train]**2)
    data_frame["xy"] = (data_frame[x_train] * data_frame[y_train])
    x2 = data_frame["x2"].sum()
    xy = data_frame["xy"].sum()
    
    a_calculation(n,x,y,x2,xy)
    b_calculation(n,x,y,x2,xy)



    

linear_regression(df,"study_hour","grade")