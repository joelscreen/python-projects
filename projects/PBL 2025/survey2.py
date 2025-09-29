import customtkinter as ctk
from PIL import Image

def survey2(app, main_content_rect, step_value_survey):
    def clearWidgets(exclude=[]):
        for widget in app.winfo_children():
            if widget not in exclude:
                widget.destroy()

    selected_option = ctk.StringVar(value="")
    options = ["Visual: Images, videos, diagrams",
               "Auditory: Listening, music, lectures",
               "Kinesthetic: Hands-on activities, movement, experiments",
               "Reading/Writing: Text, notes, lists"
               ]

    welcome_text = Image.open("assets/images/Welcome_text.png")
    welcome_text = ctk.CTkImage(dark_image=welcome_text, size=(1500, 800))
    welcome_label = ctk.CTkLabel(main_content_rect, image=welcome_text, text="")
    welcome_label.place(relx=0.2, rely=0.01)

    personalize_label = ctk.CTkLabel(main_content_rect, text="Let's personalize your learning experience", font=ctk.CTkFont(size=20, family="Arial"), bg_color="#befff5")
    personalize_label.place(relx=0.3, rely=0.15)

    step = ctk.CTkProgressBar(main_content_rect, width=500, height=10, corner_radius=10)
    step.set(step_value_survey/7)
    step.place(relx=0.25, rely=0.25)

    step_label = ctk.CTkLabel(main_content_rect, text=f"Step {step_value_survey} of 7", font=ctk.CTkFont(size=15, family="Arial"), bg_color="#befff5")
    step_label.place(relx=0.36, rely=0.28)

    survey_canvas_shadow = ctk.CTkCanvas(main_content_rect, width=600, height=610, bg="#727272", highlightthickness=0)
    survey_canvas_shadow.place(relx=0.228, rely=0.355)
    survey_canvas = ctk.CTkCanvas(main_content_rect, width=600, height=610, bg="#ffffff", highlightthickness=0)
    survey_canvas.place(relx=0.23, rely=0.35)

    survey_logo = Image.open("assets/images/Survey_logo.png")
    survey_logo = ctk.CTkImage(dark_image=survey_logo, size=(70, 70))
    survey_logo_label = ctk.CTkLabel(survey_canvas, image=survey_logo, text="", bg_color="#ffffff")
    survey_logo_label.place(relx=0.43, rely=0.03)

    studying_level_label = ctk.CTkLabel(main_content_rect, text="How do you learn best?", font=ctk.CTkFont(size=30, family="Arial"), bg_color="#ffffff")
    studying_level_label.place(relx=0.27, rely=0.45)

    rb1 = ctk.CTkRadioButton(app, text="Visual: Images, videos, diagrams", bg_color="#FFFFFF", variable=selected_option, value="1", font=ctk.CTkFont(size=15, family="Arial"), hover_color="#0059ff", width=500, height=40, corner_radius=10)
    rb1.place(x=850, y=600)

    rb2 = ctk.CTkRadioButton(app, text="Auditory: Listening, music, lectures", bg_color="#FFFFFF", variable=selected_option, value="2", font=ctk.CTkFont(size=15, family="Arial"), hover_color="#0059ff", width=500, height=40, corner_radius=10)
    rb2.place(x=850, y=650)

    rb3 = ctk.CTkRadioButton(app, text="Kinesthetic: Hands-on activities, movement, experiments", bg_color="#FFFFFF", variable=selected_option, value="3", font=ctk.CTkFont(size=15, family="Arial"), hover_color="#0059ff", width=500, height=40, corner_radius=10)
    rb3.place(x=850, y=700)

    rb4 = ctk.CTkRadioButton(app, text="Reading/Writing: Text, notes, lists", bg_color="#FFFFFF", variable=selected_option, value="4", font=ctk.CTkFont(size=15, family="Arial"), hover_color="#0059ff", width=500, height=40, corner_radius=10)
    rb4.place(x=850, y=750)

    def next_step3():
        step_value_survey = 3
        clearWidgets([main_content_rect])
        import survey3
        survey3.survey3(app, main_content_rect, step_value_survey)
    
    survey_submit = ctk.CTkButton(app, text="Next", font=ctk.CTkFont(size=20, family="Arial"), fg_color="#0059ff", hover_color="#0041c4", width=200, height=50, corner_radius=10, command=next_step3)
    survey_submit.place(x=1000, y=800)
