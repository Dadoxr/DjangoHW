from django import forms

from catalog.models import Product, Version

class ProductForm(forms.ModelForm):
    """ Формирование формы продуктов """

    stop_words_list = [
        'казино', 
        'криптовалюта', 
        'крипта', 
        'биржа', 
        'дешево', 
        'бесплатно', 
        'обман', 
        'полиция', 
        'радар'
        ]

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

        cleaned_data = self.cleaned_data.get('name')

        for word in self.stop_words_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слово "{word}"')

        return cleaned_data
    

    def clean_description(self):
        """ Проверяет стоп слова в описании """

        cleaned_data = self.cleaned_data.get('description')

        for word in self.stop_words_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слово "{word}"')
        
        return cleaned_data

class VersionForm(forms.ModelForm):
    
    class Meta:
        model = Version
        fields = "__all__"
