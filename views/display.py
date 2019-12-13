

class Display:
    """Display class"""
    def __init__(self):
        pass

    def display_categories(self, all_categories):
        """Displays the list of categories"""
        print(all_categories)
    
    def display_products(self, products):
        """Show product list"""
        for index, product in enumerate(products):
            print(f"{index+1}. {product}")

    def display_one_product(self, product):
        """View a selected product"""
        print(product)
