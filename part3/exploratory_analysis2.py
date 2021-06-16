import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인")
print(df.count())
print()

print("# df.count()가 반환하는 객체 타입 출력")
print(type(df.count()))
print()

print("# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인")
unique_values = df['origin'].value_counts()  # origin제조국가
print(unique_values)
print()

print("# value_counts 메소드가 반환하는 객체 타입 출력")
print(type(unique_values))







