import tkinter as tk
from tkinter import ttk

class StdRedirector(object):

    def __init__(self, text_window):
        self.text_window = text_window

    def write(self, output):
        self.text_window.insert(tk.END, output)

class MyFrame(tk.Frame):
    def __init__(self,*args,**kwargs):
        #new Thread to track reminders
        global reminder_thread
        reminder_thread = reminderThread(self)
        tk.Frame.__init__(self,*args,**kwargs)

        self.textBox = tk.Text(root,
            height=1,width=30,
            font=("Times", 16),
            bg="#666", fg="#0f0",
            spacing1=6, spacing3=6,
            insertbackground="#0f0"
            )
        self.textBox.insert("1.0", "$>")
        self.textBox.grid(row=1,column=1, padx=10, pady=10)
        root.bind('<Return>', self.OnEnter)
        root.bind('<Destroy>', self.onClose)
        self.textBox.focus_set()
        self.photo1 = tk.PhotoImage(file="images/mic_icon.png")

        self.btn = ttk.Button(root,command=self.OnClicked,
        image=self.photo1, style="C.TButton")
        self.btn.grid(row=1,column=2, padx=10, pady=20)
        reminder_thread.start()

    def OnEnter(self,event):
            put=self.textBox.get("1.2","end-1c")
            print(put)
            self.textBox.delete('1.2',tk.END)
            if put.startswith(search_pc):
                put = put.strip()
                link = put.split()
            #put = re.sub(r'[?|$|.|!]', r'', put)
            else:
                put = put.lower()
                put = put.strip()
                link = put.split()
            events(self, put, link)
            if put=='':
                self.displayText('Reenter')

    def OnClicked(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak.say('Hey I am Listening ')
            speak.runAndWait()
            audio = r.listen(source)
        try:
            put=r.recognize_google(audio)

            self.displayText(put)
            self.textBox.insert('1.2',put)
            put=put.lower()
            put = put.strip()
            #put = re.sub(r'[?|$|.|!]', r'', put)
            link=put.split()
            events(self,put,link)
        except sr.UnknownValueError:
            self.displayText("Could not understand audio")
        except sr.RequestError as e:
            self.displayText("Could not request results; {0}".format(e))

    def onClose(self, event):
            global reminder_thread
            reminder_thread.event.set()
            #root.destroy()

    def displayText(self, text):
        try :
            if not self.output_window.winfo_viewable() :
                self.output_window.update()
                self.output_window.deiconify()
        except :
            self.createOutputWindow()
        print(text)

    def createOutputWindow(self):
        self.output_window = tk.Toplevel()
        output_text_window = tk.Text(self.output_window)
        self.stddirec = StdRedirector(output_text_window)
        sys.stdout = self.stddirec
        output_text_window.pack()

    #Trigger the GUI. Light the fuse!
if __name__=="__main__":
    root = tk.Tk()
    view = MyFrame(root)
    style = ttk.Style()
    style.configure('C.TButton',
        background='#555',
        highlightthickness='0'
    )
    style.map("C.TButton",
        background=[('pressed', '!disabled', '#333'), ('active', '#666')]
    )
    # root.geometry('{}x{}'.format(400, 100))
    # view.pack(side="top",fill="both",expand=False)
    root.iconphoto(True, tk.PhotoImage(file=os.path.join(sys.path[0],'benji_final.gif')))
    root.title('B.E.N.J.I.')
    root.configure(background="#444")
    root.resizable(0,0)
root.mainloop()