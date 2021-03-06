# 딕셔너리를 사용하여 자료의 추가, 수정, 삭제 등의 기능을 제공하는데
# 각종 exception (예외) 을 처리할 수 있도록 함

dc = {'새우깡' : 700, '콘치즈' : 850, '꼬깔콘': 750}

def main():
    global dc
    while(True):
        try:
            ch=input("추가 i, 수정 m, 삭제 d, 전체보기 l, 종료 q : ")
            if ch not in "imdlq":               # 올바른 입력인지를 확인
                print("잘못된 선택입니다. 다시입력하세요")
                continue

            if ch == 'i':
                entry=input("상품명과 가격입력 : ")
                e1=entry.split(" ")
                if e1[0] in dc:                 # 엔트리 이미 있음
                    print(e1[0] + "는 이미 있습니다. 추가할 수 없습니다.")
                else:
                    dc[e1[0]]=int(e1[1])        # 엔트리 추가
            elif ch== 'm':
                entry=input("상품명과 가격입력 : ")
                e1=entry.split(" ")
                if e1[0] not in dc:             # 엔트리 없음
                    print(e1[0] + "가 없습니다. 수정할 수 없습니다.")
                else:
                    dc[e1[0]]=int(e1[1])        # 엔트리 업데
            elif ch== 'd':
                entry=input("상품명 입력 : ")
                try:
                    del dc[entry]               # 엔트리 삭제
                except :                        # 엔트리가 없는 경우 예외처리
                    print(entry + "가 없습니다. 삭제할 수 없습니다.")
            elif ch== 'l':
                for e in dc:
                    print(e, dc[e])
            else:                               # 입력이 'q'인 경우임
                break
        except KeyboardInterrupt :              # 키보드 예외의 경우
            print("\n인터럽트로 프로그램 종료!!")
            break
        except :                                # 그외 모든 예외에 대해
            print("\n뭔가 잘못된 경우입니다. 다시입력하세요.")


if __name__ == "__main__":                  # 이 모듈을 단독으로 실행한 경우
    main()