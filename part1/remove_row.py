import pandas as pd
# DataFrame() 함수로 테이터프레임 변환, 변수 df에 저장
exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df, end='\n\n')

# 테이터프레임 df를 복제하여 변수 df2에 저장, df2의 1개 행(row)을 삭제
df2 = df[:]
print("df2", df2, sep='\n', end='\n\n')

df3 = df2.drop('우현')
print("df3", df3, sep='\n', end='\n\n')

# 테이터프레임 df를 복제하여 변수 df4에 저장, df4의 2개 행(row)을 삭제
df4 = df[:]
print("df4", df4, sep='\n', end='\n\n')

df5 = df4.drop(['우현', '인아'], axis=0)
print("df5", df5, sep='\n', end='\n\n')

df.drop('인아', inplace=True)
print("df '인아' 행 인덱스 삭제 drop inplace=True", df, sep='\n', end='\n\n')

df.drop(['서준', '우현'], axis=0, inplace=True)
print("df '서준', '우현' 행 인덱스 삭제 drop inplace=True", df, sep='\n')
