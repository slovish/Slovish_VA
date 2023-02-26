import tkinter as tk

class optionsUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('options')
        self.root.geometry("650x450")
        self.root.configure(bg='#ffe5e5')

        title_label = tk.Label(self.root, text="Try saying this", font=('Arial', 14))
        title_label.pack(side='top', pady=10)
        label_frame1 = tk.Frame(self.root, bg = "#ffe5e5")
        label_frame1.pack(expand=True, padx=10, pady=10, side="left")
        label_frame2 = tk.Frame(self.root, bg = "#ffe5e5")
        label_frame2.pack(expand=True, padx=10, pady=10, side="right")


        labels = []

        for i in range(12):
            label = tk.Label(label_frame1, font=('Arial', 10), bg="#ffe5e5")
            label.pack(side='top', pady=2)
            labels.append(label)
        for i in range(12):
            label = tk.Label(label_frame2, font=('Arial', 10), bg='#ffe5e5')
            label.pack(side='top', pady=2)
            labels.append(label)

        labels[0].config(text="Who are you?")
        labels[1].config(text="Who created you?")
        labels[2].config(text="How are you?")
        labels[3].config(text="Why you were created?")
        labels[4].config(text="What is your name?")
        labels[5].config(text="Google search <text>")
        labels[6].config(text="Open Youtube <text>")
        labels[7].config(text="Open VScode")
        labels[8].config(text="Wikepedia/ Wikipedia <text>")
        labels[9].config(text="What is current  date / time?")
        labels[10].config(text="Open Leetcode/ codechef/ github")
        labels[11].config(text="Open my portfolio")
        labels[12].config(text="Play music")
        labels[13].config(text="Open google")
        labels[14].config(text="Tell me a joke")
        labels[15].config(text="Calculate <expression>")
        labels[16].config(text="Search <text>")
        labels[17].config(text="Tell me some news")
        labels[18].config(text="Restart/ shutdown/ sleep/ lock screen/ log off")
        labels[19].config(text="Where is <some place>")
        labels[20].config(text="What is weather")
        labels[21].config(text="What is <something>")
        labels[22].config(text="Who is <someone>")
        labels[23].config(text="Stop/ mute/ don't listen / stop listening")

        close_button = tk.Button(self.root, text='Close', command=self.root.destroy, bg='red')
        close_button.pack(pady=20, side="bottom")
        
        self.root.mainloop()

def start():
    optionsUI()