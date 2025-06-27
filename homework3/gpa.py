course1 = input().split()
course2 = input().split()
course3 = input().split()
course4 = input().split()
course5 = input().split()

def calculate_gpa(score):
    score = int(score)
    normalized_score = min(score, 90)  # 超过90分按90分计算
    return 4.0 * normalized_score / 90

total_credits = sum([
    int(course1[2]),
    int(course2[2]),
    int(course3[2]),
    int(course4[2]),
    int(course5[2])
])
weighted_gpa = (
    int(course1[2]) * calculate_gpa(course1[1]) +
    int(course2[2]) * calculate_gpa(course2[1]) +
    int(course3[2]) * calculate_gpa(course3[1]) +
    int(course4[2]) * calculate_gpa(course4[1]) +
    int(course5[2]) * calculate_gpa(course5[1])
)
print("GPA:{:.2f}".format(weighted_gpa / total_credits))
