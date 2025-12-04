
DATA ANALYST - FINAL ASSESSMENT - MODULE 3
Ariana Caldeira

---

**Description**
This repository contains the files with the solution for the final assessment of Module 3 of the Data Analytics bootcamp.  
The exercises were completed in **Jupyter Notebook** using **VSCode**, importing Python libraries, and using a `src` folder to support exploratory data analysis (EDA).

---

**Repository Contents**
- **README.md** : Repository description.  
- **evaluacion-final.md** : Full statement of the assessment.  
- **Customer Flight Activity.csv** and **Customer Loyalty History.csv** : Raw CSV files used in the assessment.  
- **EF_modulo_3_DA_Ariana.ipynb** : Jupyter Notebook with the solution to all exercises.  
- **src/** : Folder with support scripts for EDA, including:
  - `eda_soporte.py` : Custom functions for data exploration and visualization.

---

**Requirements**
To run the notebooks correctly, you need:  
- **VSCode**  
- **Python** (>=3.8 recommended)  
- Python libraries:
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Display all columns in the DataFrames
pd.set_option('display.max_columns', None)

# Import support functions from the src folder
from src import eda_soporte as eda_sp
```


**src Folder**
The src folder contains helper functions used for:
- Initial exploration of dataframes (EDA)
- Basic variable visualization
- Column statistical summary

These functions help streamline the analysis and keep the notebook organized and clean.


**Usage**
- Clone the repository:
git clone https://github.com/Adalab/bda-modulo-3-evaluacion-final-ariana-caldeira.git

- Open the notebook EF_modulo_3_DA_Ariana.ipynb in VSCode or Jupyter Notebook.
- Load the CSV files from the same folder and run the cells.
- The support functions for EDA are located in src/eda_soporte.py.



________________________________________________________________________________________________

ANALISTA DE DATOS - EVALUACIÓN FINAL - MÓDULO 3
Ariana Caldeira


**Descripción**
Este repositorio contiene los archivos con la solución de la evaluación final del Módulo 3 del bootcamp de Data Analytics.  
Los ejercicios fueron realizados en Jupyter Notebook usando VSCode, importando librerías de Python y utilizando una carpeta `src` de soporte para el análisis exploratorio de datos (EDA).



**Contenido del Repositorio**
- **README.md** : Descripción del repositorio.  
- **evaluacion-final.md** : Enunciado completo de la evaluación.  
- **Customer Flight Activity.csv** y **Customer Loyalty History.csv** : Archivos CSV crudos para usar en la evaluación.  
- **EF_modulo_3_DA_Ariana.ipynb** : Jupyter Notebook con la resolución de todos los ejercicios.  
- **src/** : Carpeta con scripts de soporte para el análisis EDA, incluyendo:
  - `eda_soporte.py` : Funciones personalizadas para exploración y visualización de datos.


**Requisitos**
Para ejecutar los notebooks correctamente se necesita:  
- **VSCode**  
- **Python** (>=3.8 recomendado)  
- Librerías Python:
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Visualizar todas las columnas de los DataFrames
pd.set_option('display.max_columns', None)

# Importar funciones de soporte desde la carpeta src
from src import eda_soporte as eda_sp
```


**Carpeta src**
La carpeta src contiene funciones auxiliares utilizadas para:
- Exploración inicial de dataframes (EDA)
- Visualización básica de variables
- Resumen estadístico de columnas

Estas funciones permiten agilizar el análisis y mantener el notebook más ordenado y limpio.


**Uso**
- Clonar el repositorio:
git clone https://github.com/Adalab/bda-modulo-3-evaluacion-final-ariana-caldeira.git

- Abrir el notebook EF_modulo_3_DA_Ariana.ipynb en VSCode o Jupyter Notebook.
- Cargar los CSV desde la misma carpeta y ejecutar las celdas.
- Las funciones de soporte para EDA se encuentran en src/eda_soporte.py.


**Autor**
Ariana Caldeira
Bootcamp Data Analytics - Evaluación Final Módulo 3