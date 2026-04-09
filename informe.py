"""
DESAFÍO INTEGRAL: AUTOMATIZACIÓN DE INFORMES + ESTRATEGIA DE GIT & GITHUB
Objetivo: Completar el script y sincronizar cada avance con la nube.
Instrucciones: Sigue los bloques 'GIT:' para la terminal y 'TODO:' para el código.
"""

# pip install pyodbc pandas

import pyodbc
import pandas as pd
import os

# =================================================================
# PASO 1: CREAR EL REPOSITORIO EN GITHUB Y CONFIGURAR ORIGEN
# -----------------------------------------------------------------
# GIT: 
# 1. Ve a GitHub y crea un nuevo repositorio.
# 2. En tu terminal (dentro de la carpeta del proyecto):
#    git init
#    git config --global user.name "Tu Nombre"
#    git config --global user.email "tu@email.com"
# 3. git remote add origin https://github.com/cesarsali96-svg/datos-accessar.git
#
# ¿POR QUÉ? 'remote add' establece el puente entre tu computadora 
# y la nube (GitHub). Ahora tus "fotos" pueden ser compartidas.
# =================================================================


# =================================================================
# PASO 2: COMMIT INICIAL (IGNORANDO LA DB) Y PUSH
# -----------------------------------------------------------------
# GIT:
# 1. Crea un archivo '.gitignore' y escribe dentro: *.accdb   
# 2. git add .
# 3. git commit -m "Initial commit: Ignorando archivos de datos"
# 4. git push -u origin main
#
# ¿POR QUÉ? El primer 'push' con '-u' vincula tu rama local con la de GitHub.
# El .gitignore evita que archivos pesados o sensibles suban a la nube.
# =================================================================


# =================================================================
# PASO 3: LECTURA DE LA BASE DE DATOS (ACCESS)
# -----------------------------------------------------------------
def conectar_access():
    """Establece la conexión con el archivo Access (.accdb)."""
    # TODO: Asegúrate de tener el archivo .accdb en la misma carpeta.
    ruta_db = os.path.abspath("NOMBREARCHIVO.accdb")
    str_conn = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        f'DBQ={ruta_db};'
    )
    try:
        conn = pyodbc.connect(str_conn)
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

# GIT: Una vez escrita la función:
# 1. git add .
# 2. git commit -m "Agregada lógica de conexión a Access"
# 3. git push
# =================================================================


# =================================================================
# PASO 4: FORZAR ERROR, COMMIT Y REVERSAR (REVERT)
# -----------------------------------------------------------------
# TODO: Escribe una línea de código con un error (ej: x = variable_inexistente + 10).







# GIT:
# 1. git add .
# 2. git commit -m "Commit con errores detectados"
# 3. git push
#
# Verifica que los cambios se hayan subido a GitHub, luego volvemos a la
# versión segura (la anterior):
#
# 4. git revert HEAD
# 5. git push
#
# ¿POR QUÉ? 'git revert' crea un nuevo commit que deshace los cambios 
# del anterior. Es la forma más profesional y segura de "echarse para 
# atrás" sin alterar el historial compartido con otros.
# =================================================================


# =================================================================
# PASO 5: FUNCIONALIDADES LIBRE (ANÁLISIS DE DATOS)
# -----------------------------------------------------------------
def procesar_informacion(conexion):
    if conexion:
        print("--- CONEXIÓN EXITOSA: PROCESANDO DATOS ---")

        # --- PARTE A: GUIADA ---
        # TODO: Carga una tabla de tu Access (ej: 'Ventas') a un DataFrame.

        # query = "CONSULTA SQL..."
        # df = pd.read_sql(query, conexion)

        
        # TODO: Realiza un filtro simple (ej: registros con valor > 100)
        # y muestra los primeros 5 resultados con print(df.head()).
        
        # GIT:
        # 1. git add .
        # 2. git commit -m "feat: Lectura y filtrado base de datos"
        # 3. git push
        
        # --- PARTE B: LIBRE ---
        # TODO: ¡Es tu turno! Crea una nueva función o lógica. 
        # Ideas: exportar a Excel, una interfaz, agrupar datos por categoría o crear una gráfica.
        
        # RECOMENDACIÓN: Ve haciendo un commit y un push por cada pequeña mejora.
        # "El push constante es tu seguro de vida contra fallos de hardware".
        pass


# TODO: Realiza correctamente los llamados a las funciones
db = conectar_access()
if db:
    # TODO: Llama la función de procesar información. HINT: no te olvides del argumento ()


    db.close()