import RPi.GPIO as GPIO
import dht11
import time
import datetime
fname = "output/{}.csv".format(datetime.datetime.now().strftime("%Y%m%d"));
f=open(fname,"a");


# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)
f.write('time,count,humidity,Temperature\n')
f.close()
try:
    for count in range(10):
        
        result = instance.read()
        if result.is_valid():
            f=open(fname,"a");
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            
            f.write('{},{},{},{}\n'.format(datetime.datetime.now().strftime("%H%M"),(count+1),(result.humidity),(result.temperature)));
           # if count % 30==0:
            f.close()

        time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()