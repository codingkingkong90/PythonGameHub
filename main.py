import customtkinter as ctk
from app.ui import home
from app.ui import game_libary
from app.ui import sign_up
from app.ui import login
from app.ui import settings
from app.ui import profile
from app.ui import password_reset

root = ctk.CTk()
root.title("GameHub")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.state("zoomed")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

active_frame = None

def navigate_to(page_name):
    global active_frame

    if active_frame is not None:
        active_frame.grid_forget()
        active_frame.destroy()

    if page_name == "home":
        active_frame = home.create_home_page(root, navigate_to)
    elif page_name == "game_libary":
        active_frame = game_libary.create_game_libary(root, navigate_to)
    elif page_name == "sign_up":
        active_frame = sign_up.create_signup_page(root, navigate_to)

    if active_frame is not None:
        active_frame.pack(expand=True, fill="both")

navigate_to("home")
root.mainloop()
