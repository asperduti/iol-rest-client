from iol_rest_client import RestClient
import datetime

client = RestClient(username="", password="")

print(client.get_estado_cuenta())
print(client.get_operaciones())
resultado_compra = client.comprar("bCBA", "XOM", 1, 1350, "t0", datetime.datetime.now().strftime("%Y-%m-%d T17:59:59.000Z"))
print(resultado_compra)
print(client.delete_operacion(resultado_compra["numeroOperacion"]))