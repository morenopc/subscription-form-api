from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class SubscriptionsApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_customer_subscriptions(self):
        """Testing create a new customer subscription"""

        payload = {
            'name': 'Moreno Cunha',
            'email': 'moreno@amara.org',
            'subscription_type': 'free'}

        self.client.post(reverse('api:subscriptions'), payload)

        exists = Subscription.objects.filter(
            name='Moreno Cunha', email='moreno@amara.org',
            subscription_type='free').exists()
        self.assertTrue(exists)

    def test_retrieve_subscriptions_list(self):
        """Test retrieving a list of subscriptions"""

        Subscription.objects.create(
            name='Carl Yu', email='carl@pculture.org',
            subscription_type='free')
        Subscription.objects.create(
            name='Margarita Shamraeva', email='mshamraeva@pculture.org',
            subscription_type='plus')
        Subscription.objects.create(
            name='Sam Slottow', email='sam@amara.org',
            subscription_type='pro')

        serializer = SubscriptionSerializer(
            Subscription.objects.all(), many=True)

        response = self.client.get(reverse('api:subscriptions'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data contains 3 subscriptions.
        self.assertEqual(len(response.data), 3)

        # Check that the response data is equal to the stored records.
        self.assertEqual(response.data, serializer.data)
