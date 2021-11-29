from django.test import TestCase
from .models import Pictures,Category,Location

# Create your tests here.
class PicturesTestClass(TestCase):

    def setUp(self):
        """
        Create a pic for testing
        """
        Pictures.objects.create(
            name="Test Image",
            description="Test Description",
            location=Location.objects.create(loc="Test Location"),
            category=Category.objects.create(name="Test Category"),
            pub_date=None
        )

    def test_pic_name(self):
        """
        Test that the pic name is correct
        """
        pic = Pictures.objects.get(name="Test Image")
        self.assertEqual(pic.name, "Test Image")

    def test_pic_description(self):
        """
        Test that the pic description is correct
        """
        pic = Pictures.objects.get(name="Test Image")
        self.assertEqual(pic.description, "Test Description")

    def test_pic_location(self):
        """
        Test that the image location is correct
        """
        pic = Pictures.objects.get(name="Test Image")
        self.assertEqual(pic.location.loc, "Test Location")

    def test_pic_category(self):
        """
        Test that the image category is correct
        """
        pic = Pictures.objects.get(name="Test Image")
        self.assertEqual(pic.category.name, "Test Category")


class CategoryTestClass(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")

class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(loc="Test Location")

    def test_location_loc(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(loc="Test Location")
        self.assertEqual(location.loc, "Test Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(loc="Test Location")
        self.assertEqual(str(location), "Test Location")