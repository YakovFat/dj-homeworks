from django import template
from datetime import datetime
import re


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.now()
    date_value = datetime.utcfromtimestamp(value)
    result = now - date_value
    second = result.total_seconds()
    minutes = second / 60
    if minutes < 10:
        return 'только что'
    elif 10 <= minutes <= 1440:
        return f'{int(minutes/60)} часов назад'
    else:
        return date_value.date()


@register.filter
def format_score(value):
    if value:
        if value < -5:
            return 'все плохо'
        elif -5 <= value < 5:
            return 'нейтрально'
        elif value >= 5:
            return 'хорошо'
    else:
        return 'рейтинг отсутствует'

# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте отзыв'
    elif 0 < value <= 50:
        return value
    else:
        return '50+'


@register.filter
def format_selftext(value, count):
    value_split = value.split(' ')
    if len(value_split) > count*2:
        value_split = value_split[:count] + ['...'] + value_split[-count:]
        value = ' '.join(value_split)
        return value
    else:
        return value



