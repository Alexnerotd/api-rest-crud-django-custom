from rest_framework.authtoken.models import Token

user_id = 1  # Reemplaza con el ID del usuario que deseas
try:
    token = Token.objects.get(user_id=user_id)
    token_key = token.key
except Token.DoesNotExist:
    token_key = None
