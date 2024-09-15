from django.utils.timezone import now
from rest_framework_simplejwt import authentication


class JWTAuthentication(authentication.JWTAuthentication):
  """
  Update last_login user field if the user is authenticated
  """

  def get_user(self, validated_token):
    """
    Attempts to find and return a user using the given validated token.
    """
    user = super(JWTAuthentication, self).get_user(validated_token)
    user.last_login = now()
    user.save()
    return user
