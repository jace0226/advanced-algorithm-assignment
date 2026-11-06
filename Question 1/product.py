# Define the Product entity class
class Product:
    # Represents a pharmacy product entity
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: RM{self.price:.2f}, Stock: {self.stock}"