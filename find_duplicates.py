import os
import pandas as pd

file = "statcast_data.csv"

df = pd.read_csv(file)

df2 = df[['player_name', 'pitcher']].drop_duplicates()
print(df2[['player_name']].value_counts())

print(df[df['player_name'].str.contains('Feigl')])
