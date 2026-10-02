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
        user_name = signup_username.get().strip()
        user_email = signup_email.get().strip()
        user_pwd = signup_password.get().strip()

        if not user_name or not user_email or not user_pwd:
            error_message.set("All fields are required.")
            return

        result = firebase_auth.signup_user(user_email, user_pwd)
        
        if result["success"]:
            user_data = result["user"]

            user_id = user_data["localId"]
            id_token = user_data["idToken"]
            try:
                firestore.create_user_document(
                    user_id,
                    user_name,
                    user_email,
                    id_token
                )
            except Exception as e:
                error_message.set(f"Auth succeeded, but profile creation")
                print("--- FIRESTORE WRITE ERROR START ---")
                print(e)
                print("--- FIRESTORE WRITE ERROR END ---")
                

    password_check.password_requirments(password, confirm_password, error_message)
    
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
