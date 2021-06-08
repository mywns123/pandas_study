# 필요한 라이브러리 불러오기
from def_deep_func import *
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
import pandas as pd

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 30)  # 출력할 최대 열의 개수
pd.set_option('display.width', 600)  # 콘솔 출력 너비

# MNIST(손글씨) 데이터셋 불러오기 훈련세트와 테스트세트로 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# train와 test 7:3으로 분류
train_images, test_images, train_labels, test_labels = train_test_split(
    train_images, train_labels,
    test_size=0.3, random_state=42
)

array_type("훈련이미지", train_images)
array_type("훈련라벨", train_labels)
array_type("검증이미지", test_images)
array_type("검증라벨", test_labels)