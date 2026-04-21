from rest_framework.decorators import api_view
from rest_framework.response import Response
from query.models import UserReadModel

@api_view(['GET'])
def get_users(request):
    users = UserReadModel.objects.using('read_db').all()

    data = [
        {
            "username": u.username,
            "email": u.email
        }
        for u in users
    ]

    return Response(data)