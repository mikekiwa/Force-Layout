import pandas as pandas
print(pd.read_csv('input.csv', usecols=['col1,col2']).to_json('output.json'))