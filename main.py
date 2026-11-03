
# Importando Libreria Clases Abstractas
from abc import ABC, abstractmethod

# Clases Base
class Producto(ABC):
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass

class ProductoFisico(Producto):
    def obtener_descripcion(self) -> str:
        return f"[Producto Físico] {self.nombre} - S/ {self.precio:.2f} (Stock: {self.stock})"

class ProductoDigital(Producto):
    def obtener_descripcion(self) -> str:
        return f"[Producto Digital] {self.nombre} - S/ {self.precio:.2f} (Licencia Virtual)"

# Patron Factory Method
class ProductoFactory(ABC):
    @abstractmethod
    def crear_producto(self, nombre: str, precio: float, stock: int) -> Producto:
        pass

class ProductoFisicoFactory(ProductoFactory):
    def crear_producto(self, nombre: str, precio: float, stock: int) -> Producto:
        return ProductoFisico(nombre, precio, stock)

class ProductoDigitalFactory(ProductoFactory):
    def crear_producto(self, nombre: str, precio: float, stock: int) -> Producto:
        return ProductoDigital(nombre, precio, stock)

