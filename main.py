# import the modules 
from tkinter import *
import speech_recognition as sr    
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import os
from gtts import gTTS

Window= Tk()
#add title
Window.title("Language Processor-2")
#add dimensions 
# Window.geometry("800x400")

font_tup = ("Comic Sans MS", 15)

#heading 
heading1 = Label(Window, text = "Voice Notepad",font = "bold, 30 ")
heading1.grid(row=0,column=1,padx=20,pady=20)
#Text label
Output_text = Text(Window, height= 4, width = 40,  font= font_tup)
Output_text.grid(row=1,column=1,pady = 20,padx=20)

#function     
def To_Text():
  # code for voice to text converstion
  r = sr.Recognizer()
  with sr.Microphone() as source:
      a = "Speak anything.."
      Output_text.insert(END, a)
      Output_text.delete(1.0, END)
      audio = r.listen(source)
      try:
        text = r.recongnize_google(audio, language =  'eng-in')
      except:
          text = "Sorry! Your Voice was not recongnized"
      Output_text.delete(1.0, END)
      Output_text.insert(END, text)
def save():
    #Code for save the text
    fout = asksaveasfile(defaultextension = ".txt")
    if fout:
        print(Output_text.get(1.0, END), file = fout)
    else:
        messagebox.showinfo("Warning", "TEXT NOT SAVED")
        

  

# our convert to text function using command = To_Text 
startVoive_btn = Button(Window, text = 'Speech-to-text',
                   font = 'bold, 15', command = To_Text,width=20)
startVoive_btn.grid(row=1,column=0,pady = 20,padx=20)

# our SAVE function using command =save
save_button = Button(Window, text='Save the Text',font = 'bold, 15',width=20,command=save)
save_button.grid(row = 1, column = 2,pady = 10,columnspan=3)






### Text-to-speech
entry = Entry(Window, width = 40, font=font_tup) 
entry.grid(row=2,column=1,pady = 20,padx=20)


def play():
    language = 'en'
    myobj = gTTS(text = entry.get(), lang = language, slow = False)
    myobj.save("convert.wav")
    os.system("convert.wav")
    entry.delete(0, END)

btn_txt_sc= Button(Window, text = "Text-to-speech",font = 'bold, 15',width=20, command=play)
btn_txt_sc.grid(row=2,column=0,padx=10)



# start the gui 
Window.mainloop() 
