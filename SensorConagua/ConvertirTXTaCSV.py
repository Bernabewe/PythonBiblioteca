"""
Este script lee el archivo de texto de la estacion, filtra los registros por el año 
especificado, limpia los valores nulos y exporta el resultado a un archivo CSV.
"""
import pandas as pd

def procesar_datos_conagua_corregido(ruta_txt, anio_objetivo="2025"):
    # Inicia el procesamiento del archivo para el anio objetivo
    print(f"Procesando archivo: {ruta_txt} para el anio {anio_objetivo}...")
    
    # Carga el contenido completo del archivo de texto
    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        
    # Inicializa la lista de datos y define las columnas oficiales
    datos_filtrados = []
    columnas_oficiales = ['Fecha', 'Precip', 'Evap', 'Tmax', 'Tmin']
    
    # Recorre las lineas y filtra aquellas que inician con el anio solicitado
    for linea in lineas:
        if linea.strip().startswith(f"{anio_objetivo}-"):
            fila = linea.split()
            
            # Valida que la fila contenga las cinco columnas necesarias
            if len(fila) >= 5:
                datos_filtrados.append(fila[:5])
                
    # Verifica si se encontraron registros tras el filtrado
    if not datos_filtrados:
        print(f"Error: No se encontraron registros para el anio {anio_objetivo}.")
        return None
        
    # Crea el DataFrame con la informacion recolectada
    df = pd.DataFrame(datos_filtrados, columns=columnas_oficiales)
    
    # Reemplaza la etiqueta de texto Nulo por valores vacios de Pandas
    df = df.replace("Nulo", pd.NA)
    
    # Convierte la columna de fecha al formato temporal correcto
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    
    # Transforma las columnas climaticas a valores numericos
    columnas_numericas = ['Precip', 'Evap', 'Tmax', 'Tmin']
    for col in columnas_numericas:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    # Guarda el dataset limpio en un archivo con formato CSV
    nombre_csv = ruta_txt.replace('.txt', f'_{anio_objetivo}.csv')
    df.to_csv(nombre_csv, index=False)
    
    print(f"Listo! Se guardaron {len(df)} registros en el archivo: {nombre_csv}")
    return df