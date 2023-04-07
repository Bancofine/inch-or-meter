unit = input("변환할 단위를 입력하세요 (inch 또는 meter): ")

if unit == "inch":
    inch = float(input("인치를 입력하세요: "))  # 사용자로부터 인치 입력받기
    meter = inch * 0.0254  # 인치를 미터로 변환하기
    print("{:.2f} 인치는 {:.2f} 미터입니다.".format(inch, meter))  # 결과 출력하기

elif unit == "meter":
    meter = float(input("미터를 입력하세요: "))  # 사용자로부터 미터 입력받기
    inch = meter / 0.0254  # 미터를 인치로 변환하기
    print("{:.2f} 미터는 {:.2f} 인치입니다.".format(meter, inch))  # 결과 출력하기

else:
    print("잘못된 단위입니다. inch 또는 meter 중 하나를 입력해주세요.")
