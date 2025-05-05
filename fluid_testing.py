import customtkinter as ctk
from PIL import Image
from Fluid import password_conversion_char_array, convert_pwd_in_array
from Fluid_dict import Fluid_table


def on_submit():
    password = entry.get()
    if password:
        convert_pwd_in_array(password)
    else:
        print("Please enter a password.")

app = ctk.CTk()
app.title("Fluid Zero")
app.geometry("700x450")
app.configure(fg_color="black")


user_image = Image.open("user_logo.png")
user_image = user_image.resize((600, 600), Image.Resampling.LANCZOS)
user_logo = ctk.CTkImage(user_image)

user_logo = ctk.CTkImage(light_image=user_image, size=(250, 250))
user_logo_label = ctk.CTkLabel(app, image=user_logo, text=None)
user_logo_label.pack(pady=40, anchor="center")


entry = ctk.CTkEntry(app, placeholder_text="Password", show="*", width=350, height=35, font=("Arial", 20))
entry.pack(pady=10)


submit_button = ctk.CTkButton(app, text="Login", fg_color="orange",command=on_submit, width=150, height=40, font=("Arial", 14))
submit_button.pack(pady=10)


app.mainloop()
