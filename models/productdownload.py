import requests

from settings.settings import url
from .product import Product

class ProductDownloader:
    """Class who downloads the products"""

    def __init__(self):
        self.url = url

    def product_by_category(self, category):
        """Search parameter in the API"""

        parametres = {
            "action": "process",
            "json": 1,
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "page_size": 1000
        }

        reponse = requests.get(self.url, params=parametres)
        return reponse.json()

    def filter_product(self, product_list):
        """Add products sorted to the list"""
        produits_triés = []
        for article in product_list['products']:
            if Product.is_valid(article):
                produits_triés.append(Product(**article))

        return produits_triés
