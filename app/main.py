import customtkinter as ctk

root = ctk.CTk()
root.title("GameHub")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.attributes("-fullscreen", True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

active_frame = None

def navigate_to(page_name):
    if active_frame is not None:
        active_frame.grid_forget()
        active_frame.destroy()
    

