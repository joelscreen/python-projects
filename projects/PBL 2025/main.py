import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PBL 2025")
app.geometry("400x300")

gui = Image.open("assets/images/gui.png")
gui = gui.resize((app.winfo_screenmmwidth(), app.winfo_screenmmheight()))
gui_photo = ctk.CTkImage(gui)
gui_label = ctk.CTkLabel(app, image=gui_photo, text="")
gui_label.place(relx=0, rely=0)

app.mainloop()
