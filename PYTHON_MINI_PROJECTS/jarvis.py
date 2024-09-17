import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import json
from pyChatGPT import ChatGPT
import subprocess
import json
import difflib as d


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def default():
        
       
            print("listening......")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                # speak("Listening, sir.")
                print("Listening....")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                try:
                
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    print("Recognizing.....")
                    val = r.recognize_google(audio, language="en-in")
                    # print(f"User said: {query}")

                except sr.WaitTimeoutError:
                    
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                    # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")
                    
                except sr.UnknownValueError:
                    
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")
                except sr.RequestError as e:
                    
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                    
                    
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")
        
        
            return val


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening, Subhayan.")
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
        except sr.WaitTimeoutError:
            speak("I didn't catch that. Please try again.")
            return "none"
        except sr.UnknownValueError:
            speak("I didn't understand that. Please try again.")
            return "none"
        except sr.RequestError as e:
            speak("Could not request results; check your network connection.")
            print(f"Could not request results; {e}")
            return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak('''hey subhayan,
          I am Adrika, please tell me how can I help you''')

if __name__ == "__main__":
  
    e=default().lower()

    if e=="wake up":
          wish()
          while True:

            
        
            query = take_command().lower()
            if "google" in query:
                os.system("start https://www.google.com")
            elif "calculator" in query:
                speak("Opening Calculator")
                os.system("calc")
            elif "command prompt" in query or "cmd" in query:
                speak("Opening Command Prompt")
                os.system("start cmd")
            elif "notepad" in query:
                speak("opening notepad")
                os.system("notepad")
            elif "powerpoint" in query:
                speak("opening powerpoint")
                os.startfile("powerpnt")

            elif "love" in query:
                speak('''i love you too my baby.You are my life sona''')
            elif "code" in query:
                speak("opening vscode")
                os.startfile("C:\\Users\\subha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif "open camera" in query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img =cap.read()
                    cv2.imshow("webcam",img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif "ip address" in query:
                ip=requests.get("https://api.ipify.org").text
                speak(f"your id address is {ip}")
                print(f"your id adddress is {ip}")
            elif "wikipedia" in query:
                speak("searching wikipedia")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
                
            elif"open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif"open stackoverflow" in query:
                webbrowser.open("www.stackoverflow.com")
            elif"open facebook" in query:
                webbrowser.open("www.facebook.com")
            elif "search" in query:
                cm=take_command().lower()
                webbrowser.open(f"{cm}")
            elif"send message" in query:
                
                speak("What is the message?")
                cm = take_command().lower()
                try:
                        
                        kit.sendwhatmsg_instantly("+9477033200", cm)
                        speak("Message has been sent")
                except Exception as e:
                    speak("An error occurred while sending the message")
                    cm=take_command().lower()
                    kit.sendwhatmsg_instantly("9477033200",cm)
            elif"music" in query:
                speak("what music would you like to hear")
                cm=take_command().lower()
                kit.playonyt(cm)
                speak("enjoy your music sir")
                break
            elif"play video on youtube" in query:
                speak("what video would you like to see sir")
                cm=take_command().lower()
                kit.playonyt(cm)
                speak("enjoy your video sir")
                break
            elif"news" in query:
                
                speak("which news do you want to see")
                cm=take_command().lower()
                r=requests.get(f"https://newsapi.org/v2/everything?q={cm}&from={datetime.date.today()}&sortBy=publishedAt&apiKey=e733a5ee87f74b24916cd362109f2739")
                j=json.loads(r.text)
                k=0
                for i in j["articles"]:
                    speak(i["title"])
                    speak(i["description"])
                    print(i["title"])
                    print(i["description"])
                    print("------------------------------------------------------------------------------")
                    k=k+1
                    if(k==5):
                        speak(f"thats all about {cm}")
                        break
            elif "help" in query:
                speak("at your service subhayan")
                session_token='''eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Eweo-wBL5UzwGZB3.1iaokS0qz3uMSRnhhApuPd89mFg315iQJbo1UZsEwXMYVbYUXup-r-mz0aVBW2kB8D0t2K4ppFYJGZ7bMP61QQxVe1X2cIxWPOuHPXLwWbliaQnGYDK_W1G9Ijpeqt02YeiFlxxM31FfdhsTl5bTF5QMSRCyTNtRnTTsGVla6989F9KIKpy1qUTZ9V5EKQzLVcQ8ThtRBZ0xf3LYwIHnqbb5qmF9d-kRxkf11IIIfv5BDG7QeuWnBSAA4CdL89t0NOLuEMjWSGcegyeDW1Nrj12eBVFTZAZk-pg9argg49FhH_Sgzjag4TeaURFxlLbS1CVrp_FxZuuoysKwu1t8WqjbxuVsoozGxOK6LFyMyDCVUT_uRAeChYR8ctwXTBwN0zcTVAndmp2IXUF7psL47BBAqZpHClQ31Nmm71_ArX34Lg2VnoN1J9TlupI20421JwDGgleKLY3K5uMO5mH7tIz9T5DvPFFBKCd6oZfnkiaAPME7LdQial1o6-Xy6vbpg6NOXUt-E0ID4CwADxE9CgEjxZG90iiN2RwfJP1R4ju_aodXamqQ4s5uAZJNGl90RzmtMowOBnjYcHphZ5S90gSmq6KrukK_qEfJd6jWhGcQPd9Eav0TH5EKcWjSf28W1iryG_8wCEM6qoDBoEcHBDcyFKOisEsfQrn-XheV6s9MVNMjCuG1HW8CpryIPGHBbk7iyroVjxQG3Rq5gzC7IkLZdaH5kPgS_QRiYiygS2AFiUZ7qHwOiJ5am21FqKVEBd8qZsHeQVQUVRiOjVe3lZ_V5-rCahEep-rilimoYbL88HFvG28IqTgZNelJdLVr50pJMa9az0IEB2CU47uL9BHdDhslUmwRpAw3gvbsWPAcW8rkZSvrxhcVOVtlP0U8zcU-C8io1ww3sr5ap2k8If4TADd4MZT7aRu-Z8ti5j9dHfr3Bo0bcrG6_URAMuhCwLPJrRUx1RXBjAv20mSK-WNGd5_OZIJGkjCcHYx0XMLv7e_djSKXXs37S8hIGx-fh75PyRkMkwW9mA6GdwHl21yvD0nTPkhwbbrEmtV-kTKWq_5Z9M2p7mPyFAXU-poCmAvySFSF4ZoSpWhonXGoFR_Jh3UbB5iWGxr72IqCp9s5NnKEq2BofLCD7lp_C3ss25VRFtTa-l1RXrE8Id0-PEwSCDYoO0iOR3tRpkitIXUTJdj7DeOhbEkDIDVInqf9S7PhTO9cwlhSlCxoy_0Wj24PBnvKkYi1E5PCVAcj6FEA1qGzTPgBR88RohoQ2jeRzGoCpSreaQxEsn7vVtyrS-EmVnGUl7A_6502MLdGF5y0x5yqUjGS3bxsZoLh9bEKAmv2MLwH8f0B7BW1dPWM4X7MMZYVyTEVn8mLGEBXuJjZNJ_Ngff2xsnpddPWBGkPGvI54ksJMexE34QrvvlBP42urdILMKzUV3p4t0sT137EhT86hYmOrcVbjBEBg5kfcbkXyevJwZuoE58f5Ny8IvVxOQMLm0ZA_DUKtF-JCCtUrqL-fsYCZcwqi0KDiQVo4T4xHjAdqpMK5_hEHc5AvyPTgiCPSwYrInTn6PiiZ3NlMB4vmrSi7_VjUs1zlp83IHwuNwdHoNMi6btnXGGC3rQzqoQrcRve2hoc1Qr72ix60tFxqHS4346kKwDe4XWrb_eb0YsO7B3NxAnpnY_DvoPpIBn1PlH4RE_Gq5OFsaxEthBn2piu7_CZC3LEf6XfuNXOvxkI6jnDm3wagjsc8feq8HnKJ32YO49dm3qqX3r2EJZ3uWM4zRaMoxxh5Ffg4ML_MQCcRj27Nq5_NGzBpAeZnn4W1XXmfMANwZ4VxURu8NoEEEdy0KXrTbxgjgo-fyMf8AHWrw5VuPecKzwUNl3vyhEW5E5lQZWEz0SMSGEcgIQfK4PZJQHPLuLOcEoJ3376uIcSHFMRD6Nti5_dZd9iSqWkctn1RU7W2fU5Tf7DXJdKahTItlwxD6izx5BZzBzzxGLE4N24XPGTxG25-cSw5xeOj-xVPaOEkQgpMSyscnPJcl0mIVk38IoRlYK7mTTJAShFu4aIvW9SHTQM14DYPbLCdJj2Vnuu9oDKoPsWEw6R6gql18KQoKm-_PtNcQBOtvtla7p-xvpQqgJWIgh1fTq2N9s0BqzVzTEF5vCSnY6GX6ywTHCDa5-B2MVJ_zAl18FerqXqr_rSr0UvgdHiFcVN6RITNQnq18UKPCy3eayMbJrGiW4y1URiqAM5dxAMdfe5hz-ci_qtqwzPTceX-r7Ypcgbbq8egzLkYr-fmgGQvKUpuk5aLtIeF87i_CgCbQ9-x9pMA3ZVx_HZMFoL65kfP8zx83vZY1m_3E7m8fSZhrjJ0ze81EOkBPpiR2fT4L30idw_jVjDYDWuzwDE-lGV6lJkE2Cm2MGzLIC03qMMQPD2grzL8k5wjqm2O-f_4irHPH6oNTP9y-vW9kItFvMMQP9Tu3sPY-fQFuMlLOlalP1TwjiXAikMXsMXcOA7gvNpSXZpRc5En6MPHY89gK1nwtQF78J5L0wHL8NzcNpeK2-s2CzOtqVB_5yP_kSCtxfeijIet79fmzmthHB9W0z5KMogoB3_8zKcdyqEE5lP7TbTSJ_C4R6s7kdfeelr-ErFM39ITnbc9jVxeYmGVqwI8JKYErJkRzx8ozaoVcxPEQlDRCJoNuoz1IfsHfCfXFQ0NYb2c8oSiTTd4isEXbEG3niU82qaQiFr88dJx7l9EecL7smwVc-UuRHWqG23Db-py_c7pwjipVmkViWNKZECIJclCUGgZVnEVqKy6crENkPCSPRtGJcOkQWqtB7eZNgCmFCLysWWGynM2TM2qMW8f8kkPvYukEyj7ZlNbc3lAUbYHefP275_FhXUFwkkqQUYjg9FzEaThFlMhzOkVTpPF1saqhKbXCby3bDJCioAjjL8972DUM_prZUmqe5tVyAnb8Wk69rKV4i-pT78ENeamTNPrqH-Rqe_THAWc-0ihJlruMI3Ho0QlHpU7CHpmjRCMHrOTg.-MBSspJkb2XQxOR59tn8_w'''
                api=ChatGPT(session_token)
                cm=take_command().lower()
                res=api.send_message(cm)
                speak(res["message"])
                print(res["message"])



            elif "cpp" in query:
                speak("opening devc++")
                os.startfile("C:\\Program Files (x86)\\Embarcadero\\Dev-Cpp\\devcpp.exe")
                speak("enjoy your code sir")
                break

            elif "translate" in query:
                
            #  word=takecommand().lower()
            #  translate(word)


                
                speak("tell the word you want to search: ")
                word=take_command().lower()
                
                j=json.load(open("data.json"))
                def translate(w):
                    if w in j.keys():
                        print(j[w])
                    elif d.get_close_matches(w,j.keys()):
                        print(f"did you mean this {d.get_close_matches(w,j.keys())[0]}")
                        speak(f"did you mean this {d.get_close_matches(w,j.keys())[0]}")
                        print(f"then the word meaning is {j[d.get_close_matches(w,j.keys())[0]]}")
                        speak(f"then the word meaning is {j[d.get_close_matches(w,j.keys())[0]]}")

                    else:
                        print("the word is not found")
                        speak("the word is not found")
                
                translate(word)

    # print(translate('ca'))
                    






            



            
            elif "exit" in query or "stop" in query:
                speak('''Goodbye, sir
                    Please come again''')
                break
        # Add more commands here
