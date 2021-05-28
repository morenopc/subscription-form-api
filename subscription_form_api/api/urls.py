from django.urls import path

from .views import SubscriptionListCreateAPIView


app_name = 'api'
urlpatterns = [
    path('subscriptions/', SubscriptionListCreateAPIView.as_view(),
         name='subscriptions')
]
