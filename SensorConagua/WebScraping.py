"""
Este script esta diseñado para descargar los archivos txt que la CONAGUA ofrece al publico
sobre ciertos sensores a lo largo del pais. La URL original es esta:
https://smn.conagua.gob.mx/es/climatologia/informacion-climatologica/informacion-estadistica-climatologica

Al tomar el nombre del sensor extrae su ID mediante regex y utiliza el link oficial 
para obtener el archivo txt y posteriormente convertilo a un csv limpio para su uso en el proyecto.
"""
import requests
import re
import urllib3

# Desactiva las advertencias por no verificar el SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def descargar_datos_estacion(variable_sensor):
    """
    Recibe el nombre de la estacion y su ID, extrae el ID, 
    construye la URL directa y descarga el archivo .txt de CONAGUA.
    """
    # Procesa la entrada del usuario
    print(f"Procesando entrada: '{variable_sensor}'")
    
    # Busca el ID de cinco digitos en la cadena
    match = re.search(r'\d{5}', variable_sensor)
    
    # Valida la existencia del ID
    if not match:
        print("Error: No se encontro un ID de 5 digitos.")
        return None
        
    # Asigna el ID detectado
    id_estacion = match.group()
    print(f"ID detectado: {id_estacion}")
    
    # Identifica el codigo del estado y define el mapa de carpetas
    codigo_estado = id_estacion[:2]
    estados_map = {'25': 'sin', '26': 'son', '02': 'bc', '03': 'bcs'}
    carpeta_estado = estados_map.get(codigo_estado, 'sin')
    
    # Genera la direccion de descarga directa
    url = f"https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Diarios/{carpeta_estado}/dia{id_estacion}.txt"
    print(f"Peticion directa a: {url}")
    
    # Define los encabezados para simular un navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # Realiza la peticion al servidor ignorando la verificacion SSL
        respuesta = requests.get(url, headers=headers, timeout=10, verify=False)
        
        # Guarda el contenido en un archivo local si la respuesta es exitosa
        if respuesta.status_code == 200:
            nombre_archivo = f"datos_estacion_{id_estacion}.txt"
            
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
                
            print(f"Archivo descargado y guardado como: {nombre_archivo}\n")
            return nombre_archivo
        else:
            print(f"Error en la descarga. Codigo HTTP: {respuesta.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ocurrio un error de red: {e}")
        return None