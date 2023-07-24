from django import template

register = template.Library()

@register.inclusion_tag('demo_app1/partials/custom_buttons.html')
def query_button(target):
    return {'target': target}