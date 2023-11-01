from django import forms

from catalog.models import Product, Version
from django.conf import settings

class ProductForm(forms.ModelForm):
    """ Формирование формы продуктов """

    class Meta:
        """ Описание формы продуктов """

        model = Product
        fields = ("name", "description", "preview", "category", "price", )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'Some help text for field'

    def clean_name(self):
        """ Проверяет стоп слова в названии """

        name = self.cleaned_data.get('name')

        if self._field_contains_forbidden_words(name):
                raise forms.ValidationError('Название содержит запрещенные слова')

        return name
    
    def clean_description(self):
        """ Проверяет стоп слова в описании """

        description = self.cleaned_data.get('description')

        if self._field_contains_forbidden_words(description):
                raise forms.ValidationError('Название содержит запрещенные слова')
        
        return description

    @staticmethod
    def _field_contains_forbidden_words(field_value: str) -> bool:
        field_value = field_value.lower()
        return any(field_value in forbidden_word for forbidden_word in settings.STOP_WORDS_LIST)



class VersionForm(forms.ModelForm):
    
    class Meta:
        model = Version
        fields = "__all__"





