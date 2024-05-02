from django.contrib import admin
from django.urls import path, include

from myapp.views.checkout import CheckOut
from myapp.views.orders import Order
from myapp.views.login import Login
from myapp.views.register import Register
from myapp.views.home import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('home/', Home, name='home'),
    path('checkout/',CheckOut, name='checkout'),
    path('orders/', Order, name='orders'),

]
