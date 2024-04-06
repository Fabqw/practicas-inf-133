from zeep import Client

client = Client(
    "http://localhost:8000/"
)

# peticion o requests
result1 = client.service.Suma(10,21)
result2 = client.service.Resta(11,7)
result3 = client.service.Multiplicacion(8,61)
result4 = client.service.Division(676,26)

print(result1)
print(result2)
print(result3)
print(result4)
