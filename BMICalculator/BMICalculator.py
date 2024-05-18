from PIL import Image, ImageTk
import customtkinter as ctk

SMALL_FONT_STYLE = ("Josefin Sans", 16, "bold")
DEFAULT_FONT_STYLE = ("Josefin Sans", 18, "bold")
ENTRY_FONT_STYLE = ("Ubuntu Mono", 16, "bold")
RESULT_FONT_STYLE = ("Jost",48,"bold")

PURE_DARK = "#000000"
LABEL_COLOR = "#FFFFFF"
WARN_COLOR = "#FF0000"

ctk.set_appearance_mode("dark")

del_image = ctk.CTkImage(Image.open("ImageResources\del.png"), size=(20,20))


class BMICalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x550")
        self.window.resizable(False, False)
        self.window.title("AppStaticsX™-BMICalculator")
        self.window.iconbitmap(r'ImageResources\\icon.ico')


        logo = Image.open("ImageResources\logo.png").resize((100,100)) 
        self.logo_img = ImageTk.PhotoImage(logo)
        self.logo_label = ctk.CTkLabel(self.window, image=self.logo_img, fg_color="transparent", text="", bg_color="transparent")
        self.logo_label.pack(pady=15)

        self.frame1 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent")
        self.frame1.pack()

        self.lable1 = ctk.CTkLabel(self.frame1, text="Enter Height (cm):", font=SMALL_FONT_STYLE, text_color=LABEL_COLOR)
        self.lable1.pack(side="left", padx=20)

        self.entry1 = ctk.CTkEntry(self.frame1, height=30, width=90, fg_color="white", border_width=2, text_color=PURE_DARK, font=ENTRY_FONT_STYLE)
        self.entry1.pack(side="left", padx=10)

        self.c_button1 = ctk.CTkButton(self.frame1, text="", width=24, height=24, image=del_image, fg_color=WARN_COLOR, command=self.clear_val1)
        self.c_button1.pack(side="right")

        self.frame2 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent")
        self.frame2.pack(pady= 10)

        self.lable2 = ctk.CTkLabel(self.frame2, text="Enter Weight (kg):", font=SMALL_FONT_STYLE, text_color=LABEL_COLOR)
        self.lable2.pack(side="left", padx=20)

        self.entry2 = ctk.CTkEntry(self.frame2, height=30, width=90, fg_color="white", border_width=2, text_color=PURE_DARK, font=ENTRY_FONT_STYLE)
        self.entry2.pack(side="left", padx=10)

        self.c_button2 = ctk.CTkButton(self.frame2, text="", width=24, height=24, image=del_image, fg_color=WARN_COLOR, command=self.clear_val2)
        self.c_button2.pack(side="right")

        self.frame3 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent")
        self.frame3.pack(pady= 10)

        self.cal_button = ctk.CTkButton(self.frame3, text="View Results", font=DEFAULT_FONT_STYLE, width=150, fg_color="#0E8849", command=self.cal_bmi)
        self.cal_button.pack()

        self.lable3 = ctk.CTkLabel(self.frame3, text="Your BMI is", font=SMALL_FONT_STYLE, text_color=LABEL_COLOR)
        self.lable3.pack(pady=10)

        self.lable4 = ctk.CTkLabel(self.frame3, text="N/A", font=RESULT_FONT_STYLE, text_color=LABEL_COLOR)
        self.lable4.pack(pady=0)

        self.lable5 = ctk.CTkLabel(self.frame3, text="Your BMI N/A", font=DEFAULT_FONT_STYLE, text_color=LABEL_COLOR)
        self.lable5.pack(pady=0)

        self.empty_frame = ctk.CTkFrame(self.window, width=400, height=10)
        self.empty_frame.pack(pady=10)

        self.frame4 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent")
        self.frame4.pack(pady= 0, padx=50)

        self.indicator1 = ctk.CTkFrame(self.frame4, height=10, width=75, fg_color="yellow")
        self.indicator1.pack(side="left")

        self.indicator_lab1 = ctk.CTkLabel(self.frame4, text="UNDERWEIGHT < 18.5", font=("Josefin Sans", 12, "bold"))
        self.indicator_lab1.pack(side="right", padx=10)

        self.frame5 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent")
        self.frame5.pack(pady= 0, padx=50)

        self.indicator1 = ctk.CTkFrame(self.frame5, height=10, width=75, fg_color="green")
        self.indicator1.pack(side="left")

        self.indicator_lab2 = ctk.CTkLabel(self.frame5, text="NORMAL 18.5-25        ", font=("Josefin Sans", 12, "bold"))
        self.indicator_lab2.pack(side="right", padx=10)

        self.frame6 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent",)
        self.frame6.pack(pady= 0, padx=50)

        self.indicator1 = ctk.CTkFrame(self.frame6, height=10, width=75, fg_color="orange")
        self.indicator1.pack(side="left")

        self.indicator_lab3 = ctk.CTkLabel(self.frame6, text="OVERWEIGHT 25-30  ", font=("Josefin Sans", 12, "bold"))
        self.indicator_lab3.pack(side="right", padx=10)

        self.frame7 = ctk.CTkFrame(self.window, height=100, width=400, fg_color="transparent")
        self.frame7.pack(pady= 0, padx=50)

        self.indicator1 = ctk.CTkFrame(self.frame7, height=10, width=75, fg_color="red")
        self.indicator1.pack(side="left")

        self.indicator_lab4 = ctk.CTkLabel(self.frame7, text="OBESE > 30              ", font=("Josefin Sans", 12, "bold"))
        self.indicator_lab4.pack(side="right", padx=10)


    def clear_val1(self):
     self.entry1.delete(0, "end")

    def clear_val2(self):
     self.entry2.delete(0, "end")

    def cal_bmi(self):
        height_input = self.entry1.get()
        weight_input = self.entry2.get()

        if not height_input or not weight_input:
           self.lable4.configure(text="😕", text_color=LABEL_COLOR)
           self.lable5.configure(text="Values Can't be Empty", text_color=WARN_COLOR)
           self.lable3.configure(text="")
           return

        try:
           height = float(height_input)
           weight = float(weight_input)
        except ValueError:
           self.lable4.configure(text="😕", text_color=LABEL_COLOR)
           self.lable5.configure(text="Please Enter Valid Values", text_color=WARN_COLOR)
           self.lable3.configure(text="")
           return

        height_in_meter = height/100

        bmi = round(float(weight/height_in_meter**2), 2)

        self.lable4.configure(text=bmi)

        if bmi <= 18.5:
            self.lable5.configure(text="You are UNDERWEIGHT", text_color=LABEL_COLOR)
            self.lable4.configure(text=bmi, text_color="yellow")
            self.lable3.configure(text="Your BMI is")
        elif bmi > 18.5 and bmi <= 25:
            self.lable5.configure(text="You are NORMAL", text_color=LABEL_COLOR)
            self.lable4.configure(text=bmi, text_color="green")
            self.lable3.configure(text="Your BMI is")
        elif bmi > 25 and bmi <= 30:
            self.lable5.configure(text="You are OVERWEIGHT", text_color=LABEL_COLOR)
            self.lable4.configure(text=bmi, text_color="orange")
            self.lable3.configure(text="Your BMI is")
        else:
            self.lable5.configure(text="You are OBESE", text_color=LABEL_COLOR)
            self.lable4.configure(text=bmi, text_color="red")
            self.lable3.configure(text="Your BMI is")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    bmical = BMICalculator()
    bmical.run()