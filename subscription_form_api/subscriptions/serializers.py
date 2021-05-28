from rest_framework import serializers

from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Customer subscription serializer"""

    class Meta:
        model = Subscription
        fields = '__all__'
