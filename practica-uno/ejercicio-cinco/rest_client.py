import requests

url = "http://localhost:8000/animales"

print("--- Animales actuales ---")
get_response = requests.get(url)
print(get_response.text)

print("--- Nuevo animal ---")
nuevo_animal = {
    "nombre": "Tiburoncin",
    "especie": "Pez",
    "genero": "Macho",
    "edad": 2,
    "peso": 20.5
}
response = requests.post(url, json=nuevo_animal)
print(response.text)

print("--- Animales actuales ---")
response = requests.get(url)
print(response.text)

print("--- Animales por especie ---")
especie = "Pez"
response_especie = requests.get(f"{url}/?especie={especie}")
print(response_especie.text)

print("--- Animales por genero ---")
genero = "Hembra"
response_genero = requests.get(f"{url}/?genero={genero}")
print(response_genero.text)

print("--- Actualización de animal ---")
id = 1
actualizacion_animal = {
    "nombre": "Max",
    "edad": 3
}
response = requests.put(f"{url}/{id}", json=actualizacion_animal)
print(response.text)

print("--- Eliminar animal ---")
id = 2
response_eliminar = requests.delete(f"{url}/{id}")
print(response_eliminar.text)
