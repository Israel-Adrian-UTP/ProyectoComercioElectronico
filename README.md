# Plataforma de Comercio Electronico - CompuX

Sistema modular de comercio electronico desarrollado en Python para automatizar la gestion de inventario, el carrito de compras, el calculo de envios, el procesamiento de pagos y la emision de comprobantes para la empresa CompuX.

Este proyecto corresponde al curso de **Diseno de Patrones** (V Ciclo) de la Universidad Tecnologica del Peru (UTP).

## Descripcion del Problema

CompuX gestiona la venta de laptops, celulares, accesorios, licencias de software y garantias extendidas. El manejo manual de estas operaciones ocasiona errores de stock, cobros inconsistentes y alta complejidad al integrar nuevos metodos de pago o modalidades de entrega. El sistema propuesto resuelve estas limitaciones mediante una arquitectura desacoplada y extensible.

## Arquitectura y Patrones de Diseno

La aplicacion implementa tres patrones de diseno fundamentales bajo los principios SOLID:

1. **Factory Method (Creacional)**
   - **Clases:** `ProductoFactory`, `ProductoFisicoFactory`, `ProductoDigitalFactory`.
   - **Proposito:** Delega la instanciacion de productos fisicos y digitales a subclases especializadas, cumpliendo con el Principio Abierto/Cerrado (OCP) al permitir agregar nuevas categorias sin modificar el codigo cliente.

2. **Facade (Estructural)**
   - **Clase:** `CheckoutFacade`.
   - **Proposito:** Provee una interfaz unificada (`finalizar_compra`) que orquesta la validacion de stock, el calculo de envio, el cobro, la actualizacion del inventario y la generacion del comprobante, ocultando la complejidad de los subsistemas.

3. **Strategy (Comportamiento)**
   - **Interfaces y Clases:** `MetodoPago` (`PagoTarjeta`, `PagoYape`) y `CalculoEnvio` (`EnvioLima`, `EnvioProvincia`).
   - **Proposito:** Encapsula los algoritmos de pago y tarifas de envio en clases independientes e intercambiables en tiempo de ejecucion, evitando estructuras condicionales rigidas.

## Manejo de Excepciones

El sistema cuenta con excepciones personalizadas para controlar reglas de negocio especificas:
- `StockInsuficienteError`: Se lanza cuando la cantidad solicitada supera las unidades disponibles en inventario.
- `PagoRechazadoError`: Se lanza cuando la pasarela de pago no aprueba la transaccion.
- `TipoProductoInvalidoError`: Se lanza al intentar instanciar una categoria de producto no soportada.

## Requisitos del Sistema

- **Lenguaje:** Python 3.10 o superior (probado en Python 3.14).
- **Dependencias:** Solo utiliza la libreria estandar de Python (`abc`). No requiere paquetes externos.
- **Editor recomendado:** Visual Studio Code.
