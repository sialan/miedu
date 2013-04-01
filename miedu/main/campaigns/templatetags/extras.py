from django import template

register = template.Library()

@register.filter
def percentage_of(amount_pledged, goal):
    try:
        return "%d%%" % (float(amount_pledged) / goal * 100)
    except (ValueError, ZeroDivisionError):
        return ""