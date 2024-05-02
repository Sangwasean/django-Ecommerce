from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from myapp.models.user import User
from django.views import View
from myapp.models.products import Products
from myapp.models.orders import Order
from myapp.middlewares.auth import authMiddleware


class Order(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})