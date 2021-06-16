import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

pd.set_option('display.max_columns', len(df.columns))  # 출력할 최대 열의 개수

pd.set_option('display.max_colwidth', 30)  # 출력 열의 너비

pd.set_option('display.width', 1000)  # 출력 전체폭 너비

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
print("# 데이터프레임 df의 내용을 일부 확인", end='\n\n')
print("df.head()", df.head(), sep='\n', end='\n\n')
print("df.tail()", df.tail(), sep='\n')

print("# df의 모양과 크기 확인:(행의 개수, 열의 개수)를 투플로 반환")
print(df.shape)
print()

print("# 데이터프레임 df의 내용 확인")
print(df.info())
print()

print("# 데이터프레임 df의 자료형 확인")
print(df.dtypes)
print()

print("# 시리즈(mpg 열)의 자료형 확인")
print(df.mpg.dtypes)
print()

print("# 데이터프레임 df의 기술통계 정보 확인")
print(df.describe(), '\n', df.describe(include='all'))
