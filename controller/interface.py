from models.bdd.dbreading import DbReading
from views.display import Display


class Interface:

    def __init__(self, auth):
        self.dbreading = DbReading(auth)
        self.display = Display()
        self.products = []

    def fetch_categories(self):
        """Méthode est appellée quand l'utilisateur demande les catégories"""
        all_categories = self.dbreading.get_all_categories()
        self.display.display_categories(all_categories)

    def fetch_products(self, id_category):
        self.products = self.dbreading.get_category_products(id_category)
        self.display.display_products(self.products)

    def fetch_one_product(self, index):
        selected_id = self.products[index-1].id
        product = self.dbreading.get_product(selected_id)
        self.display.display_one_product(product)

    def fetch_substitutes(self, index):
        product = self.products[index-1]
        self.products = self.dbreading.get_substitute(product)
        self.display.display_products(self.products)