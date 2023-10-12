from tkinter import *

main_frame = Tk()
main_frame.minsize(width=300, height=400)
main_frame.title("BMI Calculator")

lbl_height = Label(text="Height (cm)")
lbl_height.config(font=("Verdana", 14, "normal"))
lbl_height.pack(side="top", padx=5, pady=5)
inp_height = Entry()
inp_height.config(font=("Verdana", 14, "normal"))
inp_height.config(fg="green")
inp_height.pack(side="top", padx=10, pady=10)

lbl_weight = Label(text="Weight (kg)")
lbl_weight.config(font=("Verdana", 14, "normal"))
lbl_weight.pack(side="top", padx=5, pady=5)
inp_weight = Entry()
inp_weight.config(font=("Verdana", 14, "normal"))
inp_weight.config(fg="green")
inp_weight.pack(side="top", padx=10, pady=10)

lbl_bmi = Label(text="")
lbl_bmi.config(fg="blue", font=("Verdana", 14, "normal"))
lbl_bmi.pack(side="top")

lbl_bmi_class = Label(text="")
lbl_bmi_class.config(fg="blue", font=("Verdana", 10, "normal"))
lbl_bmi_class.pack(side="top")


def calcBMI():
    try:
        if len(inp_height.get()) == 0 or len(inp_weight.get()) == 0:
            lbl_bmi_class.config(text="")
            lbl_bmi.config(fg="red")
            lbl_bmi.config(text="You must enter both input!")
        else:
            lbl_bmi.config(fg="blue")
            user_height = float(inp_height.get())
            user_weight = float(inp_weight.get())
            # print(type(user_height))
            bmi = round((user_weight / pow((user_height / 100), 2)), 1)
            # print(bmi)
            # lbl_bmi.config(text=f"{bmi} kg/m2")
            if bmi < 16:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Severe Thinness")
            elif 16 <= bmi < 17:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Moderate Thinness")
            elif 17 <= bmi < 18.5:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Mild Thinness")
            elif 18.5 <= bmi < 25:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Normal")
            elif 25 <= bmi < 30:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Overweight")
            elif 30 <= bmi < 35:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Obese Class I")
            elif 35 <= bmi < 40:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Obese Class II")
            elif bmi >= 40:
                lbl_bmi.config(text=f"Your BMI: {bmi} kg/m2")
                lbl_bmi_class.config(text="Classification: Obese Class III")
    except ValueError:
        lbl_bmi_class.config(text="")
        lbl_bmi.config(fg="red")
        lbl_bmi.config(text="Enter a valid input!")


btn_calculate = Button(text="CALCULATE", command=calcBMI)
btn_calculate.config(bg="green", fg="white", font=("Verdana", 14, "normal"))
btn_calculate.pack(side="top", padx=10, pady=20)

main_frame.mainloop()
