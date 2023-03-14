import os
from functools import wraps


def env_wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        app_env = os.getenv("APP_ENV")
        if app_env == "development":
            print("App in development mode, not performing action!")
            return
        elif app_env == "staging" or app_env == "production":
            return func(*args, **kwargs)
        else:
            raise ValueError(f"Invalid APP_ENV: {app_env}")

    return inner
