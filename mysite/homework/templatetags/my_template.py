from random import randint, choices
from string import ascii_letters, digits
from django import template

register = template.Library()

@register.simple_tag
def getint():
    return randint(1,100)

@register.simple_tag
def getslug():
    return ''.join(choices(ascii_letters + digits, k = randint(5,10)))
