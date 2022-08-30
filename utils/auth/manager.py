from functools import wraps
from flask_login import LoginManager, current_user
from utils.auth.roles import role_enum

login_manager = LoginManager()


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if current_user.role != role_enum.get(role, -1) and role != "ANY":
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
