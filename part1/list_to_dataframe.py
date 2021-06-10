import pandas as pd

list_data = [[15, '남', '덕영중'], [17, '여', '수리중']]
list_index = ['준서', '예은']
list_col = ['나이', '성별', '학교']

df = pd.DataFrame(data=list_data, index=list_index, columns=list_col)
print('리스트를 이용한 행 인덱스/열 이름 지정하여, 테이터프레임 만들기')
print(df, df.index, df.columns, sep='\n', end='\n\n')
