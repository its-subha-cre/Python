import time
from plyer import notification
import schedule
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def notif():
    notification.notify(
        title="Drinking Water Reminder",
        message='Water is vital to our health. Stay hydrated!',
        timeout=2  # Display the notification for 2 seconds
    )
    speak("please drink water")

# Schedule the notification to run every 30 minutes
schedule.every(4).seconds.do(notif)

# Keep the script running to check for scheduled tasks
while True:
    # speak("please drink water")
    schedule.run_pending()
    time.sleep(1)
 
