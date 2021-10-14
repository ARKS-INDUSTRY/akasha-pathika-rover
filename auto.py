import RPi.GPIO as GPIO
import time

right_forward = 22
right_backward = 27
left_forward = 24
left_backward = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(right_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_backward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_backward, GPIO.OUT, initial=GPIO.LOW)
    
    

def forward():
    initialise()
    print('Forward')
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)

def backward():
    initialise()
    print('Backward')
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)

def right():
    initialise()
    print('Right')
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)

def left():
    initialise()
    print('Left')
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)
    
def stop():
    GPIO.cleanup()
    quit()

def main():
    initialise()
    forward()
    time.sleep(3)
    GPIO.cleanup()

    initialise()
    backward()
    time.sleep(2)
    GPIO.cleanup()

    initialise()
    right()
    time.sleep(3)
    GPIO.cleanup()

    initialise()
    left()
    time.sleep(3)
    GPIO.cleanup()

    initialise()
    stop()
    time.sleep(2)
    GPIO.cleanup()
    
    initialise()
    forward()
    time.sleep(5)
    GPIO.cleanup()

    initialise()
    backward()
    time.sleep(5)
    GPIO.cleanup()
    
    initialise()
    stop()

main()

#arudhran when u r codding compile