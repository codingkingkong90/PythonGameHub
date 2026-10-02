import customtkinter as ctk
from ..services import firestore
from ..services import firebase_auth
from ..services import password_check

def create_signup_page(parent, router):
    signup_card = ctk.CTkFrame(parent)
    signup_card.grid_propagate(False)

    signup_card.columnconfigure(0, weight=1)
    signup_card.rowconfigure(0, weight=1)

    signup_container = ctk.CTkFrame(signup_card, fg_color="#333333")
    signup_container.grid(row=0, column=0)

#global variables-------------------------------------------------------------
    password = ctk.StringVar(value="Enter a password")
    confirm_password = ctk.StringVar(value="Reenter your password")
    error_message = ctk.StringVar(value="")
#functions--------------------------------------------------------------------
    def handle_signup():
        username = signup_username.get().split()
        email = signup_email.get().split()
        password = signup_password.get().split()
        
        result = firebase_auth.signup_user(email, password)

        if signup_button:
            if result["success"]:
                try:
                    firestore.create_user_document(
                        result["localId"],
                        username,
                        email,
                        result["idToken"]
                    )
                except:
                    pass

    password.trace_add("write", password_check.password_requirments(password, confirm_password, error_message))
    
    signup_username = ctk.CTkEntry(signup_container, placeholder_text="Username")
    signup_username.grid(row=1, column=0, pady=5)

    signup_email = ctk.CTkEntry(signup_container, placeholder_text="Email")
    signup_email.grid(row=2, column=0, pady=5)

    signup_password = ctk.CTkEntry(signup_container, textvariable=password)
    signup_password.grid(row=3, column=0, pady=5)

    signup_confirm_password = ctk.CTkEntry(signup_container, textvariable=confirm_password)
    signup_confirm_password.grid(row=4, column=0, pady=5)

    error_label = ctk.CTkLabel(signup_container, textvariable=error_message)
    error_label.grid(row=5, column=0, pady=5)

    signup_button = ctk.CTkButton(signup_container, text="Signup", command=handle_signup)
    signup_button.grid(row=6, column=0, pady=5)

    return signup_card
