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

print("\n==== Missing Values ====")
print(df.isna().sum())

# ===============================================
# 3. REMOVE DUPLICATE commit_hash VALUES
# ===============================================
print("\nDuplicates before cleaning:", df.duplicated(subset="commit_hash").sum())

df = df.drop_duplicates(subset="commit_hash", keep="first")

print("Duplicates after cleaning:", df.duplicated(subset="commit_hash").sum())