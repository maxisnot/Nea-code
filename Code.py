import machine
import utime
import ssd1306

# Set up OLED display
i2c = machine.I2C(0, scl=machine.Pin(14), sda=machine.Pin(15))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# Set up switch pins as inputs with pull-ups
switch1 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
switch2 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
switch3 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)

# Global variables
start_time = 0
timings = []

# Function to handle switch interrupts
def switch_callback(pin):
    global start_time, timings

    if pin == switch1:  # First switch pressed
        if start_time == 0:
            start_time = utime.ticks_ms()
            print("Timer started")
        else:
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            timings.append(elapsed_time)
            start_time = 0
            print("First timing:", elapsed_time)
    elif pin == switch2:  # Second switch pressed
        if start_time == 0:
            print("Timer not started yet")
        else:
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            timings.append(elapsed_time)
            start_time = 0
            print("Second timing:", elapsed_time)
            # Calculate score
            score = -(10000 - sum(timings) * 20)
            # Update OLED display
            oled.fill(0)
            oled.text("Score: {}".format(score), 0, 0)
            oled.show()
    elif pin == switch3:  # Third switch pressed
        if start_time == 0:
            print("Timer not started yet")
        else:
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            timings.append(elapsed_time)
            start_time = 0
            print("Third timing:", elapsed_time)

# Attach switch interrupts to pins
switch1.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=switch_callback)
switch2.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=switch_callback)
switch3.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=switch_callback)

# Main loop
while True:
    pass
