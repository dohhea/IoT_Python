# 두개의 스레드가 동시에 더하기를 함
# 경쟁조건 (Race Condition 발생)

import threading

# Thread가 실행할 코드
def sum(n, name):
    global total
    for i in range(1,n+1):
        lock.acquire()                                  # mutex 획득
        total += i
        lock.release()                                  # mutex 반납
    print("Subthread " + name, "= ", total)
    
lock=threading.Lock()                                   # mutex lock 생성
total=0                                                 # 전역변수. 두개의 스레드에서 동시 접근

t1 = threading.Thread(target=sum, args=(100000, "t1"))  # Thread t1 생성
t1.start()                                              # Thread t1 실행

t2 = threading.Thread(target=sum, args=(100000, "t2"))     # Thread t2 생성
t2.start()                                              # Thread t2 실행

t1.join()                                               # main Thread는 t1이 종료할 때 까지 대기
t2.join()                                               # main Thread는 t2이 종료할 때 까지 대기

print("Main Thread total = ", total)

