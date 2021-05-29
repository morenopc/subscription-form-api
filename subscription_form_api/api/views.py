from rest_framework import generics
from rest_framework.permissions import AllowAny

from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class SubscriptionListCreateAPIView(generics.ListCreateAPIView):
    """Create and list customer subscriptions"""

    queryset = Subscription.objects.order_by('-id')[:10]
    serializer_class = SubscriptionSerializer
    permission_classes = (AllowAny, )
