print("Le Hoa Hiep")
print("235752021610073")
import tkinter as tk

window = tk.Tk()
window.title("Cửa sổ Tkinter Đơn Giản")
window.geometry("300x200")

label = tk.Label(window, text="Xin chào Tkinter!")
label.pack(pady=20)

button = tk.Button(window, text="Mở", command=lambda: label.config(text="Đã mở!"))
button.pack(pady=10)

button = tk.Button(window, text="Đóng", command=lambda: label.config(text="Đã đóng!"))
button.pack(pady=10)
 

window.mainloop()

