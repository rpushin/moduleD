from django import template
 
register = template.Library() # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются(

@register.filter(name='censor')
def multiply(value):
    value = value.replace('хуй', 'куй')
    value = value.replace('пизда', 'да-да')
    return value