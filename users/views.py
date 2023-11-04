import random
from django.conf import settings
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.core.mail import send_mail
from django.forms import ValidationError
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from users.forms import EmailConfirmationForm, MyUserCreationForm

from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_confirmation')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save()
        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.object.confirmation_code = code
        self.object.save()
        
        send_mail(
            subject='Подтверждение почты MolokoShop',
            message=f'Ваш проверочный код: {code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)

class EmailConfirmationView(FormView):
    form_class = EmailConfirmationForm
    template_name = 'users/email_confirmation.html'
    success_url = reverse_lazy('catalog:products')


    def form_valid(self, form):
        confirmation_code = form.cleaned_data['confirmation_code']
        user = User.objects.get(confirmation_code=confirmation_code)
        user.confirmation_code = None
        user.save()
        return super().form_valid(form)


class MyPasswordResetView(PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")
    

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name="users/password_reset_done.html"

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='users/password_reset_confirm.html'
    success_url = reverse_lazy("users:password_reset_complete")

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='users/password_reset_complete.html'



class ProfileView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', 'avatar', 'phone', 'country')
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        
        return self.request.user 
