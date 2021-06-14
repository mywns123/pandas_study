import pandas as pd

exam_data = {'name': ['test1', 'test2', 'test3'],
             'math': [90, 80, 70],
             'eng': [98, 89, 95],
             'music': [85, 95, 100],
             'kor': [100, 90, 90]
             }

df = pd.DataFrame(exam_data)
print(df)


df = df.set_index('name')
print(df, sep='\n', end='\n\n')

print(df.loc['test1'], sep='\n', end='\n\n')

print(df.eng)

add_dict = {'name': 'test4', 'math': None, 'eng': 99, 'music':99, 'kor':99}
sr_add = pd.Series(add_dict, name=add_dict['name'])

df.dropna(axis=0, inplace=True)
print(df, end='\n\n' )