# # MNIST(손글씨) 데이터셋 불러오기 훈련세트와 테스트세트로 불러오기
# (①   (train_images, train_labels), (test_images, test_labels) = mnist.load_data()  )
#
# # train와 test 7:3으로 분류
# (①
# train_images, test_images, train_labels, test_labels = train_test_split(
#     train_images, train_labels,
#     test_size=0.3, random_state=42
# )
# )
# # 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
# # train이미지는 [0-255]사이의 값인 uint8 타입의 (48000, 28 , 28) 크기를 가지 3차원 배열을
# # -> 0과 1사이의 값을 가지는 float32타입의 (48000, 28*28)크기인 2차원 배열로 변경
# (② train_images = train_images.reshape(-1, 28 * 28)       )
# train_images = train_images / 255.0
#
# (③ test_images = test_images.reshape(-1, 28 * 28)       )
# test_images = test_images.astype('float32') / 255
#
# # 레이블을 범주형으로 원핫 인코딩
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
#
#
# # 모델 구조 정의하기 (신경망 생성, 여기에서는 Sequential 클래스 사용)
# (  ④
# dense1 = layers.Dense(100, activation='relu', input_shape=(28 * 28,), name="hidden1")
# dense3 = layers.Dense(50, activation='relu', name="hidden2")
# drop4 = layers.Dropout(0.4)
# dense2 = layers.Dense(10, activation='softmax', name="output")
# model = models.Sequential([dense1, dense3, drop4, dense2])
# )
#
# # 모델 컴파일 하기
# (⑤  model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])  )
#
# # fit() 메서드로 모델 훈련 시키기 : 128개씩 5번 반복
# (⑥   model.fit(train_images, train_labels, epochs=5, batch_size=128)          )
#
# # 테스트 데이터로 정확도 측정하기
# print("테스트 데이터로 정확도 측정하기")
# (⑦      test_loss, test_acc = model.evaluate(test_images, test_labels)        )
# print('test_acc  : ', test_acc)