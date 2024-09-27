import smbus
import threading
import RPi.GPIO as GPIO

NUMBER_OF_LEDS = 30
NUMBER_OF_RGB_LEDS = 10

RED_OFFSET = 0
GREEN_OFFSET = 1
BLUE_OFFSET = 2

#I2C ID where the LED Driver is on
I2C_ID = 10

#Address for the LS31FL3236A
LED_ADDRESS = 0x3c
LED_DRIVER_SHUTDOWN_REG = 0x00
LED_DRIVER_PWM_PORT_OFFSET = 0x01
LED_DRIVER_PWM_UPDATE_REG = 0x25
LED_DRIVER_LED_CONTROL_REG = 0x26 

LED_ON = 0x01
LED_OFF = 0x00

LED_SL_HALF_CURRENT = 0x02

#The LED map
led_map = [0x00] * NUMBER_OF_RGB_LEDS

#For each LED, set OUT to 1 and set SL to Imax/2
led_ctrl = [LED_ON | LED_SL_HALF_CURRENT] * NUMBER_OF_RGB_LEDS

CONNECT_TO_PC_LED = 0
MULTI_LED = 5
TRIG_BUTTON = 5
MULTI_BUTTON = 4

toggle_update = False

multiState = 0
Status_Page = 0
Waiting_For_Update = 0
Color_Wheel = 0
update_rate = 0.1

def UpdateMultiLED():
	global led_map, toggle_update
	if toggle_update == True:
		SetMembraneRGBLED(MULTI_LED, 200, 200, 200)
	else:
		SetMembraneRGBLEDOff(MULTI_LED)
	return

def UpdateConnectionLED():
	global led_map, toggle_update
	if toggle_update == True:
		SetMembraneRGBLED(CONNECT_TO_PC_LED, 200, 200, 200)
	else:
		SetMembraneRGBLEDOff(CONNECT_TO_PC_LED)
	return

def StartLEDUpdaterThread():
	global led_map, toggle_update, Waiting_For_Update, update_rate
	threading.Timer(update_rate, StartLEDUpdaterThread).start()
	if multiState == Status_Page: 
		UpdateConnectionLED()
		UpdateMultiLED()
	toggle_update = not toggle_update
	Waiting_For_Update = 0
	i2c.write_i2c_block_data(LED_ADDRESS, LED_DRIVER_PWM_PORT_OFFSET, led_map)
	i2c.write_byte_data(LED_ADDRESS, LED_DRIVER_PWM_UPDATE_REG, 0x00)


def SetMembraneRGBLEDOff(ledNumber):
	global led_map
	SetMembraneRGBLED(ledNumber, 0, 0, 0)


def SetAllRGBLEDs(red, green, blue):
	for ledIndex in range(0, 10):
		SetMembraneRGBLED(ledIndex, red, green, blue)

def SetMembraneRGBLED(ledNumber, red, green, blue):
	global led_map
	led_map[3 * ledNumber + RED_OFFSET] = red
	led_map[3 * ledNumber + GREEN_OFFSET] = green
	led_map[3 * ledNumber + BLUE_OFFSET] = blue
	return

def IncrementMultiState(channel):
	global multiState, update_rate
	SetAllRGBLEDs(0,0,0)	
	if multiState > 0:
		multiState = 0
		update_rate = 0.1
	else:
		multiState = multiState + 1
		update_rate = 0.05
	return

if __name__ == '__main__':
	#Set up GPIO triggering
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(MULTI_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(TRIG_BUTTON, GPIO.IN,  pull_up_down=GPIO.PUD_UP)

	#Add event to swtich to Color Wheel
	GPIO.add_event_detect(MULTI_BUTTON, GPIO.RISING, callback=IncrementMultiState, bouncetime=100)

	#Since the LED driver is on i2c 1
	i2c = smbus.SMBus(I2C_ID)
 
	#Take the LED driver out of shutdown
	i2c.write_byte_data(LED_ADDRESS, LED_DRIVER_SHUTDOWN_REG, 0x01)

	#Write to the LED control registers for each LED
	i2c.write_i2c_block_data(LED_ADDRESS, LED_DRIVER_LED_CONTROL_REG, led_ctrl)

	#Tell LED Driver to update its PWM for each LED
	i2c.write_byte_data(LED_ADDRESS, LED_DRIVER_PWM_UPDATE_REG, 0x00)

	#Start Update thread for LEDs
	StartLEDUpdaterThread()

	while(1):
		if multiState == 1 and not Waiting_For_Update:
			if Color_Wheel == 0:
				SetAllRGBLEDs(255, 0, 0)
			elif Color_Wheel == 1:
				SetAllRGBLEDs(0,0,0)
			elif Color_Wheel == 2:
				SetAllRGBLEDs(0, 255, 0)
			elif Color_Wheel == 3:
				SetAllRGBLEDs(0, 0, 0)
			elif Color_Wheel == 4:
				SetAllRGBLEDs(0, 0, 255)
			elif Color_Wheel == 5:
				SetAllRGBLEDs(0,0,0)

			if Color_Wheel < 5:
				Color_Wheel = Color_Wheel + 1
			else:
				Color_Wheel = 0

			Waiting_For_Update = 1

		elif multiState == 2:
			SetMembraneRGBLED(0, 150, 0, 60)
