import customtkinter as ctk

def create_home_page(parent, router):
    home_card = ctk.CTkFrame(parent)
    home_card.grid_propagate(False)

    home_card.columnconfigure(0, weight=1)
    home_card.rowconfigure(0, weight=1)

    main_label = ctk.CTkLabel(home_card, text="Welcome to the GameHub")
    main_label.grid()

