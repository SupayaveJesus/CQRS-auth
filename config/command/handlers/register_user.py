from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from events.user_events import user_created_event

def register_user(data):
    user_model = get_user_model()
    user = user_model.objects.create(
        username=data["username"],
        email=data["email"],
        password=make_password(data["password"]),
    )

    user_created_event(user)

    return user