import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("# horsepower 열의 고유값 확인", df['horsepower'].unique(),  sep='\n', end='\n\n')

nan_list = [int(i) for i, a in df['horsepower'].items() if a == "?"]
print(" '?' 데이터 검색 결과 :", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)
print("# horsepower 열의 고유값 확인", df['horsepower'].unique(),  sep='\n', end='\n\n')

nan_list = [int(i) for i, a in df['horsepower'].items() if a == "?"]
print(" '?' 데이터 검색 결과 :", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')

print("누락 데이터 행을 삭제 전 행의 개수", df['horsepower'].shape)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
print("누락 데이터 행을 삭제 전 행의 개수", df['horsepower'].shape)

print("# horsepower 열의 자료형 확인", df['horsepower'].dtypes,  sep='\n', end='\n\n')
df['horsepower'] = df['horsepower'].astype('float')
print("# horsepower 열의 자료형 확인", df['horsepower'].dtypes,  sep='\n', end='\n\n')

print("# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기")
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

# 3개의 bin 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'],  # 데이터 배열
                      bins=bin_dividers,  # 경계 값 리스트
                      labels=bin_names,  # bin 이름
                      include_lowest=True)  # 첫 경계값 포함

print("# horsepower 열, hp_bin 열의 첫 15행을 출력")
print(df[['horsepower', 'hp_bin']].head(15), '\n')

print(df['hp_bin'].cat.categories)











