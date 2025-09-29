import customtkinter as ctk
import survey1

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PBL 2025")
app.geometry("400x300")
app.attributes("-fullscreen", True)

screen_w = app.winfo_screenwidth()
screen_h = app.winfo_screenheight()

step_value_survey = 1

app.configure(fg_color="#fafafa")
main_content_rect = ctk.CTkCanvas(app, width=screen_w, height=screen_h, bg="#befff5", highlightthickness=0)
main_content_rect.place(relx=0.2, rely=0)

survey1.survey1(app, main_content_rect, step_value_survey)

def full_screen(event=None):
    app.attributes("-fullscreen", True)
def exit_fullscreen(event=None):
    app.attributes("-fullscreen", False)

app.bind("<F11>", full_screen)
app.bind("<Escape>", exit_fullscreen)

app.mainloop()
