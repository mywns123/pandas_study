import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
tup_index = ['이름', '생년월일', '성별', '학생여부']
sr = pd.Series(tup_data, tup_index)

print(f"sr[0]\n{sr[0]}")
print(f"sr['이름']\n{sr['이름']}")
print()
print(f"sr[[1, 2]]\n{sr[[1, 2]]}")
print(f"sr[['생년월일', '성별']]\n{sr[['생년월일', '성별']]}")
print()
print(f"sr[1 : 2]\n{sr[1 : 2]}")
print(f"sr['생년월일' : '성별']\n{sr['생년월일' : '성별']}")
