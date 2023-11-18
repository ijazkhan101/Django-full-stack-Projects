from django.contrib import admin
from django.urls import path
from pages import views
from products.views import product_details_view ,product_create_view
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product/', product_details_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('admin/', admin.site.urls),
]
