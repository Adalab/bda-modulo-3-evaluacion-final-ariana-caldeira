
# DOCUMENTO DE SOPORTE A ANALISIS EDA

import pandas as pd
import numpy as np

# Imputación de nulos
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
import seaborn as sns
import matplotlib.pyplot as plt

# Visualizar todas las columnas de los DataFrames
pd.set_option('display.max_columns', None)



#__________________________________________________
# FUNCIÓN .READ CSV
def open_csv(ruta):   
    """
    Intenta cargar un archivo CSV. Si falla por codificación, 
    intenta de nuevo con 'latin1'.
    """
    try:
        df = pd.read_csv(ruta)
        print("Archivo cargado con éxito")
        return df
    except Exception:
         try:
            df = pd.read_csv(ruta, encoding='latin1')
            print("Archivo cargado con éxito (latin1)")
            return df
         except Exception as e:
            print(f"❌ No se pudo cargar el archivo. ERROR: {e}")
            return pd.DataFrame()



#____________________________________________________
# PRIMERA EXPLORACIÓN EDA - Resumen
def eda_1(df: pd.DataFrame):

    print("🔍 EXPLORACIÓN RÁPIDA EDA")

    # 1. Dimensiones del dataframe
    print("\n____ DIMENSIONES ____")
    print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")

    # 2. Mostrar Tipos de Datos de cada columna
    print("\n____ TIPO DE DATOS ____")
    print(df.dtypes)

    # 3. Filas Duplicadas
    print("\n____ DUPLICADOS ____")
    print(df.duplicated().sum())

    # 4. Mostrar el Porcentaje de Nulos (isna().sum()/len(df)*100)
    print("\n____ % DE NULOS ____")
    null_percentages = round((df.isna().sum() / len(df)) * 100, 2)
    print(null_percentages)

    # 5. Buscar si hay columnas con valores únicos
    print("\n____ VALORES ÚNICOS ____")
    print(df.nunique())

    print("\n--- ✅ Inspección EDA terminada ---")



#_________________________________________________________
# ANÁLISIS ESTADÍSTICO DE COLUMNAS NUMÉRICAS
def eda_num(df: pd.DataFrame):
    
    # 1. Identificar columnas numéricas
    num_cols = df.select_dtypes(include=np.number).columns
    
    if len(num_cols) == 0:
        print("❌ No se encontraron columnas numéricas para analizar.")
        return

    print(" ")
    print(f"🔍 ANALIZANDO COLUMNAS NUMÉRICAS")
    print(", ".join(num_cols)) # imprime los nombres separados por coma
    print("________________________________________________")


    # ___INICIO BLOQUE DE CÁLCULO DE ESTADÍSTICAS___
    
    # 2. Obtener el resumen estadístico con .describe()
    describe = df[num_cols].describe().T

    # 3. Calcular la moda - no incluida en .describe()
    # toma el primer valor si existe
    mode_series = df[num_cols].mode().iloc[0] 


    # 4. Crear 2 DataFrames con todos los cálculos estadísticos
    df_stats = pd.DataFrame({
        'Mínimo': describe['min'].round(2),
        'Máximo': describe['max'].round(2),
        'Media': describe['mean'].round(2),
        'Moda': mode_series.round(2),
        'Mediana (50%)': describe['50%'].round(2)})
    
    df_disper = pd.DataFrame({
        'Q1 (25%)': describe['25%'].round(2),
        'Q3 (75%)': describe['75%'].round(2),
        'IQR (Q3-Q1)': describe['75%']-describe['25%'].round(2)})
    
    # 5. Mostrar la tabla de resumen estadístico
    print(" ")
    print("📊 ESTADÍSTICAS DESCRIPTIVAS NUMÉRICAS")
    print(" ")
    print(df_stats)
    print(" ")
    print(df_disper)
    print(" ")
    print("________________________________________________")
    print(" ")

    # ___INICIO BLOQUE DE GENERACIÓN DE GRÁFICOS (Boxplots)___
    print("🗳️ BOXPLOTS PARA DETECTAR OUTLIERS Y DISTRIBUCIÓN")
    
    # 6. Configurar el lienzo (Una sola vez)
    n_cols = 2
    n_rows = (len(num_cols) + 1) // n_cols
    plt.figure(figsize=(15, 5 * n_rows))
    plt.suptitle('Boxplots por Columna Numérica', fontsize=16, y=1.02)
    
    # 7. Generar los Boxplots (Bucle para generar los subplots)
    for i, col in enumerate(num_cols):
        plt.subplot(n_rows, n_cols, i + 1)
        sns.boxplot(y=df[col], orient='v', color="darkorange")
        plt.title(f'Distribución de {col}')
        plt.ylabel(col)
    
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.show()
    print("\n -- análisis terminado --")




#_________________________________________________________
# ANÁLISIS ESTADÍSTICO DE COLUMNAS CATEGÓRICAS
def eda_cat(df: pd.DataFrame):

    # 1. Identificar columnas categóricas (object, category)
    cat_cols = df.select_dtypes(include=['object', 'category']).columns

    if len(cat_cols) == 0:
        print("❌ No se encontraron columnas categóricas para analizar.")
        return

    print(" ")
    print(f"🔍 ANALIZANDO COLUMNAS CATEGÓRICAS")
    print(", ".join(cat_cols))
    print("________________________________________________")

    # 2. Mostrar estadísticas: moda, valores únicos, value_counts
    print("\n📊 ESTADÍSTICAS DESCRIPTIVAS CATEGÓRICAS\n")

    for col in cat_cols:
        print(f"____________ {col.upper()} ____________")
        print(f"Moda: {df[col].mode()[0]}") #[0]para extraer solo el primero valor de moda
        print(f"Valores únicos: {df[col].nunique()}")
        print(" ")
        print(df[col].value_counts())

        # COUNT PLOT 
        plt.figure(figsize=(6, 3))
        sns.countplot(y=df[col],  #invertí los axis para una mejor visualización
                    order=df[col].value_counts().head(10).index, #añadí un límite de visualización de 10 valores para que el gráfico sea más claro
                    color="skyblue")

        plt.title(f'Countplot — {col}')
        plt.xlabel("Frecuencia")
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()
        print("__________________________________________________________________\n")
