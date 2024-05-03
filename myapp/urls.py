from django.contrib import admin
from django.urls import path, include
from myapp.views.checkout import CheckOut
from myapp.views.orders import Order
from myapp.views.login import Login, logout
from myapp.views.register import Register
from myapp.views.home import Home
from  myapp.middlewares.auth import authMiddleware

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', authMiddleware(Order.as_view()), name='orders'),

]
