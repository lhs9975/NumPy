# NumPy의 주요한 객체는 다차원의 동종 어레이.
# 보통 숫자로 구성되는 어레이는 모두 동일한 타입의 요소를 갖고, 음이 아닌 정수(0, 1, 2, ...)로 인덱싱된다.

# 2. 기본 사용
import numpy as np

a = np.array([1, 2, 3])  # 1차원 어레이 생성
print(a)

# 3. 어레이 생성/초기화
a = np.zeros(3)
b = np.ones((2,3))

print(a)
print(b)

# 4. 수학 연산
a = np.array([1., 2., 3., 4.])
b = np.array([4., 3., 2., 1.])

print(np.add(a, b))
print(np.multiply(a, b))
print(np.mean(a))

# np.add() 함수를 이용해서 두 어레이의 합을 계산할 수 있다.
# np.multiply() 함수를 이용해서 두 어레이의 곱을 계산할 수 있다.
# np.mean() 함수를 이용해서 어레이의 평균을 계산할 수 있다.

# 5. 난수 생성
a = np.random.rand(2, 5)
b = np.random.randn(3, 4)

print(a)
print(b)

# np.random.rand() 함수를 이용해서 0과 1 사이의 난수로 구성된 어레이를 생성할 수 있다.
# np.random.randn() 함수를 이용해서 표준 정규 분포를 따르는 난수로 구성된 어레이를 생성할 수 있다.

# 6. 상수
a = np.pi
b = np.e

print(a)
print(b)

# np.pi 상수는 원주율을 나타낸다.
# np.e 상수는 오일러 상수를 나타낸다.