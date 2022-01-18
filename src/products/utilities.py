from os.path import splitext
from django.utils import timezone


def get_manufacturer_logo_path(instance, filename):
    """ Get path of manufacturer logo """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1]
    return f'manufacturers/{ timestamp }{ file_ext }'


def get_product_image_path(instance, filename):
    """ Get path of product image """
    timestamp = timezone.now().timestamp()
    file_ext = splitext(filename)[1]
    return f'products/{ timestamp }{ file_ext }'
