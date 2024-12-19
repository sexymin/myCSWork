import random

# 가위,바위,보 이미지 리스트
ascii_art= [
    """가위 ✂️""", """바위 🪨""", """보📄 """
]

# 결과 리스트 and 가위바위보 리스트
select = ["가위", "바위", "보"]
win = ["무승부!", "승리!", "패배!"]
# 승패 결정 함수 
def check_winner(_user, _com):
    if _user == _com:
        return 0  # 무승부
    elif (_user == 0 and _com == 2) or (_user == 1 and _com == 0) or (_user == 2 and _com == 1):
        return 1  # 승리
    else:
        return 2  # 패배
#게임 실행 함수
def play_game():
    print("가위바위보 게임에 오신 것을 환영합니다!")
    print("0: 가위, 1: 바위, 2: 보")
# 0,1,2 선택지 0,1,2 외 다른걸 입력하면 ValueError 리턴    
    try:
        user_choice = int(input("선택을 입력하세요 (숫자 0, 1, 2): "))
        if user_choice not in [0, 1, 2]:
            raise ValueError("잘못된 입력입니다.")
    except ValueError as e:
        print(e)
        return

    # 컴퓨터 선택
    com_choice = random.randint(0, 2) #0부터 1까지
    result = check_winner(user_choice, com_choice) #승패 결정함수에서 내 선택과 컴퓨터 선택까지 비교

    # 결과 출력
    print("\n내 선택:")
    print(ascii_art[user_choice]) #내 선택과 이미지 맞춰서 출력
    print("컴퓨터 선택:")
    print(ascii_art[com_choice]) #컴퓨터 선택과 이미지 맞춰서 출력
    print(f"결과: {win[result]}\n")
# 게임 다시시작 함수 (if __name__ == "__main__": 함수는 직접 실행할 때만 코드를 실행하도록 보장)
if __name__ == "__main__":
    while True:
        play_game()
        again = input("다시 하시겠습니까? (y/n): ").strip().lower()
        if again != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break






