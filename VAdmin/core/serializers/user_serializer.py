import django.contrib.auth.password_validation as validators
from rest_framework import serializers, exceptions
from core.models import User


class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  permissions = serializers.SerializerMethodField(read_only=True)
  is_superuser = serializers.BooleanField()

  class Meta:
    model = User
    fields = (
      'pk', 'username', 'first_name', 'last_name', 'email', 'rol',
      'permissions', 'is_superuser', 'password'
    )
    datatables_always_serialize = fields

  def get_permissions(self, obj: User):
    permissions = self.context.get('permissions')
    return permissions

  def validate(self, data):
    user = User(**data)
    password = data.get('password')
    try:
      validators.validate_password(password=password, user=user)
    except exceptions.ValidationError as e:
      raise serializers.ValidationError({"password": list(e.messages)})
    return super(UserSerializer, self).validate(data)
  
  def create(self, validated_data):
    user = super(UserSerializer, self).create(validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user