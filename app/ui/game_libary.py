import customtkinter as ctk

def create_game_libary(parent, router):
    main_libary_card = ctk.CTkFrame(parent)
    main_libary_card.grid_propagate(False)

    main_libary_card.columnconfigure(0)
    main_libary_card.rowconfigure(0)

    snake_libary_card = ctk.CTkFrame(main_libary_card, fg_color="#333333")
    snake_libary_card.grid(row=0, column=0, pady=10, sticky="nw")

    pong_libary_card = ctk.CTkFrame(main_libary_card, fg_color="#333333")
    pong_libary_card.grid(row=0, column=1, pady=10)    

    #snake_libary-----------------------------------------------------------
    return main_libary_card

