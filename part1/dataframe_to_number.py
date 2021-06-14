import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns', len(titanic.columns))
pd.set_option('display.max_colwidth', 15)  # 출력 열의 너비
pd.set_option('display.width', 1000)

print("# titanic 데이터 셋", type(titanic), titanic.head(), titanic.shape, sep='\n', end='\n\n')

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), type(df), sep='\n', end='\n\n')

print("# 데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition), sep='\n')

