import random

# 가위,바위,보 이미지로 표현하기
ascii_art= [
    """
 가위
    ✂️
    """,
    """
     바위
     🪨
    """,
    """
     보
      📄 
    """
]

# 결과 리스트 and 가위바위보 리스트
select = ["가위", "바위", "보"]
win = ["무승부!", "승리!", "패배!"]
# 승패 결정 함수 (있는 경우가 많지 않기 때문에 노가다)
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
    
    try:
        user_choice = int(input("선택을 입력하세요 (숫자 0, 1, 2): "))
        if user_choice not in [0, 1, 2]:
            raise ValueError("잘못된 입력입니다.")
    except ValueError as e:
        print(e)
        return

    # 컴퓨터 선택
    com_choice = random.randint(0, 2)
    result = check_winner(user_choice, com_choice)

    # 결과 출력
    print("\n내 선택:")
    print(ascii_art[user_choice])
    print("컴퓨터 선택:")
    print(ascii_art[com_choice])
    print(f"결과: {win[result]}\n")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("다시 하시겠습니까? (y/n): ").strip().lower()
        if again != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break





