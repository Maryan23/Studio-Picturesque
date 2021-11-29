from django.test import TestCase
from .models import Pictures,Category,Location


# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.montreal = Location(loc='Montreal')

    def test_location_instance(self):
        self.assertTrue(isinstance(self.montreal,Location))

    def test_save_location(self):
        self.montreal.save_location()
        places = Location.objects.all()
        self.assertTrue(len(places)> 0)

    def test_delete_location(self):
        self.montreal.save_location()
        places=Location.objects.all()
        self.assertEqual(len(places),1)
        self.montreal.delete_location()
        places = Location.objects.all()
        self.assertEqual(len(places), 0)

    def test_display_locations(self):
        self.montreal.save_location()
        self.assertEqual(len(Location.display_all_locations()),1)

    def test_update_location(self):
        self.montreal.save_location()
        self.montreal.update_location(self.montreal.id,'bot')
        update = Location.objects.get(loc = "bot")
        self.assertTrue(update.loc, 'bot')

class CategoryTestClass(TestCase):
    def setUp(self):
        self.rare = Category(name="rare")

    def test_save_category(self):
        self.rare.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.rare.save_category()
        categories= Category.objects.all()
        self.assertEqual(len(categories),1)
        self.rare.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),0)

    def test_update_category(self):
        self.rare.save_category()
        self.rare.update_category(self.rare.id,'bot')
        update = Category.objects.get(name = "bot")
        self.assertTrue(update.name, 'bot')

    def test_display_categories(self):
        self.rare.save_category()
        self.assertEqual(len(Category.display_all_categories()),1)


class PictureTestClass(TestCase):
    def setUp(self):
        self.rare = Category(name = 'rare')
        self.montreal = Location(loc = 'Montreal')
        self.lake = Pictures(image='image.png',name ='jiazghou', description = 'vast', category= self.rare, location= self.montreal,pub_date=None)

    def test_pic_instance(self):
        '''
        test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.lake, Pictures))

    def test_save_pic(self):
        self.rare.save_category()
        self.montreal.save_location()
        self.lake.save_picture()
        pic = Pictures.objects.all()
        self.assertEqual(len(pic)>0,1)
    
    