from django.urls import path
from . import views

urlpatterns = [
    
   path('',views.products,name='products'),
   path("<int:product_id>", views.product,name='product'),
   path('search/', views.search ,name='search') ,
   path('add/', views.basket_add, name='basket_add'),
   path('basket/', views.basket_view, name='basket_view'),

]
