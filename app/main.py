import customtkinter as ctk
from ui import home

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

    if active_frame is not None:
        active_frame.pack(expand=True, fill="both")

navigate_to("home")
root.mainloop()
    

