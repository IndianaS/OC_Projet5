from settings.settings import keywords


class Product:
    """Class that contains product information"""

    def __init__(self, **article):
        """Initialization of the product object"""
        self.product_name_fr = article.get('product_name_fr')
        self.stores = article.get('stores')
        self.nutrition_grade_fr = article.get('nutrition_grade_fr')
        self.id = article.get('id')
        self.brands = article.get('brands')
        self.id_category = article.get('id_category')
        self.url = article.get('url')

    @classmethod
    def is_valid(cls, article):
        """Method of product validation"""
        is_valid = True
        for word in keywords:


            if word not in article:
                is_valid = False
                break


            if not article[word]:
                is_valid = False
                break

        return is_valid

    def __repr__(self):
        return f"Product({self.product_name_fr})"

    def __str__(self):
        return f"{self.product_name_fr} ({self.nutrition_grade_fr.upper()})"
