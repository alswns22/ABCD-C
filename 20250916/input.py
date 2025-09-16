# -*- coding: utf-8 -*-

def print_gugudan(num):
    """입력받은 숫자의 구구단을 출력하는 함수"""
    print(f"\n=== {num}단 ===")
    for i in range(1, 10):
        result = num * i
        print(f"{num} × {i} = {result}")

def main():
    """메인 함수"""
    try:
        # 사용자로부터 구구단 수 입력받기
        num = int(input("구구단을 출력할 숫자를 입력하세요 (1~9): "))
        
        # 입력값 유효성 검사
        if 1 <= num <= 9:
            print_gugudan(num)
        else:
            print("1부터 9까지의 숫자만 입력해주세요.")
            
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    main()