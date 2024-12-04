from django.test import SimpleTestCase

#examples

#TO RUN - python manage.py test

### class TestHelloView(SimpleTestCase):
        #def test_hello_jet(self):
        #response = self.client.get("/hello/jet/") - where it is pulling from
        #self.assertContains(response,"Hello Jet") - expected outcome

class TestWarmup1View(SimpleTestCase):
    def test_false(self):
        response = self.client.get("/warmup1/7")
        self.assertContains(response, "False")
