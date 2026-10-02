min_legnth = 8

def password_requirments(password, confirm_password, label):
    password_str = password.get()
    confirm_password_str = confirm_password.get()
    
    has_lower = any(c.islower() for c in password_str)
    has_upper = any(c.isupper() for c in password_str)
    has_digit = any(c.isdigit() for c in password_str)
    has_legnth = len(password_str) >= min_legnth

    if not (has_lower and has_upper and has_digit and has_legnth):
        label.set("Your password must contain 8 characters and at least 1 digit, 1 uppercase letter and 1 lowercase letter")
    elif password_str != confirm_password_str:
        label.set("Passwords do not match.")
    else:
        label.set("")
         
