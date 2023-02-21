from rest_framework import serializers
from .models import Portfolio, Dividend

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        fields='__all__'

class PortfolioCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )

    def validate_user(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required')
        return value

    class Meta:
        model = Portfolio
        fields = '__all__'