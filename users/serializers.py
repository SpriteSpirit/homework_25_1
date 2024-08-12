from rest_framework import serializers
from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор платежа """

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя """
    payments = PaymentSerializer(source='payment', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    """ Сериализатор регистрации нового пользователя """
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )

        user.set_password(password)
        user.save()
        return user
