import pandas as pd
import glob


csv_files = glob.glob("./*.csv")

dfs = []

for filename in csv_files:
    df = pd.read_csv(filename)
    dfs.append(df)

combine_csv = pd.concat(dfs, ignore_index=False, sort=False)
combine_csv.to_csv("./records.csv", index=True)
