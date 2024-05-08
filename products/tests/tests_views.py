from django.test import TestCase
from django.urls import reverse
from products.models import Product

class ProductViewTests(TestCase):
    def setUp(self):
        # Create some test data
        self.product1 = Product.objects.create(
            name='Test Product 1',
            description='Description of Test Product 1',
            price=10.99,
        )
        self.product2 = Product.objects.create(
            name='Test Product 2',
            description='Description of Test Product 2',
            price=20.99,
        )

    def test_all_products_view(self):
        # Test the all_products view
        response = self.client.get(reverse('products'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_product_detail_view(self):
        # Test the product_detail view
        response = self.client.get(reverse('product_detail', args=(self.product1.id,)))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, self.product1.name)
