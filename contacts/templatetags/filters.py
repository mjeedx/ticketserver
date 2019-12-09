from django import template

register = template.Library()


@register.filter(name='tel_mod')
def tel_mod(tel):
    tel = str(tel)
    tel_format = "(" + tel[0:3] + ") " + tel[3:6] + " " + tel[6:8] + " " + tel[8:10]
    return str(tel_format)
