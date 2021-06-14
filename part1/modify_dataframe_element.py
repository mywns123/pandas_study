import pandas as pd

exam_data = {
    '이름': ['서준', '우현', '인아'],
    '수학': [90, 80, 70],
    '영어': [98, 89, 95],
    '음악': [85, 95, 100],
    '체육': [100, 90, 90]
}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print("# '이름' 열을 새로운 인덱스로 지정하고, df객체에 변경사항 반영", df, sep='\n', end='\n\n')

print("# 테이터프레임 df의 특정 원소를 변경하는 방법 iloc : '서준'의 '체육'점수 100 -> 80")
df.iloc[0][3] = 80
print(df, end='\n\n')

print("# 테이터프레임 df의 특정 원소를 변경하는 방법 iloc : '서준'의 '체육'점수 80 -> 60")
df.iloc[0][3] = 60
print(df, end='\n\n')

print("# 테이터프레임 df의 특정 원소를 변경하는 방법 loc : '서준'의 '체육'점수 60 -> 90")
df.loc['서준']['체육'] = 90
print(df, end='\n\n')

print("# 테이터프레임 df의 특정 원소를 변경하는 방법 loc : '서준'의 '체육'점수 90 -> 100")
df.loc['서준']['체육'] = 100
print(df, end='\n\n')

print("# 테이터프레임 df의 원소 여러개를 변경하는 방법: '서준'의 '음악', '체육'점수 모두 50")
df.loc['서준', ['음악', '체육']] = 50
print(df, end='\n\n')

print("# 테이터프레임 df의 원소 여러개를 변경하는 방법: '서준'의 '음악', '체육'점수 100, 50")
df.loc['서준', ['음악', '체육']] = 100, 50
print(df, end='\n\n')