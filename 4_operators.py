print('===== 연산자 ====')

# 연산 -> 처리를 하기 위한 목적
# 1. 산술 연산자
print('==산술연산자==')
a = 5
b = 2

# 사칙연산 (더하기, 빼기, 곱하기, 나누기)
print(a + b) # 7 -> int
print(a - b) # 3 -> int
print(a * b) # 10 -> int
print(a / b) # 2.5 -> float (int / int => float)

# 몫, 나머지, 제곱
# //, %, **
print(a // b)
print(a % b) # ... 뒤에 붙어서 %는 나머지이다.
print(a ** b)

# print(12/0) # 수학적으로 할 수 없는 연산은 파이썬도 할 수 없다.


# 2. 복합 연산자
# a = a + b -> 너무 길다
# 산술연산자 & 할당연산자를 함께(복합) 쓰는 연산
# +=, -=, *=
print('==복합연산자==')

print(a)
a += 1
print(a)

# 3. 비교 연산자

# 값과 값을 비교한다. -> True, False
# A와 B를 비교, 딱 두개만 비교

print('==비교연산자==')

# (1) 대소 비교
print(a, b) # 6 2

print(a < b) # a가 작다면 True / a가 작지 않다면 False
print(a >= b) # a가 크거나 같다면, True

# 무엇이 맞는가에 대한 고민이 든다면?
# 일단 실행 (>= / =>)

# (2) 일치 여부 비교
# == : 같다.
# != : 같지 않다.

print(a == b)
print(a != b)

# 숫자 외 자료형의 경우
c = '123'
d = '456'

# print(a > d) # 같은 자료형이 아니면, 대소 비교 어려움
print(a == d) # 같은 자료형끼리 비교하지 않더라도, 일치 비교는 가능하다

# 4. 논리연산자
print('==논리연산자==')
# False로 해석될 수 있는 변수 e 작성
e = 0
# e = 0.0
# e = ""
print(type(e))
print(bool(e))

print(a, b, c, d, e)
# 6 2 "123" "456" 0

# A and B : A,B 둘다 True여야 True 
# A or B : A,B 둘중 하나라도 True 이면, True
# not A : A가 False이면, True

# 비교연산을 논리연산의 재료로 삼기
print(a > b) # True
print(c == d) # False
print(a > b and c == d) # True and False -> False

condition_1 = a > b
condition_2 = c == d
print(condition_1 and condition_2) # False
print(condition_1 or condition_2) # True

# 논리연산과 단축평가
print('==단축평가==')
print(True or False) # True를 만나고, or 연산임을 안 순간 더이상 평가하지 않음

# 극단적 예시 중 하나
print(True or sdflwnnknljhqljwhjn) # True
print(False and jihljugiuiukng) # False

# 연산자 정리
# "처리"

# 1. 산술 연산자 (+,-,*,/,//,%,**)
# 2. 복합 연산자 (+=, -=, *= ...)
# 3. 비교 연산자 (==, !=, <, >, >=, <=)
# 4. 논리 연산자 (and, or, not)
