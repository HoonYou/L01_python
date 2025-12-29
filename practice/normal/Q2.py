# [실습 2]
# 입력된 문자열을 뒤집은 문자열을 구하시오.
# ex) banana 입력 시 ananab 출력
# answer = ""
# # 로직 작성
# for i in range(len(word) - 1, -1, -1):
#     answer = answer + word[i]
# print(answer)

word = "banana"

print(word[::-1])
# print(reversed_word)  # 'banana' 입력 시 reversed_word == 'ananab'
