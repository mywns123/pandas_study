import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
tup_index = ['이름', '생년월일', '성별', '학생여부']
sr = pd.Series(tup_data, tup_index)
print(sr)

print("튜플를 시리즈로 변화하여 변수 sr에 저장", sr, sep='\n', end='\n\n')
print(type(sr.index), sr.index, sep='\n', end='\n\n')
print(type(sr.values), sr.values, sep='\n', end='\n\n')