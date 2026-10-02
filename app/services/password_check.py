min_legnth = 8
errors = ["lowercase letter", "uppercase letter", "digit", "special chracter"]

def check_condition(condition, error, label_name):
        if condition:
            label_name.set(f"Your password needs {error}")
        else:
            label_name.set("")
            

def password_requirments(password, confirm_password, label):
    
    if not isinstance(password, str) or not isinstance(confirm_password, str):
        label.set("Password must be a string")
        return
    
    if len(password) < min_legnth:
         label.set(f"Your password must be at least {min_legnth} characters long")
         return
    
    if password != confirm_password:
         label.set("Passwords do not match")
         return
        
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    check_condition(has_lower, errors[0], label_name=label)
    check_condition(has_upper, errors[1], label_name=label)
    check_condition(has_digit, errors[2], label_name=label)