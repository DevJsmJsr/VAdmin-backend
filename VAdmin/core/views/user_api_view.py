from rest_framework import generics
from typing import Any
from core.serializers import UserSerializer
from django.contrib.auth.models import Permission
from rest_framework.request import Request
from rest_framework.response import Response
from core.models import User

class UserListCreateAPIView(generics.ListCreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  
  def list(self, request: Request, *args: Any, **kwargs: Any):
    user = request.user
    user.get_user_permissions()
    
    if user.is_superuser:
      permissions = Permission.objects.all()
    else:
      permissions = (
          user.user_permissions.all() | Permission.objects.select_related(
              'content_type').filter(group__user=user)
      )
    permissions = [
      f"{permission.content_type.app_label}.{permission.codename}"
      for permission in permissions
    ]
    context = {
      'request': self.request,
      'format': self.format_kwarg,
      'view': self,
      'permissions': permissions,
      'is_superuser': user.is_superuser
    }
    serializer = self.get_serializer(instance=user, context=context)
    return Response(serializer.data)