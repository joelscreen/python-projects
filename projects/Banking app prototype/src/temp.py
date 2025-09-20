import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("My Application")
app.geometry("400x300")

username = ""
password = ""

def enableFullscreen(event=None):
    app.attributes("-fullscreen", True)

def disableFullscreen(event=None):
    app.attributes("-fullscreen", False)

enableFullscreen()

def mainPage():
    for widget in app.winfo_children():
        widget.destroy()
    ctk.CTkLabel(app, text="Welcome to the TKinter Banking App", font=("Arial", 24), bg="#ffffff").place(x=700, y=100)
    ctk.CTkButton(app, text="Login", font=("Arial", 14), command=login, bg="#0042A5", fg="#FFFFFF").place(x=1800, y=100)

def createAccount():
    for widget in app.winfo_children():
        widget.destroy()

    login_signup = Image.open("assets/login_signup_bg.png")
    login_signup = login_signup.resize((1000, 1600))
    login_signup_photo = ImageTk.PhotoImage(login_signup)
    label = ctk.CTkLabel(app, image=login_signup_photo, text="")
    label.place(x=1600, y=0)

    ctk.CTkLabel(app, text="Username:", font=("Arial", 14), bg_color="transparent").place(x=680, y=479)
    ctk.CTkLabel(app, text="Password:", font=("Arial", 14), bg_color="transparent").place(x=680, y=514)
    ctk.CTkLabel(app, text="Confirm Password:", font=("Arial", 14), bg_color="transparent").place(x=630, y=544)

    usernameregister = ctk.CTkEntry(app, font=("Arial", 14))
    usernameregister.place(x=800, y=480)

    passwordregister = ctk.CTkEntry(app, font=("Arial", 14), show="*")
    passwordregister.place(x=800, y=512)

    confpasswordregister = ctk.CTkEntry(app, font=("Arial", 14), show="*")
    confpasswordregister.place(x=800, y=544)

    def requirements():
        global message_label, username, password

        message_label = None

        if message_label is not None:
            message_label.destroy()

        reg_u = usernameregister.get()
        reg_p = passwordregister.get()
        conf_reg_p = confpasswordregister.get()

        if reg_u == "" or reg_p == "" or conf_reg_p == "":
            text = "⚠️ Please fill in all details"
        elif reg_p != conf_reg_p:
            text = "⚠️ Passwords do not match"
        elif len(reg_p) < 8:
            text = "⚠️ Password must be at least 8 characters long"
        elif len(reg_u) < 5:
            text = "⚠️ Username must be at least 5 characters long"
        else:
            username = reg_u
            password = reg_p
            text = "✓ Account Created Successfully! Redirecting to Main Page..."

        if text != "✓ Account Created Successfully! Redirecting to Main Page...":
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), bg="#ff0000", fg="#FFFFFF")
            message_label.place(x=608, y=800)
        else:
            message_label = ctk.CtkLabel(app, text=text, font=("Arial", 14), bg="#00ff00", fg="#000000")
            message_label.place(x=608, y=800)
            app.after(2000, mainPage)

    register_button = ctk.CTkButton(app, text="Register", font=("Arial", 14), command=requirements)
    register_button.place(x=800, y=580)


def login():
    for widget in app.winfo_children():
        widget.destroy()
        
    ctk.CTkLabel(app, text="Username:", font=("Arial", 14), bg="#ffffff").place(x=680, y=467)
    ctk.CTkLabel(app, text="Password:", font=("Arial", 14), bg="#ffffff").place(x=680, y=512)

    usernameregister = ctk.CTkEntry(app, font=("Arial", 14))
    usernameregister.place(x=911, y=480, anchor=ctk.CENTER)

    passwordregister = ctk.CTkEntry(app, font=("Arial", 14), show="*")
    passwordregister.place(x=800, y=512)

    def logineErrors():
        global message_label

        message_label = None

        if message_label is not None:
            message_label.destroy()

        log_u = usernameregister.get()
        log_p = passwordregister.get()

        if log_u == "" or log_p == "":
            text = "⚠️ Please enter in all the details!!"
        elif log_u != username or log_p != password:
            text = "⚠️ Invalid username or password!! Please try again."
        else:
            text = "✓ Logged in Successfully! Redirecting to the main page..."

        if text != "✓ Logged in Successfully! Redirecting to the main page...":
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), bg="#ff0000", fg="#FFFFFF")
            message_label.place(x=608, y=800)
        else:
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), bg="#00ff00", fg="#000000")
            message_label.place(x=608, y=800)
            app.after(2000, mainPage)

    register_button = ctk.CTkButton(app, text="Login", font=("Arial", 14), command=logineErrors)
    register_button.place(x=800, y=580)

createAccount()

app.bind("<Escape>", disableFullscreen)
app.bind("<F11>", enableFullscreen)

app.mainloop()
