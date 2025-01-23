from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователей."""

    class Meta:
        model = User
        fields = ('username', 'email',)


class UserDetailSerializer(ModelSerializer):
    """Сериализатор для просмотра профиля пользователя."""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone',
                  'avatar', 'date_of_birth',)
