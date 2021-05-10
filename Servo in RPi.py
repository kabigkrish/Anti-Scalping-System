# Importing libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as OUTPUT and set servoMotor as pin 11 as PWM
GPIO.setup(11, GPIO.OUT)
servoMotor = GPIO.PWM(11, 50) # 11 is pin and 50 = 50 Hz pulse

# Start PWM running but with value of 0 (pulse off)
servoMotor.start(0)
print("Waiting for 2 seconds")
time.sleep(2)

# Rotating the servo
print("Rotating 180 degrees in 10 steps")

duty = 2

while duty <= 12:
  servoMotor.ChangeDutyCycle(duty)
  time.sleep(1)
  duty = duty + 1

# Wait for 10 seconds
time.sleep(10)

# Turn back to 90 degrees
print("Turning back to 90 degrees")
servoMotor.ChangeDutyCycle(7)
time.sleep(5)

# Turn back to 0 degrees
print("Turning back to 0 degrees")
servoMotor.ChangeDutyCycle(0)

#Clean things up
servoMotor.stop()
GPIO.cleanup()
