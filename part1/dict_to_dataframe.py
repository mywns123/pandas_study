import pandas as pd
# 열 이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {
    'c0': [1, 2, 3],
    'c1': [4, 5, 6],
    'c2': [7, 8, 9],
    'c3': [10, 11, 12],
    'c4': [13, 14, 15]
}

# 판다스 DataFrame() 함수로 딕셔너리를 테이터프레임으로 변환, 변수 df에 저장.
df = pd.DataFrame(dict_data)
# df의 자료형 출력
print(type(df), df, sep='\n', end='\n\n')
# df의 인덱스, 컬럼 출력
print('df의 인덱스', df.index, sep='\n', end='\n\n')
print('df의 컬럼', df.columns, sep='\n')