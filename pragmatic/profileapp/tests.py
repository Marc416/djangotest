from django.test import TestCase

from profileapp.models import User


# Create your tests here.
class TestProfile(TestCase):
    # def setUp(self) -> None:
        # self.user = User()

    def test_user_count(self):
        self.assertTrue(1, 1)
