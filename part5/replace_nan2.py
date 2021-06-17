import seaborn as sns

df = sns.load_dataset('titanic')

print("# embark_town 열의 829행의 NaN 데이터 출력")
print(df['embark_town'][825:830], '\n')

nan_list = [int(i) for i, a in df['embark_town'].isna().items() if a is True]
print("누락 데이터 검색 결과 :", df.embark_town[nan_list], sep='\n', end='\n\n')


print("# embark_town 열의 829행의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기")
most_counts = df['embark_town'].value_counts().max()
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print("df['embark_town']", most_freq, most_counts, sep='\n', end='\n\n')

df['embark_town'].fillna(most_freq, inplace=True)
print("# embark_town 열 NaN 값이 most_freq 값으로 치환", df.embark_town[nan_list], sep='\n', end='\n\n')

print("# embark_town 열의 829행의NaN 데이터 출력(NaN 값이 most_freq 값으로 대체)")
print(df['embark_town'][825:830], '\n')





