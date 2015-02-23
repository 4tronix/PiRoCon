# initio Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# Also demonstrates writing to the LEDs
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


import initio, time

speed = 100

initio.init()

# main loop
try:
    while True:
        initio.forward(speed)
        print 'Forward'
        time.sleep(3)
        initio.reverse(speed)
        print 'Reverse'
        time.sleep(3)
        initio.spinRight(speed)
        print 'Spin Right'
        time.sleep(3)
        initio.spinLeft(speed)
        print 'Spin Left'
        time.sleep(3)
        initio.stop()
        print 'Stop'
        time.sleep(3)

except KeyboardInterrupt:
    initio.cleanup()
    
