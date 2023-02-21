
# code for pico by max knight 

# Display Image & text on I2C driven ssd1306 OLED display
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
# for timer citcuits
import utime

###                                                           Timer function                                                           ###

start_time = 0
def timer(action):
    global start_time # uses a global var

    if action == 1:
        start_time = utime.ticks_ms()
        print('timer started') # innitioates the timer

    elif action == 2:
        if start_time == 0:
            print("Timer has not been started yet")
            return 0
        else:
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)  # Calculate elapsed time
            print("Elapsed time:", elapsed_time, "milliseconds")
            return elapsed_time

    elif action == 3:
        if start_time == 0:
            print("Timer has not been started yet")
            return 0
        else:
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)  # Calculate elapsed time
            start_time = 0  # Reset start time to 0
            print("Timer stopped")
            print("Elapsed time:", elapsed_time, "milieseconds")
            return elapsed_time

###                                                            End of class                                                             ###

###                                                 Class that has the pi display port on it                                            ###
WIDTH  = 128                                            
# oled display width
HEIGHT = 32                                            
# oled display height

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)      
# Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper())
# Display device address
print("I2C Configuration: "+str(i2c))                  
# Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

# Raspberry Pi logo as 32x32 bytearray/ bitvector of ras pi got the bit arrfrom google will use as a buffer icon
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 96, 0)

# Add some text
oled.text("Raspberry Pi",5,5)
oled.text("Pico",5,15)

# Finally update the oled display so the image & text is displayed
oled.show()
###                                                            End of class                                                            ###

###                                                       Switch Class innitioate                                                      ###

mechanisiam1Input = Pin(2, Pin.IN)
if mechanisiam1Input == 1:
    timer(1)
else:
    pass

mechanisiam2Input = Pin(, Pin.IN)
if mechanisiam2Input == 1:
    timer(2)
    time2 = elapsed_time
else:
    pass

mechanisiam3Input = Pin(2, Pin.IN)
if mechanisiam3Input == 1:
    timer(2)
    time3 = elapsed_time
else:
    pass


###                                                            End of class                                                            ###

# code code

# timer(1) # Start the timer
# timer(2) # Get the elapsed time so far
# timer(3) # Stop the timer and get the final elapsed time
