import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_id = phone['id']
            name = phone['name']
            price = phone['price']
            image = phone['image']
            release_date = phone['release_date']
            lte_exists = phone['lte_exists']
            slug = slugify(name)
            phone_object = Phone(id=phone_id, name=name, image=image, price=price,
                                 release_date=release_date, lte_exists=lte_exists, slug=slug)
            phone_object.save()
