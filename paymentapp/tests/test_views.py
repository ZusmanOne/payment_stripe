from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from paymentapp.models import Item
from rest_framework.test import APITestCase


class ItemTestAPI(APITestCase):

    def test_post_method(self):
        item = {
            "id":1,
            "name": "test name",
            "description": 'test text',
            "price": 100,
        }
        response = self.client.post('http://127.0.0.1:8000/', item)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data['name'], str)

    def test_get_method(self):
        self.test_post_method()
        url = 'http://127.0.0.1:8000/item/1/'
        response = self.client.get(reverse('item-detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


