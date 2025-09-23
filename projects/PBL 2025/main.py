import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PBL 2025")
app.geometry("400x300")

screen_w = app.winfo_screenwidth()
screen_h = app.winfo_screenheight()

gui = Image.open("assets/images/gui.png")
gui_photo = ctk.CTkImage(dark_image=gui, size=(screen_w, screen_h))
gui_label = ctk.CTkLabel(app, image=gui_photo, text="")
gui_label.place(relx=0, rely=0)

def full_screen(event=None):
    app.attributes("-fullscreen", True)
def exit_fullscreen(event=None):
    app.attributes("-fullscreen", False)

app.bind("<F11>", full_screen)
app.bind("<Escape>", exit_fullscreen)

app.mainloop()
