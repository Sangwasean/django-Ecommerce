# ecommerce/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class authMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            # Redirect to login page if not authenticated
            return redirect(reverse('login'))

        # If user is authenticated, continue with the request
        response = self.get_response(request)
        return response
