import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕' 으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./남북한발전전력량.xlsx')

pd.set_option('display.max_columns', len(df.columns))  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 30)  # 출력 열의 너비
pd.set_option('display.width', 1000)  # 출력 전체폭 너비

df_ns = df.iloc[[0, 5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

tdf_ns = df_ns.T
print(tdf_ns.head())

tdf_ns.plot(kind='bar', title="남북한발전전력량")
plt.show()
