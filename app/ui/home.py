import customtkinter as ctk

def create_home_page(parent, router):
    home_card = ctk.CTkFrame(parent)
    home_card.grid_propagate(False)

    home_card.columnconfigure(0, weight=1)
    home_card.rowconfigure(0, weight=1)

    home_container = ctk.CTkFrame(home_card, fg_color="transparent")
    home_container.grid(row=0, column=0)

    main_label = ctk.CTkLabel(home_container, text="Welcome to the GameHub", font=("Arial", 50))
    main_label.grid(row=1, column=0, pady=10)

    play_button = ctk.CTkButton(home_container, text="Game Libary", hover_color="light blue", command= lambda: router("game_libary"))
    play_button.grid(row=2, column=0, pady=10)

    profile_button = ctk.CTkButton(home_container, text="Profile", hover_color="light blue", command= lambda: router("sign_up"))
    profile_button.grid(row=3, column=0, pady=10)

    return home_card

