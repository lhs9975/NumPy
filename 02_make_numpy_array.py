# 2024_07_24

# np.array() 사용하기
# 파이썬 리스트 또는 튜플을 np.array() 함수에 전달하면 NumPy 어레이를 생성할 수 있다.


import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(type(a))
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b)
print(type(b))
print(b.dtype)

# 어레이를 생성할 때, np.array()에 숫자들을 그대로 입력하는 실수를 하게 됨.

# a = np.array(1,2,3,4)    # WRONG
# b = np.array([1,2,3,4])  # RIGHT
# c = np.array((1,2,3,4))  # RIGHT

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)