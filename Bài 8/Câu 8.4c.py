print("Le Hoa Hiep")
print("235752021610073")
from tkinter import * 
window = Tk() 
window.title(" Chào mừng bạn đến với app LikeGeeks") 
window.geometry('350x200') 
lbl = Label(window, text="Xin chào") 
lbl.grid(column=0, row=0) 
def clicked(): 
    lbl.configure(text="Nút đã được nhấp !!") 
btn = Button(window, text=" Nhấp vào tôi", command=clicked) 
btn.grid(column=1, row=0) 
window.mainloop()
