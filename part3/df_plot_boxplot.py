import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕' 으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

pd.set_option('display.max_columns', len(df.columns))  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 30)  # 출력 열의 너비
pd.set_option('display.width', 1000)  # 출력 전체폭 너비

print("auto-mpg", df.head(), sep='\n', end='\n\n')

df[['mpg', 'cylinders']].plot(kind='box', title="연비의 분포 및 실린더 개수 분포")
plt.show()
