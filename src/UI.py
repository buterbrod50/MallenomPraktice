from tkinter import *
from tkinter import messagebox, filedialog
from proccesing import get_image_info, get_image_details

def on_close():
    if messagebox.askokcancel("Выйти?"):
        tk.destroy()

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        photo, resized_img, original_size = get_image_info(file_path)
        image_label.config(image=photo)
        image_label.image = photo
        image_label.place(x=320, y=10)
        
        info_text = get_image_details(file_path, resized_img, original_size)
        info_label.config(text=info_text)
        info_label.place(x=10, y=600)

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_close)
tk.title("приложение манипуляции с изображением")
tk.resizable(False, False)
tk.wm_attributes("-alpha", True)

btn_open = Button(tk, text="Выбрать изображение", command=open_image, width=40, height=2)
btn_open.pack(side="top", anchor="nw", padx=10, pady=10)

btn_close = Button(tk, text="Переименовать", command=on_close, width=40, height=2)
btn_close.pack(side="top", anchor="nw", padx=10, pady=10)

canvas = Canvas(tk, width=900, height=600)
canvas.pack(side=LEFT)

image_label = Label(tk)
info_label = Label(tk, justify=LEFT)
info_label.pack(side="bottom", anchor="sw")

tk.mainloop()