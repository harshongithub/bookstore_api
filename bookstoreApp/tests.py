from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from .models import Book
from .serializers import BookSerializer

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            published_date="2023-01-01",
            price=Decimal("500.20")
        )

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(str(self.book), "Test Book")

    def test_book_fields(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.description, "Test Description")
        self.assertEqual(str(self.book.published_date), "2023-01-01")
        self.assertEqual(self.book.price, Decimal("500.20"))

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(
            title="API Test Book",
            author="API Test Author",
            description="API Test Description",
            published_date="2023-01-01",
            price=Decimal("29.99")
        )
        self.valid_payload = {
            'title': 'New Book',
            'author': 'New Author',
            'description': 'New Description',
            'published_date': '2023-02-01',
            'price': '39.99'
        }
        self.invalid_payload = {
            'title': '',
            'author': 'Invalid Author',
            'description': 'Invalid Description',
            'published_date': '2023-03-01',
            'price': 'invalid_price'
        }

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.pk}))
        book = Book.objects.get(pk=self.book.pk)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('book-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('book-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            reverse('book-detail', kwargs={'pk': self.book.pk}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_create(self):
        response = self.client.post(reverse('book-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_update(self):
        response = self.client.put(
            reverse('book-detail', kwargs={'pk': self.book.pk}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_delete(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'newuser',
            'password': 'newpassword'
        }

    def test_user_registration(self):
        response = self.client.post(reverse('register'), data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        User.objects.create_user(username='newuser', password='newpassword')
        response = self.client.post(reverse('token_obtain'), data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_invalid_login(self):
        response = self.client.post(reverse('token_obtain'), data={
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
