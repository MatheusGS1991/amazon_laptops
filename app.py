import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

root = ctk.CTk()
root.configure(bg='white', relief=tk.SUNKEN, bd=9)
root.overrideredirect(True)
root.geometry('525x1019+0+0')

img_logo = tk.PhotoImage(file='data/imagens/logo_extenso_384x216.png')

lb_logo = tk.Label(root, image=img_logo, bd=4, relief=tk.RIDGE)
lb_logo.place(x=34, y=25)












root.mainloop()
