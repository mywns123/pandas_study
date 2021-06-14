import pandas as pd

exam_data = {
    '이름': ['서준', '우현', '인아'],
    '수학': [90, 80, 70],
    '영어': [98, 89, 95],
    '음악': [85, 95, 100],
    '체육': [100, 90, 90]
}
df = pd.DataFrame(exam_data)
print(df, end='\n\n')

df.loc[3] = 0
print("# 새호운 행(row) 추가 - 같은 원소 값을 입력", df, sep='\n', end='\n\n')

df.loc[4] = ['동규', 90, 80, 70, 60]
print("# 새호운 행(row) 추가 - 원소 값 여려개의 배열 입력", df, sep='\n', end='\n\n')

df.loc['행5'] = df.loc[3]
print("# 새호운 행(row) 추가 - 기존 행을 복사", df, sep='\n', end='\n\n')




