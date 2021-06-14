import pandas as pd

exam_data = {
    '이름': ['서준', '우현', '인아'],
    '수학': [90, 80, 70],
    '영어': [98, 89, 95],
    '음악': [85, 95, 100],
    '체육': [100, 90, 90]
}
df = pd.DataFrame(exam_data)
print("# 데이터 프레임 df", df, sep='\n', end='\n\n')


df.set_index('이름', inplace=True)
print("# '이름' 열을 새로운 인덱스로 지정하고, df객체에 변경사항 반영", df, sep='\n', end='\n\n')

a = df.loc['서준', '음악']
print("# 데이터 프레임 df의 특정 원소 1개 선택('서준'의 '음악' 점수)", a, type(a), sep='\n', end='\n\n')

b = df.iloc[0, 2]
print(b, type(b), sep='\n', end='\n\n')

c = df.loc['서준', ['음악', '체육']]
print("# 데이터 프레임 df의 특정 원소 2개 선택('서준'의 '음악', '체육' 점수)", c, type(c), sep='\n', end='\n\n')

d = df.iloc[0, [2, 3]]
print(d, type(d), sep='\n', end='\n\n')

e = df.loc['서준', '음악': '체육']
print(e, type(e), sep='\n', end='\n\n')

f = df.iloc[0, 2:]
print(f, type(f), sep='\n', end='\n\n')

g = df.loc[['서준', '우현'], ['음악', '체육']]
print("# 데이터 프레임 df의 특정 원소 2개 선택('서준', '우현'의 '음악', '체육' 점수)", g, type(g), sep='\n', end='\n\n')

h = df.iloc[[0, 1], [2, 3]]
print(h, type(h), sep='\n', end='\n\n')

i = df.loc['서준': '우현', '음악': '체육']
print(i, type(i), sep='\n', end='\n\n')

j = df.iloc[0:2, 2:]
print(j, type(j), sep='\n', end='\n\n')

