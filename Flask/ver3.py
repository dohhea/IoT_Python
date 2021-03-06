# 웹서버 프로그램 웹 브라우저에서 http://localhost:5000/led/on 의 형식으로 접근
# 이렇게 하여 LED 작동시킴

from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 7
GPIO.setmode(GPIO.BOARD)        #BOARD는 커넥터 pin번호 사용
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/led/on")
def led_on():
    GPIO.output(LED, GPIO.HIGH)
    return "LED ON"

@app.route("/led/off")
def led_off():
    GPIO.output(LED, GPIO.LOW)
    return "LED OFF"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP" 

if __name__ == "__main__":
    app.run(host="0.0.0.0")