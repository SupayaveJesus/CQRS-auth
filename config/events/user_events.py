from query.models import UserReadModel


def user_created_event(user):
    print(f"Event|: User created -> { user.username}")

    UserReadModel.objects.using("read_db").create(
        username=user.username,
        email=user.email
    )