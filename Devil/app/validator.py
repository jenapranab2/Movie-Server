from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>429496729600:
        raise ValidationError('maximum limit 50GB')