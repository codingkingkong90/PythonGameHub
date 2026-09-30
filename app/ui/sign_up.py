import customtkinter as ctk
#from ..services import firestore

def create_signup_page(parent, router):
    main_libary_card = ctk.CTkFrame(parent)
    main_libary_card.grid_propagate(False)

    main_libary_card.columnconfigure(0, weight=1)
    main_libary_card.rowconfigure(0, weight=1)

    libary_container = ctk.CTkFrame(main_libary_card, fg_color="transparent")
    libary_container.grid(row=0, column=0)