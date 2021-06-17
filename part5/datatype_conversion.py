import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("# 각 열의 자료형 확인")
print(df.dtypes, '\n')

print("# horsepower 열의 고유값 확인")
print(df['horsepower'].unique(), '\n')

nan_list = [int(i) for i, a in df['horsepower'].items() if a == "?"]
print(" '?' 데이터 검색 결과 :", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')

print("# 누락 데이터('?') np.nan 으로 변경")
df['horsepower'].replace('?', np.nan, inplace=True)

nan_list = [int(i) for i, a in df['horsepower'].isna().items() if a is True]
print(" 'non' 데이터 검색 결과 :", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')

df.dropna(subset=['horsepower'], axis=0, inplace=True)
nan_list = [int(i) for i, a in df['horsepower'].isna().items() if a is True]
print(" 'non' 데이터 검색 결과 :", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')

print("# horsepower 열의 자료형 확인", df['horsepower'].dtypes, sep='\n', end='\n\n')

df['horsepower'] = df['horsepower'].astype('float')

print("# horsepower 열의 자료형 확인", df['horsepower'].dtypes, sep='\n', end='\n\n')

print("# origin 열의 고유값 확인")
print(df['origin'].unique(), '\n')

print("# origin 열의 자료형 확인",  df['origin'].dtypes,  df['origin'][20:30], sep='\n', end='\n\n')
print("# 정수형 데이터를 문자형 데이터로 변환")
df['origin'].replace({1:'USA', 2:'EU', 3:'JAPAN'}, inplace=True)
print("# origin 열의 자료형 확인",  df['origin'].dtypes,  df['origin'][20:30], sep='\n', end='\n\n')

print("# origin 열의 고유값과 자료형 확인")
print(df['origin'].unique(), df['origin'].dtypes, sep='\n', end='\n\n')

print("# 범주형을 문자열로 다시 변환 전", df['origin'].dtypes, sep='\n', end='\n\n')
df['origin'] = df['origin'].astype('category')
print("# origin 열의 문자열 자료형을 범주형으로 변환 후", df['origin'].dtypes, sep='\n', end='\n\n')

print("# 범주형을 문자열로 다시 변환")
df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes, sep='\n', end='\n\n')