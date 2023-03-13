import pandas as pd
from mtranslate import translate

input_file = input("Enter your excel file name: ")
input_file = input_file + '.xlsx'
df = pd.read_excel(input_file)

for i in range(len(df)):
    for j in range(len(df.columns)):
        cell = df.iloc[i, j]
        if isinstance(cell, str):
            result = translate(cell, 'en', 'es')
            df.iloc[i, j] = result

df.to_excel('output1.xlsx', index=False)
