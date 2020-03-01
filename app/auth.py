from flask import redirect, session

# Stab
def login_required(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
    return wrapper
