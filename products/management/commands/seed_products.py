from django.core.management.base import BaseCommand

from products.models import Product
from products.data import PRODUCTS


class Command(BaseCommand):
    help = "Test məhsullarını database-ə əlavə edir"

    def handle(self, *args, **kwargs):

        for item in PRODUCTS:
            Product.objects.get_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "image": item["image"],
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Məhsullar uğurla əlavə edildi!")
        )