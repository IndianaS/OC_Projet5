

class Display:
    """Display class"""

    def display_categories(self, all_categories):
        """Displays the list of categories"""
        for index, categorie in all_categories:
            print(f"{index}. {categorie}")

    def display_products(self, products):
        """Show product list"""
        for index, product in enumerate(products):
            print(f"{index+1}. {product}")

    def display_one_product(self, product):
        """View a selected product"""
        content = f"""
        Produit de substitution :
        Nom du produit : {product.product_name_fr}
        Nutriscore : {product.nutrition_grade_fr}
        Magasin : {product.stores}
        Marque : {product.brands}
        Code Barre : {product.id}
        URL : {product.url}
        """
        print(content)

    def display_favorites(self, favorites):
        """Show product list"""
        for index, product in enumerate(favorites):
            print(
                f"{index+1}. Produit sélectionné: {product['product_compared']}\
=> Produit substitué: {product['product_sub']}"
            )
