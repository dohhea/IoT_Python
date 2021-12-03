# 이 예제는 파이썬 프로그램에서 외부의 명령을 실행하는 방법을 보여줌
# Subprocess 를 만들어 이 프로그램(프로세스)와 별도의 프로그램을 실행하도록 함

import subprocess

proc1=subprocess.run(['ls', '-la'])         # ls -la 명령을 쉘에서 실행 
proc2=subprocess.run(['nano'])              # 편집기 명령을 쉘에서 실행
