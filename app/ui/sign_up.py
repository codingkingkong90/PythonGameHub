import customtkinter as ctk
from ..services import firestore
from ..services import firebase_auth

def create_signup_page(parent, router):
    signup_card = ctk.CTkFrame(parent)
    signup_card.grid_propagate(False)

    signup_card.columnconfigure(0, weight=1)
    signup_card.rowconfigure(0, weight=1)

    signup_container = ctk.CTkFrame(signup_card, fg_color="transparent")
    signup_container.grid(row=0, column=0)

#global variables-------------------------------------------------------------
    password = ctk.StringVar()
    min_legnth = 8
    errors = ["lowercase letter", "uppercase letter", "digit", "special chracter"]

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


    def check_condition(condition, errors):
        if condition:
            for error in errors:
                error_label.config(text="Your password needs " + errors[error])
        else:
            error_label.grid_remove()
            

    def password_requirments(*args):
        password = signup_password.get().split()
        confirm_password = signup_confirm_password.get().split()

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c.isspecial() for c in password)

        check_condition(has_lower, errors[0])


    signup_username = ctk.CTkEntry(signup_container, placeholder_text="Username")
    signup_username.grid(row=1, column=0, pady=5)

    signup_email = ctk.CTkEntry(signup_container, placeholder_text="Email")
    signup_email.grid(row=2, column=0, pady=5)

    signup_password = ctk.CTkEntry(signup_container, textvariable=password)
    signup_password.grid(row=3, column=0, pady=5)

    signup_confirm_password = ctk.CTkEntry(signup_container, placeholder_text="Please rewrite your password")
    signup_confirm_password.grid(row=4, column=0, pady=5)

    error_label = ctk.CTkLabel(signup_container, textvariable=errors)
    error_label.grid(row=5, column=0, pady=5)

    signup_button = ctk.CTkButton(signup_container, text="Signup")
    signup_button.grid(row=6, column=0, pady=5)

