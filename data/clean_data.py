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


# ===============================================
# 4. REMOVE NEGATIVE VALUES
# ===============================================
numeric_cols = ["files_changed", "lines_added", "lines_deleted", "message_length"]
invalid_rows = df[(df[numeric_cols] < 0).any(axis=1)]
print("\nInvalid negative rows to remove:")
print(invalid_rows)

df = df[~(df[numeric_cols] < 0).any(axis=1)]

# ===============================================
# 5. REMOVE LOGICALLY INCONSISTENT ROWS
#    (0 files changed but lines changed != 0)
# ===============================================
inconsistent = df[(df["files_changed"] == 0) &
                  ((df["lines_added"] > 0) | (df["lines_deleted"] > 0))]

print("\nInconsistent rows to remove:")
print(inconsistent)

df = df[~((df["files_changed"] == 0) &
          ((df["lines_added"] > 0) | (df["lines_deleted"] > 0)))]

# ===============================================
# 6. HANDLE OUTLIERS (cap at 99th percentile)
# ===============================================
def cap_outliers(series):
    threshold = series.quantile(0.99)
    return np.where(series > threshold, threshold, series)
for col in numeric_cols:
    df[col] = cap_outliers(df[col])

# ===============================================
# 7. CREATE NEW FEATURES 
# ===============================================
# Total lines changed
df["lines_changed"] = df["lines_added"] + df["lines_deleted"]
# Show Output
print(df[["lines_added", "lines_deleted", "lines_changed"]])

# Change density
df["change_density"] = df["lines_changed"] / df["files_changed"].replace(0, 1)
