from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(User):
    refresh = RefreshToken.for_user(User)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
