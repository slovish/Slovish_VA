import tkinter as tk

class songs_ui:
    def __init__(self,songs):

        self.root = tk.Tk()
        self.root.title('songs')

        label_frame = tk.Frame(self.root)
        label_frame.pack(expand=True, padx=50, pady=50)

        title_label = tk.Label(label_frame, text="choose from below or say random", font=('Arial', 14))
        title_label.pack(side='top', pady=10)

        labels = []
        for i in range(len(songs)):
            label = tk.Label(label_frame, font=('Arial', 10))
            label.config(text=songs[i].split(".")[0])
            label.pack(side='top', pady=5)
            labels.append(label)

        close_button = tk.Button(self.root, text='Close', command=self.root.destroy)
        close_button.pack(side='bottom', pady=20)

        self.root.mainloop()


def start(songs):
    songs_ui(songs)