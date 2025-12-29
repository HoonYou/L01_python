# 학생들의 이름과 시험 점수가 2차원 리스트로 주어집니다.
# 점수가 두 번째로 높은 학생(들)의 이름을 리스트 형태로 출력하시오.
# (점수가 가장 높은 학생이 여러 명일 수 있으며, 두 번째로 높은 점수도 여러 명일 수 있습니다.)
scores = [
    ["Kim", 88],
    ["Lee", 95],
    ["Park", 92],
    ["Choi", 85],
    ["Jung", 95],
    ["Kang", 92],
]

scores = [
    ["Kim", 88],
    ["Lee", 95],
    ["Park", 92],
    ["Choi", 85],
    ["Jung", 95],
    ["Kang", 92],
]

# 1. 점수만 추출하고 중복 제거

# unique_scores = []
# for name, score in scores:
#     unique_scores.append(score)
# score_2nd = (sorted(set(unique_scores), reverse=True))[1]
# print(score_2nd)


score_2nd = sorted(set([score for name, score in scores]), reverse=True)[1]
print(score_2nd)

answer = [name  for name, score in scores if score == score_2nd]
print(answer)

# # 3. 해당 점수를 가진 학생들 찾기
# runner_up_students = [name for name, score in scores if score == second_highest]

# print(runner_up_students)
