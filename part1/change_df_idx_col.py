from list_to_dataframe import df

df.index = ['학생1', '학생2']
df.columns = ['연령', '남여', '소속']
print('행 인덱스, 열 이름 변경하기', df, df.index, df.columns, sep='\n', end='\n\n')


df.rename(columns={'연령': '나이', '남여': '성별', '소속': '학교'}, inplace=True)
print("열 이름 중 '연령'을 '나이'으로, '남녀'를 '성별'로, '소속'을 '학교'로 바꾸기")
print(df, df.index, df.columns, sep='\n', end='\n\n')


df.rename(index={'학생1': '준서', '학생2': '예은'}, inplace=True)
print("df의 행 인덱스 중에서 '학생1'을 '준서'로, '학생2'를 '예은'로 바꾸기")
print(df, df.index, df.columns, sep='\n', end='\n\n')
