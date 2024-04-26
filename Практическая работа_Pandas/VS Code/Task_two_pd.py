import pandas as pd

input_df = [{'name' : 'Sujeet', 'age' : 10}, 
            {'name' : 'Sameer', 'age' : 11},
            {'name' : 'Simit', 'age' : 12}]

df = pd.DataFrame(input_df)
print('Orginal DataFrame: \n', df)

print('\nRows iterated using iterrows():')
for index, row in df.iterrows():
    print(row['name'], row['age'])