from django.test import TestCase
from .models import Book

# Create your tests here.
class BookModelTest(TestCase):

    def setUpTestData():
        # set up non-modified objects use by all test methods
        Book.objects.create(name='Pride and Prejudice', author_name='Jane Austen', genre='classic', book_type='hardcover', price='23.71')

    def test_book_name(self):
        # Get a book object to test
        book = Book.objects.get(id=1)

        # Get the metadata for the name field and use it to query its data
        field_label = book._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        book = Book.objects.get(id=1)

        max_length = book._meta.get_field('author_name').max_length

        self.assertEqual(max_length, 120)  

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/books/list/1')