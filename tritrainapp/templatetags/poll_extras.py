from django import template

register = template.Library()

@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 3600) % 60
    mseconds = int(td.microseconds) // 1000

    if hours == 0:
        if minutes == 0:
            return '{}.{}'.format(str(seconds).zfill(2), str(mseconds).zfill(3))
        else:
            return '{}:{}.{}'.format(str(minutes).zfill(2), str(seconds).zfill(2), str(mseconds).zfill(3))
    return '{}:{}:{}.{}'.format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), str(mseconds).zfill(3))


