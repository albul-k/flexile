from django.test import TestCase
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(
            first_name="John",
            last_name="White"
        )