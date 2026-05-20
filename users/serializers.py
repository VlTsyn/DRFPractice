from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    """Сериализация пользователей"""

    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    """Сериализация платежей"""

    class Meta:
        model = Payment
        fields = '__all__'