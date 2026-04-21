from rest_framework.decorators import api_view
from rest_framework.response import Response
from command.services.user_service import register_user_service

@api_view(['POST'])
def register_user(request):
    try:
        user = register_user_service(request.data)
        return Response({
            'message': 'success User created',
            'username': user.username
        })
    except Exception as e:
        return Response({
            'message': 'error creating user',
            'error': str(e)},
            status=400)

