
#CLASE
class Cliente:
  #CONSTRUCTOR
  def __init__(self,Id_Cliente,Nombre_Cliente,Correo_Cliente):
    self.Id_Cliente = Id_Cliente
    self.Nombre_Cliente = Nombre_Cliente
    self.Correo_Cliente = Correo_Cliente
#CLASE
class Producto:
  #CONSTRUCTOR
  def __init__(self,Id_Producto,Codigo_Producto,Nombre_Producto,Existencia_Producto):
    self.Id_Producto = Id_Producto
    self.Codigo_Producto = Codigo_Producto
    self.Nombre_Producto = Nombre_Producto
    self.Existencia_Producto = Existencia_Producto
#CLASE
class Pedido:
  #CONSTRUCTOR
  def __init__(self,Id_Pedido,Total_Pedido,Estado_Pedido):
    self.Id_Pedido = Id_Pedido
    self.Total_Pedido = Total_Pedido
    self.Estado_Pedido = Estado_Pedido
#CLASE
class Administrador:
  #CONSTRUCTOR
  def __init__(self,Id_Administrador,Nombre_Administrador,Correo_Administrador):
    self.Id_Administrador = Id_Administrador
    self.Nombre_Administrador = Nombre_Administrador
    self.Correo_Administrador = Correo_Administrador

print("Creando Clases")

