from .firebase_config import auth

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return {"success": True, "user": user}
    except Exception as e:
        error_message = str(e)
        return {"success": False, "error": error_message}

def signup_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return {"success": True, "user": user}
    except Exception as e:
        error_message = str(e)
        return {"success": False, "error": error_message}