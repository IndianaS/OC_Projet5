from models.category import Category
from models.productdownload import ProductDownloader
from settings.settings import liste_de_catégories, mots_clef


class CategoryDownloader:
    """Download the categories"""

    def __init__(self):
        pass

    def get_category(self):
        """Add the categories to the list"""
        all_category = []
        for category in liste_de_catégories:
            cat = Category()
            cat.name = category
            get_products = ProductDownloader()
            products = get_products.product_by_category(category)
            cat.products = get_products.filter_product(products)
            all_category.append(cat)

        return all_category
