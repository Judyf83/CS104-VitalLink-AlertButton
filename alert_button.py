import time
import RPi.GPIO as GPIO
import requests
BOT_TOKEN = "8907443032:AAEK7nvDiubAmfveArdRqCFf0Gd4EPjLun4"
CHAT_ID = "8738818316"
url = f"https://api.telegram.org/bot8907443032:AAEK7nvDiubAmfveArdRqCFf0Gd4EPjLun4/sendMessage"
data = {
	"chat_id": CHAT_ID,
	"Text": "Someone pressed the alert button!"
}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
  	try:
	   if response.status_code == 200:
		print("Telegram alert sent successfully!")
           else:
                print(f"Failed to send Telegram alert. Status code: {response.status_code}")
        except Exception as e:
            print(f"Network error occurred: {e}")     

   	button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)
