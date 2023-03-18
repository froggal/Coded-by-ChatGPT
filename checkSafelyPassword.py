def check_password(password):
    # 비밀번호의 길이가 8자 이상인지 확인
    if len(password) < 8:
        return False
    
    # 비밀번호에 영문자, 숫자, 특수문자가 모두 포함되어 있는지 확인
    has_letter = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()":
            has_special = True
    if not (has_letter and has_digit and has_special):
        return False
    
    return True

# 사용자로부터 비밀번호 입력 받기
password = input("비밀번호를 입력하세요: ")

# 비밀번호 검사 수행
if check_password(password):
    print("비밀번호가 유효합니다.")
else:
    print("비밀번호가 유효하지 않습니다.")
