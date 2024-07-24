# 2024_07_24

# numpy.ndarray 클래스

"""
ndarray.ndim
: 어레이의 축의 개수(차원).

ndarray.shape
: 어레이의 차원. 각 차원의 어레이의 크기를 나타내는 정수의 튜플.
n개의 행, m개의 열을 갖는 행렬의 경우, shape은 (n, m). 따라서 shape 튜플의 길이는 축의 개수가 됨.

ndarray.size
: 어레이의 요수의 총 개수. shape 튜플의 요소의 곱과 같음.

ndarray.dtype
: 어레이의 요소의 타입을 나타내는 객체.
표준 파이썬 타입을 이용해서 dtype을 만들거나 지정할 수 있음.
이 외에도 NumPy는 numpy.int32, numpy.int16, numpy.float64와 같은 고유한 타입을 제공함.

ndarray.itemsize
: 어레이의 각 요소의 바이트 크기.
예를 들어, float64 타입의 요소를 갖는 어레이는 itemsize가 8 (=64/8).
complex32 타입을 갖는 어레이의 itemsize는 4 (=32/8). ndarray.dtype.itemsize와 같음.

ndarray.data
: 어레이의 실제 요소를 갖는 버퍼.
보통, 인덱스 기능을 이용해서 어레이의 요소에 접근하기 때문에 이 속성을 사용할 필요가 없을 것임.
"""

import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
print('a.shape:', a.shape)             # 어레이의 차원
print('a.ndim:', a.ndim)               # 어레이의 축의 개수
print('a.dtype.name:', a.dtype.name)   # 어레이 요소의 타입
print('a.itemsize:', a.itemsize)       # 어레이 요소의 바이트 크기
print('a.size:', a.size)               # 어레이 요소의 총 개수
print('type(a):', type(a))             # 어레이의 타입

'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
a.shape: (3, 5)
a.ndim: 2
a.dtype.name: int32
a.itemsize: 4
a.size: 15
type(a): <class 'numpy.ndarray'>
'''