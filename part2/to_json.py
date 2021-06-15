import pandas as pd

# 판다스 DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
data = {
    'name': ['Jerry', 'Riah', 'Paul'],
    'algol': ["A", "A+", "B"],
    'basic': ["C", "B", "B+"],
    'c++': ["B+", "C", "C+"],
}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)  # name 열을 인덱스로 지정
print(df)

print("# to_json()메소드를 사용하여 JSON 파일로 내보내기, 파일 명은 df_sample.json로 저장")
df.to_json("./df_sample.json")