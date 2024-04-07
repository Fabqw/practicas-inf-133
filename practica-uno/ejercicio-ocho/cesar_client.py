import requests

url = "http://localhost:8000/mensajes"


print("--- Nuevo mensaje ---")
nuevo_mensaje = {
    "contenido": "Hola mundo"
}
response = requests.post(url, json=nuevo_mensaje)
print(response.text)

print("--- Nuevo mensaje ---")
nuevo_mensaje = {
    "contenido": "Adios mundo"
}
response = requests.post(url, json=nuevo_mensaje)
print(response.text)

print("--- Mensajes Actuales ---")
response = requests.get(url)
print(response.text)

print("--- Mensajes con id ---")
id = 2
response_ci = requests.get(f"{url}/{id}")
print(response_ci.text)

print("--- Actualizacion mensaje con id ---")
id = 2
actualizacion_mensaje = {
    "contenido": "Vamos a jugar"
}
response = requests.put(f"{url}/{id}", json=actualizacion_mensaje)
print(response.text)


print("--- Eliminar mensaje con id ---")
id = 1
response = requests.delete(f"{url}/{id}")
print(response.text)

print("--- Mensajes Actuales ---")
response = requests.get(url)
print(response.text)
