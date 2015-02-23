import time
import initio

initio.init()

try:
    while True:
        dist = initio.getDistance()
        print "Distance: ", int(dist)
        time.sleep(1)

except KeyboardInterrupt:
    print
    pass

finally:
    initio.cleanup()
