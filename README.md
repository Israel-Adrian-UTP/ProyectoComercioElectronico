# Plataforma de Comercio Electr贸nico - CompuX

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Arquitectura](https://img.shields.io/badge/Patrones-Factory%20%7C%20Facade%20%7C%20Strategy-success.svg)
![Principios](https://img.shields.io/badge/Principios-SOLID-orange.svg)

Proyecto acad茅mico desarrollado para el curso de **Dise帽o de Patrones** de la **Universidad Tecnol贸gica del Per煤 (UTP)**. Consiste en el dise帽o e implementaci贸n de una plataforma E-commerce modular y extensible en Python para la empresa ficticia **CompuX**, aplicando patrones de dise帽o creacionales, estructurales y de comportamiento bajo los principios SOLID.

---

## Descripci贸n del Problema y Soluci贸n

**CompuX** es una empresa peruana dedicada a la venta de tecnolog铆a (laptops, celulares, accesorios, licencias de software y garant铆as extendidas). La gesti贸n manual de sus ventas generaba errores de stock, cobros inconsistentes y dificultad para integrar nuevos m茅todos de pago.

**Soluci贸n:** Un sistema automatizado orientado a objetos que gestiona el cat谩logo de productos, carrito de compras, validaci贸n de inventario, c谩lculo din谩mico de env铆os, pasarelas de pago y emisi贸n de comprobantes sin acoplamiento r铆gido.

---

## Arquitectura y Patrones de Dise帽o Implementados

El sistema sigue una arquitectura limpia aplicando tres patrones fundamentales de dise帽o de software:

1. **Factory Method (Creacional):**
   * **Clases:** `ProductoFactory`, `ProductoFisicoFactory`, `ProductoDigitalFactory`.
   * **Prop贸sito:** Desacopla la instanciaci贸n de productos (`ProductoFisico` y `ProductoDigital`), permitiendo agregar nuevas categor铆as en el futuro sin modificar el c贸digo cliente (Principio Abierto/Cerrado).
2. **Facade (Estructural):**
   * **Clase:** `CheckoutFacade`.
   * **Prop贸sito:** Provee una interfaz 煤nica y simplificada (`finalizar_compra`) que orquesta los subsistemas complejos del proceso de compra: validaci贸n de stock, c谩lculo de env铆o, procesamiento de pago, descuento de inventario y generaci贸n de comprobante.
3. **Strategy (Comportamiento):**
   * **Interfaces y Estrategias:** 
     * Pagos: `MetodoPago` $\rightarrow$ `PagoTarjeta`, `PagoYape`.
     * Env铆os: `CalculoEnvio` $\rightarrow$ `EnvioLima` (S/ 15.00), `EnvioProvincia` (S/ 35.00).
   * **Prop贸sito:** Permite intercambiar algoritmos de pago y tarifas de env铆o en tiempo de ejecuci贸n, eliminando estructuras condicionales complejas (`if/elif`).

### Manejo de Excepciones Personalizadas
* `StockInsuficienteError`: Controla intentos de compra que superan el inventario disponible.
* `PagoRechazadoError`: Gestiona fallos en la pasarela de pago.
* `TipoProductoInvalidoError`: Previene la creaci贸n de tipos de producto no soportados.

---

## Requisitos e Instalaci贸n

### Requisitos Previos
* **Python 3.14** (o superior compatible con anotaciones de tipo est谩ndar).
* No requiere librer铆as externas (usa 煤nicamente el m贸dulo nativo `abc`).

## 馃捇 Ejemplo de Salida en Consola

Al ejecutar `main.py`, el sistema realiza una prueba integral del flujo de compra (creaci贸n de inventario, armado de carrito, env铆o a provincia y pago con Yape):

```text
=== INICIANDO SISTEMA DE LA PLATAFORMA COMPUX ===

--- PRODUCTOS CREADOS E INVENTARIO INICIAL ---
[Producto F铆sico] Laptop Gamer ASUS - S/ 3500.00 (Stock: 4)
[Producto Digital] Licencia Antivirus 1 A帽o - S/ 120.00 (Licencia Virtual)

--- PROCESANDO CHECKOUT ---
Subtotal carrito: S/ 3740.00
Costo de env铆o: S/ 35.00
-> Procesando pago con Yape: S/ 3775.00

========================================
          COMPROBANTE DE PAGO           
========================================
- Laptop Gamer ASUS x 1 = S/ 3500.00
- Licencia Antivirus 1 A帽o x 2 = S/ 240.00
TOTAL PAGADO (Incluyendo env铆o): S/ 3775.00
========================================

Stock actualizado de Laptop: 3
隆Pruebas ejecutadas con 茅xito y sin errores de stock/pago!
```

---

## Autores y Roles

* **Palomares Due帽as, Israel Adrian** (`U18302252`) 鈥?Arquitectura del sistema, dise帽o de patrones creacionales/estructurales y documentaci贸n general.
* **Quispe Aranda, Kevin Elias** (`U23301040`) 鈥?Implementaci贸n del patr贸n Strategy, manejo de excepciones personalizadas, pruebas e implementaci贸n en Python.

**Docente:** Ing. Miguel Angel Farfan Leyva  
**Ciclo Acad茅mico:** V Ciclo 鈥?Lima, Per煤 (2026)