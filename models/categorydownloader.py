from models.category import Category
from models.productdownload import ProductDownloader
from settings.settings import category_list


class CategoryDownloader:
    """Download the categories"""

    def get_category(self):
        """Add the categories to the list"""
        all_category = []
        for category in category_list:
            cat = Category()
            cat.name = category
            get_products = ProductDownloader()
            products = get_products.product_by_category(category)
            cat.products = get_products.filter_product(products)
            all_category.append(cat)

        return all_category
