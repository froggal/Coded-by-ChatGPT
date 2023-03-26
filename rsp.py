import random

def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if user_choice in ["가위", "바위", "보"]:
            return user_choice
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

def get_computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("사용자: " + user_choice)
    print("컴퓨터: " + computer_choice)
    
    if user_choice == computer_choice:
        print("비겼습니다!")
    elif user_choice == "가위" and computer_choice == "보":
        print("이겼습니다!")
    elif user_choice == "바위" and computer_choice == "가위":
        print("이겼습니다!")
    elif user_choice == "보" and computer_choice == "바위":
        print("이겼습니다!")
    else:
        print("졌습니다!")

while True:
    play_game()
    play_again = input("다시 하시겠습니까? (y/n): ")
    if play_again.lower() != "y":
        break
