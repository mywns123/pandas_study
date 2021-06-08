# 필요한 라이브러리 불러오기
from def_deep_func import *
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 50)  # 출력할 최대 열의 개수
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

# 0-19 테스트 이미지 출력
count = 0
for i in range(20):
    count += 1
    plt.subplot(4, 5, count)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.title("images[{}]".format(i))
plt.tight_layout()
plt.show()

# 0-19 레이블값 출력
print("0-19 레이블값 출력 ", [train_labels[i] for i in range(20)], end='\n\n')

# 5번째 이미지및 레이블 출력
print("5번째 이미지", pd.DataFrame(train_images[4]), sep='\n')
print("5번째 레이블", train_labels[4], sep='\n', end='\n\n')

# 레이블당 샘플 개수 확인
prn_sample_cnt(np.unique(train_labels, return_counts=True))
prn_sample_cnt(np.unique(test_labels, return_counts=True))

# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
# train이미지는 [0-255]사이의 값인 uint8 타입의 (48000, 28 , 28) 크기를 가지 3차원 배열을
# -> 0과 1사이의 값을 가지는 float32타입의 (48000, 28*28)크기인 2차원 배열로 변경
array_type("훈련이미지 타입/크기 변경 전 ", train_images)
train_images = train_images.reshape(-1, 28 * 28)
train_images = train_images / 255.0
array_type("훈련이미지 타입/크기 변경 후 ", train_images)

array_type("테스트 이미지 타입/크기 변경 전", test_images)
test_images = test_images.reshape(-1, 28 * 28)
test_images = test_images.astype('float32') / 255
array_type("테스트 이미지 타입/크기 변경 후", test_images)


# 레이블을 범주형으로 원핫 인코딩
print("레이블을 범주형으로 원핫 인코딩 전", train_labels.shape, pd.DataFrame(train_labels).head(), sep='\n', end='\n\n')
train_labels = to_categorical(train_labels)
print("레이블을 범주형으로 원핫 인코딩 후", train_labels.shape, pd.DataFrame(train_labels).head(), sep='\n', end='\n\n')

test_labels = to_categorical(test_labels)


# 모델 구조 정의하기 (신경망 생성, 여기에서는 Sequential 클래스 사용)
# 뉴런의 개수 : 512, 뉴련출력에 적용할 함수 : relu, 입력크기(28*28) 밀집층 추가( 완전연결층 )
dense1 = layers.Dense(100, activation='relu', input_shape=(28 * 28,), name="hidden1")
# 뉴런의 개수 : 10, 뉴련출력에 적용할 함수 : softmax, 입력 앞의 층 (은닉층)
dense3 = layers.Dense(50, activation='relu', name="hidden2")
drop4 = layers.Dropout(0.4) # overfit 감소 40%
dense2 = layers.Dense(10, activation='softmax', name="output")
model = models.Sequential([dense1, dense3, drop4, dense2])

# model 요약
print("model 요약")
model.summary()
print()


# 모델 컴파일 하기
"""
손실 함수 (loss): 손실 함수는 값을 예측하려할 때 데이터에대한 예측값과 실제의 값을 비교하는 함수로 모델을 훈련시킬 때 
                 오류를 최소화 시키기 위해 사용
        categorical_crossentropy: 여러 개의 카테고리가 있는 다중 분류, 
        binary_crossentropy:이진 분류, 
        mse(mean squared eror, mae) : 회귀문제, 
        시퀀스 학습 문제: CTC 언어인식)
옵티마이저 (optimizer) :  경사 하강법(rmsprop, sgd, adagrad, Adam, Nadam, AdaMax) 옵티마이저에 의해 결정.
"""

# model.compile(optimizer='Nadam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='AdaMax', loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='AdaGrad', loss='categorical_crossentropy', metrics=['accuracy'])