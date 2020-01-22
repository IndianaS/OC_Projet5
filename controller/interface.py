from models.bdd.dbreading import DbReading
from views.display import Display
from models.bdd.dbadd import DbAdd


class Interface:
    """Program management class"""

    def __init__(self, auth):
        """
        Instantiation of communication classes with the database,
        instantiating the class containing the views
        """
        self.dbreading = DbReading(auth)
        self.dbadd = DbAdd(auth)
        self.display = Display()
        self.products = []
        self.len = None
        self.commands = ['o', 'n', 'q', 'a']
        self.product = None
        self.next = self.menu_home
        self.choice = None
        self.running = False

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

    def fetch_one_product(self, index, contextual_list):
        """Method called when the user requests a product"""
        selected_id = contextual_list[index - 1].id
        product = self.dbreading.get_product(selected_id)
        self.display.display_one_product(product)

    def fetch_substitutes(self, index):
        """Method called when the user requests the substitutes"""
        self.product = self.products[index - 1]
        self.substitutes = self.dbreading.get_substitute(self.product)
        if not self.substitutes:
            print("Pas de substitus trouvés")
        else:
            self.len = len(self.products)
            self.display.display_products(self.substitutes)

    def fetch_favorite(self):
        """Method called when the user requests the favorites"""
        self.favorites = self.dbreading.get_favorite()
        self.len = len(self.favorites)
        self.display.display_favorites(self.favorites)

    def input_user(self, message):
        """User input recovery method"""
        while True:
            choice = input(message)

            try:
                if choice.isdigit() and 0 < int(choice) <= self.len:
                    return int(choice)
                elif choice in self.commands:
                    return choice
                else:
                    raise ValueError
            except ValueError:
                print("Votre choix n'est pas valide. \n")

    def menu_home(self):
        """Home menu management"""
        self.len = 2
        self.choice = self.input_user(
            '1 - Afficher les categories \n2 - favoris \nq - Quitter\n')
        if self.choice == "q":
            self.next = self.quit
        elif self.choice == 1:
            self.next = self.menu_categories
        elif self.choice == 2:
            self.next = self.menu_favorites

    def menu_categories(self):
        """Menu management categories"""
        print("Le choix précédent a été", self.choice)
        self.fetch_categories()
        self.choice = self.input_user('Choisir une catégorie :')
        if self.choice == "q":
            self.next = self.quit
        elif self.choice == "a":
            self.next = self.menu_home
        else:
            self.next = self.menu_products

    def menu_products(self):
        """Product menu management"""
        self.fetch_products(self.choice)

        self.choice = product_choice = self.input_user(
            'Choisir un produit de la liste :')
        if self.choice == "q":
            self.next = self.quit
        elif self.choice in ("a", "n"):
            self.next = self.menu_home
        else:
            self.fetch_one_product(self.choice, self.products)
            self.fetch_substitutes(self.choice)

            self.choice = substitute_choice = self.input_user(
                'Choisir un substitut dans la liste :')
            if self.choice == "q":
                self.next = self.quit
            elif self.choice in ("a", "n"):
                self.next = self.menu_home
            else:
                self.fetch_one_product(substitute_choice, self.substitutes)

                self.choice = self.input_user(
                    'Voulez vous enregistrer le produit?'
                    '\no pour oui / n pour non, a pour accueil :'
                )
                if self.choice == "q":
                    self.next = self.quit
                elif self.choice in ("a", "n"):
                    self.next = self.menu_home
                elif self.choice == "o":
                    self.dbadd.add_favorite(
                        self.products[product_choice - 1],
                        self.substitutes[substitute_choice - 1]
                    )
                    self.next = self.menu_home

    def menu_favorites(self):
        """Favorite menu management"""
        print("Le choix précédent a été", self.choice)
        self.fetch_favorite()
        self.substitutes = [item['product_sub'] for item in self.favorites]
        self.choice = self.input_user('Sélectionner un produit: ')
        if self.choice == "q":
            self.next = self.quit
        elif self.choice in ("a", "n"):
            self.next = self.menu_home
        else:
            self.fetch_one_product(self.choice, self.substitutes)
            self.choice = self.input_user("a pour accueil, q pour quitter: ")
            if self.choice == "q":
                self.next = self.quit
            elif self.choice == "a":
                self.next = self.menu_home

    def quit(self):
        """Methode to get out of the loop"""
        self.running = False

    def loop(self):
        """Main loop"""
        self.running = True
        while self.running:
            self.next()
