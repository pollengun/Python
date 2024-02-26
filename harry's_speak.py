import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
if __name__== '__main__':
    x = input("Enter your text : ")
    speak.Speak(x)