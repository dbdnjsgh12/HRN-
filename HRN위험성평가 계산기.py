def calculate_HRN(likelihood, frequency, severity, exposure):
    # HRN 계산
    HRN = likelihood * frequency * severity * exposure

    # 등급 할당
    if HRN <= 1:
        grade = "무시 할 수 있는 위험"
    elif HRN >= 2 and HRN <= 5:
        grade = "매우 낮은 위험"
    elif HRN >= 6 and HRN <= 10:
        grade = "낮은 위험"
    elif HRN >= 11 and HRN <= 50:
        grade = "상당한 위험"
    elif HRN >= 51 and HRN <= 100:
        grade = "높은 수준의 위험"
    elif HRN >= 101 and HRN <= 500:
        grade = "매우 높은 수준의 위험"
    elif HRN >= 501 and HRN <= 1000:
        grade = "극한 위험"
    else:
        grade = "수용 할 수 없는 위험"

    return HRN, grade

def main():
    while True:
        # 사용자로부터 발생 가능성, 노출 빈도, 상해의 정도, 노출된 사람 수 입력 받기
        likelihood = int(input("사고발생 가능성을 0부터 15까지의 숫자로 입력하세요: "))
        frequency = int(input("노출 빈도를 0부터 5까지의 숫자로 입력하세요: "))
        severity = int(input("상해의 정도를 0부터 15까지의 숫자로 입력하세요: "))
        exposure = int(input("사고에 노출된 사람 수의 정도를 1부터 12까지의 입력하세요: "))

        # HRN 계산 및 등급 출력
        HRN, grade = calculate_HRN(likelihood, frequency, severity, exposure)
        print("\n===== HRN 및 등급 =====")
        print(f"HRN: {HRN}")
        print(f"등급: {grade}")

        # 추가 입력 여부 확인
        answer = input("더 평가하시겠습니까? (Y/N): ")
        if answer.upper() != 'Y':
            break

# 프로그램 실행
main()