from gpiozero import DistanceSensor
from time import sleep
sesnor = DistanceSensor(11,8)

while True:
    print("Distance: ", sensor.distance, 'm')
    sleep(2)
