from users.serializers import UserDetailSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserDetailSerializer(user).data
    }