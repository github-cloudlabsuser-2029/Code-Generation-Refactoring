import requests

def obtener_datos_meteorologicos(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return None

# Ejemplo de uso
ciudad = "Santiago"
api_key = "3e164c0f9dfffdd1fca239aa96c16b56"
datos = obtener_datos_meteorologicos(ciudad, api_key)
if datos:
    print(f"Temperatura en {ciudad}: {datos['main']['temp']}°C")
else:
    print("No se pudieron obtener los datos meteorológicos.")