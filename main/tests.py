# Create your tests here.
from django.test import TestCase, Client
from main.models import Item
from datetime import datetime


class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class ItemTestCase(TestCase):
    def setUp(self) -> None:
        Item.objects.create(
            name = "Galon Aqua", 
            amount = 5, 
            description = "Sebuah galon aqua",
            category = "Minuman",
            )
        
        Item.objects.create(
            name = "Mangkok", 
            amount = 10, 
            description = "Mangkok dengan gambar ayam",
            category = "Alat makan",
            )
        
    def test_item(self):
        items = Item.objects.all()
        for item in items:
            self.assertIsInstance(getattr(item, 'name'), str)
            self.assertIsInstance(getattr(item, 'amount'), int)
            self.assertIsInstance(getattr(item, 'description'), str)
            self.assertIsInstance(getattr(item, 'category'), str)
            self.assertIsInstance(getattr(item, 'date_added'), type(datetime.now()))
