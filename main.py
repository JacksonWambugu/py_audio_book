import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages


numstart=input("enter the number of the page you would like to start   ")
rate=input("enter the rate you would like ")
player = pyttsx3.init()
rate=player.getProperty("rate")
player.setProperty("rate",rate)
volume=input("enter the volume you would like ")
volume=player.getProperty("volume")

voices = player.getProperty("voices")

voise=int(input("enter the voice you would like /n/t/t0.male/n/t/t1.female:: "))

print(voise)
if (voise==0):
    player.setProperty("voice",voices[0].id)
if (voise==1):
    player.setProperty("voice", voices[1].id)

#player.setProperty("voice",voices[1].id)
for num in range(int(numstart),pages):
        page=pdfreader.getPage(num)
        text = page.extractText()
        player.say(text)
        player.runAndWait()



