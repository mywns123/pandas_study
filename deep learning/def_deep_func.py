import numpy as np


def array_type(title, arrays):
    print(title, " : ", "배열 크기/타입")
    print("shape = ", arrays.shape)
    print("dtype = ", arrays.dtype)
    print("dimen = ", np.ndim(arrays))
    print("len   = ", len(arrays), end='\n\n')


# 레이블당 샘플 개수 확인
def prn_sample_cnt(ret_cnt):
    print("# 레이블당 샘플 개수 확인")
    print("type(ret_cnt) : ", type(ret_cnt))
    print("len(ret_cnt) : ", len(ret_cnt))
    print("ret_cnt[0] : ", ret_cnt[0])
    print("ret_cnt[1] : ", ret_cnt[1])
    print("샘플 개수 : ", np.sum(ret_cnt[1]), end='\n\n')