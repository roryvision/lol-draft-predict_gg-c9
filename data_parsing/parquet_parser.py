import pandas as pd

file_name = 'wards_placed.parquet'

df = pd.read_parquet(file_name)

print(df) 
