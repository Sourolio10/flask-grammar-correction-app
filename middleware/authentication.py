from functools import wraps


def login_required(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        return func(*args, **kwargs)
    return check_token