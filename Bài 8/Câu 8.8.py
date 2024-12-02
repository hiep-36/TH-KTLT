print("Le Hoa Hiep")
print("235752021610073")
import tkinter as tk
from tkinter import messagebox

def show_personal_info():
    name = entry_name.get()
    dob = entry_dob.get()
    mssv = entry_mssv.get()
    major = entry_major.get()
    
    messagebox.showinfo("Thông tin cá nhân", f"Họ tên: {name}\nNgày sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")

def show_radio_choice():
    choice = var.get()
    messagebox.showinfo("Thông tin lựa chọn", f"Bạn đã chọn số: {choice}")

root = tk.Tk()
root.title("Thông tin cá nhân & Radio Button")

frame_info = tk.LabelFrame(root, text="Thông tin cá nhân", padx=10, pady=10)
frame_info.grid(row=0, column=0, padx=20, pady=20)

tk.Label(frame_info, text="Họ tên:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame_info)
entry_name.grid(row=0, column=1)

tk.Label(frame_info, text="Ngày sinh (dd/mm/yyyy):").grid(row=1, column=0, sticky="e")
entry_dob = tk.Entry(frame_info)
entry_dob.grid(row=1, column=1)

tk.Label(frame_info, text="MSSV:").grid(row=2, column=0, sticky="e")
entry_mssv = tk.Entry(frame_info)
entry_mssv.grid(row=2, column=1)

tk.Label(frame_info, text="Ngành học:").grid(row=3, column=0, sticky="e")
entry_major = tk.Entry(frame_info)
entry_major.grid(row=3, column=1)

btn_show_info = tk.Button(frame_info, text="Hiển thị thông tin", command=show_personal_info)
btn_show_info.grid(row=4, columnspan=2, pady=10)

frame_radio = tk.LabelFrame(root, text="Lựa chọn", padx=10, pady=10)
frame_radio.grid(row=1, column=0, padx=20, pady=20)

var = tk.IntVar()

tk.Radiobutton(frame_radio, text="First", variable=var, value=1).grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame_radio, text="Second", variable=var, value=2).grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame_radio, text="Third", variable=var, value=3).grid(row=0, column=2, sticky="w")

btn_show_choice = tk.Button(frame_radio, text="Click Me", command=show_radio_choice)
btn_show_choice.grid(row=1, columnspan=10, pady=10)

root.mainloop()
