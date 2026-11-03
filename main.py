
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

# Patron Strategy
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> None:
        pass

class PagoTarjeta(MetodoPago):
    def pagar(self, monto: float) -> None:
        # Validar tarjeta y procesar pago
        print(f"-> Procesando pago con Tarjeta de Crédito/Débito: S/ {monto:.2f}")

class PagoYape(MetodoPago):
    def pagar(self, monto: float) -> None:
        print(f"-> Procesando pago con Yape: S/ {monto:.2f}")

class CalculoEnvio(ABC):
    @abstractmethod
    def calcular(self, subtotal: float) -> float:
        pass

class EnvioLima(CalculoEnvio):
    def calcular(self, subtotal: float) -> float:
        return 15.00

class EnvioProvincia(CalculoEnvio):
    def calcular(self, subtotal: float) -> float:
        return 35.00

class Carrito:
    def __init__(self):
        self.items = {}  # {Producto: cantidad}
    def agregar(self, producto: Producto, cantidad: int):
        self.items[producto] = self.items.get(producto, 0) + cantidad
    def total(self) -> float:
        return sum(prod.precio * cant for prod, cant in self.items.items())

class InventarioService:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
    def validar_stock(self, carrito: Carrito):
        for prod, cant in carrito.items.items():
            if prod.stock < cant:
                raise StockInsuficienteError(
                    f"Stock insuficiente para '{prod.nombre}'. Disponible: {prod.stock}, Solicitado: {cant}."
                )
    def descontar_stock(self, carrito: Carrito):
        for prod, cant in carrito.items.items():
            prod.stock -= cant

class Comprobante:
    def __init__(self, carrito: Carrito, total_pagado: float):
        self.carrito = carrito
        self.total_pagado = total_pagado
    def mostrar(self):
        print("\n========================================")
        print("          COMPROBANTE DE PAGO           ")
        print("========================================")
        for prod, cant in self.carrito.items.items():
            print(f"- {prod.nombre} x {cant} = S/ {prod.precio * cant:.2f}")
        print(f"TOTAL PAGADO (Incluyendo envío): S/ {self.total_pagado:.2f}")
        print("========================================\n")

# Patron Facade
class CheckoutFacade:
    def __init__(self, inventario: InventarioService):
        self._inventario = inventario

    def finalizar_compra(self, carrito: Carrito, pago: MetodoPago, envio: CalculoEnvio) -> Comprobante:
        self._inventario.validar_stock(carrito)
        costo_envio = envio.calcular(carrito.total())
        total_a_pagar = carrito.total() + costo_envio
        
        print(f"Subtotal carrito: S/ {carrito.total():.2f}")
        print(f"Costo de envío: S/ {costo_envio:.2f}")
        
        pago.pagar(total_a_pagar)
        self._inventario.descontar_stock(carrito)
        
        return Comprobante(carrito, total_a_pagar)

# Manejo De Excepciones
class StockInsuficienteError(Exception):
    """Excepción lanzada cuando no hay stock suficiente para un producto."""
    pass

class PagoRechazadoError(Exception):
    """Excepción lanzada cuando la pasarela rechaza el pago."""
    pass

class TipoProductoInvalidoError(Exception):
    """Excepción lanzada al intentar instanciar un tipo de producto desconocido."""
    pass

# Ejecucion Del Sistema
if __name__ == "__main__":
    print("=== INICIANDO SISTEMA DE LA PLATAFORMA COMPUX ===")
    # 1. Configurar servicios e inventario
    inventario = InventarioService()
    # 2. Utilizar Factorías
    factory_fisico = ProductoFisicoFactory()
    factory_digital = ProductoDigitalFactory()
    laptop = factory_fisico.crear_producto("Laptop Gamer ASUS", 3500.00, 4)
    licencia = factory_digital.crear_producto("Licencia Antivirus 1 Año", 120.00, 20)
    inventario.agregar_producto(laptop)
    inventario.agregar_producto(licencia)
    print("\n--- PRODUCTOS CREADOS E INVENTARIO INICIAL ---")
    print(laptop.obtener_descripcion())
    print(licencia.obtener_descripcion())
    # 3. Armar Carrito de Compras
    mi_carrito = Carrito()
    mi_carrito.agregar(laptop, 1)
    mi_carrito.agregar(licencia, 2)
    # 4. Procesar pago y envío
    facade = CheckoutFacade(inventario)
    metodo_pago = PagoYape()
    metodo_envio = EnvioProvincia()
    # 5. Generar Comprobante De Pago
    try:
        print("\n--- PROCESANDO CHECKOUT ---")
        comprobante = facade.finalizar_compra(mi_carrito, metodo_pago, metodo_envio)
        comprobante.mostrar()
        print(f"Stock actualizado de Laptop: {laptop.stock}")
        print("¡Pruebas ejecutadas con éxito y sin errores de stock/pago!")
        
    except (StockInsuficienteError, PagoRechazadoError) as e:
        print(f"[Error de Negocio]: {e}")
    except Exception as e:
        print(f"[Error Inesperado]: {e}")
