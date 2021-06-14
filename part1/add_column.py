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

df['국어'] = [80, 90, 100]
print("# 테이터프레임 df에 '국어'점수 열(column)을 추가, 테이터 값은 80지정", df, sep='\n')

df['평균'] = round(df.mean(axis=1), 2)
df['총점'] = df.sum(axis=1)
print("# 테이터프레임 df에 '평균', '총점' 열(column)을 추가", df, sep='\n')
