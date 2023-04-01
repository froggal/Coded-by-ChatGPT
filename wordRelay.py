# 끝말잇기 게임 구현하기

print("끝말잇기 게임을 시작합니다!")

# 첫 번째 단어 입력 받기
last_word = input("첫 번째 단어를 입력하세요: ")

# 게임 시작
while True:
    # 다음 단어 입력 받기
    next_word = input("다음 단어를 입력하세요: ")
    
    # 이전 단어의 마지막 글자와 다음 단어의 첫 글자가 같은지 확인하기
    if last_word[-1] == next_word[0]:
        # 맞으면 이전 단어 업데이트하기
        last_word = next_word
    else:
        # 틀리면 게임 종료하기
        print("틀렸습니다! 게임 종료")
        break
