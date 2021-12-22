from os.path import splitext
from django.utils import timezone


def get_store_image_path(instance, filename):
    """ Get path of store image """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1]
    return f'store/{ timestamp }{ file_ext }'
