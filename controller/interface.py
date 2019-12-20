from models.bdd.dbreading import DbReading
from views.display import Display
from models.bdd.dbadd import DbAdd

class Interface:

    def __init__(self, auth):
        self.dbreading = DbReading(auth)
        self.display = Display()
        self.products = []
        self.len = None
        self.commands = ['o', 'n', 'q']

    def fetch_categories(self):
        """Method called when the user requests categories"""
        all_categories = self.dbreading.get_all_categories()
        self.len = len(all_categories)
        self.display.display_categories(all_categories)

    def fetch_products(self, id_category):
        """A method called when the user requests products in a category"""
        self.products = self.dbreading.get_category_products(id_category)
        self.len = len(self.products)
        self.display.display_products(self.products)

    def fetch_one_product(self, index):
        """Method called when the user requests a product"""
        selected_id = self.products[index-1].id
        product = self.dbreading.get_product(selected_id)
        self.display.display_one_product(product)

    def fetch_substitutes(self, index):
        """Method called when the user requests the substitutes"""
        product = self.products[index-1]
        self.products = self.dbreading.get_substitute(product)
        self.len = len(self.products)
        self.display.display_products(self.products)

    def input_user(self, message):
        while True:
            saisie_utilisateur = input(message)

            if saisie_utilisateur in self.commands:
                return saisie_utilisateur

            else:
                try:
                    saisie_utilisateur = int(saisie_utilisateur)
                    assert saisie_utilisateur >= 1
                    assert saisie_utilisateur <= self.len
                    break

                except:
                    print("Votre choix n'est pas valide. \n")


        return saisie_utilisateur


    def loop(self):
        state = True
        while state:
            message = """1 - Afficher les categories \n2 - Favoris \nq - Quitter\n"""
            self.len = 2
            command = self.input_user(message)
            if command == 1:
                while True:
                    self.fetch_categories()
                    choice = self.input_user('Choisir une catégorie entre 1 et 5 :')
                    self.fetch_products(choice)
                    choice = self.input_user('Choisir un produit de la liste :')
                    self.fetch_substitutes(choice)
                    choice = self.input_user('Choisir un substitut dans la liste :')
                    self.fetch_one_product(choice)
                    choice = self.input_user('Voulez vous enregistrer le produit?\no pour oui / n pour non :')
                    self.dbadd.add_favorite(choice)
                    # print(choice)
                    break
            if command == 2:
                pass
            if command == 'q':
                state = False
