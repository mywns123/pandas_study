import pandas as pd

exam_data = {
    '수학': [90, 80, 70],
    '영어': [98, 89, 95],
    '음악': [85, 95, 100],
    '체육': [100, 90, 90]
}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print('exam_data', df, sep='\n', end='\n\n')

print("# 행 인덱스를 사용하여 행 1개를 선택")
label1 = df.loc['서준']  # loc 인덱서를 사용
print('label1', label1, sep='\n', end='\n\n')

position1 = df.iloc[0]  # iloc 인덱서를 사용
print('position1', position1, sep='\n', end='\n\n')


print("# 행 인덱스를 사용하여 2개 이상의 행 선택 - list이용")
label2 = df.loc[['서준', '우현']]
print('label2', label2, sep='\n', end='\n\n')

position2 = df.iloc[[0, 1]]
print('position2', position2, sep='\n', end='\n\n')


print("# 행 인덱스의 범위를 지정하여 행 선택")
label3 = df.loc['서준':'우현']
print('label3', label3, sep='\n', end='\n\n')

position3 = df.iloc[0:1]
print('position3', position3, sep='\n', end='\n\n')