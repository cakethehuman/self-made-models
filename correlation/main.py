import pandas as pd
import numpy as np

df = pd.read_csv(r"correlation\test.csv")
path = r"C:\Users\wilsen\OneDrive\Desktop\self made models\correlation\ "

def corr(data_frame):
    
    data_frame["xy"] = data_frame.iloc[:,0] * data_frame.iloc[:,1]
    data_frame["x2"] = data_frame.iloc[:,0] **2
    data_frame["y2"] = data_frame.iloc[:,1] **2
    #data gathering
    
    n = data_frame.shape[0]
    x = data_frame.iloc[:,0].sum()
    y = data_frame.iloc[:,1].sum()
    xy = data_frame.iloc[:,2].sum()
    x2 =  data_frame["x2"].sum()
    y2 = data_frame["y2"].sum()
    
    #R
    r_top = ((n*xy) - (x*y))
    r_bottom = (np.sqrt((n*(x2)-(x**2))) * (np.sqrt(n*(y2)-(y**2))))
    r = r_top/r_bottom
    
    

    df.to_csv(path+'result.csv',index = False)
    return print(r)

    
corr(df)