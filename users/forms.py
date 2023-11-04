from django.contrib.auth import forms
from django.forms import ValidationError, CharField, Form

from users.models import User


class MyUserCreationForm(forms.UserCreationForm):
    
    class Meta:
        fields = ('email','password1', 'password2',)
        model = User



class EmailConfirmationForm(Form):
    confirmation_code = CharField(max_length=6)

    def clean_confirmation_code(self):
        confirmation_code = self.cleaned_data.get('confirmation_code')
        if not User.objects.filter(confirmation_code=confirmation_code).exists():
            raise ValidationError('Неверный код подтверждения.')
        return confirmation_code