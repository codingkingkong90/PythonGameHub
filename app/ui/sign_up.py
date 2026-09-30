import customtkinter as ctk
#from ..services import firestore

def create_signup_page(parent, router):
    signup_card = ctk.CTkFrame(parent)
    signup_card.grid_propagate(False)

    signup_card.columnconfigure(0, weight=1)
    signup_card.rowconfigure(0, weight=1)

    signup_container = ctk.CTkFrame(signup_card, fg_color="transparent")
    signup_container.grid(row=0, column=0)

    username_entry = ctk.CTkEntry(signup_container)