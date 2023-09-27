from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Product

# Create your tests here.

# class mainTest(TestCase):
#     def test_main_url_is_exist(self):
#         response = Client().get('')
#         self.assertEqual(response.status_code, 200)

#     def test_main_using_main_template(self):
#         response = Client().get('')
#         self.assertTemplateUsed(response, 'main.html')

class mainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        
        self.product1 = Product.objects.create(
            name='Product 1',
            price=10.0,
            description='Description for Product 1',
            user=self.user
        )
        self.product2 = Product.objects.create(
            name='Product 2',
            price=20.0,
            description='Description for Product 2',
            user=self.user
        )

    def test_create_product_autentikasi(self):
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.post(reverse('main:create_product'), {
            'name': 'New Product',
            'price': 15.0,
            'description': 'Description for New Product',
        })
                
        new_product = Product.objects.get(name='New Product')
        self.assertIsNotNone(new_product)