from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from myapp.models.user import User
from django.views import View


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        user = User(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(user)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            user.password = make_password(user.password)
            user.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'register.html', data)

    def validateCustomer(self, user):
        error_message = None
        if (not user.first_name):
            error_message = "Please Enter your First Name !!"
        elif len(user.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not user.last_name:
            error_message = 'Please Enter your Last Name'
        elif len(user.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not user.phone:
            error_message = 'Enter your Phone Number'
        elif len(user.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(user.password) < 8:
            error_message = 'Password must be 8 char long'
        elif len(user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif user.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message