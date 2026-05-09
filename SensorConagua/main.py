import os
import sys

# Importa las funciones de los modulos externos
try:
    from WebScraping import descargar_datos_estacion
    from ConvertirTXTaCSV import procesar_datos_conagua_corregido
except ImportError:
    print("Error: Asegurate de que WebScraping.py y ConvertirTXTaCSV.py esten en la misma carpeta.")
    sys.exit(1)

def ejecutar_pipeline_clima(sensor_id, anio):
    """
    Coordina el flujo completo de descarga y conversion de datos.
    """
    print("="*50)
    print(f"INICIANDO PROCESAMIENTO: {sensor_id}")
    print("="*50)

    # Ejecuta la descarga del archivo de texto original
    archivo_txt = descargar_datos_estacion(sensor_id)

    # Verifica la existencia del archivo descargado antes de continuar
    if archivo_txt and os.path.exists(archivo_txt):
        print(f"\n[PASO 1 COMPLETADO]: Archivo {archivo_txt} listo.")
        
        # Ejecuta la limpieza y conversion al formato CSV
        df_resultado = procesar_datos_conagua_corregido(archivo_txt, anio)

        # Muestra el resumen estadistico si la conversion fue exitosa
        if df_resultado is not None:
            print(f"\n[PASO 2 COMPLETADO]: Proceso finalizado con exito.")
            print("\nResumen de los datos obtenidos:")
            print(df_resultado.describe())
        else:
            print("\n[ERROR]: El paso de conversion fallo.")
    else:
        print("\n[ERROR]: No se pudo obtener el archivo de CONAGUA. Abortando.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Define el sensor y el anio para la ejecucion
    SENSOR = "CULIACAN (DGE) - 25015"
    ANIO_TAREA = "2025"

    ejecutar_pipeline_clima(SENSOR, ANIO_TAREA)