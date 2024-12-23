from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root = Tk()
root.geometry('980x500')
root.resizable(0,0)
root.title("Your Translator")
root.config(bg = 'sky blue')

#YOUR TRANSLATOR
Label(root, text = "YOUR TRANSLATOR", font = "arial 20 bold", fg='black', bg='sky blue').pack()


#INPUT AND OUTPUT TEXT
Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 14', height = 11, fg= 'white', bg='black', wrap = WORD, padx=5, pady=5, width = 30)
Input_text.place(x=50,y = 100)

#BOX SIZE
#Label(root,text ="", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Output_text = Text(root,font = 'arial 14', height = 11, fg= 'white', bg='black', wrap = WORD, padx=3, pady=3, width = 30)
Output_text.place(x = 600 , y = 100)
 

language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=810,y=60)
dest_lang.set('choose output language')

#TranslateButton
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = 'english', dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   

#Translate Button
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate ,fg='white', bg = 'black', activebackground = 'white')
trans_btn.place(x = 455, y = 180)


root.mainloop()
