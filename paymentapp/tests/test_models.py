from django.test import TestCase
from paymentapp.models import Item


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = Item.objects.create(
            name='test name',
            description='test text',
            price=100,
        )

    def test_instance_model(self):
        item = Item.objects.get(id=1)
        self.assertIsInstance(item, Item)

    def test_name_content(self):
        item = Item.objects.get(id=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, 'test name')

    def test_discription_content(self):
        item = Item.objects.get(id=1)
        expected_object_name = f'{item.description}'
        self.assertEqual(expected_object_name, 'test text')

    def test_price_content(self):
        item = Item.objects.get(id=1)
        expected_object_name = item.price
        self.assertEqual(expected_object_name, 100)
