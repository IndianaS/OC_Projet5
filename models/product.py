from settings.settings import mots_clef


class Product:
    def __init__(self, **article):
        self.product_name_fr = article['product_name_fr']
        self.stores = article['stores']
        self.nutrition_grade_fr = article['nutrition_grade_fr']
        self.id = article['id']
        self.brands = article['brands']
    
    @classmethod
    def is_valid(cls, article):
        is_valid = True
        for mot in mots_clef:
      
      # On vérifie que le dictionnaire contient la clé
            if mot not in article:
                is_valid = False
                break
      
      # On vérifie que ça contient un truc
            if not article[mot]:
                is_valid = False
                break

        return is_valid

    def __repr__(self):
        return f"{self.product_name_fr}"