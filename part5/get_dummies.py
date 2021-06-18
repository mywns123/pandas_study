import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

pd.set_option('display.max_columns', len(df.columns))  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', int(df['name'].apply(len).max()))  # 출력 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 출력 전체폭 너비

print('df.head()', '\n', df.head(), '\n')


df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print("# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기")
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

# 3개의 bin 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'],  # 데이터 배열
                      bins=bin_dividers,  # 경계 값 리스트
                      labels=bin_names,  # bin 이름
                      include_lowest=True)  # 첫 경계값 포함

print("# hp_bin 열의 범주형 데이터를 더미 변수로 변환")
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15), '\n')

print("df[['horsepower', 'hp_bin']].head(15)", '\n', df[['horsepower', 'hp_bin']].head(15), '\n')
