from django import template

register = template.Library()


@register.filter
def color_for_cell(value, cell):
    if cell == 0:
        return ''
    if cell == 13:
        return 'gray'
    if value:
        val = float(value)
        if val < 0:
            return 'green'
        if 1 < val <= 2:
            return 'LightCoral'
        if 2 < val <= 5:
            return 'Crimson'
        if 5 < val:
            return 'DarkRed'
    return ''

