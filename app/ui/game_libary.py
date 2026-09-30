import customtkinter as ctk

def create_game_libary(parent, router):
    main_libary_card = ctk.CTkFrame(parent)
    main_libary_card.grid_propagate(False)

    main_libary_card.columnconfigure(0, weight=1)
    main_libary_card.rowconfigure(0, weight=1)

    libary_container = ctk.CTkFrame(main_libary_card, fg_color="transparent")
    libary_container.grid(row=0, column=0)

    snake_libary_card = ctk.CTkFrame(libary_container, fg_color="#333333")
    snake_libary_card.grid(row=1, column=0, pady=10, sticky="nw")

    snake_libary_card.place(x=0, y=0)

    #snake_libary-----------------------------------------------------------
    return main_libary_card

