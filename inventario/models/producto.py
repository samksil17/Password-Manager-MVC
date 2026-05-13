class Producto:
    """Modelo de Producto - Capa de negocio (POO)"""
    
    def __init__(self, nombre, precio, stock, categoria, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
    
    def reducir_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if cantidad > self.stock:
            raise ValueError(f"Stock insuficiente. Disponible: {self.stock}")
        self.stock -= cantidad
    
    def aumentar_stock(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.stock += cantidad
    
    def esta_bajo_stock(self, limite=5):
        return self.stock < limite
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'categoria': self.categoria
        }
    
    def __repr__(self):
        return f"Producto({self.id}, '{self.nombre}', ${self.precio}, Stock:{self.stock}, {self.categoria})"
