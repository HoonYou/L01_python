# 자료형

# 1. 숫자
# 1) 정수 (int)
print(1)
print(-1)
print(0)
print(type(1)) # 자료형 확인 가능

# 2) 실수
print(3.141592)
print(-12.3)

# 질문
print(type(3.0))
# <class 'float'>
# 소수점 여부에 따라, float가 된다.

# 2. 문자열 (str)
print('강동호')
print("이지원")
print(type('이름의 타입은?')) # <class 'str'>

print('"서채원"') # 같은 세트로 묶어 줘야만 한다. ->따옴표 안에 따옴표를 쓸 수도 있다
# print('"서채원') # 에러 발생

print(type('')) # 공백도, 빈문자열도 문자다!
print(type(' '))

print(123)
print('123')

print(type(123))
print(type('123'))

print(123 == '123') # 비교 연산을 통해 같은지 확인

# 3. 불린
print(True)
print(False)

print(type(True))
print(type(False))
# print(type(true)) # 에러 발생

# 정리!
# 1. 숫자 : 정수(int), 실수(float)
# 2. 문자 : 문자열(str) -> "12345" ,'!@#$!@#$!@#$' 문자들의 모음
# 3. 불린 : 불린형(bool) -> True, False (주의! 대소문자 구분 주의)


print('=== 명시적 형변환 ===')
# 정수형으로 변환 : int()
print(1.23)
print(int(1.23))

print(type(1.23))
print(type(int(1.23)))

print('20')
print(int('20')) 
# 정수로 "바로" 변환 가능한 형태일때 가능

print("20.0")
# print(int("20.0")) # 에러 발생

# 실수형 변환 : float()
print(float(-10)) # 정수를 실수로
print(float('20.0')) # 문자열을 실수로
print(type(float(-10)))

# 문자열 : str()
print(type(str(True)))

# 불린형 : bool()
# True / False
print(bool(0.0))
print(bool(0.0000000000000001))


# 자료형 정리
# 1. 숫자형
# 정수 (int) : 소수점이 없는 숫자 (0,+,-)
# 실수 (float) : 소수점이 있는 숫자 (3.14)

# 2. 문자열 (str)
# 문자의 형태를 가진 모든 글자의 모음
# "쌍따옴표", '따옴표' 를 통해 만든다 (단, 짝이 맞아야 함)
print('따옴표 "안"에 따옴표')
print('따옴표 \'안\'에 따옴표')

# 3. 불린형 (bool)
# True, False -> 대소문자 주의

# 각 자료형들은 내장함수 int(),float(),str(),bool()을 통해
# 명시적 형변환을 할 수 있습니다!