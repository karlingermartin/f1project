from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.driver_list_url = reverse("driver_list")
        self.constructor_list_url = reverse("constructor_list")
        self.circuit_list_url = reverse("circuit_list")

    def test_driver_list_GET(self):
        response = self.client.get(self.driver_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "f1app/driver_list.html")

    def test_constructor_list_GET(self):
        response = self.client.get(self.constructor_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "f1app/constructor_list.html")

    def test_circuit_list_GET(self):
        response = self.client.get(self.circuit_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "f1app/circuit_list.html")
