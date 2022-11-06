from django.test import SimpleTestCase
from django.urls import reverse, resolve
from f1app.views import AboutView, DriverListView, DriverDetailView, ConstructorListView, ConstructorDetailView, CircuitListView, CircuitDetailView


class TestUrls(SimpleTestCase):
    def test_about_url_is_resolved(self):
        url = reverse("about")
        self.assertEquals(resolve(url).func.view_class, AboutView)

    def test_driver_list_url_is_resolved(self):
        url = reverse("driver_list")
        self.assertEquals(resolve(url).func.view_class, DriverListView)

    def test_driver_detail_url_is_resolved(self):
        url = reverse("driver_detail", args=['1'])
        self.assertEquals(resolve(url).func.view_class, DriverDetailView)

    def test_constructor_list_url_is_resolved(self):
        url = reverse("constructor_list")
        self.assertEquals(resolve(url).func.view_class, ConstructorListView)

    def test_constructor_detail_url_is_resolved(self):
        url = reverse("constructor_detail", args=['1'])
        self.assertEquals(resolve(url).func.view_class, ConstructorDetailView)

    def test_circuit_list_url_is_resolved(self):
        url = reverse("circuit_list")
        self.assertEquals(resolve(url).func.view_class, CircuitListView)

    def test_circuit_detail_url_is_resolved(self):
        url = reverse("circuit_detail", args=['1'])
        self.assertEquals(resolve(url).func.view_class, CircuitDetailView)
