import tkinter as tk
import threading
import main as va
import time
import textwrap
import options as o


class VoiceAssistantUI:
    def __init__(self):
        va.wishme()
        self.root = tk.Tk()
        self.root.title('Voice Assistant UI')
        self.assistant_running = False

        # Set window size and position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width / 2)
        window_height = int(screen_height / 2)
        window_x = int(screen_width / 2 - window_width / 2)
        window_y = int(screen_height / 2 - window_height / 2)
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, window_x, window_y))

        self.root.configure(bg='#ffe5e5')
        
        # Create a frame to hold the button
        frame1 = tk.Frame(self.root, bg ='#ffe5e5')
        frame1.pack(expand=True)

        frame2 = tk.Frame(self.root, bg ='#ffe5e5')
        frame2.pack()

        # Create a round button with text
        self.toggle_button = tk.Button(frame1, text='Start Assistant', command=self.toggle_assistant, width=10, height=2, bd=0, bg='#00FF7F',font=('Arial', 16))
        self.toggle_button.config(borderwidth=3, highlightthickness=10, relief='flat')
        self.toggle_button.pack(side='left', padx=10, pady=2)
        
        self.options_but = tk.Button(frame1, text='Show\nOptions', command=self.show_options, width=7, height=2, bd=0, bg='#e5ffff',font=('Arial', 12))
        self.options_but.pack(side='right',padx=10, pady=2)
        self.gif_label = tk.Label(frame2, text="",bg='#ffe5e5',font=('Arial', 14))

        search_frame = tk.Frame(self.root)
        search_frame.pack(expand=True)

        # Create a search field and a search button
        self.search_field = tk.Entry(search_frame, width=50)
        self.search_field.config(font=('Arial',14))
        self.search_field.pack(side='left', padx=0, pady=2)

        self.search_button = tk.Button(search_frame, text='SEARCH', command=self.t_search, bd=1, bg='gray', activebackground='darkgray', font=('Arial', 14))
        self.search_button.pack(side='left', padx=5, pady=2)
        
        # Create a label to display search results
        self.result_label = tk.Text(self.root, width=80, height=10, bg='#e5ffff')
        self.result_label.config(font=('Arial',12))

        self.root.mainloop()

    def write_speak(self,results):
        self.result_label.delete('1.0', tk.END)
        i = 1
        for item in results:
            self.result_label.insert(f"{i}.0",f"{i}. "+self.wrapper(item)+"\n\n")
            va.speak(item)
            i+=1

    def wrapper(self, results):
        dedented_text = textwrap.dedent(results).strip()
        return textwrap.fill(dedented_text, width=100)


    def t_search(self):
        self.result_label.pack_forget()
        input_text = self.search_field.get()
        results = va.text_search(input_text)
        if results:
            self.result_label.pack()
            self.write_speak(results)
            va.speak("press stop assitant to pause either i will refresh page in 5 seconds")
            time.sleep(5)

        else:
            self.result_label.pack_forget()
        return

    def tog_false(self):
        self.toggle_button.config(text='Stop Assistant',bg='#FF4C4C')
        self.gif_label.pack()
        self.gif_label.config(text=".....Listening.....",bg='#ffe5e5')

    def tog_true(self):
        self.gif_label.pack_forget()
        self.toggle_button.config(text='Start Assistant', bg='#00FF7F')

    def toggle_assistant(self):
        if not self.assistant_running:
            self.assistant_running = True
            self.tog_false()
            self.assistant_thread = threading.Thread(target=self.run_assistant)
            self.assistant_thread.start()
        else:
            self.assistant_running = False
            self.tog_true()

    def run_assistant(self):
        va.start_doing()
        while self.assistant_running:
            if va.keep_doing:
                self.result_label.pack_forget()
                results = va.command_search()
                print(results)
                if results:
                    self.result_label.pack()
                    self.write_speak(results)
                    va.speak("press stop assistant to pause. either i will refresh page in 5 seconds")
                    time.sleep(5)
            else:
                self.assistant_running = False
                self.tog_true()


    def show_options(self):
        o.start()
    

if __name__ == '__main__':
    ui = VoiceAssistantUI()
