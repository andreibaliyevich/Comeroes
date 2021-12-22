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


def get_stats_of_reviews(reviews):
    """ Returns statistics of product reviews """
    stats_of_reviews = {}

    for number in range(5, 0, -1):
        number_count = reviews.filter(rating=number).count()
        if number_count:
            number_percent = (number_count * 100) / reviews.count()
        else:
            number_percent = 0
        stats_of_reviews[str(number)] = (number_count, int(number_percent))

    return stats_of_reviews
