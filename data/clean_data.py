import pandas as pd
import numpy as np

# ===============================================
# 1. LOAD THE ENTIRE DATASET 
# ===============================================
df = pd.read_csv(r"E:\Software engineering projec\bug-risk\data\commits_small.csv")
print("==== Original shape ====")
print(df.shape)
print(df.head())

# ===============================================
# 2. CHECK BASIC INFO
# ===============================================
print("\n==== Data Info ====")
print(df.info())