from django.urls import path
from f1app import views

urlpatterns=[
    path("about/", views.AboutView.as_view(), name="about"),
    #drivers
    path("", views.DriverListView.as_view(), name="driver_list"),
    path("drivers/<int:pk>/", views.DriverDetailView.as_view(), name="driver_detail"),
    path("driver/new/", views.DriverCreateView.as_view(), name="driver_new"),
    path("driver/<int:pk>/edit/", views.DriverUpdateView.as_view(), name="driver_edit"),
    path("driver/<int:pk>/delete/", views.DriverDeleteView.as_view(), name="driver_delete"),
    #constructors
    path("constructor/", views.ConstructorListView.as_view(), name="constructor_list"),
    path("constructor/<int:pk>/", views.ConstructorDetailView.as_view(), name="constructor_detail"),
    path("constructor/new/", views.ConstructorCreateView.as_view(), name="constructor_new"),
    path("constructor/<int:pk>/edit/", views.ConstructorUpdateView.as_view(), name="constructor_edit"),
    path("constructor/<int:pk>/delete/", views.ConstructorDeleteView.as_view(), name="constructor_delete"),
    #circuits
    path("circuit/", views.CircuitListView.as_view(), name="circuit_list"),
    path("circuit/<int:pk>/", views.CircuitDetailView.as_view(), name="circuit_detail"),
    path("circuit/new/", views.CircuitCreateView.as_view(), name="circuit_new"),
    path("circuit/<int:pk>/edit/", views.CircuitUpdateView.as_view(), name="circuit_edit"),
    path("circuit/<int:pk>/delete/", views.CircuitDeleteView.as_view(), name="circuit_delete"),
]