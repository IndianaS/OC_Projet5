

class Display:
    """Display class"""
    def __init__(self):
        pass

    def display_categories(self, all_categories):
        """Display categories"""
        print(all_categories)
    
    def display_products(self, products):
        """Display products"""
        for index, product in enumerate(products):
            print(f"{index+1}. {product}")

    def display_one_product(self, product):
        print(product)
