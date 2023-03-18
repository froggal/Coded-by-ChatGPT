while True:
    # 사용자로부터 입력 받기
    expression = input("계산식을 입력하세요: ")
    
    # 프로그램 종료 조건 확인
    if expression.lower() == "exit":
        print("프로그램을 종료합니다.")
        break
    
    # 계산 수행
    try:
        result = eval(expression)
        print("결과는 ", result, "입니다.")
    except:
        print("잘못된 입력입니다.")
