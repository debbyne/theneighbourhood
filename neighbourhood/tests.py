from django.test import TestCase
from .models import Profile, Post, Business, Neighbourhood
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(name='moringa',email='kinyadebbyne@gmail.com',location='Kiambu' )
        self.user.save()



class TestNeigbourhood(TestCase):
    def setUp(self):
        self.Neighbourhood = Neighbourhood(name='Jujamaica', description='good vibes', location='Kiambu',occupants_count='11')
        self.Neighbourhood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Neighbourhood, Neighbourhood))



class TestBusiness(TestCase):
    def setUp(self):
        self.user = User(name='Moringa', email='kinyadebbyne@gmail.com', location= 'Kiambu')
        self.user.save()

        self.busines = Business(name='Top Clean Solutions', email='kinyadebbyne@gmail.com', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.busins, Business))

    def test_save_hood(self):
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_hood(self):
        business = Business.objects.all().delete()
        self.assertTrue(len(business) > 0)