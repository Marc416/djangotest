from django.test import TestCase

from accountapp.models import HelloWorld


class TestHelloWorld(TestCase):
    fixtures = ['hello.json']

    def TestHello(self):
        h = HelloWorld.objects.get(id=1)
        print(h.text)
        self.assertEqual(h.text, "super new")
