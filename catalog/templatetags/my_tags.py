from django import template

register = template.Library()

# Создание тега
@register.simple_tag()
def mediapath(val):
    print(val)
    if val:
        return f'/media/{val}'
    return '/media/images/Placeholder-1.png'
