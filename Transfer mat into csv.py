from scipy.io import loadmat
import pandas as pd
data = loadmat(r"C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\tem\Data_Ning.mat")
df = data["Data"]
data2 =pd.DataFrame(df)

data2.to_csv(r"C:\\Users\\jiaxi\\OneDrive\Desktop\RBAC 2022\tem\Data_Ning.csv",index=None)
