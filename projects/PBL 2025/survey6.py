import customtkinter as ctk
from PIL import Image

def survey6(app, main_content_rect, step_value_survey):
    def clearWidgets(exclude=[]):
        for widget in app.winfo_children():
            if widget not in exclude:
                widget.destroy()
    
    def update_label(value):
        motivation_label.configure(text=int(float(value)))

    selected_option = ctk.IntVar(value=5)
    options = ["15 minutes: Quick daily sessions",
               "30 minutes: Focused learning",
               "1 hour: Deep practice",
               "2+ hours: Extensive study"
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

    studying_level_label = ctk.CTkLabel(main_content_rect, text="Motivation level", font=ctk.CTkFont(size=30, family="Arial"), bg_color="#ffffff")
    studying_level_label.place(relx=0.24, rely=0.45)

    motivation_label = ctk.CTkLabel(app, text=selected_option.get(), font=ctk.CTkFont(size=40, family="Arial Bold"), text_color="#0077FF", bg_color="#FFFFFF")
    motivation_label.place(x=1100, y=550)

    ctk.CTkLabel(app, text="Not motivated", font=ctk.CTkFont(size=15, family="Arial"), bg_color="#FFFFFF").place(x=830, y=680)
    ctk.CTkLabel(app, text="Highly motivated", font=ctk.CTkFont(size=15, family="Arial"), bg_color="#FFFFFF").place(x=1300, y=680)

    slider = ctk.CTkSlider(app, from_=0, to=10, number_of_steps=10, command=update_label, variable=selected_option, width=500, height=20, corner_radius=10, button_length=30, button_color="#0059ff", progress_color="#0059ff", bg_color="#FFFFFF")
    slider.set(5)
    slider.place(x=850, y=650)

    def next_step7():
        step_value_survey = 7
        clearWidgets([main_content_rect])
        import survey7
        survey7.survey7(app, main_content_rect, step_value_survey)

    survey_submit = ctk.CTkButton(app, text="Next", font=ctk.CTkFont(size=20, family="Arial"), fg_color="#0059ff", hover_color="#0041c4", width=200, height=50, corner_radius=10, command=next_step7)
    survey_submit.place(x=1000, y=800)
